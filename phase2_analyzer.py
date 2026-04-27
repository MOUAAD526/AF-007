#!/usr/bin/env python3
"""
Phase 2 — Competitor Body Text Analysis
========================================
Reads the .json sidecar files produced by Phase 1 (enriched by watcher).
Cross-references Pre_Post.jsonl for social signals per record.
For each file:
  1. Sends article_context + JSONL social signals + competitor data to LLM
  2. Appends the Battle Plan Brief to the matching .md file (clean sentinel block)
  3. Saves battle_plan_generated_at flag to JSON sidecar (preserves body_text)

Usage:
    python phase2_analyzer.py                  # Process all sidecars in latest run
    python phase2_analyzer.py --limit 5        # Process first 5 only
    python phase2_analyzer.py --start-from 10  # Resume from index 10
    python phase2_analyzer.py --watch          # Keep running, wait for new files
    python phase2_analyzer.py --dry-run        # Validate inputs, no LLM calls
"""

import argparse
import json
import logging
import os
import sys
import time
import shutil
from datetime import datetime, timezone
from pathlib import Path

# import httpx (removed for manual agent mode)

# ---------------------------------------------------------------------------
# SECRETS — loaded from .env
# ---------------------------------------------------------------------------
_ENV_CANDIDATES = [
    Path(__file__).resolve().parent.parent / "project_root" / ".env",
    Path(__file__).resolve().parent / ".env",
    Path(".env"),
]
for _env_path in _ENV_CANDIDATES:
    if _env_path.exists():
        for _line in _env_path.read_text(encoding="utf-8").splitlines():
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _, _v = _line.partition("=")
                _k = _k.strip()
                _v = _v.strip().strip('"').strip("'")
                if _k and _k not in os.environ:
                    os.environ[_k] = _v

# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------
PROJECT_ROOT        = Path(__file__).parent
PHASE1_ROOT         = PROJECT_ROOT
PRE_POST_JSONL      = PROJECT_ROOT / "Pre_Post.jsonl"
DEFAULT_RUN_DIR     = PROJECT_ROOT / "run 1"
# OPENROUTER_KEY      = os.environ.get("OPENROUTER_API_KEY", "")
# MODEL               = "deepseek/deepseek-v4-flash"
MIN_BODY_CHARS      = 200
DELAY_BETWEEN_CALLS = 5  # Reduced since agent takes time to write
BATTLE_PLAN_SENTINEL = "<!-- BATTLE_PLAN_BRIEF -->"

# ---------------------------------------------------------------------------
# LOGGING
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("phase2")


# ---------------------------------------------------------------------------
# JSONL LOADER
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# BACKUP UTILITY (Global Rule #4)
# ---------------------------------------------------------------------------
def backup_file(file_path: Path):
    """Moves the file to a 'Previous Versions' folder with a timestamp suffix."""
    if not file_path.exists():
        return

    backup_dir = file_path.parent / "Previous Versions"
    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
    backup_path = backup_dir / backup_name

    print(f"BACKUP: Moving {file_path} to {backup_path}")
    time.sleep(1)

    shutil.move(str(file_path), str(backup_path))


def load_jsonl_index(path: Path) -> dict[str, dict]:
    """Load Pre_Post.jsonl and index by primary_keyword (lowercase)."""
    index = {}
    if not path.exists():
        logger.warning(f"Pre_Post.jsonl not found at {path}")
        return index
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
                kw = (record.get("primary_keyword") or "").strip().lower()
                if kw:
                    index[kw] = record
            except Exception:
                pass
    logger.info(f"Loaded {len(index)} records from Pre_Post.jsonl")
    return index


