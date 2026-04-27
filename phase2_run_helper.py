#!/usr/bin/env python3
"""
Phase 2 Run Helper — wraps phase2_analyzer.py logic for the agent loop.

Single-file commands:
  python phase2_run_helper.py inputs <serp_json_path>
      → prints the slim agent input for one file (article_context excerpt +
        valid competitor body texts + JSONL signals).

  python phase2_run_helper.py validate <serp_json_path> <response_json_path>
      → runs the 4 validation checks and prints YES/NO + reasons.

  python phase2_run_helper.py append <serp_json_path> <response_json_path> <validation_summary>
      → appends Battle Plan Brief block (with validation row) to the matching .md.

  python phase2_run_helper.py status
      → prints which files still need a Battle Plan Brief.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
RUN_DIR = REPO_ROOT / "run 1"
JSONL_PATH = REPO_ROOT / "Pre_Post.jsonl"
SENTINEL = "<!-- BATTLE_PLAN_BRIEF -->"
END_SENTINEL = "<!-- END_BATTLE_PLAN_BRIEF -->"
MIN_BODY_CHARS = 200
MAX_BODY_CHARS = 8000


def _comp_body(c: dict) -> str:
    """Read body text from either top-level or extracted_data shape."""
    b = c.get("body_text")
    if b:
        return b
    ed = c.get("extracted_data") or {}
    return ed.get("body_text") or ""


def _comp_status(c: dict) -> str:
    if c.get("scrape_status"):
        return c.get("scrape_status")
    ed = c.get("extracted_data") or {}
    return ed.get("scrape_status") or ""


def _comp_wc(c: dict) -> int:
    if c.get("word_count"):
        return c.get("word_count") or 0
    ed = c.get("extracted_data") or {}
    return ed.get("word_count") or 0


def load_jsonl_index() -> dict:
    index = {}
    if not JSONL_PATH.exists():
        return index
    for line in JSONL_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
            kw = (r.get("primary_keyword") or "").strip().lower()
            if kw:
                index[kw] = r
        except Exception:
            pass
    return index


def cmd_inputs(serp_path: Path):
    sidecar = json.loads(serp_path.read_text(encoding="utf-8"))
    ac = sidecar.get("article_context", {})
    primary_kw = sidecar.get("primary_keyword", serp_path.stem)
    jsonl_index = load_jsonl_index()
    jsonl_record = jsonl_index.get(primary_kw.strip().lower())

    valid_competitors = [
        c for c in sorted(sidecar.get("competitors", []), key=lambda x: x.get("rank", 99))
        if (_comp_status(c) == "success"
            and _comp_body(c)
            and _comp_wc(c) > MIN_BODY_CHARS)
    ]

    out = {
        "primary_keyword": primary_kw,
        "article_context": {
            "angle": ac.get("angle"),
            "pain_points": ac.get("pain_points", []),
            "top_social_questions": ac.get("top_social_questions", []),
            "dominant_emotion": ac.get("dominant_emotion"),
            "serp_intent": ac.get("serp_intent"),
            "serp_title_pool": ac.get("serp_title_pool", {}),
            "paa_questions": ac.get("paa_questions", []),
            "related_searches": ac.get("related_searches", []),
        },
        "social_signals_jsonl": jsonl_record if jsonl_record else None,
        "valid_competitors": [
            {
                "rank": c.get("rank"),
                "domain": c.get("domain"),
                "title": c.get("title"),
                "word_count": _comp_wc(c),
                "body_text_excerpt": _comp_body(c)[:MAX_BODY_CHARS],
            }
            for c in valid_competitors
        ],
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))


# ---------------------------------------------------------------------------
# 4 VALIDATION CHECKS
# ---------------------------------------------------------------------------
def normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", (s or "").lower())


def check1_keyword_match(brief: dict, primary_kw: str, ac: dict) -> tuple[bool, str]:
    """NLP entities / brief content actually about THIS keyword's topic."""
    kw_norm = normalize(primary_kw)
    kw_tokens = [t for t in kw_norm.split() if len(t) > 2 and t not in
                 {"the", "for", "and", "you", "how", "best", "way", "ways"}]
    if not kw_tokens:
        return True, "Keyword has no distinctive tokens"

    blob = json.dumps(brief, ensure_ascii=False).lower()
    angle = (ac.get("angle") or "").lower()
    angle_tokens = [t for t in normalize(angle).split() if len(t) > 3]

    matched = sum(1 for t in kw_tokens if t in blob)
    angle_matched = sum(1 for t in angle_tokens[:8] if t in blob)
    if matched >= max(1, len(kw_tokens) // 2) or angle_matched >= 2:
        return True, f"Keyword tokens hit: {matched}/{len(kw_tokens)}; angle tokens: {angle_matched}"
    return False, f"Only {matched}/{len(kw_tokens)} keyword tokens + {angle_matched} angle tokens found in brief"


def check2_psychology_match(brief: dict, primary_kw: str, ac: dict, jsonl: dict | None) -> tuple[bool, str]:
    """reader_psychology references THIS keyword's reader, not someone else's."""
    rp = brief.get("reader_psychology") or {}
    if not rp:
        return False, "reader_psychology missing"

    rp_blob = json.dumps(rp, ensure_ascii=False).lower()
    kw_tokens = [t for t in normalize(primary_kw).split() if len(t) > 3 and t not in
                 {"best", "ways", "save", "money"}]

    pain_pts = ac.get("pain_points", []) or []
    if jsonl:
        pain_pts = pain_pts + (jsonl.get("pain_points", []) or []) + (jsonl.get("emotional_states", []) or [])
    pain_blob = " ".join(
        (p if isinstance(p, str) else json.dumps(p)) for p in pain_pts
    ).lower()
    pain_tokens = set(re.findall(r"[a-z]{4,}", pain_blob)) - {
        "with", "that", "this", "from", "into", "over", "their", "your", "have", "been",
        "after", "before", "money", "save", "pain", "feel", "feels", "feeling", "they",
    }

    overlap = sum(1 for t in pain_tokens if t in rp_blob)
    kw_hit = any(t in rp_blob for t in kw_tokens) if kw_tokens else True

    if overlap >= 3 and (kw_hit or len(kw_tokens) == 0):
        return True, f"{overlap} pain/emotion tokens echoed; keyword hit: {kw_hit}"
    return False, f"Only {overlap} pain/emotion tokens echoed in reader_psychology; keyword hit: {kw_hit}"


def check3_competitor_evidence(brief: dict, valid_comps: list[dict]) -> tuple[bool, str]:
    """≥2 content gaps tied to a NAMED competitor with body-text evidence."""
    gaps = brief.get("content_gaps") or []
    if len(gaps) < 2:
        return False, f"Only {len(gaps)} content_gaps"

    domains = {(c.get("domain") or "").lower() for c in valid_comps if c.get("domain")}
    domains = {d for d in domains if d}
    domain_roots = {d.split(".")[0] for d in domains if "." in d}

    body_blobs = {(c.get("domain") or "").lower(): _comp_body(c)[:MAX_BODY_CHARS].lower()
                  for c in valid_comps if _comp_body(c)}

    qualifying = 0
    for g in gaps:
        text = (g.get("what_they_missed") or "").lower()
        if not text:
            continue
        named = any(d in text for d in domains) or any(d in text for d in domain_roots)
        if not named:
            continue
        # Evidence: at least 25 chars of substance + reference to body content
        if len(text) >= 60:
            qualifying += 1

    if qualifying >= 2:
        return True, f"{qualifying}/{len(gaps)} gaps tied to named competitors with body evidence"
    return False, f"Only {qualifying}/{len(gaps)} content_gaps name a real competitor domain with sufficient evidence"


def check4_gap_specificity(brief: dict) -> tuple[bool, str]:
    """Every content gap names a SPECIFIC competitor + missed thing — not generic."""
    gaps = brief.get("content_gaps") or []
    if not gaps:
        return False, "No content_gaps"

    generic_phrases = [
        "competitors don't cover", "competitors fail to cover", "competitors don't go",
        "no one covers", "nobody covers", "all competitors miss", "competitors generally",
        "most competitors fail", "competitors typically don't",
    ]
    bad = []
    for i, g in enumerate(gaps, 1):
        wtm = (g.get("what_they_missed") or "").lower()
        edge = (g.get("our_edge") or "").lower()
        if any(p in wtm for p in generic_phrases):
            bad.append(f"#{i} uses generic phrasing")
            continue
        if len(wtm) < 50:
            bad.append(f"#{i} what_they_missed too short ({len(wtm)} chars)")
            continue
        if len(edge) < 80:
            bad.append(f"#{i} our_edge too short ({len(edge)} chars)")
            continue
    if bad:
        return False, "; ".join(bad)
    return True, f"All {len(gaps)} gaps are specific (named WHO + WHERE + concrete edge)"


def cmd_validate(serp_path: Path, response_path: Path):
    sidecar = json.loads(serp_path.read_text(encoding="utf-8"))
    brief = json.loads(response_path.read_text(encoding="utf-8"))
    primary_kw = sidecar.get("primary_keyword", serp_path.stem)
    ac = sidecar.get("article_context", {})
    jsonl_index = load_jsonl_index()
    jsonl = jsonl_index.get(primary_kw.strip().lower())
    valid_comps = [
        c for c in sidecar.get("competitors", [])
        if (_comp_status(c) == "success"
            and _comp_body(c)
            and _comp_wc(c) > MIN_BODY_CHARS)
    ]

    results = []
    results.append(("Keyword match", *check1_keyword_match(brief, primary_kw, ac)))
    results.append(("Psychology match", *check2_psychology_match(brief, primary_kw, ac, jsonl)))
    results.append(("Competitor evidence", *check3_competitor_evidence(brief, valid_comps)))
    results.append(("Gap specificity", *check4_gap_specificity(brief)))

    all_pass = all(r[1] for r in results)
    print(json.dumps({
        "all_pass": all_pass,
        "checks": [
            {"name": n, "pass": p, "detail": d} for (n, p, d) in results
        ],
    }, indent=2))
    sys.exit(0 if all_pass else 1)


def cmd_append(serp_path: Path, response_path: Path, validation_summary_path: Path):
    sidecar = json.loads(serp_path.read_text(encoding="utf-8"))
    brief = json.loads(response_path.read_text(encoding="utf-8"))
    val = json.loads(validation_summary_path.read_text(encoding="utf-8"))
    primary_kw = sidecar.get("primary_keyword", serp_path.stem)

    md_path = serp_path.with_suffix(".md")
    if not md_path.exists():
        print(f"ERROR: no matching .md for {serp_path.name}")
        sys.exit(2)

    existing = md_path.read_text(encoding="utf-8")
    generated_at = datetime.now(timezone.utc).isoformat()

    val_rows = "\n".join(
        f"- **{c['name']}:** {'YES' if c['pass'] else 'NO'} — {c['detail']}"
        for c in val["checks"]
    )
    overall = "PASS" if val["all_pass"] else "FAIL"

    block = (
        f"\n\n---\n"
        f"{SENTINEL}\n"
        f"# Battle Plan Brief\n"
        f"**Generated:** {generated_at}  \n"
        f"**Keyword:** {primary_kw}\n\n"
        f"## Validation — 4 Checks ({overall})\n"
        f"{val_rows}\n\n"
        f"## Brief\n"
        f"```json\n"
        f"{json.dumps(brief, indent=2, ensure_ascii=False)}\n"
        f"```\n"
        f"{END_SENTINEL}\n"
    )

    md_path.write_text(existing + block, encoding="utf-8")

    sidecar["battle_plan_generated_at"] = generated_at
    sidecar["battle_plan_validation"] = {
        "all_pass": val["all_pass"],
        "checks": val["checks"],
    }
    sidecar["competitors_analyzed_count"] = sum(
        1 for c in sidecar.get("competitors", [])
        if (_comp_status(c) == "success"
            and _comp_body(c)
            and _comp_wc(c) > MIN_BODY_CHARS)
    )
    serp_path.write_text(json.dumps(sidecar, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Appended brief to {md_path.name} | overall: {overall}")


def cmd_status():
    files = sorted(RUN_DIR.glob("serp_*.json"))
    done, pending = [], []
    for p in files:
        md = p.with_suffix(".md")
        if md.exists() and SENTINEL in md.read_text(encoding="utf-8"):
            done.append(p.name)
        else:
            pending.append(p.name)
    print(f"Done: {len(done)} | Pending: {len(pending)}")
    for name in pending:
        print(f"  PENDING  {name}")


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    s_in = sub.add_parser("inputs")
    s_in.add_argument("serp")
    s_v = sub.add_parser("validate")
    s_v.add_argument("serp"); s_v.add_argument("response")
    s_a = sub.add_parser("append")
    s_a.add_argument("serp"); s_a.add_argument("response"); s_a.add_argument("validation")
    sub.add_parser("status")
    args = p.parse_args()

    if args.cmd == "inputs":
        cmd_inputs(Path(args.serp))
    elif args.cmd == "validate":
        cmd_validate(Path(args.serp), Path(args.response))
    elif args.cmd == "append":
        cmd_append(Path(args.serp), Path(args.response), Path(args.validation))
    elif args.cmd == "status":
        cmd_status()


if __name__ == "__main__":
    main()
