"""Repair hero image prompts in hero_image_queue_final.json.

Builds a clean, fixed-structure prompt for each entry using:
  - the entry's `style` to look up eyebrow / mood / dominant visual
  - `post_title` and `primary_keyword` to derive a natural 2-5 word topic line
  - existing numbers / outcome phrases (from post_title or current visible text)
    to derive a short result-or-angle line
  - a deterministic per-style support line

Only the `prompt` field is rewritten; all other fields are preserved.

Usage:
    python repair_hero_prompts.py --mode test   # first 20 -> hero_image_queue_repaired_test20.json
    python repair_hero_prompts.py --mode final  # all      -> hero_image_queue_repaired.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).parent
SRC = ROOT / "hero_image_queue_final.json"
TEST_OUT = ROOT / "hero_image_queue_repaired_test20.json"
FULL_OUT = ROOT / "hero_image_queue_repaired.json"


# --------------------------------------------------------------------------------------
# Style map
# --------------------------------------------------------------------------------------

STYLE_MAP: dict[int, dict[str, str]] = {
    1:  {"eyebrow": "REAL MONEY RESULT",
         "mood": "Provocative and controlled, one result creates the curiosity gap.",
         "dominant": "A single large amber result number."},
    2:  {"eyebrow": "SAVINGS ACTION PLAN",
         "mood": "Warm, achievable, and editorial.",
         "dominant": "A warm minimal desk layout."},
    3:  {"eyebrow": "MONEY RESET GUIDE",
         "mood": "Tense then relieving, disorder gives way to control.",
         "dominant": "A clean before-and-after split."},
    4:  {"eyebrow": "BUDGET SYSTEM MAP",
         "mood": "Confident and educational without becoming a lesson slide.",
         "dominant": "A simple four-part budget layout."},
    5:  {"eyebrow": "FINANCIAL FIELD GUIDE",
         "mood": "Authoritative and restrained.",
         "dominant": "A quiet amber result mark on deep navy."},
    6:  {"eyebrow": "MISSING MONEY MAP",
         "mood": "Dramatic but useful, recognition comes before relief.",
         "dominant": "A bold recognition headline."},
    7:  {"eyebrow": "FAST MONEY PLAN",
         "mood": "Energetic and action-oriented.",
         "dominant": "A bold action headline with one amber result."},
    8:  {"eyebrow": "ADULT MONEY GUIDE",
         "mood": "Premium editorial authority with large type and open space.",
         "dominant": "An oversized editorial headline on an open canvas."},
    9:  {"eyebrow": "BUDGET MAP GUIDE",
         "mood": "Inviting and practical.",
         "dominant": "A tidy grid of unlabeled warm cards."},
    10: {"eyebrow": "REAL MONEY DATA",
         "mood": "Credible and data-forward.",
         "dominant": "A large data number beside open space."},
    11: {"eyebrow": "TRUSTED MONEY GUIDE",
         "mood": "Calm authority and institutional trust.",
         "dominant": "A calm blue circular focal mark."},
    12: {"eyebrow": "SAVINGS DECISION GUIDE",
         "mood": "Clear-headed and decisive.",
         "dominant": "A bright blue panel with one large metric."},
    13: {"eyebrow": "FINANCIAL BLUEPRINT PLAN",
         "mood": "Precise, professional, and actionable.",
         "dominant": "A flat blue result card."},
    15: {"eyebrow": "MONEY OPTION COMPARISON",
         "mood": "Neutral and trustworthy, options feel evenly weighted.",
         "dominant": "A balanced comparison layout with unlabeled panels."},
    16: {"eyebrow": "REAL MONEY STORY",
         "mood": "Warm, human, and lived-in.",
         "dominant": "A large editorial pull quote."},
    17: {"eyebrow": "MONEY APP DECISION",
         "mood": "Clean and practical.",
         "dominant": "A clean unlabeled app-style card."},
    18: {"eyebrow": "MONEY BUCKET SYSTEM",
         "mood": "Structured and clear.",
         "dominant": "A simple unlabeled branching map."},
    19: {"eyebrow": "FINANCIAL RULE GUIDE",
         "mood": "Instructive and decisive.",
         "dominant": "A simple stacked proportion bar."},
}

DEFAULT_STYLE = {
    "eyebrow": "MONEY GUIDE",
    "mood": "Calm, practical, and editorial.",
    "dominant": "A single clean editorial focal point.",
}


def style_number(style_field: str) -> Optional[int]:
    m = re.match(r"\s*Style\s+(\d+)", style_field, re.I)
    return int(m.group(1)) if m else None


def style_lookup(style_field: str) -> dict[str, str]:
    n = style_number(style_field)
    return STYLE_MAP.get(n, DEFAULT_STYLE)


# Support line varies per style for natural variety while staying on the spec list.
SUPPORT_LINE_BY_STYLE: dict[int, str] = {
    1:  "Real clarity",
    2:  "Start today",
    3:  "Compare calmly",
    4:  "No guesswork",
    5:  "The real math",
    6:  "Real clarity",
    7:  "Start today",
    8:  "Real clarity",
    9:  "No guesswork",
    10: "The real math",
    11: "Next step",
    12: "Next step",
    13: "The real math",
    15: "Compare calmly",
    16: "Start today",
    17: "Next step",
    18: "No guesswork",
    19: "No guesswork",
}


def support_line(style_field: str) -> str:
    n = style_number(style_field)
    return SUPPORT_LINE_BY_STYLE.get(n, "Next step")


# --------------------------------------------------------------------------------------
# Topic line builder (from primary_keyword + post_title)
# --------------------------------------------------------------------------------------

ACRONYMS = {
    "ac", "apy", "apr", "atm", "bls", "cd", "dca", "diy", "doe", "dot",
    "ev", "eia", "fafsa", "fdic", "fmcsa", "hsa", "hysa", "ira", "irs",
    "k", "mma", "pslf", "roi", "tco", "tsa", "uk", "us", "usa", "usda",
    "vs", "vsls", "wifi",
}
SMALL_WORDS = {"a", "an", "and", "as", "at", "by", "for", "in", "of", "on",
               "or", "the", "to", "vs", "with"}

# Brand / product names worth preserving as plain text and guarding against logos.
BRAND_NAMES = {
    "acorn", "acorns", "amazon", "aldi", "ally", "amex", "americanexpress",
    "betterment", "capitalone", "chase", "chime", "citi", "costco", "digit",
    "discover", "etsy", "fidelity", "kroger", "lyft", "marcus", "oportun",
    "robinhood", "schwab", "sofi", "sephora", "starbucks", "target",
    "trader", "uber", "upwork", "vanguard", "walmart", "wealthfront",
}

# Stop-word fillers that frequently appear in the keyword/title and should be dropped.
KEYWORD_FILLERS = {
    "a", "an", "the", "of", "in", "on", "to", "for", "with",
    "is", "are", "do", "does", "be", "have", "has", "should", "i", "you",
    "your", "my", "our", "their", "they", "people", "still", "really",
    "actually", "would", "can", "as", "at", "by", "from", "against", "than",
    "or", "and", "but",
}


def _titlecase_word(w: str) -> str:
    if not w:
        return w
    low = w.lower()
    if low in ACRONYMS:
        return low.upper()
    return w[0].upper() + w[1:].lower()


def title_case(text: str) -> str:
    parts = text.split()
    out = []
    for i, p in enumerate(parts):
        # keep currency / percentage / ratio tokens untouched (and uppercase trailing K/M)
        if re.fullmatch(r"\$[\d,]+(?:\.\d+)?(?:[KkMm])?", p) or "/" in p or p.endswith("%"):
            out.append(p.replace("k", "K").replace("m", "M") if p.startswith("$") else p)
            continue
        if i > 0 and p.lower() in SMALL_WORDS:
            out.append(p.lower())
        else:
            out.append(_titlecase_word(p))
    return " ".join(out)


def strip_dup_words(text: str) -> str:
    """Drop adjacent duplicate tokens, e.g. 'Paycheck Paycheck' -> 'Paycheck'."""
    parts = text.split()
    out: list[str] = []
    for w in parts:
        if out and out[-1].lower() == w.lower():
            continue
        out.append(w)
    return " ".join(out)


def detect_brand(text: str) -> Optional[str]:
    for tok in re.findall(r"[A-Za-z]+", text.lower()):
        if tok in BRAND_NAMES:
            return tok
    return None


def _join_ratio(kw: str) -> Optional[str]:
    """If the keyword starts with 'N N N' (2 or 3 small ints) followed by 'rule', return slashed form."""
    m = re.match(r"^(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+rule\b", kw)
    if m:
        return f"{m.group(1)}/{m.group(2)}/{m.group(3)} Rule"
    m = re.match(r"^(\d{1,3})\s+(\d{1,3})\s+rule\b", kw)
    if m:
        return f"{m.group(1)}/{m.group(2)} Rule"
    return None


def _strip_leading_numerics(kw: str) -> str:
    """Drop leading pure-numeric tokens like '1 100 money saving chart' -> 'money saving chart'."""
    return re.sub(r"^(?:\d+\s+){1,3}(?=[a-z])", "", kw)


def _normalize_amount_in_text(s: str) -> str:
    # "10 000" -> "$10,000"
    s = re.sub(r"\b(\d{1,3})\s(\d{3})\b", lambda m: f"${int(m.group(1))},{m.group(2)}", s)
    # bare "1000" / "5000" -> "$1,000" / "$5,000"
    s = re.sub(r"\b(\d{4,6})\b", lambda m: f"${int(m.group(1)):,}", s)
    # bare "1000" already covered by above; handle "100" or "500" (3-digit) only when leading
    return s


# Pattern -> formatter rules for primary_keyword. Order matters; first match wins.
_TOPIC_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    # Apps
    (re.compile(r"^best money saving apps for (.+)$"), r"\1 Savings Apps"),
    (re.compile(r"^best money saving apps$"), "Money Saving Apps"),
    (re.compile(r"^apps? to help save money$"), "Money Saving Apps"),
    (re.compile(r"^apps? for saving money on (.+)$"), r"\1 Savings App"),
    (re.compile(r"^apps? to save money for a (.+)$"), r"\1 Savings App"),
    (re.compile(r"^apps? to save money for (.+)$"), r"\1 Savings App"),
    (re.compile(r"^apps? to save money on (.+)$"), r"\1 Savings App"),
    (re.compile(r"^money saving apps? for (.+)$"), r"\1 Savings Apps"),
    (re.compile(r"^money saving apps?$"), "Money Saving Apps"),

    # "how to save money ..."
    (re.compile(r"^how to save money on (.+)$"), r"\1 Savings"),
    (re.compile(r"^how to save money for a (.+)$"), r"Saving for a \1"),
    (re.compile(r"^how to save money for (.+)$"), r"Saving for \1"),
    (re.compile(r"^how to save money with (.+)$"), r"\1 Savings"),
    (re.compile(r"^how to save money$"), "Money Saving Tips"),
    (re.compile(r"^how can i save money on (.+)$"), r"\1 Savings"),
    (re.compile(r"^how can i save money$"), "Money Saving Tips"),
    (re.compile(r"^how can i get ahead financially$"), "Get Ahead Financially"),
    (re.compile(r"^best ways? to save money on (.+)$"), r"\1 Savings"),
    (re.compile(r"^best ways? to save money for a (.+)$"), r"Saving for a \1"),
    (re.compile(r"^best ways? to save money for (.+)$"), r"Saving for \1"),
    (re.compile(r"^best way to save money for a (.+)$"), r"Saving for a \1"),
    (re.compile(r"^best way to save money for (.+)$"), r"Saving for \1"),
    (re.compile(r"^best way to save money on (.+)$"), r"\1 Savings"),
    (re.compile(r"^best ways? to save money$"), "Money Saving Tips"),
    (re.compile(r"^ways to save money on (.+)$"), r"\1 Savings"),
    (re.compile(r"^ways to save money$"), "Money Saving Tips"),
    (re.compile(r"^tips to save money on (.+)$"), r"\1 Savings"),

    # "how much / how to save N in months"
    (re.compile(r"^how much money should i (?:have in|keep in)(?: my)? savings(?: account)?$"),
        "How Much in Savings"),
    (re.compile(r"^how much money should i have saved by (\d+)$"), r"Saved by \1"),
    (re.compile(r"^how much money should i save up to move out$"), "Move-Out Savings"),
    (re.compile(r"^how much money should i save (.+)$"), r"\1 Savings"),
    (re.compile(r"^how much should i save (.+)$"), r"\1 Savings"),
    (re.compile(r"^how much spending money (?:a|per) week.*$"), "Weekly Spending Money"),
    (re.compile(r"^how to save (\d+(?:\s\d{3})?) in (.+)$"),
        lambda m: f"Save {_normalize_amount_in_text(m.group(1))} in {m.group(2)}"),
    (re.compile(r"^how to save (\d+)k? in (\d+) (years|months|weeks)$"),
        lambda m: f"Save ${m.group(1)}K in {m.group(2)} {m.group(3).capitalize()}"),
    (re.compile(r"^how to save (\d+(?:\s\d{3})?) (?:a|per) (month|week|day|year)$"),
        lambda m: f"Save {_normalize_amount_in_text(m.group(1))} a {m.group(2)}"),
    (re.compile(r"^how to save a million dollars in (\d+) (years|months|weeks)$"),
        lambda m: f"$1M in {m.group(1)} {m.group(2).capitalize()}"),

    # "do/does ... save money"
    (re.compile(r"^do (.+) save money$"), r"\1 Savings"),
    (re.compile(r"^does (.+) save (?:you )?money$"), r"\1 Savings"),

    # "is N a lot of money in savings"
    (re.compile(r"^is (\d+)k a lot of money in savings$"), r"$\1K in Savings"),

    # "saving money ..."
    (re.compile(r"^saving money for (.+)$"), r"Saving for \1"),
    (re.compile(r"^saving money on (.+)$"), r"\1 Savings"),
    (re.compile(r"^saving money (.+)$"), r"\1 Savings"),
    (re.compile(r"^save money (.+)$"), r"\1 Savings"),
    (re.compile(r"^saving for (.+)$"), r"Saving for \1"),

    # "what is the connection between goals and savings"
    (re.compile(r"^what is the connection between (.+)$"), r"\1"),
    (re.compile(r"^what is the (.+)$"), r"The \1"),

    # "why ... saving (their) money"
    (re.compile(r"^why might some people still prefer manually saving their money$"),
        "Manual Money Saving"),
    (re.compile(r"^why is saving money (.+)$"), r"Why Saving Matters"),
    (re.compile(r"^why is (.+)$"), r"Why \1"),

    # "best temperature for X to save money" / "best time to do X to save money"
    (re.compile(r"^best temperature for (.+) to save money$"), r"\1 Temperature"),
    (re.compile(r"^best time to (.+) to save money$"), r"\1 Timing"),
    (re.compile(r"^best (.+) to save money$"), r"\1 Savings"),

    # "online shopping saves money"
    (re.compile(r"^(.+) saves money$"), r"\1 Savings"),

    # Generic catch-all: drop leading "how to" / "how can i" / "how do(es)"
    (re.compile(r"^how (?:to|can i|do i|does)\s+(.+)$"), r"\1"),

    # "money market account vs savings account"
    (re.compile(r"^money market (?:account )?vs savings account$"),
        "Money Market vs Savings"),
    (re.compile(r"^(.+) vs (.+)$"), r"\1 vs \2"),

    # Financial goals
    (re.compile(r"^financial goals? (?:for|by) (.+)$"), r"Goals by \1"),
    (re.compile(r"^financial goals?$"), "Financial Goals"),

    # "can you withdraw money from savings"
    (re.compile(r"^can you withdraw money from savings$"), "Savings Withdrawals"),

    # "high yield savings vs cd vs money market"
    (re.compile(r"^high yield savings vs cd vs money market$"), "HYSA vs CD vs MMA"),
    (re.compile(r"^highest yield money market savings accounts$"), "High Yield MMA"),
    (re.compile(r"^high yield (.+) account.*$"), r"High Yield \1"),

    # "money saving X" -> keep
    (re.compile(r"^money saving (.+)$"), r"Money Saving \1"),
]


# Fallbacks for keyword fragments that look like the X group inside a captured pattern.
# We'll run a small post-cleanup on those captured X groups.
_TRAILING_PREP_RE = re.compile(
    r" (?:a|an|the|of|to|for|with|in|on|at|by|as|against|from)$", re.I
)


def _clean_capture(x: str) -> str:
    x = x.strip(" ?.")
    # collapse multi-space
    x = re.sub(r"\s+", " ", x)
    # drop leading verbs / fillers like 'do '
    x = re.sub(r"^(?:do|to|for|on|with|in)\s+", "", x, flags=re.I)
    # drop trailing/leading articles and dangling prepositions
    x = re.sub(r"^(?:a|an|the)\s+", "", x, flags=re.I)
    while True:
        new = _TRAILING_PREP_RE.sub("", x)
        if new == x:
            break
        x = new
    # normalise plural forms of common heads
    x = re.sub(r"\bcars?\b", "Car", x, flags=re.I)
    x = re.sub(r"\bhotels?\b", "Hotel", x, flags=re.I)
    x = re.sub(r"\bhouses?\b", "House", x, flags=re.I)
    return x


def build_topic(primary_keyword: str, post_title: str) -> str:
    kw = primary_keyword.strip().lower()
    kw = kw.rstrip("?.!")

    # Ratio short-circuit
    ratio = _join_ratio(kw)
    if ratio:
        return ratio

    # Drop leading enumeration noise
    kw = _strip_leading_numerics(kw)

    # Try patterns
    topic = None
    for pat, fmt in _TOPIC_PATTERNS:
        m = pat.match(kw)
        if not m:
            continue
        if callable(fmt):
            topic = fmt(m)
        else:
            topic = m.expand(fmt) if "\\" in fmt else fmt
        # Clean any captured pieces (best-effort)
        topic = _clean_capture(topic)
        break

    if topic is None:
        topic = kw  # fall through to generic cleanup

    topic = strip_dup_words(topic)
    topic = title_case(topic)

    # Drop ONLY leading and trailing filler tokens; keep prepositions between content words.
    words = topic.split()
    while words and words[0].lower() in KEYWORD_FILLERS:
        words.pop(0)
    while words and words[-1].lower() in KEYWORD_FILLERS:
        words.pop()
    if len(words) > 5:
        words = words[:5]
        # Don't end on a stranded preposition after truncation.
        while words and words[-1].lower() in KEYWORD_FILLERS:
            words.pop()
    return " ".join(words)


# --------------------------------------------------------------------------------------
# Result-or-angle line builder
# --------------------------------------------------------------------------------------

NON_CLAIM_BY_STYLE: dict[int, str] = {
    1:  "Clear next step",
    2:  "Start with math",
    3:  "Compare calmly",
    4:  "The useful system",
    5:  "Clear next step",
    6:  "Clear next step",
    7:  "Start with math",
    8:  "Clear next step",
    9:  "The useful system",
    10: "The useful system",
    11: "Clear next step",
    12: "Compare calmly",
    13: "Start with math",
    15: "Compare calmly",
    16: "Clear next step",
    17: "Clear next step",
    18: "The useful system",
    19: "Start with math",
}


_RATIO_PATTERN = re.compile(r"\b(\d{1,3})[\s/](\d{1,3})[\s/](\d{1,3})\b")
_DOLLAR_WITH_PERIOD = re.compile(
    r"\$\s?(\d{1,3}(?:,\d{3})*(?:\.\d+)?(?:[Kk])?)\s?(?:/|per\s?)(month|mo|year|yr|week|wk|day|hr|hour)\b",
    re.I,
)
_PLAIN_DOLLAR = re.compile(r"\$\s?(\d{1,3}(?:,\d{3})*(?:\.\d+)?(?:[Kk])?)\b")
_PERCENT = re.compile(r"\b(\d+(?:\.\d+)?)%")
_AGE = re.compile(r"\bby\s+(\d{2})\b", re.I)
_WEEK_PLAN = re.compile(r"\b(\d+)[- ](week|day|month|year|line)\b", re.I)
_TEMP_F = re.compile(r"\b(\d{1,3})°F\b")


def _ratio_label(post_title: str) -> Optional[str]:
    m = _RATIO_PATTERN.search(post_title)
    if not m:
        return None
    return f"{m.group(1)}/{m.group(2)}/{m.group(3)} rule"


def _suffix_for_topic(topic_lower: str) -> str:
    if "rule" in topic_lower:
        return "plan"
    if "audit" in topic_lower:
        return "audit"
    return "plan"


def build_result_line(
    post_title: str,
    style_field: str,
    visible_text_old: list[str],
    topic_line: str,
) -> str:
    sources = " ".join([post_title, *visible_text_old])
    topic_lower = topic_line.lower()
    suffix = _suffix_for_topic(topic_lower)

    # Don't repeat ratio if the topic line already contains it
    if not _RATIO_PATTERN.search(topic_line):
        m = _RATIO_PATTERN.search(post_title)
        if m:
            return f"{m.group(1)}/{m.group(2)}/{m.group(3)} rule"

    m = _DOLLAR_WITH_PERIOD.search(sources)
    if m:
        return f"${m.group(1)}/{m.group(2).lower()} {suffix}"

    m = _PLAIN_DOLLAR.search(sources)
    if m:
        amt = m.group(1)
        return f"${amt} {suffix}"

    m = _PERCENT.search(sources)
    if m:
        return f"{m.group(1)}% {suffix}"

    m = _AGE.search(sources)
    if m:
        return f"By age {m.group(1)}"

    m = _WEEK_PLAN.search(sources)
    if m:
        return f"{m.group(1)}-{m.group(2).lower()} {suffix}"

    m = _TEMP_F.search(sources)
    if m:
        return f"{m.group(1)}°F plan"

    n = style_number(style_field) or 0
    fallback = NON_CLAIM_BY_STYLE.get(n, "Clear next step")
    # avoid colliding with the support line for the same style
    if fallback.lower() == SUPPORT_LINE_BY_STYLE.get(n, "").lower():
        fallback = "Clear next step" if fallback != "Clear next step" else "The useful system"
    return fallback


# --------------------------------------------------------------------------------------
# Old visible text extraction (so we can recover existing numbers / outcome phrases)
# --------------------------------------------------------------------------------------

def extract_old_visible_text(prompt: str) -> list[str]:
    m = re.search(r"VISIBLE TEXT:.*?\n((?:- .*\n?)+)", prompt, re.DOTALL)
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith("- "):
            v = line[2:].strip()
            v = v.strip('"').strip("'").strip()
            if v:
                out.append(v)
    return out


# --------------------------------------------------------------------------------------
# Prompt assembly
# --------------------------------------------------------------------------------------

NEW_TEMPLATE = """Wide landscape hero banner, 4096x2048 pixels, 2:1 ratio.
Premium flat editorial design for a personal finance blog.