# ---------------------------------------------------------------------------
# ANALYSIS PROMPT
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """You are a Senior SEO Content Strategist for Adulting Finance, a personal finance blog.
Target audience: adults aged 18–55 who are stressed, frustrated, or anxious about money.

Your output will be used by two downstream teams:
  - WRITING LLM: uses content_gaps, nlp_entities, eeat_requirements,
    style_critique, and reader_psychology to write the full article.
  - HOOKS & TITLES LLM: uses title_intelligence and reader_psychology
    to write title variants and article opening hooks.

Vague output = a bad article. Concrete, evidence-based output = a winning article.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MANDATORY RULES — READ BEFORE DOING ANYTHING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THINK STEP BY STEP. DO NOT RUSH.
Reason through every task fully before writing any output.
Before putting anything in any field, ask:
"Can I point to the exact place in the input where this came from?"
If the answer is no → apply the SKIP RULE.

NO-INVENTION RULE (no exceptions, applies to every single field):
- Do NOT add JSON fields that are not in the output schema.
- Do NOT add any tags, markers, or labels anywhere in any field.
  These are all banned: [PIN] [CTA] [IMAGE] [TOOL] [TABLE] [PRINTABLE] [VIDEO] [AD]
- Do NOT invent statistics, study names, or data points.
  Only use data found in competitor body_text or paa_questions answers.
- Do NOT use Reddit, TikTok, Twitter, or forum quotes as authority signals. Ever.
- Do NOT rename schema fields. Use the exact field names from the schema.
- Do NOT copy competitor sentences verbatim.

SKIP RULE:
If the input does not give you enough real evidence to fill a field confidently,
output null or [] for that field and move to the next task.
A correct null is always better than a guessed or invented answer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IS ACTUALLY IN YOUR INPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read this section carefully before analyzing anything.

FROM article_context:
  angle            → OUR planned content angle. Not a competitor angle.
  pain_points      → Pre-identified pain points from our enrichment process.
  top_social_questions → Pre-identified questions from our enrichment. Different
                     from JSONL social_questions. Both are valuable, different sources.
  dominant_emotion → The single dominant emotional state for this keyword audience.
  serp_intent      → What the searcher actually wants from this keyword.
  serp_title_pool  → Real SERP titles from 3 pools: primary, long_tail, question.
                     Use all 3 pools for title_intelligence.
  paa_questions    → Real Google PAA questions with Google-pulled answers.
                     These are high-value. Use for content_gaps, eeat_requirements,
                     nlp_entities, and title_intelligence.
  related_searches → Google's related search suggestions for this keyword.
                     Use for nlp_entities and title_intelligence pattern analysis.

FROM Social Signals (JSONL — when present, sourced from real reader posts):
  signal_summary   → Pre-written overview of all signals. Read this first to orient.
  pain_points      → Raw pain points from actual social posts. More specific and
                     authentic than article_context.pain_points.
  emotional_states → The real emotional states readers are in for this topic.
  angles           → Different framings readers use. Feed into content_gaps.
  social_questions → Exact questions readers asked in real posts. Feed into content_gaps.
  seo_questions    → SEO-framed versions of social questions. Feed into content_gaps.
  repeated_phrases → Exact phrases that appear repeatedly in reader posts.
                     These are the words the reader thinks in. Use in directives
                     and reader_psychology.

FROM competitors[] — for each competitor:
  rank         → SERP position.
  domain       → Website domain.
  title        → Their article title. Use for title_intelligence.
  word_count   → Words scraped. 0 or very low = blocked page or product page.
  scrape_status → "success" or "failed".
  body_text    → The article content. Capped at 8000 characters. Your only
                 competitor content source.
  headings     → ALWAYS EMPTY []. Ignore completely.
                 The line "H2 Headings: (none extracted)" appears in every competitor
                 block. It is always empty. Do not reference it or draw conclusions from it.

WHICH COMPETITORS TO ANALYZE:
  Only analyze competitors where ALL THREE of these are true:
    - scrape_status is "success"
    - body_text is not null
    - word_count is above 200
  Competitors failing any condition have no real content. Skip them entirely.
  Do not mention them in your output.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK 1 — CONTENT GAP ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Find exactly 3 things competitors failed to answer or answered poorly.

HOW TO FIND THEM:
  Step 1: Read ALL valid competitor body_text fully before choosing any gap.
  Step 2: Cross-reference against our angle, JSONL angles, social_questions,
          seo_questions, and paa_questions.
  Step 3: Choose the 3 gaps that create the strongest competitive advantage.
          Do not pick the first 3 you notice.

Each gap has exactly these 3 fields:

  "name" → 3–6 words. A short label only.

  "what_they_missed" →
    What competitors said OR specifically failed to say.
    Name the domain or describe their exact approach.
    Show evidence from their body_text.
    Never write "competitors failed to cover X" without naming WHO and WHERE.

  "our_edge" →
    What our article must do concretely. Must include ALL of:
    - The section type (H2, comparison table, numbered list, callout)
    - The method or framework name if applicable
    - The specific steps or data points the writer must include
    - One concrete example showing what this looks like in the article

GOOD "our_edge":
  "Add an H2: 'What to Do With Your $5,050 After Day 100.'
   Build a 3-row decision table — columns: Goal | Action | Why It Works.
   Row 1: No emergency fund → Move $1,000 to a 4%+ HYSA immediately.
   Row 2: High-interest debt → Apply the rest to the highest-rate balance first.
   Row 3: Both covered → Open a Roth IRA with the remaining amount.
   Source: paa_question 'What should you do with your $5,050 after the challenge?'
   which ramseysolutions.com mentioned but never answered with a real decision framework."

BAD "our_edge" (never do this):
  "Cover what readers should do with their savings after the challenge."
  → No section type. No table. No steps. No example. The writer cannot act on this.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK 2 — SEMANTIC NLP ENTITIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Extract 10–15 non-obvious terms Google NLP expects in a winning article on this topic.

SOURCES — pull from all of these:
  - Valid competitor body_text: what specific terminology do they use?
  - paa_questions[].a: what terms appear in Google's own answers?
  - related_searches: what keyword patterns does Google associate with this topic?
  - JSONL repeated_phrases and angles: what terms do readers use naturally?

BEFORE including any term, apply this test:
  Q1: Would a personal finance beginner know this term without looking it up?
  Q2: Is this term already in the primary keyword, main title, or angle?
  If YES to either → exclude it.

DEDUPLICATION RULE:
  If two terms describe the same concept → keep only the most specific one.
  Example: never include both "dopamine hit" and "dopamine-driven behavior" —
  keep only "behavioral substitution loop."

GOOD entities:
  "incremental deposit structure", "gamified savings mechanic",
  "cash envelope methodology", "sinking fund buffer",
  "progressive contribution schedule", "opportunity cost of idle cash",
  "behavioral substitution loop", "micro-commitment savings"

BAD entities (never include):
  "save money", "budget", "emergency fund", "fixed expenses",
  "variable costs", "track spending" — all too basic for this audience.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK 3 — E-E-A-T REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Output 2–3 specific data points or trust signals our article must include.

VALID sources — only these:
  - Named institutional statistics with source and year
    Example: "U.S. Bureau of Economic Analysis: personal savings rate ~4%, 2023"
  - Named studies or surveys found in competitor body_text
  - Specific numerical data from paa_questions[].a that competitors ignored or buried
  - Named tools or calculators cited in valid competitor body_text

INVALID — never use as E-E-A-T:
  - Reddit, TikTok, Twitter, forum posts or quotes
  - "Experts say..." with no named expert or study
  - Any number or statistic not found in the input data

SKIP RULE: Cannot find a real verifiable signal → output null. Never invent one.

GOOD E-E-A-T item:
  "paa_questions confirm the exact total: $5,050 from summing $1 through $100.
   Pair this with the U.S. personal savings rate (~4%, BEA 2023) to show the reader
   that completing this challenge puts them statistically far above the average
   American — and why a real system is required to get there, not just intention."

BAD E-E-A-T item (never do this):
  "Quote the social signal 'I tracked everything and still ended up broke'
   to establish authority."
  → A reader comment is not an authority signal. Remove it.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK 4 — WRITING STYLE ANALYSIS & DECISION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Only analyze competitors where scrape_status is "success", body_text is not null,
and word_count is above 200.

Step A — LIST all distinct tones found across valid competitor body_text.
  Name which domain used each tone.
  Minimum 2 tones. If all valid competitors share one tone, list all domains under it.

Step B — PICK exactly ONE winning tone using this strict priority order:

  Priority 1 — JSONL emotional_states and pain_points (from real reader posts).
    Match tone to the emotional state readers are ACTUALLY in right now.
      "shame or embarrassment"         → validation first, gentle instruction second.
      "frustration after failure"      → direct, system-focused, no motivational fluff.
      "confusion about where to start" → structured, step-by-step, minimal jargon.
      "excited but overwhelmed"        → energetic but organized, clear milestones.

  Priority 2 — article_context.dominant_emotion.
    What emotional state does our angle create in the reader?

  Priority 3 — The gap competitors collectively left open.
    All clinical and formal → conversational wins.
    All casual and gamified → structured authority wins.
    All generic → hyper-specific and data-driven wins.

  Priority 4 — serp_intent keyword type.
    Informational (how-to, what is, guide) → warm, educational, patient.
    Transactional or comparison → direct, confident, efficient.

Step C — State decision reason in EXACTLY this format:
  "Priority [N] fired — [exact signal from input, quoted or closely paraphrased] —
   [what specific gap this tone fills that competitors missed]"

GOOD decision_reason:
  "Priority 1 fired — JSONL emotional_state 'confusion and frustration' +
   article_context.dominant_emotion 'Confusion and Frustration' +
   JSONL pain_point 'collecting tracking data without knowing what to do with it' —
   A structured, step-by-step tone fills the gap left by gamified challenge content
   that makes saving look fun but never explains the system behind it."

BAD decision_reason (never do this):
  "Priority 1 fired — Frustration — Reader needs a direct tone."
  → Does not quote the actual signal. Does not name the gap filled.

Step D — Output 3–5 writing directives.
Every directive must be a REPEATABLE RULE applied to every relevant paragraph.
Not a one-time example. A rule that governs every instance of the same situation.

FORMAT: "When [situation], always [action]. Never [opposite]."

GOOD directive:
  "When referencing any cost or recurring charge, always name a specific dollar amount.
   Never write 'subscription fees' — write '$14.99/month streaming subscription.'
   Pull real dollar amounts from JSONL repeated_phrases when available."

BAD directive (never do this):
  "Call out the forgotten $89 gym membership."
  → One specific example disguised as a rule. Cannot be applied elsewhere.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK 5 — READER PSYCHOLOGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analyze the emotional transition the reader must make through the article.

Use these sources in this priority order:
  1. JSONL emotional_states, repeated_phrases, pain_points — most authentic.
  2. article_context.dominant_emotion and top_social_questions.
  3. article_context.pain_points and paa_questions tone — if JSONL is absent.

Output EXACTLY these 3 fields — no more, no fewer:

  "triggering_thought" →
    The specific anxious or frustrated thought that caused this search.
    Closely derived from a real signal in the input. Quote or paraphrase it.
    1–2 sentences maximum.

  "desired_internal_shift" →
    The emotional state change the article must create.
    Format: "From [initial state] to [target state]." One phrase only.

  "bridge_content" →
    The specific section or method that creates this shift.
    Name it concretely. Reference a content gap from Task 1 if applicable.
    You may include a short analogy here as a sentence — not as a new field.

FIELDS THAT ARE BANNED — never add these:
  "power_analogy", "key_insight", "metaphor", "hook",
  "summary", "emotional_arc", "conversion_note"
  If you want an analogy → one sentence inside bridge_content. Not a new field.

GOOD output:
  {
    "triggering_thought": "I've been tracking my spending for months and I'm still
      broke at the end of every week. The problem must be me, not my system.",
    "desired_internal_shift": "From Self-Blaming Tracker to Confident System Builder",
    "bridge_content": "The incremental deposit structure section — reframing failure
      as a design problem, not a discipline problem. Like a leaking pipe: the fix
      is not to carry water harder, it is to replace the pipe."
  }

BAD output (never do this):
  {
    "triggering_thought": "...",
    "desired_internal_shift": "...",
    "bridge_content": "...",
    "power_analogy": "Willpower is a bucket; automation is a dam."
  }
  → "power_analogy" is not in the schema. It is forbidden.
  → Place the analogy as a sentence inside bridge_content instead.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TITLE INTELLIGENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before writing titles, analyze ALL of these:
  - serp_title_pool.primary, long_tail, and question — all 3 pools combined.
  - Each valid competitor's title field.
  - related_searches — keyword patterns Google connects to this topic.
  - article_context.angle and content gaps from Task 1 — your differentiation source.

Output EXACTLY these 3 fields:

  "dominant_title_pattern" →
    The formula most competitors use across all 3 SERP pools combined.
    Be specific about structure and recurring elements.
    Example: "Number-led challenge + savings total amount + '(Free Printable)' suffix"

  "short_title" →
    Our differentiated title for the HTML <title> tag in Google search results.
    MAXIMUM 60 CHARACTERS including every space and punctuation mark.
    COUNT every character before outputting. If over 60 → shorten first.
    Must differ meaningfully from competitor titles.
    Must reflect our angle or a content gap — not a minor rewording of what exists.

  "long_title" →
    Longer version for the article H1 heading or Pinterest pin.
    MAXIMUM 80 CHARACTERS including every space and punctuation mark.
    COUNT every character before outputting. If over 80 → shorten first.

The field "our_differentiation" does not exist. Never output it.

GOOD output:
  {
    "dominant_title_pattern": "Number-led challenge + $5,050 savings total + '(Free Printable)' or '(PDF)' suffix",
    "short_title": "1-100 Savings Chart: What to Do After Day 100",
    "long_title": "The 1-100 Money Saving Chart — And the Plan for What Comes Next"
  }
  → short_title = 45 characters ✓   long_title = 62 characters ✓

BAD output (never do this):
  {
    "dominant_title_pattern": "...",
    "our_differentiation": "Save $5,050 With the 1-100 Savings Chart: A Complete Step-by-Step Guide to What Comes After"
  }
  → "our_differentiation" does not exist in the schema.
  → Title is 91 characters — exceeds the 80-character limit.
  → Missing "short_title" and "long_title" as separate required fields.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GLOBAL RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1.  Do NOT reproduce competitor sentences verbatim.
2.  Do NOT invent statistics not present in the input data.
3.  Do NOT add JSON fields not in the output schema.
4.  Do NOT add tags, markers, or notation anywhere ([PIN], [CTA], etc.).
5.  Do NOT use social quotes as E-E-A-T authority signals.
6.  Every claim must trace to a specific field in the input. If it cannot → skip it.
7.  If evidence is insufficient for a field → output null or []. Never guess.
8.  Only analyze competitors where scrape_status is "success", body_text is
    not null, and word_count is above 200.
9.  Ignore "H2 Headings: (none extracted)" in every competitor block.
    Headings are always empty in the input. That line carries no information.
10. Output only valid JSON. No intro text. No explanation. No markdown wrapper.
11. Reason step by step through each task before writing any output. Do not rush.
12. Keep total output under 1400 words.
"""


def build_user_prompt(
    article_context: dict,
    competitors: list[dict],
    jsonl_record: dict | None,
) -> str:
    serp_title_pool  = article_context.get("serp_title_pool", {})
    paa_questions    = article_context.get("paa_questions", [])
    related_searches = article_context.get("related_searches", [])

    core_context = {
        k: v for k, v in article_context.items()
        if k not in ("serp_title_pool", "paa_questions", "related_searches")
    }

    comp_blocks = []
    for c in competitors:
        title         = (c.get("title") or "").strip()
        headings      = c.get("headings", [])
        body          = (c.get("body_text") or "").strip()
        headings_text = " | ".join(headings) if headings else "(none extracted)"
        comp_blocks.append(
            f"--- Competitor #{c['rank']} ({c['domain']}, {c.get('word_count', '?')}) ---\n"
            f"Title: {title}\n"
            f"H2 Headings: {headings_text}\n"
            f"Body:\n{body[:8000]}"
        )

    paa_text = "\n".join(
        f"Q: {item.get('q', '')}\nA: {item.get('a', '')}"
        for item in paa_questions
    ) if paa_questions else "(none)"

    related_text = "\n".join(f"- {t}" for t in related_searches) if related_searches else "(none)"

    if jsonl_record:
        social_block = f"""
## Social Signals (from Pre_Post.jsonl)
Pain Points:
{json.dumps(jsonl_record.get("pain_points", []), indent=2)}

Emotional States:
{json.dumps(jsonl_record.get("emotional_states", []), indent=2)}

Angles:
{json.dumps(jsonl_record.get("angles", []), indent=2)}

Social Questions:
{json.dumps(jsonl_record.get("social_questions", []), indent=2)}

SEO Questions:
{json.dumps(jsonl_record.get("seo_questions", []), indent=2)}

Repeated Phrases (from social):
{json.dumps(jsonl_record.get("repeated_phrases", []), indent=2)}

Signal Summary:
{json.dumps(jsonl_record.get("signal_summary", {}), indent=2)}
"""
    else:
        social_block = "\n## Social Signals\n(No matching Pre_Post.jsonl record found)\n"

    return f"""## Article Context
{json.dumps(core_context, indent=2)}

## SERP Title Pool (primary + long-tail + question SERPs)
{json.dumps(serp_title_pool, indent=2)}

## People Also Ask (Google-validated questions + answers)
{paa_text}

## Related Searches (secondary intent signals)
{related_text}
{social_block}
## Competitor Articles ({len(competitors)} articles)
{"\n\n".join(comp_blocks)}

## Your Output — output ONLY this JSON, no markdown wrapper:

{{
  "content_gaps": [
    {{
      "name": "short gap name",
      "what_they_missed": "what competitors said or failed to say",
      "our_edge": "what our article must specifically do better"
    }}
  ],
  "nlp_entities": [
    "non-obvious term or jargon the writer must weave in naturally"
  ],
  "eeat_requirements": [
    "specific stat, study, or trust signal our article must include"
  ],
  "style_critique": {{
    "all_tones_found": [
      {{ "tone": "formal instructional", "used_by": "domain1.com, domain2.com" }}
    ],
    "winning_tone": "the single tone our article must use",
    "decision_reason": "Priority N fired — [specific signal] — [gap this fills]",
    "our_directives": [
      "specific actionable writing instruction"
    ]
  }},

"title_intelligence": {{
    "dominant_title_pattern": "formula used by most competitors across all 3 SERP pools",
    "short_title": "our differentiated title — MAX 60 characters including spaces",
    "long_title": "longer version — MAX 80 characters including spaces"
}},
  "reader_psychology": {{
    "triggering_thought": "the specific fear or thought that caused the search",
    "desired_internal_shift": "from [initial emotion] to [target emotion]",
    "bridge_content": "the specific piece of information that creates this shift"
  }},
  "internal_linking": null
}}

Rules:
- content_gaps: exactly 3 items
- nlp_entities: 10 to 15 items
- eeat_requirements: 2 to 3 items
- style_critique.all_tones_found: list every distinct tone found, min 2
- style_critique.winning_tone: exactly 1, never a list
- style_critique.decision_reason: must name the priority number and the exact signal
- style_critique.our_directives: 3 to 5 specific instructions
- title_intelligence: always present
- reader_psychology: must be detailed based on emotional signals
- internal_linking: always null
- Keep total output under 1400 words
"""