Use a spacious layout with one dominant visual anchor, clear breathing room,
and strong hierarchy. The image should look like a finished website hero,
not a dense infographic, worksheet, dashboard, or classroom slide.

STYLE:
{mood}

DOMINANT VISUAL:
{dominant}

VISIBLE TEXT:
Render only this text, copied exactly:
- "{eyebrow}"
- "{topic}"
- "{result}"
- "{support}"

No other words, labels, captions, UI text, annotations, placeholder text,
or extra numbers.

Any card, panel, badge, chart, bar, grid, tree, device, paper, circle,
or desk element must stay unlabeled unless its text is listed above.

COLOR:
Near-white, warm cream, deep navy, and calm blue surfaces. Amber accents.
Green success details. No palette swatches, color chips, visible hex codes,
watermarks, website addresses, brand logos, brand-style marks, decorative
finance icons, shadows, 3D effects, bevels, or stock-finance props.{brand_guard}

QUALITY:
Crisp high-resolution editorial banner suitable for final 4096x2048 export.
Clean edges, readable text, balanced spacing, and calm premium composition.
"""

BRAND_GUARDRAIL = (
    "\nRender any company or product name as plain text only — no logo, "
    "no brand mark, no recognizable brand styling."
)


def repair_prompt(entry: dict) -> str:
    style_field = entry["style"]
    style_info = style_lookup(style_field)
    topic = build_topic(entry["primary_keyword"], entry["post_title"])
    old_visible = extract_old_visible_text(entry.get("prompt", ""))
    result = build_result_line(entry["post_title"], style_field, old_visible, topic)
    support = support_line(style_field)

    brand = detect_brand(entry["post_title"]) or detect_brand(entry["primary_keyword"])
    brand_guard = BRAND_GUARDRAIL if brand else ""

    return NEW_TEMPLATE.format(
        mood=style_info["mood"],
        dominant=style_info["dominant"],
        eyebrow=style_info["eyebrow"],
        topic=topic,
        result=result,
        support=support,
        brand_guard=brand_guard,
    )


# --------------------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------------------

BANNED_PHRASES = [
    "not an infographic or classroom chart",
    "Blue labels",
]
BANNED_SECTIONS = [
    "COMPOSITION:",
    "TYPOGRAPHY:",
    "TYPOGRAPHY HIERARCHY:",
    "CREATIVE DIRECTION:",
    "CRITICAL EXPORT RULES:",
    "SIMPLICITY OVERRIDE",
]
KEYWORD_SALAD_FRAGMENTS = [
    "Much Should Have", "Buying House 5", "Electric Bill Eia",
    "Electric Heating Heat", "Digit Now Oportun",
    "Challenges 12 Challenge", "Living Paycheck Paycheck",
]


def validate(prompt: str, entry: dict) -> list[str]:
    errors: list[str] = []
    if prompt.count("STYLE:") != 1:
        errors.append("STYLE section count != 1")
    if prompt.count("DOMINANT VISUAL:") != 1:
        errors.append("DOMINANT VISUAL section count != 1")
    if prompt.count("VISIBLE TEXT:") != 1:
        errors.append("VISIBLE TEXT section count != 1")

    m = re.search(r"VISIBLE TEXT:.*?\n((?:- .*\n?)+)", prompt, re.DOTALL)
    bullets = []
    if m:
        for line in m.group(1).splitlines():
            if line.strip().startswith("- "):
                bullets.append(line.strip())
    if not (3 <= len(bullets) <= 4):
        errors.append(f"visible text bullets={len(bullets)} (need 3 or 4)")
    norm = [b.lower() for b in bullets]
    if len(set(norm)) != len(norm):
        errors.append(f"duplicate visible text bullets: {bullets}")

    for sec in BANNED_SECTIONS:
        if sec in prompt:
            errors.append(f"banned section present: {sec}")
    for ph in BANNED_PHRASES:
        if ph.lower() in prompt.lower():
            errors.append(f"banned phrase present: {ph}")
    for frag in KEYWORD_SALAD_FRAGMENTS:
        if frag.lower() in prompt.lower():
            errors.append(f"keyword-salad fragment in output: {frag}")

    return errors


def assert_other_fields_unchanged(old_entry: dict, new_entry: dict) -> None:
    for k in old_entry:
        if k == "prompt":
            continue
        if old_entry[k] != new_entry[k]:
            raise AssertionError(
                f"non-prompt field '{k}' changed for record {old_entry.get('record_index')}"
            )


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------

def repair(data: dict, limit: Optional[int]) -> dict:
    queue = data["queue"]
    if limit is not None:
        queue = queue[:limit]

    new_queue = []
    all_errors: list[tuple[int, str, list[str]]] = []
    for entry in queue:
        new_entry = dict(entry)
        new_entry["prompt"] = repair_prompt(entry)
        assert_other_fields_unchanged(entry, new_entry)
        errs = validate(new_entry["prompt"], new_entry)
        if errs:
            all_errors.append((entry["record_index"], entry["slot"], errs))
        new_queue.append(new_entry)

    if all_errors:
        msg = "\n".join(f"  rec {r}/{s}: {e}" for r, s, e in all_errors)
        raise SystemExit(f"validation failed:\n{msg}")

    return {"meta": data["meta"], "queue": new_queue}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("test", "final"), required=True)
    args = parser.parse_args()

    with SRC.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if args.mode == "test":
        out = repair(data, limit=20)
        out_path = TEST_OUT
    else:
        out = repair(data, limit=None)
        out_path = FULL_OUT

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Total entries rebuilt: {len(out['queue'])}")
    print(f"Output: {out_path.name}")


if __name__ == "__main__":
    main()