# ---------------------------------------------------------------------------
# AGENT INTERACTIVE CALL
# ---------------------------------------------------------------------------
def call_llm_via_agent(user_prompt: str, run_dir: Path) -> dict:
    """
    Instead of calling an API, we save the prompt and wait for the agent 
    to provide the JSON response in a file.
    """
    task_path = run_dir / "current_analysis_task.md"
    resp_path = run_dir / "current_analysis_response.json"

    # 1. Prepare the full prompt for the agent
    full_prompt = f"# SYSTEM PROMPT\n{SYSTEM_PROMPT}\n\n# USER PROMPT\n{user_prompt}"
    task_path.write_text(full_prompt, encoding="utf-8")

    print(f"\n" + "="*60)
    print(f"AGENT TASK GENERATED: {task_path.name}")
    print(f"1. Please read the prompt in: {task_path}")
    print(f"2. Provide your analysis as a raw JSON object.")
    print(f"3. SAVE your response to: {resp_path}")
    print(f"Waiting for response file...")
    print("="*60 + "\n")

    # 2. Wait for the agent to create the response file
    while not resp_path.exists():
        time.sleep(2)

    # 3. Read and parse the response
    try:
        raw = resp_path.read_text(encoding="utf-8").strip()
        
        # Strip markdown code blocks if the agent included them
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[-1]
            raw = raw.rsplit("```", 1)[0]
        
        data = json.loads(raw)
        
        # 4. Clean up temporary files
        task_path.unlink(missing_ok=True)
        resp_path.unlink(missing_ok=True)
        
        return data
    except Exception as e:
        print(f"ERROR PARSING AGENT RESPONSE: {e}")
        print("Please fix the JSON in the response file and the script will try again.")
        # We don't unlink so the user can fix it
        while resp_path.exists():
            time.sleep(2)
            return call_llm_via_agent(user_prompt, run_dir) # Recursive retry


# ---------------------------------------------------------------------------
# MD APPENDER — clean, non-destructive
# ---------------------------------------------------------------------------
def append_battle_plan_to_md(
    md_path: Path,
    battle_plan: dict,
    primary_kw: str,
    generated_at: str,
    article_context: dict,
    force: bool = False,
) -> bool:
    try:
        existing = md_path.read_text(encoding="utf-8")
    except Exception as exc:
        logger.error(f"Cannot read {md_path.name}: {exc}")
        return False

    if BATTLE_PLAN_SENTINEL in existing:
        logger.warning(f"  Battle plan already in {md_path.name} — skipping md write")
        return True

    # Prepare Strategic Research Summary
    pain_points = article_context.get("pain_points", [])
    title_pool  = article_context.get("serp_title_pool", {})
    
    research_block = (
        f"\n\n---\n"
        f"## Strategic Research Summary\n"
        f"**Dominant Emotion:** {article_context.get('dominant_emotion', 'Unknown')}\n\n"
        f"### Core Pain Points\n"
        + "\n".join([f"- {p}" if isinstance(p, str) else f"- {p.get('theme', '')}" for p in pain_points]) +
        f"\n\n### SERP Title Pool\n"
        f"- **Primary:** {len(title_pool.get('primary', []))} titles\n"
        f"- **Long-tail:** {len(title_pool.get('long_tail', []))} titles\n"
        f"- **Question:** {len(title_pool.get('question', []))} titles\n"
    )

    battle_block = (
        f"\n\n---\n"
        f"{BATTLE_PLAN_SENTINEL}\n"
        f"# Battle Plan Brief\n"
        f"**Generated:** {generated_at}  \n"
        f"**Keyword:** {primary_kw}\n\n"
        f"```json\n"
        f"{json.dumps(battle_plan, indent=2, ensure_ascii=False)}\n"
        f"```\n"
        f"<!-- END_BATTLE_PLAN_BRIEF -->\n"
    )

    try:
        backup_file(md_path)
        md_path.write_text(existing + research_block + battle_block, encoding="utf-8")
        return True
    except Exception as exc:
        logger.error(f"Cannot write to {md_path.name}: {exc}")
        return False


# ---------------------------------------------------------------------------
# CORE PROCESSOR
# ---------------------------------------------------------------------------
def process_sidecar(
    sidecar_path: Path,
    jsonl_index: dict[str, dict],
    run_dir: Path,
    dry_run: bool = False,
    force: bool = False,
) -> bool:
    with open(sidecar_path, "r", encoding="utf-8") as f:
        sidecar = json.load(f)

    article_context = sidecar.get("article_context")
    competitors     = sidecar.get("competitors", [])
    primary_kw      = sidecar.get("primary_keyword", sidecar_path.stem)

    if not article_context:
        logger.warning(f"  No article_context in {sidecar_path.name} — skipping")
        return False

    if "serp_title_pool" not in article_context:
        logger.warning(f"  Watcher not done yet for {sidecar_path.name} — skipping")
        return False

    md_path = sidecar_path.with_suffix(".md")
    if not md_path.exists():
        logger.warning(f"  No matching .md for {sidecar_path.name} — skipping")
        return False

    if BATTLE_PLAN_SENTINEL in md_path.read_text(encoding="utf-8"):
        logger.info(f"  Already processed: {md_path.name} — skipping")
        return False

    jsonl_record = jsonl_index.get(primary_kw.strip().lower())
    if not jsonl_record:
        logger.warning(f"  No JSONL record for '{primary_kw}' — continuing without social signals")

    valid_competitors = [
        c for c in sorted(competitors, key=lambda x: x.get("rank", 99))
        if len((c.get("body_text") or "").strip()) >= MIN_BODY_CHARS
    ]

    if not valid_competitors:
        logger.warning(f"  No body text >= {MIN_BODY_CHARS} chars — skipping")
        return False

    logger.info(
        f"  {len(valid_competitors)} competitors | "
        f"PAA: {len(article_context.get('paa_questions', []))} | "
        f"Related: {len(article_context.get('related_searches', []))} | "
        f"JSONL: {'yes' if jsonl_record else 'no'}"
    )

    if dry_run:
        logger.info(f"  [DRY-RUN] Would analyze '{primary_kw}'")
        return True

    logger.info(f"  Preparing prompt for '{primary_kw}'...")
    user_prompt  = build_user_prompt(article_context, valid_competitors, jsonl_record)
    battle_plan  = call_llm_via_agent(user_prompt, run_dir)
    generated_at = datetime.now(timezone.utc).isoformat()

    if not append_battle_plan_to_md(md_path, battle_plan, primary_kw, generated_at, article_context, force=force):
        logger.error(f"  Failed to write battle plan to {md_path.name}")
        return False

    sidecar["battle_plan_generated_at"]   = generated_at
    sidecar["competitors_analyzed_count"] = len(valid_competitors)

    # Save updated sidecar (preserves body_text as requested)
    backup_file(sidecar_path)
    with open(sidecar_path, "w", encoding="utf-8") as f:
        json.dump(sidecar, f, indent=2, ensure_ascii=False)

    logger.info(f"  Done: {md_path.name} updated | {sidecar_path.name} preserved with analysis metadata")
    return True


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Phase 2 — Competitor Body Analysis")
    parser.add_argument("--input-dir",  type=str, default="", help="Specific run folder to process")
    parser.add_argument("--limit",      type=int, default=0,  help="Process only first N sidecars")
    parser.add_argument("--start-from", type=int, default=0,  help="Start from index N")
    parser.add_argument("--delay",      type=int, default=DELAY_BETWEEN_CALLS, help="Seconds between LLM calls")
    parser.add_argument("--only",       nargs="+", default=[], help="Exact serp JSON filenames or stems to process")
    parser.add_argument("--force",      action="store_true",  help="Reprocess selected files even if already marked done")
    parser.add_argument("--watch",      action="store_true",  help="Keep running, wait for new files")
    parser.add_argument("--dry-run",    action="store_true",  help="Validate inputs, no LLM calls")
    args = parser.parse_args()

    if args.input_dir:
        input_dir = Path(args.input_dir)
    else:
        if DEFAULT_RUN_DIR.exists():
            input_dir = DEFAULT_RUN_DIR
        else:
            run_folders = sorted([d for d in PHASE1_ROOT.glob("run_*") if d.is_dir()])
            if not run_folders:
                logger.error(f"No run folders found in {PHASE1_ROOT}")
                sys.exit(1)
            input_dir = run_folders[-1]

    jsonl_index = load_jsonl_index(PRE_POST_JSONL)

    logger.info(f"Run folder:  {input_dir}")
    logger.info(f"JSONL index: {len(jsonl_index)} records")
    logger.info(f"Watch mode:  {'ON' if args.watch else 'OFF'}")
    logger.info(f"Delay:       {args.delay}s between LLM calls")
    logger.info(f"Min body:    {MIN_BODY_CHARS} chars")

    total_processed = 0

    while True:
        sidecar_files = sorted(input_dir.glob("serp_*.json"))
        if args.only:
            wanted = set()
            for item in args.only:
                name = Path(item).name
                wanted.add(name)
                wanted.add(Path(name).stem)
            sidecar_files = [path for path in sidecar_files if path.name in wanted or path.stem in wanted]
        if not sidecar_files and not args.watch:
            logger.error(f"No serp_*.json files found in {input_dir}")
            sys.exit(1)

        start = args.start_from
        end   = start + args.limit if args.limit > 0 else len(sidecar_files)
        batch = sidecar_files[start:end]

        unprocessed = []
        for path in batch:
            try:
                data    = json.loads(path.read_text(encoding="utf-8"))
                md_path = path.with_suffix(".md")
                already_done = (
                    "battle_plan_generated_at" in data or
                    (md_path.exists() and BATTLE_PLAN_SENTINEL in md_path.read_text(encoding="utf-8"))
                )
                if args.force or not already_done:
                    unprocessed.append(path)
            except Exception:
                pass

        if not unprocessed:
            if args.watch:
                logger.info("No new files. Waiting 30s...")
                time.sleep(30)
                continue
            else:
                logger.info("All files already processed. Done.")
                break

        logger.info(f"Found {len(unprocessed)} unprocessed files")

        for i, path in enumerate(unprocessed):
            logger.info(f"[{i+1}/{len(unprocessed)}] {path.name}")
            try:
                if process_sidecar(path, jsonl_index, input_dir, dry_run=args.dry_run, force=args.force):
                    total_processed += 1
                    if not args.dry_run and i < len(unprocessed) - 1:
                        time.sleep(args.delay)

                if args.limit > 0 and total_processed >= args.limit:
                    logger.info(f"Reached limit of {args.limit}.")
                    return

            except Exception as e:
                logger.error(f"  ERROR: {e}")

        if not args.watch:
            break

    logger.info(f"Done — Total processed: {total_processed}")


if __name__ == "__main__":
    main()
