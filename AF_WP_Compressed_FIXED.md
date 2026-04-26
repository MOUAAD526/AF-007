# AF WRITING PLAYBOOK — COMPRESSED PRODUCTION REFERENCE
**Version:** v15 Compression Pass — Patches 1–9 Applied (§5.1–§5.7 + §5.10 restored; §5.8, §5.9, §7-A, §7-B, §7-C Cheat Sheets, §6.3 Decision Trees, §7.5 supplementary QA, Article Brief Field Summary)
**Format:** Operational Rules + Swipe Files Only
**Purpose:** Load this alongside the core playbook. All pedagogical narrative removed. 100% of operational data preserved. File is production-ready for Full Draft Mode, Refresh Mode, and all session types.

---

SECTION 0: THE AF PLAYBOOK OPERATING SYSTEM

---

0-A: What This Document Is

This playbook is the single-source-of-truth knowledge base governing all content production for Adulting Finance. It controls every dimension of AF output: voice and tone, article structure, SEO and GEO optimization, conversion architecture, trust and E-E-A-T compliance, and visual formatting systems. Any AI writing assistant, human writer, or editor must load this document — or the Runtime Brief (Companion Asset 10) — before producing, revising, or reviewing any AF content. No exceptions exist for experienced writers or routine assignments; the rules apply uniformly to every session.

---

0-B: Session Sequence

Every content production session must follow these nine steps in order. Steps may not be skipped or resequenced.

1. Load the Playbook (or Runtime Brief). Confirm the most current version is loaded. If any section has been updated since the last session, reload the full document.
Multi-session handoff rule: For projects that span more than one session (e.g., competitor audit in Session A, drafting in Session B), load the completed Article Brief from the previous session alongside the Playbook at the start of every subsequent session. The Article Brief is the handoff document. It must contain: locked writing style, locked persona, tone dial settings, word count target, H2/H3 outline, competitor audit findings summary, and original contribution statement. A session that resumes without a completed Article Brief must restart from Step 2.
2. Receive or draft the Article Brief (Companion Asset 1). The brief must be complete before writing begins. Missing fields in the brief are not optional — resolve them before proceeding to Step 3.
Incomplete Brief Fallback: If required fields remain missing after one explicit request, apply this hierarchy: (1) Fields that are resolvable by logic (post type, persona, tone dial) — resolve using the rules in this playbook and flag the assumption in the output header. (2) Fields requiring external data (target keyword, competitor URLs, word count target) — halt Step 2 and request the specific missing field by name; do not proceed to Step 3 until resolved. (3) Never silently assume a missing field. Every assumption must be declared at the top of the session output.
3. Run Competitor Analysis (Companion Asset 2). Analyze the top 10 SERP results for the target keyword. URLs may be provided manually by the user, retrieved automatically by an AI agent, or delivered via N8N automation. Regardless of source, this step is a hard blocking gate — Step 4 does not begin until it is complete. The agent must fetch and fully read 5–10 competitor pages (full HTTP reads, not snippet summaries). Before advancing to Step 4, state in the session output: “Competitor audit complete. Pages read: [N]. Average word count: [X]. Target word count: [X × multiplier] = [Y]. CA-2 populated.” Any session that skips this confirmation and proceeds to Step 4 is non-compliant and the resulting draft must be discarded and rewritten.
4. Select writing style (Section 4.5-A) and persona (Section 4.2 Decision Tree). Lock in the style and persona before drafting. Mid-draft style switching is not permitted.
5. Write the first draft following all structural rules. Apply all rules from Sections 1 through 8. Produce the complete draft — no partial drafts proceed to review.
6. Run the Fact-Verification Ledger (Companion Asset 3). Every factual claim, statistic, rate, threshold, and named study must be entered and sourced before the draft advances. Unsourced claims are removed or rewritten at this stage.
7. Run the Draft Review Checklist (Companion Asset 4). Complete the full checklist. Any failed item requires a targeted revision before the scorecard is run.
8. Score with the Weighted Draft Scorecard (Companion Asset 5). Calculate the composite score. Drafts that do not meet the minimum passing threshold are returned for revision. Document the score for the production record.
9. Pre-Publish QA and submit. Confirm all metadata, internal links, image ALT text, schema type, and CMS fields are complete. Submit only after QA sign-off.

---

0-C: Rule Priority Ladder

When rules from different sections of this playbook conflict, the rule with the higher level number overrides the lower. Level 7 is the highest authority; Level 1 is the lowest.

1. Visual and formatting rules — Govern typography, callout placement, image sizing, and table structure.
2. GEO optimization rules — Govern AI-answer targeting, entity density, and direct-answer formatting for generative search.
3. SEO and keyword placement rules — Govern primary keyword placement, density, heading optimization, and internal linking.
4. Structural rules — Govern intro length, conclusion length, H2 and H3 spacing, callout type and placement, and FAQ format.
5. ELI12 voice system and banned-phrase compliance — Governs reading level, sentence length, jargon replacement, and all prohibited language.
6. Factual accuracy and source verification (Tier 1/2 sources only) — No claim advances without a verified source meeting tier requirements.
7. YMYL / E-E-A-T compliance (non-negotiable — regulatory and trust) — Overrides every other rule. Regulatory accuracy, required disclaimers, and trust signals cannot be sacrificed for any reason.

> Interpretation rule: When two rules at the same level appear to conflict, escalate to the Conflict Resolution Map (Section 0-D). If the map does not resolve it, YMYL compliance is the default resolution.

---

0-D: Conflict Resolution Map

Use this table when two rules produce incompatible requirements in the same draft. Apply the Resolution column as the operative rule. Do not average or compromise between conflicting rules — follow the resolution exactly.

| Conflict Scenario | Rule A | Rule B | Resolution | Rationale |
|---|---|---|---|---|
| ELI12 simplicity requirement conflicts with mandatory YMYL disclaimer language | ELI12 voice: plain language, short sentences, no legal-sounding phrasing | YMYL: specific disclaimer copy must appear verbatim or in substance | YMYL wins. Include the required disclaimer copy in full. If possible, follow the disclaimer immediately with a plain-language translation in a separate sentence. | Regulatory and trust compliance is Level 7. Voice preference is Level 5. No voice preference overrides a trust or compliance requirement. |
| Keyword density target conflicts with natural-voice requirement | SEO: use primary keyword X times within the body | ELI12 voice: sentences must read naturally; forced repetition is a banned pattern | Voice wins. Write naturally. Place the primary keyword in high-value positions (title, first 100 words, one H2, meta fields) and allow natural recurrence. Do not force additional insertions. | Google's ranking systems reward natural language and penalize keyword stuffing. SEO performance is better served by voice compliance than mechanical density. |
| Intro word count rule conflicts with Answer Block placement | Structural rule: intro must be 150–200 words | Structural rule: Answer Block must appear before the first H2 | Both are required and additive. The intro (150–200 words) and the Answer Block (40–60 words) are separate, sequential elements. The intro comes first; the Answer Block follows directly. Total pre-H2 content will be approximately 190–260 words. | These are not competing rules — they govern different elements. Both must be present in every draft. |
| Visual placement rule conflicts with content flow | Formatting rule: callout or image placed after every second H2 | Content flow: inserting a visual at that position would interrupt a critical explanatory sequence | Content flow wins. Move the visual to the next natural break point (end of the current explanatory sequence). Document the placement deviation in the production record. | A visual that breaks reader comprehension defeats its purpose. Formatting rules serve communication; they do not override it. |
| GEO stat-citation requirement conflicts with sentence readability | GEO rule: inline source citation must accompany every statistic for AI-answer credibility | Readability rule: inline citations that interrupt sentence flow violate ELI12 phrasing standards | Both are required. Rewrite the sentence to carry the statistic and citation without awkward interruption. Use a construction such as: "According to the Bureau of Labor Statistics (2023), X percent of…" — this satisfies both rules simultaneously. | Neither rule can be dropped. The rewrite obligation falls on the writer, not on the rules. |
| CTA placement rule conflicts with emotional arc stage | Conversion rule: CTA must appear at [specified position] in the article | Emotional arc rule: that position is in the Problem Agitation stage, where a hard CTA is inappropriate | Emotional arc sets the stage; CTA type must match. Do not place a conversion CTA during Problem Agitation. Use a soft CTA (resource link, empathy bridge) at that position. Place the conversion CTA at the first emotionally appropriate stage (Solution or Proof). | A CTA placed against the emotional arc produces friction and suppresses conversion. Emotional sequencing is a structural rule (Level 4) applied to conversion architecture. |

---

0-E: Source-Use Protocol

All four rules apply to every draft. They are not guidelines — they are production requirements.

1. Every factual claim must have a source. No statistic, rate, threshold, named study, or attributed finding may appear in a draft without a corresponding entry in the Fact-Verification Ledger (Companion Asset 3). Phrases such as "studies show," "research suggests," or "experts say" without a named source are banned. Name the study, institution, or publication every time.

2. Source tiers govern which claims sources can support:
 - Tier 1 (load-bearing claims): U.S. government sources (.gov domains), peer-reviewed academic journals, Federal Reserve publications, Bureau of Labor Statistics, U.S. Census Bureau, and equivalent sovereign statistical agencies.
 - Tier 2 (supporting claims): Established financial institutions (Vanguard, Fidelity, Charles Schwab), major nonpartisan research organizations (Pew Research Center, Gallup, RAND), and established national news organizations with original reporting (Wall Street Journal, New York Times, Reuters — when citing their original data, not aggregated third-party data).
 - Tier 3 (trend illustration only): Industry blogs, content aggregators, personal finance aggregator sites. Tier 3 sources may illustrate a trend or frame a discussion but may never serve as the sole source for any factual claim. A Tier 1 or Tier 2 source must substantiate any underlying fact.

Reddit Exception — Research Use Only
Reddit is permitted as a research input for reader language, emotional framing, real-world scenarios, and genuine pain points. Search any relevant subreddit or thread for the topic — there are thousands of communities covering personal finance, debt, budgeting, investing, and life-stage money situations. The right threads to use are whichever ones contain the most authentic reader language for the specific topic being written.
Reddit is never a source for financial facts, rates, limits, or regulatory claims. Any factual claim from a Reddit thread must be verified against a Tier 1 or Tier 2 source before appearing in the draft.
For AI agents: Include Reddit in every topic search alongside competitor URLs. Extract pain points, language patterns, and real scenarios. Flag any specific numerical claims for verification.

3. Time-sensitivity rule: Any claim that includes a specific year, interest rate, income threshold, contribution limit, or percentage figure must include the publication year inline at first use (e.g., "as of 2024"). Any source dated more than three years prior to the current publication date must be flagged in the Fact-Verification Ledger as [VERIFY — original source dated YYYY] and either updated with a current source or removed before publication.
Exception to the three-year rule: Foundational research studies (e.g., NNG eye-tracking studies, Kahneman/Tversky prospect theory) are exempt from the three-year re-verification requirement if: (a) a documented update methodology exists and is noted in the Evidence Registry, and (b) no contradicting peer-reviewed research has been published. The three-year rule applies strictly to rates, limits, thresholds, and regulatory figures — not to durable research findings.

4. When no Tier 1 or Tier 2 source exists for a claim: The claim must be rewritten as a principle, framework, or general guidance (not a stated fact), or removed entirely. No claim advances to publication solely on the basis of common knowledge, editorial judgment, or Tier 3 sourcing.
Exception — reader-verifiable facts: A claim the reader can verify by a single primary action (e.g., checking their own bank’s current APY, looking up their own credit card rate) may be stated without a Tier 1/2 source if the post includes an explicit verification instruction: “Check your current APY in your account settings — most traditional banks show 0.01–0.5%.” Do not use this exception for regulatory thresholds, tax rules, contribution limits, or any claim that carries legal or compliance weight. Those require Tier 1 verification regardless.
5. LLM/AI agent rule for sessions without live web access: When a factual claim cannot be verified in real time, apply this hierarchy in order: (1) Use figures provided in the Article Brief if present. (2) Use the most recently known figure, add an inline date caveat (“as of [year known]”), and append [VERIFY BEFORE PUBLISH] immediately after the claim. (3) Never omit a load-bearing claim entirely — flag it rather than delete it. Do not use this rule for regulatory thresholds, tax limits, or contribution limits — those must always be verified before the draft advances.

---

0-F: Originality Requirement

Every AF post must contain at least one element that cannot be found in the top 10 SERP results for the target keyword — verified during the competitor analysis step (Step 3 of the Session Sequence). Qualifying originality elements include: a named AF original framework (e.g., a decision tree, a scoring matrix, a tiered system), a novel combination of publicly available data sets that produces a new insight, a proprietary analogy or explanatory model that reframes a standard concept, or a first-person case study drawn from direct experience. A draft that restates, reorganizes, or lightly paraphrases what already exists in the top 10 results adds no competitive or reader value. If the originality check confirms the draft contributes nothing not already present in the SERP, the draft fails and must be revised — it does not advance to the Fact-Verification Ledger or any subsequent step until an original element is incorporated.

---

0-G: Standard Output Contract

Every AF content production session produces a defined deliverable set. The required outputs differ by mode.

#### Full Draft Mode

A completed Full Draft Mode output must contain all ten of the following elements. Partial outputs do not qualify as complete deliverables.

1. Complete article text from title through conclusion, including all body sections, callouts, and FAQ — no placeholder text, no bracketed fill-ins.
2. Meta title (50–65 characters including spaces) and meta description (150–160 characters including spaces), both containing the primary keyword.
3. URL slug (3–5 words, lowercase, hyphen-separated, containing the primary keyword).
4. All H2 and H3 headings presented in hierarchical outline form, confirming no heading level is skipped.
5. Three callout blocks — Type A (Stakes Moment callout), Type B (How-To Moment callout), Type C (Completion / CTA callout) — each with complete copy ready for CMS insertion and formatted according to Section 7-A.
6. FAQ section with a minimum of four questions and action-oriented answers (not passive summaries); each answer must end with a next step or actionable takeaway.
7. Internal link recommendations — minimum three, each with: anchor text, destination URL or article title, and placement note indicating the specific paragraph or heading near which the link should appear.
8. Image and visual placement notes — one note per recommended visual, specifying placement position in the article, visual type (chart, infographic, screenshot, illustration), and a draft ALT text string for each.
9. Schema markup type recommendation — specify the most appropriate schema type (e.g., Article, FAQPage, HowTo, FinancialProduct) and note if multiple types should be combined.
10. Completed Fact-Verification Ledger (Companion Asset 3) — every factual claim in the article entered, sourced, tier-rated, and dated.

#### Revision Mode

A completed Revision Mode output must contain all four of the following elements.

1. Line-level edits presented as tracked changes (preferred) or explicit before/after pairs for every substantive change. Vague summary edits (e.g., "improved clarity throughout") are not acceptable.
2. Scorecard delta — a comparison of the pre-revision and post-revision Weighted Draft Scorecard (Companion Asset 5) scores by dimension, identifying which dimensions improved, which declined, and the change in composite score.
3. Updated Fact-Verification Ledger entries for every claim that was added, modified, or removed during revision. Unchanged claims do not require re-entry.
4. Internal link integrity confirmation — explicit confirmation that no previously placed internal links were removed or rendered incorrect by the revision, with a note on any links that required anchor text or destination updates.

---

0-H: Minimum Viable Load Guide

When loading the full playbook is operationally impractical — due to context window limitations, session time constraints, or platform restrictions — the following rules govern the minimum acceptable load.

#### The Minimum Viable Load

The Runtime Brief (Companion Asset 10) is the minimum viable load for any content production session. It contains the condensed rule set sufficient for standard production: voice rules, structural requirements, SEO and GEO essentials, source tier definitions, callout specifications, and the Session Sequence. A session may proceed using only the Runtime Brief under routine conditions.
Uploaded files take priority over Drive links. If a companion asset is uploaded directly to the session, use the uploaded version. If a Drive link is provided but inaccessible, request the file as an upload before treating it as unavailable.

#### When the Full Playbook Is Required

The Runtime Brief is not sufficient — the full playbook must be loaded — in any of the following situations:

- First-time writers or AI assistant onboarding: Any writer or AI instance producing AF content for the first time must load and process the complete playbook before any draft work begins.
- New writing style attempts: Any session that applies a writing style not previously used by that writer or assistant (per Section 4.5-A) requires full playbook load to ensure all style-specific structural and voice rules are properly integrated.
- Any YMYL-sensitive topic: Articles covering debt, taxes, investment decisions, insurance, credit, retirement accounts, or any topic with direct financial consequence to the reader require full playbook load to ensure complete E-E-A-T and disclaimer compliance.
- Quarterly playbook reviews: All scheduled reviews of the playbook for updates, revisions, or rule additions must reference the full document. Review sessions conducted against the Runtime Brief only are invalid.
- Any dispute about rule interpretation: When a writer, editor, or AI assistant encounters ambiguity or apparent conflict not resolved by the Conflict Resolution Map (Section 0-D), the full playbook is the authoritative reference. The Runtime Brief does not have authority to resolve interpretation disputes.

#### Load Confirmation Protocol

At the start of every session, confirm in writing (in the session log or production record) which document was loaded: Full Playbook or Runtime Brief. If the Runtime Brief was loaded for a session that required the full playbook, the session output is considered non-compliant and must be re-reviewed against the full playbook before publication.

---

# SECTION 4.1 — BRAND VOICE, ELI12 SYSTEM, AND TONE DIAL

**Core thesis:** "Money decisions create life consequences." Every topic passes one gate: *"What does money buy or destroy here?"* If unclear, it does not belong.

**Six Content Pillars (60/40 split):** (1) Budgeting & Money Systems, (2) Debt Freedom, (3) Smart Earning — together 60% of output for SEO authority and affiliate revenue. (4) Life-Stage Finance, (5) Financial Psychology, (6) AI and Money — 40% for sharing, signups, brand differentiation.

## ELI12 — 6 Core Voice Attributes

1. Conversational — write as if explaining to a smart friend at a coffee shop.
2. Jargon-free on first use — every finance term defined in plain language on first appearance: `term (plain-language definition)`. After first definition, use freely.
3. Empathetic — acknowledge the reader's situation without judgment.
4. Actionable — every section ends with something the reader can do.
5. Concrete with real numbers — specific dollar amounts, percentages, timeframes.
6. Non-condescending — reader is smart, just uninformed on this topic.

**Three-Word Test (drafting check):** Can you explain this concept in 3 words? If not, the sentence is too complex.

**Flesch-Kincaid Target:** Grade 7–8. Avg sentence 15–20 words. Avg syllables/word ≤1.5. Paragraphs 2–4 sentences. One idea per paragraph.

**60/40 ELI12 Split:** 60% of each post fully ELI12 (Grade 7–8); 40% may rise to Grade 9–10 for depth — and the 40% always comes after the 60% has established understanding. Section-level heuristic: for every 2 paragraphs at Grade 9–10+, at least 3 in the same section must be Grade 7–8 or below. Flag any section where Grade 9+ paragraphs outnumber Grade 7–8 as a voice-calibration failure.

## Tone Dial Table — 5 dimensions, rated 1–5

| Post Type | Warmth | Urgency | Authority | Humor | Formality |
|---|---|---|---|---|---|
| Pillar Guide | 4 | 2 | 4 | 2 | 3 |
| Tutorial / How-To | 3 | 3 | 4 | 1 | 3 |
| Listicle | 3 | 2 | 3 | 3 | 2 |
| Scenario / Decision | 4 | 4 | 3 | 1 | 3 |
| Comparison / Review | 2 | 2 | 5 | 1 | 4 |
| Data-Led | 2 | 2 | 5 | 1 | 4 |
| Money Dominoes | 4 | 4 | 3 | 2 | 2 |
| First-Gen Finance | 5 | 3 | 3 | 2 | 2 |
| Contrarian | 2 | 3 | 5 | 3 | 3 |
| 1 Rule 1 Tool | 3 | 3 | 4 | 2 | 3 |

**Red Flags by Dial Error:** Humor too high in First-Gen → trivializes systemic disadvantage. Authority too low in Comparison → wishy-washy recommendation. Warmth too low in Scenario → clinical when reader is scared. Urgency too high in Pillar → panic in educational content. Formality too high in Money Dominoes → kills chain-reaction energy. Authority too low in Contrarian → opinion instead of evidence.

**Use:** Look up post type → note 5 settings before drafting. While drafting, if a paragraph feels off, check which dial is miscalibrated. While editing, read each section aloud and flag mismatches.

---

# SECTION 4.1-A — VOICE CALIBRATION: 20 BEFORE/AFTER REWRITES

Use as a tuning fork. When voice drift creeps in, read pairs aloud. "Before" = the drift. "After" = the standard.

---

**1. Jargon Without Translation** *(Keep long-form — teaching baseline)*

**Before:** "Understanding the amortization schedule of your mortgage allows you to strategically allocate additional principal payments to reduce the overall interest burden."

**After:** "Your mortgage payment is split two ways: part goes to what you owe (principal), part goes to the bank's fee for lending you money (interest). Early on, most of your payment is interest. Here's how to flip that ratio faster."

**Failure mode:** Using financial vocabulary without translating it — assumes the reader already knows what you're teaching them.

---

**2. Passive Construction Hiding the Human Agent** *(Keep long-form — teaching baseline)*

**Before:** "A budget should be created at the beginning of each month to ensure expenses are properly allocated."

**After:** "Create your budget on the 1st of each month — before any money leaves your account. You're telling your money where to go instead of wondering where it went."

**Failure mode:** Passive voice removes the reader from the action. "A budget should be created" has no actor. "Create your budget" puts the reader in charge.

---

**3. Over-Hedging That Destroys Confidence** *(Keep long-form — teaching baseline)*

**Before:** "It may be possible that in some cases, depending on your specific circumstances, you could potentially benefit from opening a high-yield savings account."

**After:** "If your savings account earns less than 4% APY right now, you're leaving money on the table. A high-yield savings account fixes that — same FDIC insurance, better rate."

**Failure mode:** Excessive qualifiers signal that the writer is unsure. In YMYL, this destroys confidence. State the condition, state the recommendation, state the caveat when relevant.

---

**Quick-Reference: Examples 4–20**

| # | Failure Mode (Trigger) | Banned Sentence (Verbatim Before) | ELI12 Correction (Verbatim After) |
|---|---|---|---|
| 4 | Condescension Disguised as Simplicity | "Simply log into your bank account and just transfer the money. It's easy — all you have to do is set up automatic transfers!" | "Set up an automatic transfer from checking to savings for the day after payday. Takes about 4 minutes the first time. After that, it happens without you thinking about it." |
| 5 | Fake Urgency Using Clichés | "The time to act is now! Don't wait another day to start building your emergency fund — your future self will thank you!" | "Every month without an emergency fund, you're one car repair away from credit card debt. At 22% APR, a $1,200 repair costs you $1,560 if you charge it and pay minimums for 2 years. The emergency fund prevents that math." |
| 6 | Corporate Stiffness Mimicking a Bank FAQ | "Customers who maintain a minimum balance of $500 in their savings vehicle may be eligible for enhanced yield opportunities through qualifying financial institutions." | "Some high-yield savings accounts require a $500 minimum balance to get the best rate. If you don't have $500 yet, start with one that has no minimum — there are several good ones — and switch once you've built up the balance." |
| 7 | Academic Register Borrowed from Investopedia | "Dollar-cost averaging is an investment strategy whereby an investor divides the total amount to be invested across periodic purchases of a target asset to reduce the impact of volatility on the overall purchase." | "Dollar-cost averaging means investing the same amount every month regardless of what the market is doing. When prices drop, your $200 buys more shares. When prices rise, it buys fewer. Over time, this smooths out the bumps so you're not buying everything at the peak." |
| 8 | Vague Outcome Language | "This template will help you improve your overall financial health and take meaningful steps toward a more secure financial future." | "This template shows you three numbers: what you earn, what you spend, and what's left. When 'what's left' is positive and going into a savings account every month, you're winning. When it's negative, the template shows you exactly which spending categories to cut first." |
| 9 | Generic Advice Without Audience Specificity | "Everyone should have an emergency fund. Financial experts recommend saving 3-6 months of expenses." | "If you're making $40,000–$60,000 a year, your emergency fund target is probably $6,000–$12,000. That sounds like a lot. Start with $1,000 — that covers the most common emergencies (car repair, medical copay, appliance replacement) without credit card debt." |
| 10 | The False Positive Framing | "Great news! You're about to learn everything you need to know about retirement accounts. This is going to be exciting!" | "Retirement accounts are confusing. There are too many types, the rules are arbitrary, and the penalties for mistakes are steep. This post cuts through that. By the end, you'll know which account to open first, how much to put in, and what to invest in once it's open." |
| 11 | Hedged Disclaimer That Reads Like Legal Copy | "The information contained herein is for educational purposes only and should not be construed as professional financial, tax, or legal advice. Individual results may vary. Please consult with a qualified financial professional before making any financial decisions." | "This post explains how debt avalanche and snowball methods work and helps you choose between them. It's not a personalized recommendation for your specific situation — if you have complex debt (business loans, tax liens, legal judgments), talk to a nonprofit credit counselor first. For consumer debt like credit cards and student loans, the math below applies. All numbers current as of March 2025." |
| 12 | Unnecessary Preamble Before Getting to the Answer | "In today's complex financial landscape, many people find themselves wondering about the best strategies for managing their personal finances. With so many options available, it can be overwhelming to know where to begin. In this comprehensive guide, we'll explore everything you need to know about building a budget." | "A budget is a plan for your money: how much comes in, how much goes out, and where the difference goes. Here's how to build one that actually works — starting with your last month's real spending, not an idealized version of it." |
| 13 | Third-Person Distance When First-Person Would Be Warmer | "Many individuals discover that tracking expenses reveals surprising patterns in discretionary spending." | "When I tracked my own spending for the first time, I found out I was spending $340/month on food delivery. I thought it was maybe $100. That gap — between what I thought I spent and what I actually spent — is the gap the Budget Builder closes." |
| 14 | Inflation of Simple Concepts to Sound Sophisticated | "Implementing a systematic approach to discretionary expenditure reduction can yield significant positive outcomes for your aggregate financial position." | "Cutting unnecessary spending is the fastest way to free up money. Here are the three categories where most people find the biggest cuts." |
| 15 | The "Motivational Poster" Closer | "Remember, every journey begins with a single step. You've got this! Believe in yourself and your ability to achieve financial freedom. The power to transform your finances is in your hands!" | "Here's your one next step: open your bank's app, screenshot your last 30 days of transactions, and circle the three largest non-essential charges. That's the raw material for your first budget cut. Do it now — it takes 2 minutes." |
| 16 | Feature Description Instead of Outcome Description | "Download our comprehensive Excel spreadsheet with multiple tabs, conditional formatting, and built-in formulas for financial tracking!" | "Download the Budget Builder — enter your take-home pay and your actual spending from last month. It shows you exactly where your money goes, which categories to cut first, and how much you'll save per month if you do." |
| 17 | Passive Debt Framing vs Active Framing | "When debt was accumulated over time, it can feel like the situation is beyond one's control." | "You didn't wake up one morning with $15,000 in credit card debt. It built up — $200 here, $500 there, a medical bill, a car repair, a month where the math didn't work. The same way it built up, it comes down: one payment at a time, starting with the most expensive debt first." |
| 18 | False Equivalence Framing | "There's really no right or wrong answer here — it's all about what works best for you and your unique situation!" | "If your highest-rate debt is above 20% APR and your lowest is below 8%, avalanche saves you more money — period. If all your rates are within 2-3% of each other, snowball and avalanche produce nearly identical results, so pick whichever keeps you motivated. The math doesn't lie, but it does have nuance." |
| 19 | Complexity Theater | "The intricacies of credit utilization ratios and their multifaceted impact on your FICO scoring model are critical to understand before embarking on any credit optimization strategy." | "Credit utilization is how much of your credit limit you're using. If your limit is $10,000 and your balance is $3,000, your utilization is 30%. Below 30% is good. Below 10% is better. That's it — that's the whole concept." |
| 20 | The Empty Transition | "Now that we've covered the basics of emergency funds, let's move on to the next important topic: investing for beginners." | "Your emergency fund is the foundation. Once it's at $1,000 (or 3 months of expenses if you're further along), the next dollar should go somewhere it grows. Here's where." |

---

# SECTION 4.1-B — FIRST SENTENCE SWIPE FILE: 20 ELI12 OPENING TEMPLATES

Each template is ready-to-use. Adapt dollar amounts and scenario specifics. Structure and tone are calibrated to ELI12.

**Scenario 1 — Fully annotated baseline** *(Reader arrives in financial crisis / unexpected expense)*

"Your car just threw a $1,400 repair bill at you, your savings account has $83 in it, and you're trying to figure out whether the credit card or the payment plan is the less terrible option — so let's skip the lecture about emergency funds you don't have yet and talk about what to do right now, today, with the money you actually have."

*Why this works: Names exact dollar amounts of the crisis. Acknowledges both decision paths the reader is weighing. Signals this post won't lecture. Matches the reader's emotional state — not panicked, just in problem-solving mode. Earns the scroll by promising immediate, situationally specific help.*

---

**Quick-Reference: All 20 Scenarios**

| # | Reader Arrival State / Trigger | Verbatim Opening Sentence Swipe |
|---|---|---|
| 1 | Financial crisis — unexpected expense | "Your car just threw a $1,400 repair bill at you, your savings account has $83 in it, and you're trying to figure out whether the credit card or the payment plan is the less terrible option — so let's skip the lecture about emergency funds you don't have yet and talk about what to do right now, today, with the money you actually have." |
| 2 | Frustrated with previous failed attempts (budgeting failure) | "If you've downloaded a budgeting app, used it for two weeks, felt guilty about the results, and then deleted it — you're not bad at budgeting; you've been using budgets that were designed for a version of your life that doesn't exist." |
| 3 | Confused by conflicting advice online | "One blog says pay off your highest-interest debt first, another says start with the smallest balance, a third says forget debt and invest instead — and you're standing in the middle wondering if any of these people have ever actually been in debt, because none of this advice feels like it was written for someone with $200 left after rent." |
| 4 | Triggering financial event (declined card, loan rejection, bill shock) | "Getting rejected for a loan is one of those moments where the number on the screen feels like a grade on your entire adult life — but a 620 credit score is not a verdict, it's a snapshot, and snapshots change faster than you think when you know which three things to fix first." |
| 5 | Wants validation that their situation is not hopeless | "If you're reading this at 2 AM because you just added up all your debt for the first time and the number is bigger than you expected — take a breath, because that number is not a life sentence; it's a math problem, and math problems have solutions." |
| 6 | Saw a friend do something and wants to understand it | "Your coworker just mentioned they 'maxed out their Roth IRA this year' and you smiled and nodded like you knew what that meant — here's what it means, what it costs, and whether it makes sense for you right now." |
| 7 | Comparison query (which is better, A or B) | "The internet will give you 47 opinions on whether to choose a Roth IRA or a Traditional IRA, most of them written by people who don't mention the one factor that actually decides it for 80% of people: what tax bracket you're in right now versus what you expect in retirement." |
| 8 | Wants a quick specific answer (what is X) | "A 401(k) is a retirement savings account your employer sets up for you — you put money in before taxes, your employer often matches a percentage, and the whole thing grows tax-free until you withdraw it in retirement; here's the 3-minute version of everything you need to know to set yours up correctly." |
| 9 | Wants a number (how much should I have saved) | "By 30, a common benchmark is to have one year's salary saved for retirement — so if you earn $50,000, the target is $50,000 in your 401(k) or IRA — but here's what nobody tells you: if you're starting at 28 with $3,000 saved, you're not behind; you just need a different plan than someone who started at 22." |
| 10 | Decision moment (I'm about to do X, should I) | "You're about to sign a 72-month auto loan because the monthly payment looks manageable at $389, and I need you to see one number before you do: $27,972 — that's the total you'll pay for a $22,000 car, which means you're paying $5,972 for the privilege of stretching out the payments." |
| 11 | Post-breakup or life change affecting finances | "Splitting finances after a breakup is one of those things nobody prepares you for — the joint account, the shared subscriptions, the lease with both names on it — and the last thing you need right now is a lecture about budgeting; what you need is a checklist of exactly which financial accounts to separate, in which order, starting today." |
| 12 | Embarrassed, doesn't want to admit what they don't know | "If you've been nodding along in conversations about APR, compound interest, and index funds while secretly having no idea what any of those words actually mean — first, you're in the majority; second, by the end of this post, you'll know all three well enough to explain them to someone else." |
| 13 | Skeptical ("I've read all the advice and it doesn't work for me") | "If you've read every budgeting article on the internet and none of them worked — not because you're undisciplined but because they all assumed you have $500 in 'discretionary spending' you can magically redirect — then this post is written for your actual numbers, not a financial advisor's fantasy spreadsheet." |
| 14 | Irregular income, excluded from generic advice | "Every budget template on the internet assumes you get the same paycheck on the same day every month — which is useless if you're freelancing, gigging, working on commission, or doing seasonal work where February's income might be half of October's; here's a budgeting system that starts with the worst month, not the average one." |
| 15 | Young reader, first real job, first time thinking about money | "You just got your first real paycheck and after taxes, health insurance, and that 401(k) thing HR mentioned, the number is a lot smaller than the salary they offered you — and nobody told you this would happen, so let's start with what actually happened to your money between the offer letter and your bank account." |
| 16 | Just discovered they've been paying for something they shouldn't be | "You just found a $14.99/month charge on your credit card statement from a service you forgot you signed up for — and now you're wondering how many months it's been, how much you've paid total, and what other subscriptions are quietly draining your account; here's how to find all of them in 15 minutes." |
| 17 | Just made a financial mistake, looking for damage control | "You missed a credit card payment for the first time and the late fee hit instantly, and now you're wondering how bad the damage is, whether your credit score just cratered, and what you can do about it in the next 24 hours — so here's the honest answer, in order of urgency." |
| 18 | Genuinely curious, not in crisis | "Compound interest is one of those concepts that gets called 'the eighth wonder of the world' so often that the phrase has lost all meaning — so instead of telling you it's magical, let me show you what $200/month actually becomes over 10, 20, and 30 years at different rates, because the real numbers are more convincing than any quote." |
| 19 | Topic feels overwhelming, needs it broken down | "Investing sounds like it requires a Bloomberg terminal, a finance degree, and a suit — but the version of investing that actually matters for someone with a 401(k) and maybe a Roth IRA involves exactly three decisions, and you can make all three in the time it takes to order lunch." |
| 20 | Optimistic, ready to act (momentum stage) | "You've decided this is the month you get your money figured out — and that energy is worth more than any spreadsheet, so let's not waste it on theory; here's the exact sequence of actions, in order, starting with the one that takes 4 minutes and has the biggest immediate impact on your monthly cash flow." |

---

# SECTION 4.1-C — BANNED PHRASES LIST WITH MANDATORY REPLACEMENTS

Every phrase below is banned. Context column populated only where reason for failure is non-obvious.

## Category 1 — Hedge Phrases That Destroy Confidence

| Banned Phrase | Mandatory Replacement | Context |
|---|---|---|
| "It might be a good idea to…" | "Do this if [specific condition]." or state the recommendation directly. | Hedging transfers your uncertainty to the reader. Commit or don't recommend. |
| "You may want to consider…" | "Here's when this makes sense: [condition]. Here's when it doesn't: [condition]." | Three layers of hedge. Reader wants direction, not meta-suggestions. |
| "It depends on your situation." *(without specifying what it depends on)* | "It depends on three things: your interest rate, your tax bracket, and whether your employer matches. Here's how each one changes the answer." | Acceptable only when you immediately name the variables. |
| "There's no one-size-fits-all answer." | State the decision framework: "If [condition A], do X. If [condition B], do Y." | |
| "This could potentially help you…" | "This helps if [condition]. It won't help if [different condition]." | |
| "In some cases, you might find that…" | "If your [specific variable] is [specific range], then [specific outcome]." | |
| "Results may vary." | "Your timeline depends on your balance, rate, and how much extra you can pay each month. Here's the range." | |
| "It's generally recommended that…" | "The Federal Reserve data suggests…" or "Most financial planners recommend X because [specific reason]." | "Generally" signals you don't have a source. |

## Category 2 — Filler Openers That Waste the First Sentence

| Banned Phrase | Mandatory Replacement | Context |
|---|---|---|
| "In today's complex financial landscape…" | Start with the specific answer, number, or scenario. | Generic throat-clearing. Wastes the highest-value sentence in the post. |
| "Have you ever wondered…?" | State the answer the reader is looking for, then explain it. | |
| "When it comes to [topic]…" | Delete. Start with the substantive content. | |
| "As we all know…" | State the fact directly without assuming shared knowledge. | Many readers don't know it — now they feel excluded. |
| "Let's dive in!" / "Without further ado…" | Delete. Begin the first section. | |
| "In this article, we will discuss…" | Use a brief roadmap only for posts over 3,000 words: "This post covers X, Y, and Z — starting with the one that saves you the most money." | |

## Category 3 — Condescending Simplicity Phrases

| Banned Phrase | Mandatory Replacement | Context |
|---|---|---|
| "Simply…" | Remove. State the action: "Transfer $200 to your savings account." | Implies struggling is embarrassing. Remove the judgment entirely. |
| "Just…" | Remove, or acknowledge the friction: "Call your bank's customer service line (the number is on the back of your card). It takes about 10 minutes." | "Just call your bank" ignores that phone anxiety is real. |
| "Easy" / "It's easy to…" | Name the actual effort: "This takes about 15 minutes and 3 pieces of information." | |
| "All you have to do is…" | "Here's the process: [step 1], [step 2], [step 3]." | |
| "Quickly…" | State the actual time: "In about 5 minutes…" or "This takes one phone call." | |
| "In just X steps…" | "In 4 steps:" — then list them. | |

## Category 4 — Vague Outcome Language

| Banned Phrase | Mandatory Replacement | Context |
|---|---|---|
| "Improve your financial health" | "Reduce your credit utilization below 30%." / "Build $1,000 in emergency savings." / "Lower your monthly debt payments by $200." | |
| "Achieve financial wellness" | "Get to the point where an unexpected $500 expense doesn't mean credit card debt." | |
| "Reach financial freedom" | "Cover all your essential expenses from investment income" or "Have zero consumer debt and 6 months of savings." | Means something different to every reader without definition. |
| "Take control of your finances" | "See exactly where your money goes each month and decide where you want it to go instead." | Implies reader is currently out of control — shame trigger. |
| "Transform your finances" | "Go from $0 saved to $5,000 in 12 months." | |
| "Build wealth" | "Start investing $50/month in an index fund" or "Build your first $10,000 in savings." | |
| "Secure your financial future" | "Make sure next month's rent is covered even if something goes wrong this month." | |
| "Optimize your spending" | "Find the $200/month you're spending on things you forgot you were paying for." | Corporate/engineering register. Real people don't "optimize." |

## Category 5 — Clichés That Signal Generic Content

| Banned Phrase | Mandatory Replacement | Context |
|---|---|---|
| "At the end of the day…" | Delete. State the conclusion directly. | |
| "It goes without saying…" | Delete entirely, or state the fact without preamble. | |
| "The bottom line is…" | Bold the key takeaway as a standalone sentence. No intro needed. | |
| "Knowledge is power." | "Knowing your credit utilization ratio lets you predict your score movement within 10 points." | |
| "Every penny counts." | "That $47/month in forgotten subscriptions is $564/year — enough to cover your car insurance deductible." | |
| "Pay yourself first." | "Before you pay any bill, move money to savings. Set up the auto-transfer for the day after payday so it happens before you see the full balance." | Fine as a concept; overused to the point of not landing. |
| "Money doesn't grow on trees." | Delete. Replace with specific guidance relevant to the context. | |
| "Rome wasn't built in a day." | "This takes 6-12 months at $200/month. Here's the month-by-month breakdown." | |

## Category 6 — LinkedIn/Corporate Phrases That Break the ELI12 Register

| Banned Phrase | Mandatory Replacement | Context |
|---|---|---|
| "Leverage your assets…" | "Use your [specific asset] to [specific outcome]." | |
| "Synergize your financial strategies…" | "Make your savings, debt payoff, and investing plans work together instead of competing for the same dollars." | |
| "Holistic financial planning…" | "A plan that covers all five areas: spending, saving, debt, investing, and insurance." | |
| "Paradigm shift in your financial mindset…" | "Change how you think about [specific thing]." | |
| "Actionable insights…" | Delete the label. Just provide the actions. | |
| "Value proposition…" | "What you get" or "Why this is worth your time." | |
| "Empower yourself…" | "Learn to read your credit report so you can dispute errors yourself." | Vague. Empowerment comes from specific skills, not declarations. |
| "Best practices…" | "What works" or "The approach that gets the best results." | |

## Category 7 — Finance-Specific Phrases That Signal Affiliate Farm or Low-Trust Intent

| Banned Phrase | Mandatory Replacement | Context |
|---|---|---|
| "Our top picks…" | "The [X] accounts/products that scored highest on [named criteria]: [list criteria]." | Without disclosed selection criteria, reads as sponsored content. |
| "Best [product] of [year]" *(without methodology)* | "Highest-rated [products] by [specific criterion], based on [data source]. Disclose the methodology." | |
| "Our recommendation…" | "Based on [criterion], [product] fits best if your situation is [condition]. Here's why." | |
| "Exclusive offer…" | "[Product] is offering [specific terms] through [date]." | "Exclusive" is affiliate language; these offers are available to everyone. |
| "Don't miss out on…" | State the factual opportunity and its deadline: "The IRA contribution deadline for the 2024 tax year is April 15, 2025." | |
| "Click here to learn more…" | "The full rate comparison is in the table below" or "NerdWallet's rate tracker shows current APYs across 30+ accounts." | Generic affiliate CTA inside educational content breaks trust. |



---


# SECTION 4.2 — THE 4 READER PERSONAS + VOICE PERSONA DECISION TREE

Two-layer persona model: **Reader Persona** = audience archetype (who, situation, emotional state, vocabulary). **Voice Persona** = narrator delivery (tone, framing, register). Both are selected before drafting and logged in the Article Brief under separate fields. One primary reader persona per post; up to 1–2 secondary only if needed.

## The 4 Reader Personas

**Persona 1 — The Overwhelmed Starter (21–26)**
- *Life:* First real paycheck, no financial education, paralyzed by options (401k? Roth? HSA?).
- *Emotion:* Paralyzed, ashamed of not knowing basics, afraid of "wrong" choice.
- *Keeps reading:* Single clear next step; permission to start small; validation that not knowing is normal.
- *Bounces on:* Walls of text, too many options, condescension, assumed knowledge.
- *Vocabulary:* "Here's what to do first" (not "It's simple"). "Start here" (not "Just do X"). "One thing this week" (not "You need to immediately"). "You're not behind" (not "You should have started earlier").
- *Non-negotiable:* **Single-task instruction philosophy** — never more than one action item per section.

**Persona 2 — The Debt-Stressed Adult (25–32)**
- *Life:* Knows they're in trouble. Credit card and/or student debt. Tried budgeting and failed. Needs real math, not motivation.
- *Emotion:* Anxious, sometimes desperate. Shame without admitting it. Wants specifics.
- *Keeps reading:* Real numbers, specific timelines, math that shows the path out.
- *Bounces on:* "Just save more." Vague encouragement, shame language, unrealistic scenarios.
- *Vocabulary:* "Here's the math," "17 years vs 28 months," "$347/month changes everything," "You're not broken — the system is designed this way."
- *Non-negotiable:* **Specificity requirement** — always show the actual calculation (e.g., "$200/month on $5,000 at 22% APR = $2,300 interest over 31 months; $347/month = $800 interest over 16 months.").

**Persona 3 — The First-Gen Builder (22–30)**
- *Life:* First in family to navigate professional finances. Learning salary negotiation, retirement, tax optimization from scratch.
- *Emotion:* Determined but under-resourced. The "first-gen tax."
- *Keeps reading:* Specific tools and scripts, "cheat codes" framing, acknowledgment of systemic gap.
- *Bounces on:* Assumed background, corporate tone, advice that requires existing wealth.
- *Vocabulary:* "The first-gen tax," "Cheat codes nobody taught you," "Here's the exact script," named platforms (Glassdoor, Levels.fyi), "The system wasn't designed for you — here's how to use it anyway."

**Persona 4 — The Optimizing Grower (28–35)**
- *Life:* Basics down. Emergency fund + retirement accounts exist. Wants tax optimization, investment strategy, side-income scaling, wealth building.
- *Emotion:* Confident, hungry for edge. Wants advanced tactics, not 101.
- *Keeps reading:* Advanced strategies, edge cases, tax optimization, real portfolio math.
- *Bounces on:* Over-explained basics, condescending recaps, content they've outgrown.
- *Vocabulary:* "Mega Backdoor Roth," "Tax-loss harvesting window," "I-bond ladder," "Wash sale rule workaround," "Your marginal rate at this bracket."

## Voice Persona Selection — Decision Tree (Deterministic)

Run before drafting. Stop at first match. Apply Conflict Rules first.

**Conflict Rules (priority over steps):**
- A. Debt language + Salary signals → **The Empathetic Guide**.
- B. First-gen signals + Debt language → **The Encouraging Mentor**.
- C. Optimization language + Life-stage markers → **The Encouraging Mentor**.

**Steps (in order):**
1. **Debt language check** — debt payoff, collections, behind on payments, defaulted, wage garnishment, credit score repair, bankruptcy → **The Empathetic Guide**.
2. **First-generation signal check** — first in family, no financial role model, parents didn't teach, immigrant finance, starting from zero, first-gen college/professional → **The Encouraging Mentor**.
3. **Salary / income optimization check** — salary negotiation, raise, high-income strategy, backdoor Roth, mega backdoor, RSU, stock options, deferred comp → **The Straight-Talking Strategist**.
4. **Optimization / analytical check** — comparison, which is better, analysis, data, rates, returns, allocation, backtesting, modeling, spreadsheet → **The Data-Driven Analyst**.
5. **Life-stage entry marker check** — first apartment/job/credit card, college graduation, getting married, having a baby, buying first home → **The Encouraging Mentor**.
6. **Default** — none triggered → **The Empathetic Guide**. Note "Default — Empathetic Guide" so reviewers know the tree was completed.

**Lock at brief stage. Writers do not re-select persona during drafting.**

---

# SECTION 4.3 — 9-COMPONENT POST ANATOMY + VISUAL PLACEMENT

Every AF post contains exactly 9 components. Each has a job, word target, and SEO function.

| # | Component | Reader Job | SEO Job | Word Target |
|---|---|---|---|---|
| 1 | Title / H1 | Click trigger | Primary keyword signal | SEO 50–65 chars / H1 60–80+ |
| 2 | Meta Description | SERP persuasion | CTR | 150–160 chars |
| 3 | Introduction | Earn the scroll | Engagement | 150–200 words + 40–60 word Answer Block |
| 4 | Table of Contents | Navigation | Internal linking signal | Auto-generated |
| 5 | Body Sections | Teaching + decision support | Topical coverage | 300–500 words per H2 |
| 6 | Visual Elements | Comprehension + trust | Image SEO + dwell | Per Visual Placement Map |
| 7 | Conclusion | Emotional landing | Keyword reinforcement | 100–150 (Tutorial/Listicle/Data-Led) or 150–250 (Story/Money Dominoes/Scenario) |
| 8 | CTA Block | Next step conversion | Conversion signal | 50–100 words |
| 9 | Author Bio | Trust + credibility | E-E-A-T compliance | 50–75 words |

## Mandatory 3-Part Conclusion (no exceptions)

- **Part 1 — Single Takeaway.** One sentence. NOT a summary. The distilled truth of the post. Pull-quote test: could it stand alone and still communicate the post's point? E.g., "The difference between staying in debt 17 years and getting out in 28 months isn't luck or income — it's knowing which number to attack first and adding $100/month to that one payment."
- **Part 2 — 24-Hour Action.** One specific, physical, time-bound action the reader can begin in the next 24 hours with no additional research. E.g., "Open your credit card's app right now, find the APR field, and write down balance, APR, minimum payment. 4 minutes."
- **Part 3 — Thesis Connection.** One sentence connecting the post's specific topic to "Money decisions create life consequences." Must reference something specific from this post — not copy-paste-able into any other post.

Navigation elements ("Read next," related-posts) appear AFTER Part 3, separated by a visual break. **Never replace any of the three parts with navigation.**

**Failure modes:** Ending with navigation; summarizing instead of distilling; vague 24-hour action ("start your debt payoff journey today"); missing thesis connection.

## Visual Placement — 7 Production Rules (NN/g eye-tracking, Module 1)

Top 20% of an article captures >42% of viewing time; top 40% captures >65%.

1. **First Meaningful Visual in Top 20%.** Must be functional (summary table, decision tree, comparison snapshot, key formula) — never decorative stock. On mobile, large hero images can be mistaken for ads ("faux ads") and scrolled past.
2. **Visual Density:** one meaningful visual per 400–700 words. Meaningful = teaches, proves, compares, or converts. Decorative does not count.
3. **Callout Box Budget:** max 1 callout per screenful in the top 20%. Mission-critical only. Never stack callouts back-to-back without substantial body text between.
4. **Chart Placement Sequence:** always Setup (1–2 sentences naming the question and what to look for) → Chart (minimalist, direct labels, no legend lookups) → Interpretation (2–6 sentences translating into a money decision).
5. **CTA vs Informational Callout Separation:** informational callouts adjacent to the concept; CTA callouts at section boundaries, never mid-paragraph. Primary CTA near the end after value delivered; optional early CTA after the first framework/table that delivers value.
6. **Monetization Distance:** never place affiliate widgets, promo banners, or newsletter CTAs adjacent to charts/tables that must be trusted. Ads can poison adjacent content per NN/g.
7. **One Dominant Element Per Viewport:** mobile screens get one dominant attention object (headline, table, chart, or step graphic). Multiple competing colored blocks create scanning confusion.

## Visual Placement Map by Post Type

| Post Type | First Visual | Ongoing | Charts | Callouts | CTAs |
|---|---|---|---|---|---|
| Pillar Guide (3000+) | Summary table / decision tree after intro, top 20% | One per major section, prioritize first 2 screenfuls | Setup-chart-interp; declutter | Low density top 20%; no ad-like styling | Primary late; optional early after first win |
| Tutorial | Process map / step list before first action step | Screenshot/diagram per 2–4 step cluster | Only if measuring outcomes | Pitfall callouts near risky steps; don't stack | After successful completion milestone |
| Listicle | Scannable index + best-overall comparison card near top | Consistent repeating visual unit per item | Rare; summarize key metric per item | Minimal; listicles already modular | End + optional mid-list after top pick cluster |
| Comparison | Comparison table / winner-by-scenario matrix above fold | Micro-tables per criterion | Direct labels for fees/rates | "How to choose" callouts; neutral tone | Only after recommendation logic established |
| Scenario / Decision | Decision tree or scenario visual top 20% | One per scenario branch | Near interpretation if used | Stakes Moment + How-To Moment callouts | After decision framework fully presented |
| Data-Led | Key finding chart / headline metric top 20% | Interleave charts with interpretation | Heavy use, minimalist; no chartjunk | Methodology/limitations near first chart | Late; avoid polluting chart zones |
| Money Dominoes | Chain-reaction visual after the setup paragraph | One per domino transition | Before interpretive paragraph for each stage | Money Dominoes chain callout per link | After full chain demonstrated |

---

# SECTION 4.4 — TITLE MASTERY: 7 FORMULAS, SCORECARD, A/B TESTING

## Two-Title Workflow

Every post has two titles, treated as separate assets:
- **SEO Title Tag** — 40–60 chars. Appears in Google results. Optimized for CTR + keyword placement. **The hook.**
- **H1 On-Page Title** — 60–80+ chars. Appears on the page. Longer, more descriptive, more emotionally engaging. **The promise.**

They can be different.

## Hooks & Title Formulas — Companion File Load Rule

The 7 formulas below are the structural architecture. The full hook system (200+ ready-to-adapt templates across 10 categories A–J, plus series-specific formulas for Money Dominoes, First-Gen, and Real Numbers, plus bracket variations) lives in the **Adulting Finance — Master Hook & Title Formula Reference** companion file (Drive ID: `1s6cyUx8BM7TnpkAFc3tW2Zo4r1RTWGfX7_DD3Jk7qjk`). Load alongside the Playbook before any title generation session. Uploaded files take priority over Drive links — if uploaded, use directly. If Drive link is inaccessible, request the upload before proceeding. The session does not advance without this file.

**Hard session gate:** Write a minimum of **10 title options** using **at least 5 different hook categories** from the Hooks file before scoring any of them. No session advances to Article Brief approval with fewer than 10 title options scored.

## The 7 Title Formulas

1. **Number + Pain/Gain** — `[Number] [Thing] That [Outcome] When [Scenario]`. Ex: "7 Budget Categories That Actually Work When You're Living Paycheck to Paycheck."
2. **How-To + Without Pain** — `How to [Outcome] Without [Pain]`. Ex: "How to Build an Emergency Fund Without Cutting Everything You Enjoy."
3. **Question + Scenario** — `[Question] If [Specific Scenario]?` Ex: "What Happens to Your Student Loans If You Leave the Country?"
4. **Consequence Chain / Money Dominoes** — `How [Small Action] Can [Large Consequence] Over [Timeframe]`. Ex: "How One Late Payment Can Cost You $47,000 Over 10 Years."
5. **Real Numbers / Data-Led** — `We [Research Action] — Here's [Discovery]`. Ex: "We Analyzed 1,200 Budgets — Here's Where Most People Overspend."
6. **First-Gen Angle** — `The [Valuable Thing] Nobody Taught [Target Group]`. Ex: "The Financial Cheat Codes Nobody Taught First-Generation College Grads."
7. **Bracket Boost** — `[Title] [Bracket with Real Asset]`. Approved brackets: `[2026 Updated]`, `[Free Template]`, `[Calculator]`, `[Step-by-Step]`, `[With Examples]`, `[Printable Checklist]`. Brackets only with a real asset.

## 10-Point Title Scorecard (publish floor: 8/10)

| # | Criterion | Pass | Fail |
|---|---|---|---|
| 1 | Character count 40–60 (SEO title) | 52 chars | 38 or 72 |
| 2 | Primary keyword in first 60 chars of H1 | Appears naturally | Buried at end / missing |
| 3 | Specific outcome or number | "$47,000" / "7 steps" | Vague benefit |
| 4 | "So what?" test passes | Reader knows why to care | Generic topic label |
| 5 | ELI12 test | A 12-year-old gets the gist | Requires finance vocab |
| 6 | Does not start with "The" / "A" filler | Active opening word | "The Guide to…" |
| 7 | Positive or neutral sentiment | Empowering / curious | Fear-based clickbait |
| 8 | Bracket only with real asset | `[Free Calculator]` | `[Must Read!]` |
| 9 | Works as standalone social caption | Shareable without context | Needs the article |
| 10 | Not answerable with just "No" | Opens exploration | "Is Budgeting Important?" |

## Title A/B Testing Workflow

1. Identify candidates: GSC pages with impressions >500 and CTR <2.5%.
2. Write 3–5 alternatives, applying different formulas; keep keyword placement consistent.
3. Set baseline: record current CTR, impressions, average position for 21 days.
4. Change one variable at a time — only the SEO title. Do not change H1, meta description, or content simultaneously.
5. Wait 21–28 days minimum.
6. Compare results. **Mobile CTR is primary signal**; desktop secondary.
7. Title Testing Tracker fields: date changed, old title, new title, baseline CTR, new CTR, impressions, verdict.

---

# SECTION 4.5 — INTRO FRAMEWORKS + INTENT MATRIX

Intro job: convince the reader the next 1,500+ words are worth their time, in 150–200 words plus a 40–60 word Answer Block.

- **Framework A — APP (Agree → Promise → Preview).** Use for pillar guides, comprehensive how-to, beginner content. Start with shared reality, state what the post gives, preview what's coming.
- **Framework B — PAS (Problem → Agitate → Solve).** Use for scenario/decision posts, Money Dominoes, debt content. Name the problem, show why it's worse than they think (with numbers), promise the path out.
- **Framework C — Story Bridge.** Use for first-gen, financial psychology, life-stage. Micro-scenario the reader recognizes → bridge to teaching → promise of change.
- **Framework D — Data Hook.** Use for data-led, listicles, comparison. Surprising number → context → preview of what the data reveals.
- **Framework E — Direct Answer.** Use for informational queries, snippet targets, FAQ-style. Answer in first sentence → qualify (the "it depends") → promise depth.

## Intent-to-Framework Matrix

| Search Intent | Best Framework | Backup |
|---|---|---|
| Informational ("what is X") | Direct Answer | Data Hook |
| Navigational ("how to do X") | APP | PAS |
| Transactional ("best X for Y") | Data Hook | Direct Answer |
| Problem-aware ("X not working") | PAS | Story Bridge |
| Emotionally charged ("scared about X") | Story Bridge | PAS |
| Comparison ("X vs Y") | Data Hook | Direct Answer |

---

# SECTION 4.5-A — THE FIVE AF WRITING STYLES

Every post belongs to one style, determined by the title's language, structure, and intent signal. Identify before drafting. Do not mix styles within a post.

## Style 1 — TUTORIAL
- *What:* Step-by-step instruction for a specific financial task.
- *Title signals:* "How to," "Step-by-step," "Guide to," numbered steps, process verbs (Set up, Build, Create, Open, Start).
- *Architecture:* Intro = APP or Direct Answer. Numbered steps, one H2 per major phase. Every step: what to do + why it matters + what it looks like done correctly. Screenshots/decision callouts at every place the reader could go wrong.
- *Word count:* 1,800–3,200 (SERP avg +15%).
- *Register:* Calm, competent, slightly impatient with unnecessary complexity.
- *Tone dial:* Warmth 3 / Urgency 3 / Authority 4 / Humor 1 / Formality 3.
- *FAQ:* After the last step, target "what if it doesn't work" + edge cases.
- *Money Dominoes insert:* Optional; only if the task connects to a meaningful downstream consequence.
- *Distinctive rule:* Every section must produce a completed action. If a section could end without the reader doing anything, it is explanation writing — fix by adding the specific action at the end.

## Style 2 — STORY / NARRATIVE
- *What:* First-person or close-third narrative using a real or constructed scenario to teach through lived experience.
- *Title signals:* "What happened when," "I paid off," "The month I," "How one decision," scenario phrasing, specific names.
- *Architecture:* Intro = Story Bridge (always). Chronological / milestone-based — moves forward in time, not by topic. Every section: scene + internal experience + decision + consequence. Teaching embedded inside the narrative, not summarized at end.
- *Word count:* 1,500–2,800 (shorter is often stronger).
- *Register:* Vulnerable, honest, slightly imperfect — must believe the person is real.
- *Tone dial:* Warmth 5 / Urgency 3 / Authority 3 / Humor 3 / Formality 1.
- *Voice:* First-person mandatory for personal experience; close-third ("Sarah had $12,400 in credit card debt when she…") for constructed scenarios.
- *FAQ:* Only if genuine questions arise. Do not force.
- *Money Dominoes insert:* At the narrative's turning point — where the reader chose differently and the chain reaction began.
- *Distinctive rule:* The information is in the story, not after it. If teaching content could be extracted and the story discarded, it is a Tutorial with a story intro — fix by ensuring decision points and consequences are only understandable in narrative context.

## Style 3 — CONTRARIAN
- *What:* Directly challenges a widely held belief or popular financial wisdom using evidence, calculation, or real-world outcomes.
- *Title signals:* "Why you shouldn't," "Stop doing," "The problem with," "Why [popular advice] is wrong," "The myth of," "What nobody tells you about."
- *Architecture:* Intro = PAS, with the conventional advice itself as the "problem." Sections: (1) state the conventional wisdom fairly — never straw-man, (2) show conditions under which it fails, (3) show evidence/calculation for the alternative, (4) give the decision framework for when each approach applies. **Always include a "when the conventional wisdom is right" section** — trust signal.
- *Word count:* 2,000–3,500.
- *Register:* Confident, evidence-backed, slightly irreverent but not dismissive.
- *Tone dial:* Warmth 2 / Urgency 3 / Authority 5 / Humor 3 / Formality 3.
- *Data:* Tier 1 or Tier 2 evidence required for the counterargument. Personal opinion insufficient. Cite and show calculations.
- *FAQ:* Essential — addresses the most likely objections.
- *Money Dominoes insert:* Use to show downstream consequence of conventional vs alternative.
- *Distinctive rule:* The post only works if the counterargument is stronger than the conventional wisdom. If evidence is weak or the conventional wisdom is correct in most cases, write a Clarity post instead.

## Style 4 — DATA-LED
- *What:* Anchored by a specific data, research finding, or original analysis. The data is not supporting evidence — it is the central claim.
- *Title signals:* "The data on," "We analyzed," "According to," specific numbers, "Here's what [X] Americans actually spend on," "The real cost of," statistics-forward framing.
- *Architecture:* Intro = Data Hook (always). Sections: (1) key finding stated clearly, (2) context — why it matters for the reader, (3) breakdown — how the number was derived/composed/varies, (4) reader's personal version — how to calculate their number, (5) what to do with it.
- *Sourcing:* Every data claim requires a named source (Tier 1 or 2), date of data, methodology/sample. Original calculations using public data acceptable as anchor if methodology disclosed in full.
- *Visuals:* Charts/tables not optional. Apply Setup-Chart-Interpretation for every visualization.
- *Word count:* 1,800–3,200 (longer if multiple datasets).
- *Register:* Clear-eyed, authoritative, slightly surprising — the data does the emotional work.
- *Tone dial:* Warmth 2 / Urgency 2 / Authority 5 / Humor 1 / Formality 4.
- *GEO priority:* Highest GEO-value post type — optimize aggressively per Section 5.10.
- *FAQ:* After main data sections, target "what does this mean for me specifically" + methodology questions.
- *Money Dominoes insert:* Essential — translate aggregate finding into individual chain reaction.
- *Distinctive rule:* If data is not credible, specific, and translatable to the reader's own numbers, it is not Data-Led — it is a post that happens to contain a statistic.

## Style 5 — MONEY DOMINOES
- *What:* Narrative-causal post tracing a chain reaction from one financial decision through downstream life consequences. Defining structure: a 4-node chain.
- *Title signals:* "How [small action] leads to," "The chain reaction of," "What happens when," consequence-chain framing, "How [behavior] quietly [life outcome]," "The real cost of [behavior] over [time]."
- *Architecture:* Intro = PAS, the "problem" is the specific decision being traced.

  **The 4-Node Chain (mandatory):**
  - **Node 1** — Triggering decision/behavior. Specific, recognizable. *Not* "Not investing" — *yes* "Opting out of your employer's 401k match because the form looked confusing and you planned to do it later."
  - **Node 2** — First downstream financial consequence. **Show the math, don't state it.** "At 6% match on $52,000 = $3,120/yr. Over 15 years at 7% returns, $3,120/yr compounds to $78,400."
  - **Node 3** — Second consequence (financial or behavioral). The surprise — second-order effect the reader hadn't calculated. "Also miss the tax deduction → paying taxes on money that could have grown pre-tax → adds another $4,200 to the 15-year cost."
  - **Node 4** — **Life outcome (NOT another financial metric).** Options: retirement age, job freedom, health, relationships, children. "You work 3 more years than you needed to" ✓. "You have $78,400 less in retirement" ✗.

  Each node = its own H2. Money Dominoes visual (Section 5.2) appears immediately after the chain is introduced.

  **Reverse chain mandatory.** After the full chain, show what happens if the reader makes the opposite decision starting now. Gives agency, prevents horror-story ending.
- *Word count:* 1,500–2,500 (tight — propulsive, not exhaustive).
- *Register:* Urgent but not alarmist — "I did not know this was happening," not "I am doomed."
- *Tone dial:* Warmth 4 / Urgency 4 / Authority 4 / Humor 2 / Formality 2.
- *FAQ:* After full chain, target "what if I've already made this decision" + recovery paths.
- *Conclusion:* Part 3 (Thesis Connection) is the most important sentence — names the life consequence and connects to present choices.
- *Distinctive rule:* If any node could be removed without weakening the chain, the chain wasn't built right. If Node 4 is financial not life, the chain doesn't deliver the AF thesis. If reverse chain is missing, the post leaves urgency but no path forward.

## Style Identification — Title Test

| Title Pattern | Style |
|---|---|
| "How to [complete a specific task]" | Tutorial |
| "Step-by-step [process]" | Tutorial |
| "[Specific person] did [thing] — here's what happened" | Story / Narrative |
| "I [financial experience] and here's what I learned" | Story / Narrative |
| "Why you should stop [popular behavior]" | Contrarian |
| "The problem with [common advice]" | Contrarian |
| "The data shows [surprising finding]" | Data-Led |
| "We analyzed [X] — here's what we found" | Data-Led |
| "How [one decision] leads to [life consequence]" | Money Dominoes |
| "The chain reaction of [financial behavior]" | Money Dominoes |

**Tiebreaker rule:** When a title contains both a process signal ("How to," "Step-by-step") AND a personal narrative signal ("I paid off," "What happened when"), use word count target: SERP target <2,000 → Story/Narrative; ≥2,000 → Tutorial. If word count doesn't resolve, the primary emotional job decides: reader wants to understand an experience → Story; reader wants to complete a task → Tutorial.

## Content Pairs System

Every AF post belongs to one of two layers and has a required paired post.
- **ELI12 Post** — explains the concept. For first-time readers.
- **Adult Systems Post** — provides the execution tool. For readers ready to implement.

Every ELI12 links to its paired Adult Systems and vice versa. Both planned together in the editorial calendar — never publish one without scheduling the other. ELI12 prioritizes email opt-ins; Adult Systems prioritizes product/tool CTAs.

*Example:* ELI12 "What Is the Debt Avalanche Method?" ↔ Adult Systems "The Debt Avalanche Tracker: How to Run the Math on Your Actual Debts."

## "1 Rule 1 Tool" Series Format

- *Title signals:* "The [X] Rule That…" / "One Rule for…" / "The Only [Topic] Rule You Need."
- *Word count:* 800–1,400.
- *Structure:* Rule stated in one sentence → Why it exists → When it applies → When it doesn't → The one tool that applies it → FAQ (2–3 max).
- *Intro:* Direct Answer (always).
- *CTA:* Single lead magnet only — the tool referenced.
- *No Money Dominoes insert.*
- *Tone dial:* Warmth 3 / Urgency 3 / Authority 4 / Humor 2 / Formality 3.
- *Distinctive rule:* If you removed the rule or removed the tool, would the post still exist? If yes, it is a tutorial in disguise.

---

# SECTION 4.5-B — COMPARISON & REVIEW POST WRITING SPEC

A distinct sub-format within Data-Led. Highest affiliate-revenue + highest trust-risk posts on the site. **Architecture is in service of reader decision-making, not affiliate optimization.**

**Word count:** SERP top-5 avg × 1.20. Min 1,500, max 3,500 — beyond, split options into separate deep-dives linked from the comparison. Rate-sensitive (savings, credit cards, loans): add 200–400 words for mandatory data-freshness updates.

**Core principle:** A comparison that helps the reader make the right decision converts more affiliate clicks — and returns fewer readers — than one that steers toward the highest-commission product.

## Mandatory Section Sequence

1. **Decision Context (150–250 words)** — Who this is for, what scenario triggers it. "You've got your first real paycheck and HR just told you to pick a savings account. This comparison tells you which type is worth opening first." Eliminates the reader who shouldn't be reading; validates the one who should.
2. **Evaluation Criteria (BEFORE any products)** — Mandatory and non-negotiable. Every criterion reader-relevant — not "overall rating" but "monthly fee at $500 balance," "APY on balances <$10K," "minimum to open." Criteria stated AFTER products = post-hoc justification. Criteria stated BEFORE products = editorial integrity.
3. **Comparison Table** — All products vs all criteria.
   - **No highlighted "winner" column.**
   - No star ratings without disclosed methodology.
   - No "Editor's Choice" badges without editorial criteria stated in Section 2.
   - "Rates as of [Month Year]" footnote on all data.
   - **Include at least one "do nothing / no cost" baseline row.**
   - Mobile rendering: 2-column "Attribute | Value" for 2-option comparisons; Cardified Comparisons (Row Layout) for 3+ options to avoid horizontal scroll.
4. **"Which Is Right For You" Framework** — Most important section, most frequently omitted. Format: "Choose A if [conditions]. Choose B if [conditions]. Choose neither if [condition]." Written **without naming a "best" option overall.**
5. **Expanded Deep Dives (optional)** — H2 per option only when the table alone doesn't give enough to decide.
6. **FAQ** — Mandatory question: the "what if my situation doesn't fit any of the 'choose X if' conditions" scenario.

## Editorial Neutrality Rules

1. **Never highlight a winner visually without criteria.** A visual highlight = recommendation; a recommendation without criteria = opinion; an opinion in a comparison post = trust violation.
2. **Disclose affiliate relationships at the top, not in a footnote.** Disclosure template: "Adulting Finance earns a commission if you open an account through some links in this post. That never changes what we recommend — the comparison below is based on [named criteria], not commission rates."
3. **Never omit the worst performer if it is widely used.** Readers who use it and find it missing conclude (correctly) the comparison isn't comprehensive.
4. **Always include the "do nothing" baseline.** Anchors the comparison in the reader's real situation.
5. **Data must be current within 30 days for rate-sensitive comparisons.** Add "Rates verified [date]." Calendar reminder for re-verification within 30 days of publication.

## Affiliate CTA Placement (Comparison Post Exception)

Comparison posts are the exception to the standard 3-CTA Rule.
- **CTA 1** — In the comparison table itself. Clearly labeled "Open Account"/"Apply" button next to each product row, visually distinct, explicit affiliate label.
- **CTA 2** — In the "Which Is Right For You" section, after the framework — one product-specific CTA for the option matching the median reader's criteria.
- **CTA 3** — End of post, standard placement.

**Never place affiliate CTAs adjacent to the evaluation criteria section or the comparison table.** Trust-visual adjacency rule (Section 5.1) applies.

---

# SECTION 4.5-C — FORMAT TRANSLATION TABLE

Translate content calendar format labels into closest AF execution style.

| Calendar Format | Closest Playbook Style | Primary Goal | Special Execution Note |
|---|---|---|---|
| ELI12 Explainer | Explainer / Awareness | Make the concept easy to understand | Prioritize clarity, low jargon, beginner recognition |
| Adult Systems | Execution / Systems | Turn understanding into repeatable action | Focus on steps, structure, implementation logic |
| Comparison | Comparison Template | Help the reader choose | Keep tradeoffs explicit, reduce ambiguity |
| How-To + Template | Tutorial + Lead Magnet | Help the reader complete a task | Pair the how-to with a downloadable/tool |
| Real Cost / Consequence Chain | Money Dominoes / Real-Cost Style | Show downstream cost of a behavior | Emphasize consequence flow, hidden cost, urgency |
| Flagship Long-Form | Pillar / Flagship Authority | Build authority around a major topic cluster | Structure for breadth, depth, hub-style usefulness |

If no exact match exists, use closest playbook style and make the smallest necessary adjustment — do not invent a new style.

---

# SECTION 4.6 — H2/H3 HIERARCHY RULEBOOK + FAQ ACTION-SENTENCE RULE

## Heading Character Ranges

| Level | Range | Failure Mode |
|---|---|---|
| H1 | 50–65 chars (SEO title) / 60–80+ (on-page) | <50 = vague; >65 = truncated in search |
| H2 | 40–70 chars | <40 = vague; >70 = truncated on mobile |
| H3 | 30–60 chars | <30 = lazy label; >60 = sentence, not heading |
| H4 | 20–50 chars | Rarely needed (see H4 rule) |

## The 3-Question Test (every heading must pass)

1. Does it tell the reader what's coming? (Scanning headings-only must reveal the article's logic.)
2. Does it make them want to keep reading? ("The Budget" kills scroll; "Why Most Budgets Fail by Week Three" earns it.)
3. Would it work as a standalone featured-snippet heading? (Question users actually search + 40–60 word answer below = snippet eligibility.)

## Keyword Placement in Headings

- **Primary keyword:** at least one H2, ideally the first H2.
- **Secondary keywords:** distributed across H3s naturally.
- **LSI / related terms:** remaining H2/H3s where they fit without forcing.
- **Never stuff.** If a heading reads like a keyword list, rewrite. Reader first, search second.

## H2 Cadence Rule

One H2 per 300–500 words. If a section under one H2 exceeds 500 words, add H3 subheadings.

## H4 Rule

H4 only when an H3 genuinely has sub-components needing separation. In most AF posts, H4 is unnecessary. If reaching for H4, first ask: should this be an H3 under a different H2? Usually yes.

## Heading Formatting

- Never bold/italic inside headings (Kadence handles styling).
- Never end headings with periods.
- Questions in headings are strong for snippets — use for FAQ-style H3s.
- Parallel structure within a section: if one H3 starts "How to," all H3s under that H2 should start "How to."

## FAQ as Formal Structural Element (Section 4.3 supplement)

The FAQ is a required structural element in every AF post. Not optional. Same editorial discipline as intro/H2/conclusion.

**Position (fixed):** Conclusion → Type C CTA → FAQ → Author Bio. Do not move. Do not embed mid-post.

**Question Count by Post Type:**

| Post Type | Required Question Count |
|---|---|
| Tutorial | 5–7 |
| Story / Narrative | 3–5 |
| Data-Led | 5–8 |
| Contrarian | 4–6 |
| Money Dominoes | 4–6 |
| Comparison / Review | 6–8 |
| Listicle | 4–6 |

Do not exceed upper bound. Do not fall below lower bound.

**Question Sourcing — Strict Priority Order:**
1. **Google's People Also Ask** (target keyword). Prioritize questions the body doesn't already fully answer.
2. **Competitor FAQ sections** (top 5 SERP). Add anything AF hasn't sourced from PAA and the body doesn't fully cover.
3. **Reader comments / emails / DMs.** Recurring (3+) reader questions = mandatory inclusion regardless of priority.
4. **Topic-logical questions** — genuine info gaps. Don't manufacture to hit count; revisit 1–3 first.

**Answer Formatting:**
- **Length:** 40–80 words. Under 40 = insufficient for schema. Over 80 = belongs in body.
- **No verbatim repetition** from body. Rephrase and condense.
- **Mandatory action sentence (closing):** specific, immediate (present-tense: open, set up, call, calculate, download), singular (one action). Operates with Type C completion-moment energy.
  - Acceptable: *"Open your bank's app right now and set up an automatic $50 transfer to your savings account for this Friday."*
  - Unacceptable: *"Consider taking steps to improve your savings habits."*

**Banned endings:** generic conclusions; "consult a professional" redirect as the final sentence; passive summaries; "think about" / "consider."

**Schema requirement:** Every FAQ section wrapped in proper FAQPage schema (Companion Asset 8). Writers flag the section in the draft with `[FAQ SCHEMA REQUIRED]` immediately above the heading.

**Heading format (exact):** `Frequently Asked Questions` — not "Common Questions," "FAQs," "You Asked," or "People Also Ask."

**Editing QA check:** Read the last sentence of every FAQ answer aloud. Ask: "Can the reader begin doing this in the next 24 hours?" If no, rewrite as action.

---

# SECTION 4.7 — ON-PAGE SEO + RANK MATH CONFIGURATION

## Primary Keyword Placement Checklist

The primary keyword must appear in:
1. H1 title (within first 60 chars).
2. First 100 words of the introduction.
3. At least one H2 (preferably the first H2).
4. Meta description (within 150–160 char limit).
5. URL slug (core of the 3–5 word slug).
6. First image alt text (incorporated naturally).
7. Conclusion paragraph (natural reinforcement, not stuffing).

## URL Slug Rules

Format: `adulting-finance.com/[slug]`. 3–5 words max. Contains primary keyword. **No dates** (look stale on update). No stop words (the/a/an/of/for/in/on/to/and). Hyphens only (no underscores). All lowercase. **Never change a published slug** (breaks backlinks, resets GSC).

- Good: `emergency-fund-guide`, `debt-avalanche-vs-snowball`.
- Bad: `the-complete-guide-to-building-an-emergency-fund-in-2026`, `post_about_budgeting`.

## Meta Description Rules

150–160 chars. Contains primary keyword naturally. Contains a value proposition. Ends with implicit/explicit CTA. Matches search intent (informational = "learn," transactional = "compare," navigational = "step-by-step").

Template: `[What this post covers] + [specific benefit/number] + [implied action]`.
Example: *"Learn the exact debt payoff order that saves the most interest. Calculator + comparison chart included. Works for any income level."*

## Image Alt Text Rules

**One-Sentence Rule:** If you can read your alt text aloud and it tells a blind person exactly what they're missing — you're done.

- <125 chars.
- Lead with visual description before keyword phrase.
- Name specific data points in charts: *"Bar chart showing avalanche saves $1,400 more in interest than snowball."*
- Name specific tools in screenshots: *"Rank Math SEO settings panel showing focus keyword configuration."*
- Decorative images get empty alt (`alt=""`).
- Never start with "Image of" / "Picture of."

## Rank Math Configuration

- **Focus Keyword:** exact primary keyword.
- **SEO Title:** the SEO title (40–60), not the H1.
- **Meta Description:** write manually, never auto-generate.
- **Schema Type:** Article default. **Schema decision table:**
  - **Article** — primary type for all blog posts.
  - **FAQPage** — when post has dedicated FAQ with 4+ questions; combine with Article via `@graph`.
  - **HowTo** — Tutorial-style with numbered steps and defined outcome; combine with Article.
  - **FinancialProduct** — reviewing/comparing a specific financial product (savings, credit card, brokerage); use with Article.
  - **Dataset** — Data-Led with original AF-produced dataset; with Article.
  - **Default combine rule:** always include Article as primary; secondary types are additive via `@graph`, never replacements.
- **Breadcrumbs:** Enabled.
- **Open Graph:** Set featured image; verify title and description display correctly.
- **Canonical URL:** Self-referencing default (don't change unless consolidating).

## 2026 SEO Updates — AI Overview Optimization

LLM/AI agent systems are changing citation behavior. These additions strengthen traditional SEO AND AI citation probability:

1. **Direct answer sentences.** After each H2/H3 question heading, include a 40–60 word direct answer in the first paragraph. Serves snippets and AI Overview extraction.
2. **Statistical richness.** Specific numbers, percentages, dollar amounts, timeframes. Statistics increase LLM citation probability up to 40% (Princeton/Georgia Tech GEO study, 2024).
3. **Source citation density.** Cite primary sources (IRS, Federal Reserve, CFPB, specific institutions) **inline**. Authoritative attribution increases AI citation 20–25%.
4. **Named frameworks.** Give your original frameworks explicit names ("Money Dominoes," "The 60/40 Rule"). Named concepts get cited more.
5. **Entity clarity.** Author name, credentials, clear "About" references. LLMs favor identifiable entities with consistent knowledge graph presence.

---

# SECTION 4.8 — E-E-A-T, YMYL STANDARDS, AND THE SOURCING LADDER

All AF content is YMYL. E-E-A-T is the framework Google's quality raters apply. Bad financial advice harms readers directly.

## The Sourcing Ladder (Tier System)

Every claim must be sourced.

**Tier 1 — Primary / Authoritative (always preferred):** IRS publications and official tax guidance; Federal Reserve data and reports; CFPB resources; SEC filings and investor guidance; official platform docs (specific banks, brokerages, lenders); peer-reviewed academic research; Google's own documentation (Search Quality Rater Guidelines, developer docs); WCAG accessibility standards.

**Tier 2 — Expert / Industry (strong support):** SEO research from Backlinko, Ahrefs, Moz, SEMrush, Siege Media; Content Marketing Institute; HubSpot research; Nielsen Norman Group UX; Copyblogger editorial standards; recognized financial planning organizations (CFP Board, NAPFA); major financial publications (WSJ, Bloomberg) for data.

**Tier 3 — Practitioner / Community (signal only):** r/personalfinance, r/FIRE; personal finance blogger case studies; forum discussions and practitioner reports; verified-practitioner social. **Tier 3 NEVER overrides Tier 1–2 findings.**

**Prohibited list — never cite, reference, or link to:** content farms with no identifiable authors; sites with Google penalties; sources with undisclosed affiliate relationships; Wikipedia as a primary source (use to find primary sources, then cite those); social media as factual evidence (acceptable only for sentiment/anecdote); any source contradicting current IRS/Federal guidance without explicitly noting the conflict.

## Per-Article E-E-A-T Compliance Checklist

| Signal | Requirement | How |
|---|---|---|
| Experience | First-hand testing, real scenarios, personal examples | Include "I tested this" / "here's what happened when" with specifics |
| Expertise | Knowledge beyond surface | Show the math, explain the mechanism, address edge cases |
| Authoritativeness | Recognized as reliable source on topic | Consistent author bio, internal linking to related posts, external citations |
| Trustworthiness | Transparent, accurate, current, properly disclosed | Update dates, source citations, affiliate disclosures, disclaimer |

## YMYL Disclaimer

Every AF post includes a disclaimer. Human and collaborative, not corporate.

**Template:** *"This post shares research-backed strategies and real examples to help you think through [topic]. It is not personalized financial advice. Your situation has variables I can't see from here — income, debt, tax bracket, risk tolerance, dependents. Before making major financial decisions, consider consulting a certified financial planner who can see your full picture. Where I reference specific rates, limits, or rules, I've cited the source and date — but these change, so verify before acting."*

**Placement:** After the introduction, before the first H2. Style as a subtle callout (not a banner that looks like a legal warning).

**Scope note:** This placement governs the in-article disclaimer text only. The author byline (must be visible above the fold per Section 5.7 Checkpoint 1) is a CMS/Kadence theme setting, not in-article content. Byline placement is configured in WordPress post settings, not written into the article body.

---

# SECTION 4.9 — INTERNAL LINKING (HUB-AND-SPOKE)

## Architecture

Hub-and-spoke. Each of the 6 content pillars has one Pillar Page (hub) and multiple supporting posts (spokes). Every spoke links back to its pillar; the pillar links to every spoke.

**Pillar Page:** comprehensive guide (3,000–5,000 words) covering the entire topic at overview level, linking to every spoke for deep dives, primary ranking target for broad pillar keywords, updated whenever a new spoke is published.

## Spoke-to-Hub Linking Rules

1. Every spoke links to its pillar at least once — typically in intro or first body section.
2. Every spoke links to 2–3 sibling spokes (other posts under the same pillar).
3. Cross-pillar links sparingly — only when the content genuinely connects (e.g., debt → budgeting method).
4. **Anchor text must be descriptive** — never "click here" / "read more." Use the target post's primary keyword or a natural variation.
5. **Contextual placement** — links inside body paragraphs where the topic is relevant; not a "related posts" dump at the bottom.

## Pillar–Spoke Map

| Pillar | Hub Topic | Example Spokes |
|---|---|---|
| 1. Budgeting | Complete Guide to Budgeting Systems | Zero-based budget, 50/30/20, irregular income, budget apps comparison, first paycheck budget |
| 2. Debt Freedom | Complete Guide to Getting Out of Debt | Avalanche vs snowball, credit card payoff, student loans, consolidation, negotiating with creditors |
| 3. Smart Earning | Complete Guide to Increasing Your Income | Salary negotiation, side hustles, freelancing, passive income, career switching |
| 4. Life-Stage Finance | Money Guides by Life Stage | First job, moving out, getting married, having kids, mid-career optimization |
| 5. Financial Psychology | Understanding Your Money Brain | Shame and money, impulse spending, financial anxiety, couples and money, money scripts |
| 6. AI and Money | AI Tools for Personal Finance | AI budgeting tools, LLMs for finances, AI investing platforms, automation, AI tax prep |

## Density Targets

- **Minimum 3 internal links per post.**
- **Maximum 1 internal link per 300 words** (avoid over-linking).
- At least 1 link in the first 200 words.
- Pillar pages: 10–20+ internal links (one to each spoke).

## 4.9-A — Live vs Planned Link Rule

Only **published** posts may receive direct internal links in a live article. Planned posts (calendar only) remain planned links until actually published. Planned links may guide article structure and sequencing but must not appear as live internal links until the target exists. **Never insert broken, fake, placeholder, or imaginary internal links.** If no suitable published link exists, include no link rather than inventing one.

**Output note for insufficient live links:** If fewer than 3 published internal links are available at writing time, include only the available live links. Do not insert placeholder or planned links. Note in draft output: *"Internal links placed: [N]. Additional links to be added when [post title(s)] publish."* This satisfies the 0-G Output Contract item 7 without violating Rule 4.9-A.

---

# SECTION 4.10 — CTA AND MONETIZATION ARCHITECTURE

## The 3-CTA Rule

Every AF post = exactly 3 CTAs maximum. More than 3 = decision fatigue + "affiliate farm" perception.

- **CTA 1 — Early Soft CTA (optional).** Placement: after the first H2 that delivers value. Type: lead magnet / free tool / email signup. Tone: low-friction ("Grab the free template we use for this"). Visual: subtle callout, not a banner.
- **CTA 2 — Mid-Article Contextual CTA.** Placement: natural section boundary, middle third. Type: relevant to the section content (comparing tools → link detailed comparison; teaching a method → link the worksheet). Tone: integrated into teaching ("Here's the calculator that does this math for you"). Visual: inline link or small callout.
- **CTA 3 — End-of-Post Primary CTA.** Placement: after the conclusion, before author bio. Type: primary conversion goal (email list, lead magnet, course, key resource). Tone: direct but earned ("You've read the whole system. Here's the template that puts it into action."). Visual: distinct CTA block — clearly a next-step invitation, not a pop-up.

**Comparison post exception:** see Section 4.5-B.

## Email CTA Formula

`[Acknowledge what they just learned] + [Name the free resource] + [State the specific benefit] + [Single action button]`.

Example: *"You just learned the exact debt payoff order. Want the spreadsheet that calculates your personal timeline? The Debt Freedom Calculator shows your payoff date, total interest saved, and monthly targets based on your actual numbers. Get the free calculator →"*

## Monetization Integration Rules

- Affiliate links disclosed **above the fold** AND near each affiliate link.
- Never position affiliate recommendations as the "only" option.
- Always include a non-affiliate alternative (DIY, free tool, or "do nothing").
- Product recommendations include specific, verifiable pros AND cons.
- Never style affiliate callouts to look like editorial content — visual separation mandatory.

---

# SECTION 4.11 — CONTENT WORKFLOW (8-STAGE PRODUCTION SYSTEM)

## 4.11-A — AI Tool Role Map

The model used for drafting does not change source-use protocol, YMYL safeguards, or Fact-Verification Ledger requirements. If a model generates a sentence that cannot be verified under AF standards, that sentence does not advance.

| Capability | Primary Role | Best Use | Do Not Use As |
|---|---|---|---|
| LLM (long-form drafting) | Primary drafting engine | First drafts, ELI12 rewrites, paragraph restructuring, expansions preserving voice | Final authority on rates, thresholds, limits, or YMYL claims |
| LLM (complex reasoning) | High-complexity reasoning + synthesis | Pillar guides, long-form structure planning, argument logic, framework building | Speed drafting for routine posts |
| LLM (ideation / production) | Ideation + production support | Title generation, outline options, hook development, CTA variants, social captions, angle testing | Primary fact-checking layer for YMYL |
| LLM (source-backed research / verification) | Source-backed verification | Fact-checking, source gathering, citation validation, live verification, FVL support | First-pass long-form drafting for AF posts |

**Operational rule:** Draft with the tool best suited to the writing task; verify with the tool best suited to sourcing. For YMYL, an LLM configured for source-backed research is the preferred verification layer before review/scoring/QA.

## The 8 Stages (+ Stage 9 Publication Update)

**Stage 1 — Keyword Assignment.** Receive keyword from editorial calendar/publisher. Confirm search intent (informational/transactional/navigational/comparison). Identify primary, secondary, LSI terms. Check difficulty and current SERP landscape.

**Stage 2 — Competitor Audit.** Pull top 5–10 ranking URLs. Run the 45–60 minute Competitor Dissection Protocol (Section 5.5). Identify topical, comprehension, trust, and emotional-register gaps. Document in Article Brief.

**Stage 3 — Article Brief Creation.** Select post type. Set tone dial. Identify primary + secondary persona. **Calculate and declare target word count before writing begins** — fetch competitor word counts from full page reads (not snippets), avg of top 5, apply multiplier from §5.6 (1.15× low gap / 1.20× medium / 1.25× high), record as binding target. Min 2,000 for YMYL. *Writing without a declared word count target is a Stage 3 failure.* Outline H2/H3. Plan visuals via Visual Placement Map. Define the original contribution. Select intro framework. **Confirm content pair status:** record one of `[PUBLISHED — URL: ___]`, `[SCHEDULED — date: ___]`, or `[NOT YET PLANNED]`. If NOT YET PLANNED, flag and schedule the pair before this post publishes. Do not advance without pair status recorded.

**Stage 4 — First Draft.** Write intro using selected framework (150–200 + 40–60 word Answer Block). Body sections per H2/H3 hierarchy. Apply ELI12 voice + tone dial. Include source citations inline (Tier 1/2/3 labeled). Conclusion (3-part). 3-CTA Rule.

**Stage 5 — Visual Production.** Convert info architecture into a complete visual package. Visuals are not decorative.
- In-post visuals per Visual Placement Map.
- Data Visualization Framework (Section 5.4) for chart type, table structure, infographic suitability.
- AF Canva Pro brand system on all post assets.
- Featured image at 1200×630px (blog hero + Open Graph).
- 3 Pinterest pin variants at 1000×1500px each (minimum publication set).
- Optimize all exports to WebP where applicable, compress aggressively, file sizes under 100KB without visible quality loss.
- Descriptive non-stuffed ALT text for every image.

**Required Post Asset Bundle:** Featured Image 1200×630 (every post). Pinterest Pins — 3 static at 1000×1500 (every post). YouTube Thumbnail 1280×720 (only when video companion exists). Twitter/X Card 1600×900 (key statistic/quote). Email Header 600×200 (when newsletter promoted).

**Speed rule:** Visual production normally 20–30 min/post using locked templates. Don't design routine assets from scratch unless a documented reason for custom treatment exists.
**Pinterest rule:** Minimum 3 pins at publication. Section 4.12 governs the expanded variation system.

## 4.11-B — Canva Brand Kit and Template Lock

| Template | Dimensions | Primary Use |
|---|---|---|
| Pinterest Pin | 1000×1500 | Standard post promotion, listicle pins, tip cards, template previews |
| YouTube Thumbnail | 1280×720 | Video companion assets |
| Blog Featured Image | 1200×630 | Blog hero, Open Graph, social sharing base |
| Twitter / X Card | 1600×900 | Quote card, stat card, post promotion |
| Email Header | 600×200 | Newsletter promotion, ConvertKit broadcast/sequence |

**Brand Kit lock requirements:**
- Lock all primary and secondary AF brand colors in Canva before production.
- Heading font: Montserrat Bold; body font: Inter Regular. *(Canva and static brand assets only — the live WordPress site uses the system font stack defined in Appendix A.3.)*
- Upload AF logo as transparent PNG; same approved file across all templates.

**Design rule:** Adapt copy, imagery, and emphasis within the approved template family. Do not invent a new visual system per post.

**Stage 6 — Kadence Formatting.** Apply Kadence block formatting per Section 5.3. Set up callouts with correct color coding. Configure comparison tables for mobile-safe rendering. Place ConvertKit opt-in mid-article. Add Table of Contents block (H2 + H3, collapsible on mobile). Verify responsive behavior on mobile preview.

**Stage 7 — Pre-Publish QA.** Run Voice Consistency Checklist, Pre-Publish QA Checklist, Per-Article E-E-A-T Checklist (Section 4.13). Run **GEO pass** (AI appearance signals). Inline checklist:
1. Lead paragraph of every H2 contains a named statistic with inline source citation.
2. Every key concept has a clean definitional sentence (`[Term] is [definition]`).
3. At least one comparison structured as explicit parallel contrast (`Method A does X. Method B does Y.`).
4. "According to [Source]" phrasing appears 3–5 times.
5. Step-by-step content formatted as numbered lists, not prose.
6. Answer Block in intro is 40–60 words, self-contained, direct.
7. Named AF frameworks (Money Dominoes, ELI12) explicitly labeled, not paraphrased.

Verify all links work (internal + external). Check Rank Math SEO score (target green). Flesch-Kincaid readability (Grade 7–8). Mobile preview on actual device.

**Stage 8 — Publish and Distribute.** Publish in WordPress. Submit URL to GSC for indexing. Share on social per distribution plan. **Pinterest distribution:** publish/queue the 3 mandatory variants at launch; for posts on extended distribution, build the full 5-pin variation bank (§4.12-A) scheduled across separate weeks rather than clustered. Add to internal linking structure (update pillar page, links from sibling posts). Set refresh reminder for 6-month review.

**Stage 9 — Publication Update Protocol.** After publication, update site's external operating files: URL, status, live links, pillar tracker, pair relationship. *(These updates happen outside the AF Writing Playbook. The playbook remains a fixed evergreen writing asset and does not store changing operational data.)*

---

## 4.11-C — Article Brief Field Summary (Companion Asset 1)

*The Article Brief is the handoff document. §0-B Step 2 and Stage 3 of the workflow both require it complete before drafting. The full template lives in Companion Asset 1; the field list below is the working summary so a writer can recognize what each field requires without re-loading the full asset. Required-to-start fields (Stage 2 minimum to begin a new project): Fields 2, 5, 6, 12, 16.*

| # | Field | Status | What It Requires |
|---|---|---|---|
| 1 | Post Title (Working) | REQUIRED | Working title + Title Iteration Log (v1/v2/v3 with scorecard result + date). Final title scored against §4.4 Scorecard before publication. |
| 2 | Primary Keyword | REQUIRED-TO-START | `keyword (monthly volume, KD score)` + source (Ahrefs / Semrush / Moz / GKP) + data pull date. Volume must be confirmed and documented. |
| 3 | Secondary Keywords | REQUIRED | 3–5 secondary keywords with monthly volume + intended placement. Integrated naturally — never forced. |
| 4 | Target URL Slug | REQUIRED | 3–5 words, primary keyword included, lowercase, hyphen-separated, no dates, no function words, no special chars, confirmed unused on AF domain. |
| 5 | Writing Style | REQUIRED-TO-START | One of: Tutorial / Story-Narrative / Contrarian / Data-Led / Money Dominoes (§4.5-A). Rationale must align with search intent (Field 8). |
| 6 | Selected Personas | REQUIRED-TO-START | Reader Persona (§4.2 archetype) + Voice Persona (§4.2 narrator mode) + selection signal from Persona Decision Tree + 2–3 voice reminders specific to this post. |
| 7 | Target Word Count | PRE-PUBLICATION | Range (low–high). Minimum 1,500 words. Basis: writing style + competitor avg (top 3 SERP) + content gap volume + visual ratio + pillar/spoke designation. Pillars 3,500–6,000; tutorial spokes 1,800–2,800; tight narrative 1,500–2,200. Never pad. |
| 8 | Search Intent | REQUIRED | Primary: Informational / Navigational / Commercial / Transactional. Secondary intent if applicable. SERP evidence (snippet type, formats ranking, tools/calculators present, ad density, PAA questions). |
| 9 | Target Reader Profile | REQUIRED | One sentence: *"The reader arriving at this post is __, who currently knows __, and needs to leave this post able to __."* Governs vocabulary ceiling, knowledge baseline, success condition. |
| 10 | Competitor Analysis Status | PRE-PUBLICATION | Completed / In Progress / Not Started. If completed, attach Companion Asset 2. Top 3 organic results reviewed (URL, DA, word count, format, strength, weakness). |
| 11 | Content Gaps Identified | PRE-PUBLICATION | 2–5 specific gaps in competitor content + how this post fills each. Specific (`competitors lack a monthly savings calculator`) — not vague (`competitors don't go deep enough`). |
| 12 | Originality Element | REQUIRED-TO-START | Mandatory per §0-F. Type: Proprietary Framework / Unique Data Combination / Novel Analogy / Decision Tree / Case Study / Other. Description specific enough that a different writer could reproduce it. Position in post named. |
| 13 | Pillar Page Assignment | PRE-PUBLICATION | Spoke or Pillar. If Spoke: name pillar + URL. If Pillar: list planned spoke posts. **Orphans not approved.** |
| 14 | Internal Link Targets | PRE-PUBLICATION | Min 3 outgoing internal links (post title, URL, anchor idea, placement context). Plus incoming-link opportunities (existing AF posts that should link TO this new post post-publication). |
| 15 | CTA Strategy | REQUIRED | Primary conversion goal (email / lead magnet / affiliate / product / tool / share / other). Type C completion-moment description. Lead magnet / next step offered. CTA placement plan (mid-post / end / sidebar). |
| 16 | YMYL Sensitivity Level | REQUIRED-TO-START | High (direct financial/tax/legal/investment/insurance — Tier 1 mandatory, legal review recommended) / Medium (general financial education — Tier 1 for stats, Tier 2 for context) / Low (lifestyle/mindset — standard sourcing). Rationale + disclaimer requirement. |
| 17 | Key Sources Pre-Identified | REQUIRED | 3–5 sources anchoring factual claims. Tier composition matches Field 16. Source name, tier, URL, publication/last-updated date, specific claim supported. Staleness check (>3 yr → VERIFY per §0-E Rule 3). |
| 18 | Visual Plan | PRE-PUBLICATION | Visual count target (competitor avg + 2; min 3). Slot assignments (top 20%, mid-article, per-H2, Money Dominoes, final). Type per slot (decision tree, table, chart, callout, flow). Kadence block per slot. |
| 19 | Publish Target Date | REQUIRED | Calendar date + production stage gates (audit due, brief lock, draft due, edit due, asset bundle due, publish). |

**Multi-session handoff rule (§0-B):** Sessions resuming a project must load the completed Article Brief from the prior session. Required brief fields for handoff: locked writing style, locked persona, tone dial settings, word count target, H2/H3 outline, competitor audit findings summary, originality statement. A session resuming without a completed brief restarts from Step 2.

---

# SECTION 4.12 — PINTEREST SEO SYSTEM

Pinterest is a visual **search engine**, not social media. Content shelf life: 3–6 months (vs hours on Twitter/Instagram). Highest-ROI social distribution channel for evergreen personal finance.

## Pin Specifications (2026 current)

| Element | Specification |
|---|---|
| Standard Pin Size | 1000×1500 (2:3) |
| Long / Infographic Pin | 1000×2100 max (1:2.1) |
| File Format | PNG or JPG |
| Max File Size | 20 MB (aim under 10 MB) |
| Text Overlay | Eye-catching headline, 60–80pt, top of pin |
| Logo / Watermark | AF branding on every pin |

## The 3-Pin Strategy (publication minimum)

For every blog post, create 3 visually distinct pins:
1. **Pin A — Title Focus:** blog post title as headline, clean background, brand colors.
2. **Pin B — Data/Number Focus:** lead with the most compelling statistic/number from the post.
3. **Pin C — Benefit/Outcome Focus:** lead with the reader transformation/result.

Each pin meaningfully different — not just a color swap. Different headline, visual emphasis, emotional hook.

## 4.12-A — Extended Pin Variation Framework

The 3-pin strategy is the floor. For stronger distribution, use the 5-variation system that turns one post into a longer-lived visual sequence.

**Three primary pin archetypes:**
- **Template Preview Pins** — partial screenshot, styled mockup, worksheet/spreadsheet/tracker preview, resource interface. Used when post includes a content upgrade, free download, calculator substitute, checklist, or tool. **Show the thing, don't merely mention it.**
- **Tip Card Pins** — text-led, built for saves/shares/impressions. Value delivered on the pin itself: numbered list, short framework, before/after contrast, single actionable insight.
- **Infographic Pins** — tall visual assets built from original research, comparison logic, process flow, sourced statistics, or post-level data viz. Highest link-earning potential when the visual is useful enough to be referenced elsewhere.

**Preferred 5-Pin Framework (cornerstone / lead-magnet / data-led posts):**
1. Template Preview Pin highlighting the content upgrade/worksheet/tracker/downloadable.
2. Tip Card Pin using a numbered-list variation from the post.
3. Tip Card Pin using a key stat, before/after contrast, or transformation angle.
4. Infographic Pin built from the post's research, chart, comparison, or process flow.
5. Text-heavy Pull-Quote Pin using one high-value insight in large bold type.

**Scheduling rule:** Schedule the 5 variations across 5 separate weeks where possible. Extends distribution life, strengthens fresh-pin signal, increases ROI per production session.
**Capacity rule:** If time-limited, follow the 3-pin minimum at publication. Upgrade cornerstone, content-upgrade, and data-led posts to the full 5-pin framework whenever possible.

## Pinterest Algorithm Preferences (2026)

- **Fresh pins preferred:** algorithm prioritizes new, original pin images over repins. Create fresh designs, don't just re-share.
- **2:3 aspect ratio:** vertical 2:3 gets the most distribution.
- **Keyword-rich descriptions:** include target keywords naturally (Pinterest search is keyword-driven).
- **Board structure:** organize by content pillar; board names include keywords.
- **Consistent pinning:** regular cadence outperforms bulk pinning.

## Pin Description Template

*"[Keyword-rich benefit statement]. Learn [specific thing] in this comprehensive guide. Includes [free resource/template/calculator]. Perfect for [target persona description]. Read the full guide at Adulting Finance. #personalfinance #[pillar keyword] #[specific topic]"*

---

# SECTION 4.13 — ALL CHECKLISTS (Voice / Pre-Publish QA / E-E-A-T)

## Voice Consistency Checklist (during editing)

- [ ] ELI12 standard met: Flesch-Kincaid Grade 7–8.
- [ ] All finance jargon defined on first use with plain-language translation.
- [ ] Tone dial settings match the post type (check table).
- [ ] No condescending language ("it's simple," "just," "obviously").
- [ ] Primary persona language patterns used (check vocabulary table).
- [ ] Three-Word Test applied to any complex sentences.
- [ ] 60/40 ELI12 split maintained (60% Grade 7–8, 40% Grade 9–10 max).
- [ ] Paragraphs 2–4 sentences max.
- [ ] One idea per paragraph.

## Pre-Publish QA Checklist (The Last Gate — no post goes live until every box is checked)

**Voice & Tone**
- [ ] **Read the intro aloud** — does it sound like a smart friend, not a textbook? If not, rewrite.
- [ ] No sentences longer than 25 words without a compelling reason.
- [ ] At least one emotional acknowledgment in the first 300 words.
- [ ] ELI12 pass: every jargon term has a parenthetical translation on first use (default translations: §7-C.2).
- [ ] Scan for `should have` / `need to` / `obviously` — remove all instances.
- [ ] Six-attribute Voice Test (§7-C.1) passed on a random spot-check of 5 paragraphs.

**Title, Meta, Headings, Slug**
- [ ] Title scores 8+/10 on Title Scorecard.
- [ ] Meta description 150–160 chars with keyword and value proposition.
- [ ] URL slug 3–5 words with primary keyword.
- [ ] Introduction 150–200 words with Answer Block (40–60) using correct framework.
- [ ] H2 every 300–500 words; H3 as needed. No heading-level skips (H2 → H4).
- [ ] All headings pass the 3-Question Test.
- [ ] Primary keyword appears in: H1, first 100 words, one H2, meta, slug, first image alt.

**Content Quality**
- [ ] Every H2 section answers its subtopic completely (no "we'll cover this elsewhere" within a section).
- [ ] Every claim with a specific number has a named source.
- [ ] **All dollar amounts show the math** (or link to where the math is shown).
- [ ] All time-sensitive data includes `as of [Month Year]`.
- [ ] At least one personal experience sentence (E-E-A-T first-hand experience).
- [ ] Money Dominoes chain present if topic involves cascading financial decisions.
- [ ] **"Do nothing" baseline included in all comparisons** (cost of inaction visible).
- [ ] Draft word count within ±15% of declared Article Brief target. If over by >15%, trim before advancing. Record: Target [X] / Actual [Y] / Delta [Z%].
- [ ] Conclusion contains all 3 mandatory parts in order: (1) Single Takeaway — distilled, not summary; (2) 24-Hour Action — specific, completable in 24h; (3) Thesis Connection — references something specific from this post.
- [ ] Every FAQ answer ends with a specific 24-hour action sentence — verb the reader can perform, no hedging, no "consult a professional" redirect, completable within 24 hours.

**Visuals**
- [ ] Visual count meets or exceeds competitor benchmark + 2 (minimum 3 regardless of competitors).
- [ ] First meaningful visual appears in top 20% of content.
- [ ] Every chart has: title (takeaway, not topic), direct labels, source line.
- [ ] All tables render without horizontal scroll on mobile (test at 375px).
- [ ] All images have descriptive alt text under 125 chars.
- [ ] All images optimized: WebP with JPG/PNG fallback, under 150KB (target 100KB).
- [ ] **No stock photos of happy people holding credit cards** or other clichéd finance imagery.

**Internal & External Links**
- [ ] At least 3 internal links, at least 1 in first 200 words.
- [ ] External links: 2–4 to authoritative sources (government / research institutions).
- [ ] All external links open in new tab.
- [ ] No orphan links (every linked post also links back somewhere in the hub).
- [ ] §4.9-A Live vs Planned Link Rule satisfied — all internal links live or marked `[PLANNED LINK …]`.

**SEO, Schema, Technical**
- [ ] Rank Math green SEO score.
- [ ] Schema markup verified (Article + FAQPage / HowTo as applicable per §4.7 schema decision table).
- [ ] Page speed <2.5s LCP (Core Web Vitals).
- [ ] No layout shift (CLS <0.1).
- [ ] Canonical tag points to correct URL; no accidental noindex.

**GEO Compliance (§5.10)**
- [ ] Direct answer in first paragraph after intro (1–2 sentences).
- [ ] 5+ statistics with named sources in visible text.
- [ ] 3+ `according to [Institution]` attributions.
- [ ] Definitional sentences for all key terms.
- [ ] All comparisons in structured format (table or parallel sentences).

**Trust & Compliance**
- [ ] YMYL disclaimer present after introduction (light yellow callout).
- [ ] Author byline with relevant experience visible.
- [ ] Published date + last-updated date visible.
- [ ] No overpromising language (`guaranteed`, `risk-free`, `get rich`, `hack`).
- [ ] No fake urgency (`limited time`, `act now`, `only X left`).
- [ ] Affiliate disclosures visible above fold AND near each affiliate link.
- [ ] CTA asks proportional to value delivered.

**Callouts & CTAs**
- [ ] 3 CTAs maximum, correctly placed per 3-CTA Rule (§4.10) and Type A/B/C copy spec (§7-A).
- [ ] No two callouts back-to-back without intervening body text.
- [ ] Type C callout placed after conclusion paragraph, before author bio (non-negotiable).

**Distribution Assets (Stage 5 Bundle)**
- [ ] Featured image: 1200×630px, compressed <150KB, alt text set, descriptive filename.
- [ ] Pinterest pin (primary): 1000×1500px, text overlay legible at thumbnail (236px wide test).
- [ ] Pinterest pin (variant): alternate design for A/B testing.
- [ ] Pin title: keyword front-loaded, ≤100 chars. Pin description: 200–300 chars with 2–3 related keywords.
- [ ] Open Graph tags verified (Facebook Sharing Debugger).
- [ ] Twitter Card tags verified.
- [ ] All derivative assets produced from approved Canva template families (not one-off designs).
- [ ] Mobile preview checked on actual device.

## Per-Article E-E-A-T Checklist

- [ ] Experience: at least one first-hand example, test, or real scenario included.
- [ ] Expertise: math shown, mechanism explained, edge cases addressed.
- [ ] Authoritativeness: author bio present with relevant credentials/experience.
- [ ] Trustworthiness: update date visible, sources cited, disclaimers present.
- [ ] All claims supported by Tier 1 or Tier 2 sources.
- [ ] No Tier 3 source used as sole evidence for any factual claim.
- [ ] Prohibited sources not cited or linked.
- [ ] Affiliate relationships disclosed per FTC guidelines.

## Site-Wide E-E-A-T Checklist (quarterly)

- [ ] About page includes author background, mission, editorial standards.
- [ ] Author bio consistent across all posts.
- [ ] Contact information accessible.
- [ ] Privacy policy and terms of service up to date.
- [ ] Affiliate disclosure page exists and is linked from all monetized posts.
- [ ] Published posts have visible "Last Updated" dates.
- [ ] Internal linking structure intact (no broken links, orphans, dead ends).
- [ ] Schema markup (Article, Author, Organization) implemented correctly.
- [ ] GSC verified and monitored weekly.
---

# SECTIONS 5.1–5.10 — THE AF CORE DIFFERENTIATION PROTOCOL

> **⚑ Apply this framing to every production decision across Sections 5.1–5.10.**
>
> AF optimizes for comprehension over affiliate clicks. Mega-sites (NerdWallet, Bankrate, Investopedia) structure content for affiliate conversion — highlighted winner columns, product comparison tables as hero content, urgency timers, dark patterns. AF **never uses highlighted winner columns or dark patterns.** Every first visual is a teaching visual (decision tree, worked example, framework summary), never a product card. Every chart includes a "do nothing" baseline row so the reader sees the cost of inaction. Every visual is built for the reader's scenario, not an idealized one. Depth comes from original calculations, Money Dominoes chains, and real-number scenarios — not filler that serves affiliate purposes. Every paragraph must teach, prove, or move the reader toward a decision. Content refresh means a genuine content upgrade, not a date-stamp change. ELI12 voice and consistent AF frameworks (Money Dominoes, ELI12) are structural advantages mega-sites cannot replicate at scale without abandoning their business model.

---

## 5.1 — Visual Placement System

*Source: NN/g eye-tracking studies (Tier 1), Google SEO Starter Guide (Tier 1).*

### Attention Distribution Model (NN/g, ~130,000 fixations / 120 participants)

| Page Zone | Viewing Time | What Lives Here |
|---|---|---|
| Top 20% | >42% of total | Direct answer, trust cues, first meaningful visual, TOC, primary nav |
| 20–40% | Cumulative >65% in top 40% | Core framework, first proof points, first comparison/table, optional first CTA |
| 40–60% | Falling sharply | Supporting detail, examples, secondary visuals |
| 60–100% | Long tail | Edge cases, FAQs, references, bonus tools, final CTA |

**F-Pattern:** Two horizontal scans at the top, then vertical scan down the left margin. Front-load meaning in headings + first sentences. Visuals must not push the answer below the second horizontal scan. Left-aligned content gets more attention than centered/right-aligned.

### The 7 Visual Placement Rules (Production Standard)

1. **First Meaningful Visual in Top 20%.** Functional (summary table, decision tree, comparison snapshot, key formula) — never decorative stock. On mobile, large hero images can be misread as "faux ads."
2. **One visual per 400–700 words.** QA heuristic. The top 2 screenfuls must contain ≥1 meaningful visual + strong typographic structure. After that, ≥1 meaningful visual per 1–2 major sections.
3. **Callout Box Budget.** Top 20%: max 1 callout per screenful, mission-critical only. Never stack callouts back-to-back. Overuse triggers banner blindness.
4. **Setup-Chart-Interpretation triad.** 1–2 sentence setup defining the question → Chart with direct labels → 2–6 sentence interpretation translating into a money decision. Place images near relevant text. Direct labels over legends.
5. **CTA vs Informational Separation.** Informational callouts adjacent to the concept they clarify. CTA callouts at natural section boundaries — never mid-paragraph.
6. **Monetization Distance from Trust Visuals.** Never place affiliate widgets / promo banners / newsletter CTAs adjacent to charts or tables that must be trusted (NN/g: ads "poison adjacent items").
7. **One Dominant Element Per Mobile Viewport.** Multiple competing colored blocks create scanning confusion and trigger ad-avoidance behavior.

**AF differentiation:** First visual is always a teaching visual (decision tree, framework summary, worked example) — never a product comparison card with affiliate links.

---

## 5.2 — Visual Type Selection Framework

*Source: Tufte (Tier 1), Stephen Few (Tier 1), NN/g chart guidance (Tier 1).*

### Step 1 — What is the reader's question?

| Reader Question | Best Visual |
|---|---|
| "Am I making progress?" | Line chart of remaining balance over time |
| "Where does my money go?" | Horizontal bars sorted descending (NOT pie chart if >5 categories) |
| "Which option costs less?" | Grouped bar chart of total cost components |
| "How does compounding work?" | Stacked area (contributions vs growth) |
| "What should I do first?" | Numbered step list or flowchart |
| "What happens if I do X?" | Money Dominoes chain visual |

### Step 2 — Chart, Table, or Text?

- **Chart** when showing trends, comparisons, or proportions where visual patterns matter.
- **Table** when readers need exact numbers to reference, compare row-by-row, or verify.
- **Text** when the concept is linear, single-path, and doesn't benefit from spatial arrangement.

### Step 3 — Specific Chart Type by Data Type

| Data Type | Best Chart | Support Visual | Avoid |
|---|---|---|---|
| Debt payoff progress | Line chart (remaining balance vs time) | Milestone bars at 25/50/75/100% | Thermometer alone (hides time) |
| Compound interest growth | Stacked area or two lines (contributions vs total) | Log-scale panel for large spans | Area-only without labels |
| Budget allocation % | Horizontal bars sorted descending OR 100% stacked bar | Small multiple bars for month comparison | Pie/donut when >5 categories |
| Loan comparison by total cost | Grouped bars (total paid, interest, fees) | Waterfall per loan | APR-only comparisons (misleading if fees differ) |
| Emergency fund milestones | Step/milestone bar with target bands (1/3/6 months) | Monthly contribution bar chart | Single target without monthly-expense context |
| Side-hustle income growth | Line chart of monthly net | 3-month rolling average + volatility band | Cumulative-only (hides recent stagnation) |
| Money Dominoes chain | Flow diagram: 4-node horizontal chain with arrows | Annotated step list as fallback | Complex multi-branch diagrams |

**Pie chart failure modes:** >5 categories; two slices within 5% of each other; ranking/comparison purpose; mobile display. Pie charts work only for binary/ternary splits where the point is dramatic contrast.

### The 4 Visual Functions (every visual serves exactly one)

1. **Teaching Visual** — explains a concept, shows a process, demonstrates a calculation. Placement: within the body section where taught.
2. **Pacing Visual** — cognitive breather between dense sections (pull quote, single-big-number highlight, simple icon list). Placement: between H2s, especially after sections >500 words.
3. **Trust Visual** — builds credibility (sourced data chart, screenshot of real results, methodology note). Placement: near claims requiring proof, especially YMYL.
4. **Conversion Visual** — moves reader to next step (CTA callout, lead magnet preview, signup form). Placement: per 3-CTA Rule — never in trust-building zone (first 40%).

### Anti-Affiliate-Farm Patterns (banned)

- Product comparison tables with one column visually highlighted as "winner"
- Star ratings without explained criteria
- "Editor's Choice" badges without editorial methodology
- Stock photos of happy people holding credit cards
- Identical callout box styling for editorial content and affiliate promotions

### Visual Communication for Anxious Readers

- Representational visuals (situations, scenarios) over abstract charts
- Fewer data points, larger labels, more whitespace
- Frame positively: "progress toward" rather than "distance from"
- Warm colors (amber, muted teal) over cold/clinical (gray, steel blue)
- "You are here" markers on progress visuals
- Single-big-number pattern: one key takeaway in 32px+ font with short caption

---

## 5.3 — Kadence Formatting Recipes (Block-by-Block)

*Source: Kadence official docs (Tier 1).*

### Global Configuration

**Responsive breakpoints:** Desktop >1024px | Tablet 768–1024px | Mobile <768px.

**Theme settings (Customizer > General > Layout):** Content max-width 1200px (narrow 740px = ~65–75 chars/line at 18–20px). Edge spacing: D 32px / T 24px / M 16px.

**Typography (Customizer > Colors & Fonts > Typography):** Body D 20px / T 19px / M 18px; line-height 1.7; paragraph bottom margin 1em; H2 line-height 1.3; H3 1.35. Use CSS `clamp()` (min 18px, max 20px, screen 480–1200px). Body color `#1E293B`; secondary text `#6B7280`; heading color `#222222`.

**Global visual style:** Border radius 12px desktop / 10px mobile. Info/callout left accent: 4px solid (palette color). Subtle shadows only — avoid affiliate-landing-page aesthetic.

### Block-by-Block Settings

**Row Layout (section wrappers):** Padding D 48px / T 36px / M 24px top-bottom. Column gap D 24px / T 20px / M 16px. 2-column rows: D 35/65 → T 40/60 → M stack. Set collapse order deliberately — answer content first on mobile.

**Info Box — Answer Block preset (snippet target):** Background `#F4F7FF`; border `1px #D6E4FF`; left accent `4px solid #3686FF` (CSS class `.kb-answerbox`); radius D 12px / M 10px; padding D 20px / T 18px / M 16px; title 18px D / 17px M, weight 600. Content: first paragraph 40–60 words (direct answer for snippet extraction).

**Kadence Callout Color Coding System:**

| Callout Type | Background | Border Left | Use Case |
|---|---|---|---|
| Money Dominoes Chain | `#FFF8F0` (warm cream) | 4px solid `#D97706` (amber) | Each domino in chain reaction |
| Lead Magnet CTA | `#F0FDF4` (mint) | 4px solid `#16A34A` (green) | Email signup, template download |
| Stakes Moment (Type A) | `#FFF8F0` (warm amber) | 4px solid `#FDA050` (amber) | "Here's what's at risk" warnings |
| How-To Moment (Type B) | `#F0FDFA` (light teal) | 4px solid `#14B8A6` (teal) | Step-by-step action instructions |
| Completion Moment (Type C) | `#F0FDF4` (mint) | 4px solid `#16A34A` (green) | "You've done it" celebration |
| YMYL Warning | `#FFFBEB` (light yellow) | 4px solid `#D97706` (amber) | Disclaimers, "consult a professional" |
| Pro Tip | `#F5F3FF` (lavender) | 4px solid `#7C3AED` (purple) | Advanced optimization tips |
| Featured Stat | `#F8FAFC` (near white) | 4px solid `#1E293B` (charcoal) | Single-big-number highlight |
| Answer Block | `#F4F7FF` (light blue) | 4px solid `#3686FF` (blue) | Featured snippet target definitions |
| Where-This-Gets-Complicated | `#FFF7ED` (peach) | 4px solid `#EA580C` (orange) | Edge cases, exceptions, nuances |

**Table of Contents block:** H2 + H3 only (avoid H4+). Collapsible on mobile. Padding 14–16px. Margin-bottom 24px. Smooth scroll on.

**Accordion (FAQ):** H3 for major Q, H4 for nested. Title 18px D / 17px M. Title padding D 14px 16px / M 12px 14px. Content padding D 16px / M 14px. Borders `1px #E6E8EF`, radius 10–12px. **FAQ Schema:** enable only for genuine Q&A — never for marketing toggles.

**Tabs block (comparisons):** Tabs on D/T → accordion on M. Max 3–4 tabs per block. Title padding D 12px 14px / M 10px 12px.

**Advanced Table — Mobile-Safe Patterns (no horizontal scroll on mobile):**
- Pattern 1 (Best): 2-column "Attribute | Value" — left 40% / right 60%, cell padding D 12px / M 10px, ≤8–12 words per cell.
- Pattern 2: Cardified — each option as Info Box inside Row Layout (D 3-column → M 1-column stack).
- Pattern 3 (3+ columns required): Max 3 columns, short labels + icons, controlled `overflow-x` scroll fallback.

**Advanced Buttons (CTAs):** 16px font (M+D). Padding D 12px 18px / M 12px 16px. Radius 10–12px. Min tap height ~44px.

**ConvertKit opt-in:** Mid-article (after first actionable section). Container matches Info Box (`#F4F7FF` bg, `#D6E4FF` border, 12px radius). Headline 18px wt 700. Input height 44–48px. Button matches Advanced Button styling.

**Spacer/Divider:** Spacer height D 24px / T 20px / M 16px. Divider 1px solid, 40–60% width centered. Hide on mobile when noisy.

---

## 5.4 — Data Visualization Standards

*Source: Tufte (Tier 1), Stephen Few (Tier 1), NN/g (Tier 1).*

### Tufte's Principles Applied to AF

- **Data-Ink Ratio.** Every drop of ink = data. Remove gridlines (or fade to dotted), background fills, decorative borders, 3D, redundant legends. If a label can sit on the data point, delete the legend.
- **Graphical Integrity.** Visual representation proportional to numerical quantity. Common YMYL violations: truncated Y-axes that exaggerate small differences; dual Y-axes creating false correlations; area charts where area implies volume but data is linear; pies with 3D tilt. **Rule:** Y-axis at zero for bar charts. Non-zero baseline acceptable for line charts only when chart title states the range AND purpose is showing variation, not magnitude.
- **Small Multiples Over Complex Singles.** Six small charts with one line each (shared axes) > one chart with six overlapping lines.
- **Chartjunk Elimination.** No moiré, heavy gridlines, excessive ticks, decorative icons, gradient fills, drop shadows on data elements.

### Stephen Few — Chart Selection by Relationship

| Relationship | Best Chart | Finance Example |
|---|---|---|
| Comparison among items | Horizontal bar (sorted) | Monthly expenses by category |
| Comparison over time | Line chart | Net worth over 24 months |
| Part-to-whole | 100% stacked bar or treemap | Budget allocation (needs/wants/savings) |
| Distribution | Histogram or box plot | Income distribution across side hustles |
| Correlation | Scatter plot | Savings rate vs debt payoff speed |
| Ranking | Horizontal bar (sorted desc) | Which debts to pay first by interest rate |
| Deviation | Bar with reference line | Actual vs budget per category |
| Flow | Sankey or waterfall | Where each paycheck dollar goes |

### Table vs Chart Decision Rules

- **Table** when: readers need exact numbers (loan terms, rates, fees); <5 items with straightforward comparison; reader will reference later (bookmark/screenshot); multiple attributes per item side-by-side.
- **Chart** when: pattern matters more than exact values; 5+ items where visual ranking aids comprehension; time-series where trajectory matters; the "aha" comes from seeing the shape, not the number.
- **Both** when: YMYL trust requires exact numbers AND visual pattern aids understanding (chart shows the story, table below shows the proof).

### Color System for Finance Visuals (WCAG 2.1 AA compliant)

| Color | Hex | Use |
|---|---|---|
| Primary (action/positive) | `#3686FF` | Progress lines, positive bars, links |
| Secondary (growth/success) | `#16A34A` | Gains, savings growth, goal completion |
| Warning (attention needed) | `#D97706` | Approaching limits, moderate risk |
| Danger (loss/debt/risk) | `#DC2626` | Debt, losses, overspending |
| Neutral (baseline/reference) | `#64748B` | Gridlines, secondary data, labels |
| Background (chart area) | `#FFFFFF` | Always white |
| Axis/text | `#1E293B` | Axis labels, titles, annotations |

WCAG: 4.5:1 contrast for text, 3:1 for graphical elements. **Never use color alone to convey meaning** — pair with labels, patterns, or icons.

### Number Formatting Standards

| Data Type | Format | Example |
|---|---|---|
| <$1,000 | $X or $X.XX | $347 / $42.50 |
| $1,000–$999,999 | $X,XXX | $12,450 |
| >$1M | $X.XM | $1.2M |
| Percentages | X% or X.X% (1 decimal max) | 22% / 6.8% |
| Time periods | X months / X years | 18 months / 3 years |
| Dates on axes | MMM 'YY | Jan '24 / Jun '25 |
| Large round numbers | nearest meaningful unit | "about $50,000" — not "$49,847.23" |

**Exception:** When exact cents matter (loan payments, minimum payments, fee calculations), show full precision: $347.82/month.

### Annotation Standards (every chart)

1. **Title states the takeaway, not the topic.** *"You save $14,000 by choosing the 15-year mortgage"* — not *"15-year vs 30-year mortgage comparison."*
2. **Direct labels on data points or bars** (not a separate legend whenever possible).
3. **Source line below the chart:** *"Source: [Name], [Year]"* or *"Calculation: [assumption stated]."*
4. **"You are here" marker** when applicable — show the reader where their scenario falls.

**AF differentiation:** Charts always include a **"do nothing" baseline** so the reader sees the cost of inaction. Never highlight a "winner" product — highlight the decision criteria so the reader chooses for themselves.

---

## 5.5 — Competitor Audit System + Beat-the-Best Framework

*Source: Google QRG (Tier 1), Ahrefs/Semrush methodology (Tier 2), Orbit Media audit frameworks (Tier 2).*

### 5.5-A — Competitor URL Input Method (Three Modes)

**Manual Mode (plain LLM session):** Writer provides URLs. Before session, Google the primary keyword, copy top 5–10 organic (skip ads, Reddit, YouTube unless they dominate the SERP), paste into session input alongside Article Brief.

**Agent Mode (LLM with web access):** Agent retrieves URLs automatically. Must fetch and **fully read** each competitor page (full HTTP request, complete rendered text) — not snippet summaries, not cached previews. Extract per page: (1) all H2 headings verbatim, (2) actual word count from page body, (3) count of meaningful visuals (charts/tables/custom graphics — exclude stock photos), (4) Tier 1/2 citation count, (5) FAQ presence + question count. Snippet-level summaries do **not** satisfy this requirement. If a URL is blocked/paywalled, record as "Not accessible — skipped" and replace with the next organic result.

**Non-compliant output flag:** If an agent declares the audit complete but the CA-2 contains *estimated* word counts, missing H2 lists, or no visual/citation counts, the CA-2 is **non-compliant**. Do not approve. Return with: *"This CA-2 was built from snippet summaries, not full page reads. Re-run using full HTTP fetches and populate all required fields."*

**N8N Automation Mode:** N8N triggers the research as a workflow node. Input: primary keyword from Article Brief row in AF Content OS sheet. Output: completed CA-2 saved to session folder. Writing LLM receives pre-filled CA-2 — does not re-run research.

**Rules across all modes:** Competitor URLs are structural references only — never sources for financial facts. Min 5 / max 10 URLs. Skip aggregators (Reddit, Quora, Pinterest) unless they dominate the SERP. LLM must confirm + approve the CA-2 synthesis before advancing to Step 4.

### CA-2 Acceptance Criteria (9 fields — all required)

1. Target keyword confirmed.
2. Min 5 URLs with **actual** word counts (fetched, not estimated).
3. H2 headings verbatim per URL (not paraphrased, not inferred).
4. Visual asset count per URL (charts/tables/custom graphics).
5. Tier 1/2 citation count per URL.
6. ≥1 H2 gap identified (subtopic in 0–2 of top 5).
7. SERP features noted (snippet type, PAA listed, AI Overview present/absent).
8. Target word count calculated (competitor avg × multiplier).
9. Originality opportunity stated.

CA-2 missing any field is incomplete. Return for completion before Step 4. Do not proceed on a partial CA-2 regardless of time pressure.

### When to Run a Full Audit (vs 5-min SERP scan)

Full audit before any new post when keyword has: MSV >500, KD >30, SERP dominated by DR 70+ authority sites, OR any YMYL classification. Low-competition (<500 MSV / KD <20) → 5-min SERP scan replaces full audit.

### Article-Level Audit Template (per top-5 article)

**Content metrics to record:** word count, H2 count, H3 count, unique H2 topics list, visual count (exclude stock photos), visual types (table/chart/screenshot/infographic/custom illustration), FAQ presence + count, schema types used (Chrome Schema Markup Validator), internal-link count, external-link count + authority, CTA count + type (email signup, affiliate, social, related), author bio + credentials, published date + last-updated, reading level (Hemingway / readable.com).

**E-E-A-T signals checklist (per page):**
- [ ] Author byline with name (photo helps)
- [ ] Author bio with relevant credentials/experience
- [ ] "Reviewed by" / "Fact-checked by" credit
- [ ] Methodology or editorial standards disclosure
- [ ] Sources cited within content (not just bibliography)
- [ ] YMYL disclaimers present and specific
- [ ] About page linked from article
- [ ] Contact information accessible

### SERP-Level Audit Template

| SERP Feature | Present? | Implication |
|---|---|---|
| Featured snippet | Y/N + type (paragraph / list / table) | Structure your answer to match |
| People Also Ask | Y + top 8 questions | Include as H2s or FAQ items |
| AI Overview | Y/N + sources cited | Apply GEO rules (§5.10) |
| Knowledge panel | Y/N | Indicates entity-level competition |
| Video carousel | Y/N | Consider video / YouTube embed |
| Image pack | Y/N | Optimize alt text + file names |
| Sitelinks | Which competitors have them | Indicates Google's trust in site structure |
| Perspectives / forum results | Y/N | Indicates Google values real experience |

### Zero-Gap Fallback

If audit finds **no** content gaps in Steps 2–3, do not fabricate a gap or stall. Apply the §0-F Originality Requirement instead: post must include ≥1 of — a Money Dominoes chain absent from any top-10 result; a worked example using reader-specific dollar amounts that competitors handle generically; an ELI12 translation of a concept all competitors explain at Grade 11+. Document the chosen originality element in the Article Brief before writing.

### The Beat-the-Best Framework (5 steps)

1. **Match the table stakes.** Every subtopic covered by ≥3 of top 5 is mandatory. Missing one = Google may consider your content incomplete.
2. **Fill the gaps.** Subtopics in 0–2 of top 5 = your differentiation opportunities. Prioritize gaps aligned with AF expertise.
3. **Add the uncovered layer.** ≥1 substantial section (300+ words) no competitor covers. Sources: real reader questions (comments/emails/DMs), Reddit/forum threads, AF frameworks (Money Dominoes, ELI12), original calculations.
4. **Exceed on visual density.** Your visual count = competitor avg + 2 minimum. Highest-differentiation types: original charts with direct labels, decision flowcharts, worked-example tables, Money Dominoes chain visuals.
5. **Exceed on E-E-A-T signals.** Match the highest competitor's signal count + add ≥1 they lack (most commonly: personal experience narrative, original calculation methodology, or "I tested this" documentation).

### Keyword Gap Analysis Process

1. Export your site's ranking keywords (Ahrefs > Site Explorer > Organic Keywords).
2. Export each competitor's ranking keywords.
3. Use Content Gap tool: keywords competitors rank for that you don't.
4. Filter: Volume >200, KD <50, YMYL-relevant.
5. Cluster by topic theme.
6. Prioritize: high volume + low KD + strong AF framework alignment.

### Content Gap Matrix (post keyword analysis)

| Topic Cluster | Your Best Post (URL) | Your Rank | Best Competitor Post | Their Rank | Gap Type | Priority |
|---|---|---|---|---|---|---|

**Gap types:** *Missing* (no content — new post needed); *Thin* (significantly shorter/shallower than competitors — deep refresh); *Outdated* (key data/recommendations stale — refresh per §5.9).

---

## 5.6 — Word Count and Depth Calibration

*Source: Google QRG (Tier 1), Backlinko content-length studies (Tier 2), HubSpot/Semrush research (Tier 2).*

### Baseline Rule

YMYL personal finance: **minimum 2,000 words.** This is not a ranking factor (Google has explicitly stated word count is not a ranking signal) — but every study of top-ranking YMYL content finds thoroughness correlates with rankings, and thoroughness in finance requires space to explain, prove, and contextualize.

### The Calibration Formula

**Do not pick a word count in advance. Calculate it.**

`Target Word Count = (Avg of Top 5 Competitor Word Counts) × 1.15 to 1.25`

| Gap Density | Multiplier | Explanation |
|---|---|---|
| Low (competitors are thorough) | 1.15× | Slightly more depth + your unique frameworks |
| Medium (2–3 subtopic gaps found) | 1.20× | Additional sections to cover gaps |
| High (major subtopics missing across competitors) | 1.25× | Significant new content opportunity |

**Example:** Top 5 average 3,200 words. Medium gap density. Target = 3,200 × 1.20 = 3,840 words → planning target 3,800–4,000.

### Word Count Compliance Rule

The completed draft must fall within **±15%** of the declared target. A draft exceeding the target by >15% **fails the word count gate** and must be trimmed before advancing to Stage 5. Exceeding the target is **not** a quality signal — it's a compliance failure. "More depth = better" is not a valid override.

**Violation pattern:** Writing 1,800–2,500+ words when SERP-calibrated target is 1,200–1,400 inflates draft by 60–120%. Slower to read, harder to rank against lean competitors, inconsistent with ELI12 brevity. If competitor avg is <1,500, match that discipline. Every paragraph must earn its place against the target — not against an abstract notion of comprehensiveness.

**Ceiling rule:** Beyond 5,000 words, consider splitting into a hub-and-spoke cluster (pillar + supporting posts). Exceptions: ultimate guides + pillar content intentionally designed as comprehensive references.

### Depth Indicators Beyond Word Count (Google QRG signals)

| Depth Signal | What Raters Look For | AF Standard |
|---|---|---|
| Main Content sufficiency | "Satisfying amount of high-quality MC for the page's purpose" | Every H2 answers the subtopic completely — no "we'll cover this in another post" cop-outs within a section |
| Effort + originality | Evidence content required effort/skill/talent | Original calculations, custom visuals, personal experience, framework application (Money Dominoes) |
| E-E-A-T demonstration | First-hand experience or established expertise visible | "When I paid off my student loans…" / "After analyzing 50 reader debt plans…" |
| Supplementary content | Helpful features beyond main text | Calculators, downloadable templates, interactive tools, related-post suggestions |

### LLM / AI-Overview Impact on Depth Strategy (Dual-Layer)

- **Layer 1 (Top 20%):** Optimized for AI Overview extraction — direct answer, clean structure, factual density. Also your featured-snippet zone.
- **Layer 2 (Remaining 80%):** Optimized for click-through value — content that makes someone click "Read more" because the AI Overview was insufficient. Money Dominoes chains, ELI12 translations, real-number scenarios, emotional context.

### Section-Level Depth Standards

| Section Type | Minimum Words | Must Include |
|---|---|---|
| Introduction | 150–250 | Hook, stakes, promise, roadmap |
| Core Definition / Explanation (H2) | 300–500 | ELI12 translation, one visual or example |
| How-To Section (H2) | 400–700 | Numbered steps, ≥1 worked example with real dollars |
| Comparison Section (H2) | 400–600 | Table or chart, "which is right for you" decision guidance |
| Money Dominoes Section (H2) | 300–500 | 3–5 node chain with dollar amounts at each node |
| FAQ Section | 75–150 per Q&A | Direct answer first sentence, then context |
| Conclusion | 150–300 | Single next step (NOT a summary of the article) |

**Substance test:** if you deleted a paragraph, would the reader lose something they need? If no, delete it.

---

## 5.7 — Trust Architecture and Reader Psychology

*Source: Google QRG E-E-A-T (Tier 1), NN/g trust + credibility studies (Tier 1), BJ Fogg Stanford Web Credibility Project (Tier 1), behavioral finance research (Tier 2).*

### The Trust Timeline — 4 Checkpoints Per Article

#### Checkpoint 1 — First 10 Seconds (Snap Judgment)

**Trust signals visible without scrolling:** professional design (not cluttered, not ad-heavy); author byline with name (photo helps but not mandatory); clear specific title matching search intent; date of publication or last update; no interstitial popups, autoplay video, or aggressive ads above the fold.

**Trust destroyers:** generic stock photo hero ("content farm" signal); overpromising title ("Get Rich Quick"); no visible author attribution; aggressive popup before any content consumed; ads above the fold pushing content down.

#### Checkpoint 2 — First Scroll (Competence Test, ~300–500 words)

**Trust signals:** specific direct answer to the title's implied question; real numbers, not vague generalities (`$347/month` not "a reasonable monthly payment"); framework or organized structure (numbered list, decision tree, clear categories); correct terminology used naturally (not keyword-stuffed).

**Trust destroyers:** vague opener that restates the title as a question; no specific numbers/data in first 500 words; obvious keyword stuffing; factual errors (wrong APR range, outdated contribution limits, incorrect tax brackets).

#### Checkpoint 3 — Mid-Article (Monitoring Phase)

**Trust signals:** claims backed by sources (linked or cited); consistent voice/tone (no shift from educational to salesy); acknowledgment of complexity ("This gets complicated when…" signals honesty); tables/charts with labeled sources; no sudden pivot to aggressive product promotion.

**Trust destroyers:** abrupt transition from educational content to affiliate pitch; claims without supporting evidence/source; contradicting earlier statements without acknowledging the nuance; excessive superlatives ("the absolute best," "guaranteed to work," "the only way"); identical callout styling for editorial tips and sponsored content.

#### Checkpoint 4 — CTA Gate (Motivation Test)

**Trust signals:** CTA is a logical next step from the content just consumed; ask is **proportional** to value delivered (email for a template, not email for a generic "newsletter"); alternative paths offered (not just one funnel); no urgency manipulation ("limited time," countdown timers, "only X spots left").

**Trust destroyers:** CTA appears before sufficient value delivered; CTA asks for more than the content justified; fake urgency / scarcity language; no option to continue reading without engaging the CTA.

### Words and Phrases That Destroy Trust in Finance Content

- **Overpromising language (banned):** "guaranteed," "risk-free," "get rich," "secret," "hack" (when describing fundamental strategies), "passive income" (without heavy setup-effort caveats), "financial freedom" (without concrete definition), "easy money."
- **False authority (banned):** "experts agree" (which experts?), "studies show" (which studies?), "everyone knows," "it's common knowledge," "the truth is" (implies others are lying). **Replace with:** *"[Specific source] found that…"* / *"According to [Org]…"* / *"In my experience…"*
- **Hedge words signaling uncertainty (minimize):** "might," "could," "possibly," "it depends" (without naming what it depends on), "some people say," "there are many options" (without narrowing). **Replace with:** specific conditional statements (*"If your debt is above 7% APR, prioritize payoff. Below 4% APR, consider investing instead. Between 4–7%, either works — here's how to decide."*)
- **Salesy language (banned in editorial):** "act now," "don't miss out," "limited time," "exclusive offer," "click here to learn more" (as a CTA inside educational content), "you won't believe."

### Dollar Amount Psychology

| Technique | Example | When to Use |
|---|---|---|
| Monthly framing | "$347/month" instead of "$4,164/year" | Making commitments feel manageable |
| Daily framing | "$11.56/day" instead of "$347/month" | Making savings feel achievable ("two coffees") |
| Total cost framing | "$124,560 total paid on a $80,000 loan" | Making cost of inaction visceral |
| Savings delta | "You save $14,238 over the life of the loan" | Motivating action by showing reward |
| Hourly wage framing | "That subscription costs you 3 hours of work per month" | Connecting abstract costs to lived experience |
| Comparison anchoring | "$50/month — less than your streaming subscriptions combined" | Making unfamiliar amounts relatable |

**Show the math rule:** Always show the math. Never state a dollar amount without showing how you got there. "You save $14,238" requires a footnote or inline calculation showing assumptions (rate, term, payment amount). Unverifiable claims destroy YMYL trust.

### YMYL Disclaimer — Trustworthy vs Performative

**Post-level disclaimer (every post — required):** Position immediately after intro, before first H2. Styled as YMYL Warning callout (light yellow bg + amber left border, per §5.3 callout color table). Must include: (1) educational content, not personalized advice; (2) author's relevant experience or credentials (informal counts: "I paid off $47,000 in student loans over 3 years"); (3) recommendation to consult a qualified professional; (4) date last reviewed for accuracy.

- **Trustworthy:** specific about what the content IS and IS NOT — *"This post explains how debt avalanche vs snowball methods work and helps you choose between them. It is not a recommendation for your specific situation."*
- **Performative:** generic boilerplate that reads like legal protection — *"This is not financial advice. Consult a financial advisor."*

**Section-level caveats:** When a post makes a specific numerical claim (tax brackets, contribution limits, interest rate ranges), add an inline caveat with effective date — *"2024 federal tax brackets (these update annually — verify at IRS.gov for your filing year)."*

### The Anxiety-Aware Writing Framework (5 techniques)

1. **Normalize the situation before teaching the solution.** *"If you're living paycheck to paycheck, building an emergency fund feels impossible. That's not a character flaw — it's math. Let's fix the math."*
2. **Use "you" positioning that empowers, not shames.** *"Starting late? You're not alone — and starting now still matters more than you think. Here's the math."*
3. **Acknowledge the emotional weight of financial decisions.** *"This choice isn't just math — it's psychology. Avalanche saves more money. Snowball builds momentum. Both work. Here's how to pick the one you'll actually stick with."*
4. **Provide escape valves for overwhelm.** When complexity rises: *"Feeling overwhelmed? Here's the one-sentence version: [simplified rule]. If that's all you need right now, skip to [next section]."*
5. **Celebrate micro-progress.** At section boundaries in how-to posts: *"If you've done this step, you're already ahead of 70% of Americans who have no budget at all. Seriously."*

---

## 5.8 — Pinterest & Featured Image Specifications

*Source: Pinterest Business docs (Tier 1), Pinterest Engineering blog (Tier 1), Open Graph spec (Tier 1), Google image SEO docs (Tier 1), Kadence theme docs (Tier 1). Section 4.12 covers the distribution/SEO layer; this section covers the technical asset-production specs.*

### Pinterest Pin — Standard Format (Primary)
- **Dimensions:** 1000×1500 px (2:3 aspect ratio).
- **File format:** PNG (text-heavy pins) or JPG (photo pins).
- **Max size:** 20 MB hard cap; target <5 MB for fast load.
- **Color mode:** sRGB.
- **Why 2:3:** Pinterest's masonry feed gives taller pins more real estate. 2:3 is Pinterest's officially recommended ratio — displays uncropped on mobile and desktop. Taller (1:2, 1:2.1) risks feed truncation.

### Pin Design Anatomy

| Zone | Position | Content | Specs |
|---|---|---|---|
| Hook Zone | Top 20% (0–300px) | Bold headline or number | 60–80pt font, high contrast, max 8 words |
| Context Zone | Middle 50% (300–1050px) | Supporting visual or subheadline | Supporting text 36–48pt, simple icon/illustration |
| Brand Zone | Bottom 30% (1050–1500px) | URL, logo mark, or CTA text | Logo mark (not full logo), URL 24–30pt, brand color strip |

### Text Overlay Rules
- Max 3 lines of text on any pin.
- Primary headline 60–80pt bold, sans-serif (Inter / Montserrat / Poppins).
- Supporting text 36–48pt regular weight.
- Must be readable at thumbnail (~236px wide).
- High contrast required (white-on-dark or dark-on-light).
- Text overlay ≤30–40% of pin area (algorithm may deprioritize text-heavy pins).

### Pin Color Strategy
- Brand colors consistent across all pins (feed recognition).
- Warm tones (coral, amber, warm neutrals) outperform cool tones for lifestyle/finance content on Pinterest.
- **Avoid pure white backgrounds** — they vanish into Pinterest's white feed. Use off-white (#F8F7F4) or subtle color wash.
- Test 3–4 color template variations per quarter; track CTR per template.

### Pinterest SEO for Pins
- **Pin Title:** ≤100 chars. Front-load the keyword. Format: `[Keyword Phrase]: [Specific Promise]`. Ex: *"50/30/20 Budget: Exact Dollar Amounts for a $4,000 Paycheck."*
- **Pin Description:** ≤500 chars (use 200–300). Primary keyword in first sentence; 2–3 related keywords integrated naturally; clear value proposition. **No hashtags** (Pinterest deprecated hashtag search).
- **Pin Alt Text:** Describe visual content for accessibility; secondary SEO signal.

### Board Strategy
- 10–15 niche boards aligned with content pillars (Budgeting Tips, Debt Payoff Strategies, Emergency Fund Building, etc.).
- Board titles 3–5 words, keyword-rich ("Debt Payoff Strategies That Work").
- Board descriptions 200–300 chars with 3–5 related keywords.
- Pin every new post to the most relevant board first, then 2–3 secondary boards over the following week.
- Repin cadence: space repins 7–14 days apart to avoid spam signals.

### Blog Featured Image Specifications

**WordPress / Kadence Featured Image:**
- **Dimensions:** 1200×630 px (1.91:1).
- Triple duty: blog header + Open Graph (Facebook/LinkedIn) + Google Discover.
- **File format:** JPG (photos) or PNG (graphics with text).
- **Compression:** target <150 KB without visible quality loss (ShortPixel or Imagify).
- **Alt text:** descriptive, keyword-inclusive, <125 chars.

**Open Graph (`og:image`) Requirements:**
- Min 600×315 px (Facebook may crop). Recommended 1200×630.
- Max file size 8 MB.
- Must be publicly accessible URL (no auth).
- Set via Yoast/Rank Math or Kadence's built-in OG settings.

**Twitter / X Card:**
- Recommended 1200×628 px (≈OG).
- Use `summary_large_image` card type for max visibility.
- Format: JPG, PNG, WebP, or GIF (static only).

### Image Production Workflow — Per-Post Bundle

| Asset | Dimensions | Purpose | Template |
|---|---|---|---|
| Featured Image | 1200×630 | Blog header + OG + Google Discover | Canva "AF Featured" |
| Pinterest Pin (primary) | 1000×1500 | Pinterest distribution | Canva "AF Pin Standard" |
| Pinterest Pin (variant) | 1000×1500 | A/B test alternate design | Canva "AF Pin Variant" |
| In-Post Visuals | 740 px wide max | Charts, tables, infographics | Per-post |

**Naming Convention:**
- Featured: `featured-[slug].jpg`
- Pinterest: `pin-[slug]-v1.png`, `pin-[slug]-v2.png`
- In-post: `[slug]-[description].png`

**Alt Text Formula:** `[What the image shows] + [keyword context]`. Ex: *"Pie chart showing 50/30/20 budget allocation — 50% needs, 30% wants, 20% savings — for a $4,000 monthly paycheck."*

### Mobile Image Optimization
- All in-post images legible at 375px viewport (iPhone SE).
- Charts with small text: provide simplified mobile version OR ensure font ≥14px at mobile scale.
- Pinterest pins are mobile-first — always preview at thumbnail size (236px wide) before publishing.
- Lazy loading enabled for all images below fold (Kadence default).
- Serve WebP with JPG/PNG fallback (ShortPixel or server-level conversion).

### AF Differentiation Layer
Mega-sites use generic stock photography and template featured images that blend into social feeds. AF's consistent palette + typography + pin templates create pattern recognition — a reader scrolling Pinterest should recognize an AF pin before reading the brand name. Brand recognition compounds; cannot be bought, only built through consistent execution.

---

## 5.9 — Content Refresh Decision Framework

*Source: GSC documentation (Tier 1), Google "freshness" ranking systems (Tier 1), Ahrefs content audit methodology (Tier 2), Animalz / Orbit Media decay analysis (Tier 2).*

### When to Audit for Refresh — Triggers
- Quarterly scheduled review (every 90 days; review all posts published >6 months ago).
- GSC: position dropped >5 spots for primary keyword.
- GSC: clicks declined >20% month-over-month for a previously stable post.
- Annual data change: tax brackets, contribution limits, interest rate environment, fee structures.
- Algorithm update: major Google core update (check Search Status Dashboard).
- Reader signal: comments/emails reporting outdated information.

### GSC Metric Interpretation — The Four Signals Together

| Pattern | Clicks | Impressions | CTR | Avg Position | Diagnosis | Action |
|---|---|---|---|---|---|---|
| Healthy | Stable/up | Stable/up | Stable | Stable | No action | Monitor |
| Declining relevance | Down | Down | Stable | Stable | Google showing page to fewer queries | **Deep refresh** — expand topical coverage |
| Losing rank | Down | Stable | Down | Rising (worse) | Competitors overtaking | **Deep refresh** — beat-the-best audit + update |
| CTR erosion | Down | Stable | Down | Stable | Title/meta not compelling vs new competitors | **Light refresh** — rewrite title + meta |
| Impressions up, clicks flat | Stable | Up | Down | Stable/improving | Ranking for new queries; snippet not matching intent | **Light refresh** — add sections matching new query intent |
| Seasonal dip | Down | Down | Stable | Stable | Normal for seasonal topics | No action — compare YoY, not MoM |
| Sudden cliff | Down sharply | Down sharply | Any | Rising sharply | Possible penalty / technical / algo hit | Investigate manual actions, indexing, core update timing |

### Light Refresh Checklist (1–2 hours)
*Use when CTR is dropping but position stable, or minor data points are outdated.*

- [ ] Update title tag — re-run against the Title Mastery Scorecard (§4.4).
- [ ] Update meta description — current year, specific numbers, clear value prop.
- [ ] Update publication date to refresh date (`Originally published [date], updated [date]`).
- [ ] Update all dollar amounts, percentages, thresholds (tax brackets, contribution limits, APR ranges).
- [ ] Update or remove broken external links.
- [ ] Update internal links — add links to AF posts published since the original.
- [ ] Refresh featured image if dated relative to current templates.
- [ ] Add 1–2 new FAQ items based on current PAA results for the target keyword.
- [ ] Verify all disclaimers reference the current year.
- [ ] Re-submit URL to GSC for re-indexing.

### Deep Refresh Checklist (4–8 hours)
*Use when position dropped >5 spots, or competitor audit reveals significant new content gaps.*

**Phase 1 — Competitive Re-Audit**
- [ ] Run fresh competitor audit (§5.5) for the primary keyword.
- [ ] Identify new subtopics covered by competitors that your post lacks.
- [ ] Identify new SERP features (AI Overview, video carousel, PAA changes).
- [ ] Record new word count target based on updated competitor analysis (§5.6 multipliers).

**Phase 2 — Content Restructuring**
- [ ] Add new H2 sections for missing subtopics from re-audit.
- [ ] Expand thin sections — any H2 <200 words that competitors cover in 400+.
- [ ] Add or update visuals: decision trees, comparison tables, charts (target competitor visual count + 2).
- [ ] Add Money Dominoes chain if the post lacks one and the topic involves cascading consequences.
- [ ] Update all worked examples with current real-world numbers.
- [ ] Re-apply ELI12 pass — flag any jargon introduced since original lacking translation.
- [ ] Add "What changed in [Year]" section if the topic has material YoY changes.

**Phase 3 — Technical & SEO Update**
- [ ] Update schema markup (FAQ schema for new questions, HowTo if applicable).
- [ ] Update internal linking — both inbound (link from newer posts to this one) and outbound (link from this post to newer posts).
- [ ] Optimize for new featured snippet format if snippet type has changed.
- [ ] Apply GEO optimization (§5.10) if the query now triggers AI Overview.
- [ ] Update all image alt text and file names.
- [ ] Compress any new images (<150 KB per image).
- [ ] Re-submit URL to GSC.

**Phase 4 — Quality Assurance**
- [ ] Voice consistency check (§4.1, §4.13).
- [ ] E-E-A-T compliance check (§4.8, §4.13).
- [ ] Mobile rendering check (especially new tables and visuals).
- [ ] Reading level check (Grade 7–8).
- [ ] Broken link check (internal and external).

### Refresh vs New Content — Decision Tree

**Refresh the existing post when:**
- The URL has existing backlinks (Ahrefs/Semrush).
- The URL has historical ranking data (it once ranked well).
- The core topic and search intent haven't changed.
- The post needs updated data, expanded sections, or better visuals.
- Competing for the same keyword with a new post would cause cannibalization.

**Write a new post when:**
- The original targets a keyword whose intent has shifted (e.g., "best savings account" now expects rate comparison tables, but the old post is an explainer).
- The topic has splintered into multiple distinct search intents.
- The original is so thin (<800 words) that restructuring would essentially be a rewrite.
- You want to target a different keyword cluster.

**When you write a new post to replace an old one:**
1. Publish the new post.
2. Set up a 301 redirect from the old URL to the new URL.
3. Update all internal links pointing to the old URL.
4. Monitor GSC for 30 days to confirm the new URL inherits ranking signals.

### Content Decay Half-Life by Topic Type

| Topic Type | Decay Period | Refresh Trigger |
|---|---|---|
| Tax-related (brackets, deductions, credits) | 12 mo (annual) | Every January after IRS releases new numbers |
| Interest-rate-dependent (mortgages, savings, CDs) | 3–6 mo | After any Federal Reserve rate decision |
| Contribution limits (401k, IRA, HSA) | 12 mo | Every November when IRS announces next-year limits |
| Budgeting frameworks | 24–36 mo | When competitor landscape shifts or new tools emerge |
| Debt payoff strategies | 18–24 mo | When average interest rates shift significantly |
| App / tool reviews | 6–12 mo | When the tool ships major updates or pricing changes |
| Credit score guides | 12–18 mo | When FICO or VantageScore releases model updates |

### Staleness Threshold (cross-link to §0-E Rule 3)
Any source dated more than 3 years prior must be flagged **VERIFY** before the refresh is closed. Refreshes that ship without re-verifying 3+ year-old sources fail QA.

### 6-Month Refresh Reminder Rule
Set in WordPress at Stage 8 of the production workflow (§4.11). When the reminder fires, run this section's procedure — Light or Deep based on the GSC signal pattern — and log the refresh date in the Publication Update Protocol (§4.11 Stage 9).

### AF Differentiation Layer
Mega-sites refresh by updating numbers but rarely restructure or add original frameworks. When AF refreshes, the refresh includes new Money Dominoes chains, updated worked examples, and new visuals — making each refresh a genuine content upgrade, not a date-stamp change.

---

## 5.10 — Generative Engine Optimization (GEO)

*Source: Princeton/Georgia Tech "GEO: Generative Engine Optimization" peer-reviewed study (Tier 1), AI assistant documentation (Tier 1), source-selection analyses (Tier 2). Parallel optimization layer to traditional SEO — captures traffic from organic results, AI Overview click-throughs, and AI chatbot citations.*

### Princeton/Georgia Tech Findings — Strategy Impact (~10,000 queries, 9 strategies tested)

| Strategy | Visibility Uplift | Why It Works |
|---|---|---|
| Include relevant statistics | ~40% | LLMs prefer sources containing concrete data points |
| Cite authoritative sources | ~30% | Referencing known institutions (Federal Reserve, IRS, BLS) increases selection probability |
| Add quotation from named expert | ~25% | Named expert quotes give LLMs attributable claims |
| Authoritative / technical tone | 20–25% | Confident, precise language signals expertise. Hedging ("might," "could") reduces citations |
| Fluency optimization | ~15% | Well-structured, grammatically clean prose easier to extract |
| **Keyword stuffing** | **Negative** | Density tricks reduce GEO performance. LLMs evaluate semantic relevance, not keyword frequency |
| Unique/original wording (alone) | Minimal | Uniqueness only helps when combined with statistical + authoritative signals |

### The 7 GEO Production Rules

1. **Lead every section with a citable fact.** First 1–2 sentences of every H2 contain a specific, sourced statistic or concrete claim an LLM could extract as a standalone answer.
   *Before:* "Building an emergency fund is one of the most important financial steps."
   *After:* "According to the Federal Reserve's 2023 Survey of Household Economics, 37% of Americans cannot cover a $400 emergency expense without borrowing. An emergency fund covering 3–6 months of essential expenses eliminates this vulnerability."
2. **Cite by name, not by link.** LLMs cannot follow hyperlinks — they extract text. Include institution name + specific data point in the visible text.
   *Before:* "Interest rates have risen significantly ([source](link))."
   *After:* "The Federal Reserve raised the federal funds rate to 5.25–5.50% in July 2023, the highest level since 2001 (Federal Reserve Board of Governors, FOMC Statement)."
3. **Use definitional sentences for key concepts.** Structure as `[Term] is [definition]` immediately after the H2/H3 that introduces the concept (also the featured-snippet extraction zone).
   *Example:* "The debt avalanche method is a debt payoff strategy where you make minimum payments on all debts and direct all extra money toward the debt with the highest interest rate, regardless of balance size."
4. **Structure comparisons as explicit contrast patterns.** Parallel structure → LLMs extract more reliably.
   *Example:* "The debt avalanche method minimizes total interest paid. The debt snowball method maximizes psychological momentum. Avalanche saves $1,200–$3,400 more on $30,000 of mixed-rate debt. Snowball produces the first account payoff 2–4 months faster, which Harvard Business Review research suggests increases the probability of completing the full payoff plan."
5. **Include "according to" attribution inline.** Strong LLM citation trigger. Use 3–5 times per 2,000-word post, spaced naturally across sections.
6. **Answer the question in the first two sentences.** AI Overviews preferentially extract from content with a direct answer early. Structure: `[Direct answer]. [One sentence of essential context or qualification].`
7. **Use numbered lists and tables for extractable structure.** LLMs extract structured formats more reliably than prose. Steps → numbered list. Options/types → bullet list or table. Comparisons → table with clear column headers. Criteria → numbered list with bold criterion + explanation.

### Tier 1 GEO Citation Sources for AF

Federal Reserve (surveys, rate decisions, economic data) · IRS (tax brackets, contribution limits, filing rules) · Bureau of Labor Statistics (employment, inflation, wage data) · Consumer Financial Protection Bureau (credit, lending, consumer data) · Social Security Administration (benefits, retirement) · FINRA (investing basics, broker data) · National Foundation for Credit Counseling (debt statistics) · Google Quality Rater Guidelines (meta-content about SEO/YMYL).

### GEO vs Traditional SEO — Where They Diverge (and how AF satisfies both)

| Element | Traditional SEO | GEO | AF Standard |
|---|---|---|---|
| Keyword placement | Title, H1, first 100 words, meta | Less important — semantic meaning matters | Both — keyword in title/H1 + semantic depth throughout |
| Source citation | External links (link equity) | Inline named citations (text-extractable) | Both — named citation in text + hyperlink for human readers |
| Content structure | H2/H3 hierarchy for crawlers | Clean definitional sentences + structured lists | Both — semantic headings + extractable answer formats |
| Freshness signal | Updated date in schema/byline | Current statistics + recent source dates in visible text | Both — schema date + inline "as of [date]" on data points |
| Authority signal | Backlink profile, domain authority | Named institutional sources in visible text | Both — backlinks + cite authoritative sources inline |
| Answer format | Featured snippet (40–60 words) | Concise self-contained answers (2–3 sentences) | Both — snippet-optimized answer blocks + GEO-optimized opening paragraphs |

### AI Overview Source Selection Patterns

**What gets cited:** pages that directly answer the query in first 200 words; pages with specific numbers, dates, named sources; pages from domains with established topical authority; pages with clean heading structure matching query intent; pages updated within last 12 months (time-sensitive topics).

**What gets skipped:** pages that bury the answer after long intros; vague/hedging language ("it depends" without specifying); pages optimized for affiliate conversion (product tables dominate); thin content (<500 words on complex topics); aggressive ad interstitials/popups (Core Web Vitals signal).

### GEO Audit Checklist (Apply Every Post)

- [ ] First paragraph after intro contains a direct, specific answer (1–2 sentences)
- [ ] ≥5 specific statistics with named sources in visible text
- [ ] ≥3 "according to [Institution]" attributions spread across the post
- [ ] All key concepts have clean `[Term] is [definition]` sentences
- [ ] All comparisons use parallel structure or tables
- [ ] Steps are numbered lists, not prose paragraphs
- [ ] Time-sensitive data includes "as of [Month Year]" inline
- [ ] No keyword stuffing (read aloud — sentences sound natural)
- [ ] The post could be quoted in a 2-sentence AI answer and make sense without surrounding context

### AF Differentiation Layer
GEO creates a structural advantage for smaller, focused sites. Mega-sites optimize for affiliate conversion — product comparison tables and "apply now" CTAs over clean extractable educational answers. AF's editorial model (teach first, convert second) naturally aligns with what LLMs cite: clear definitions, specific numbers, named sources, structured explanations. Every post built to AF standards is simultaneously GEO-optimized — without additional work.

---

# SECTION 7 — CALLOUT BLOCK COPY SPECIFICATIONS

*Authority source for §0-G output contract item 5 ("Three callout blocks Type A / B / C, each with complete copy ready for CMS insertion and formatted according to Section 7-A"). Section 5.3 (Kadence Color Coding) governs the **visual** spec; this section governs the **copy** spec — when each callout fires, what it says, and how it bridges to its lead magnet.*

## 7-A — The Micro-Conversion Map: Three Callout Types and Placement Positions

This is the production spec a writer uses to place the three conversion callout points within any AF post. **Every post gets these three callouts — no more, no fewer** (unless no lead magnet exists for the topic, in which case Types A and B become internal links — see Zero-Asset Phase below).

### TYPE A — THE STAKES MOMENT CALLOUT

**Purpose:** Catch readers at the moment of peak problem vividness — right when they feel "this is my situation" — before that motivation fades into the next section. Micro-CTA, not a full CTA.

**Placement rule:** Immediately after the section where the problem's cost is made concrete. Typically the "why this matters" / "what this costs you" section, ~25–35% into the post. Specifically: **after the H2 containing the loss-aversion calculation** (Stage 3 of the Emotional Arc).

**Copy pattern:** One-sentence problem acknowledgment + one-sentence offer of the first specific action + "no [barrier]" trust reducer.

**Kadence block:** Warm amber background **#FFF8F0**, 4px left accent border **#FDA050**, single action button or text link. **Visual weight: light** — a nudge, not a billboard.

**Full example:**
> "If reading that $4,200-in-interest number made your stomach drop, you're not the only one. The Debt Payoff Tracker shows you exactly what it takes to make that number shrink — just your balance, your rate, and your payment. No finance degree. No spreadsheet skills. Takes 90 seconds."
>
> [Get My Debt Payoff Tracker — Free]

**What makes it work:** "Reading that number" callbacks specific content just consumed. "Made your stomach drop" names the emotion without amplifying it. "You're not the only one" normalizes (shame neutralization). Specific inputs ("just your balance, your rate, and your payment") minimize effort. "No finance degree. No spreadsheet skills." removes barriers. "90 seconds" is a credible time commitment.

### TYPE B — THE HOW-TO MOMENT CALLOUT

**Purpose:** Catch readers who have just learned how to do something and are in a "ready to apply this" state. The reader is in a progress job — they want to act on what they just learned.

**Placement rule:** Immediately after the primary instructional section — the H2 that teaches the core method, framework, or process. Typically 55–70% into the post. Specifically: **after the H2 where the reader has enough knowledge to use the tool but hasn't yet applied it to their own numbers.**

**Copy pattern:** One-sentence callback to what they just learned + offer of the tool that makes it immediately applicable to their numbers + specificity about what the tool does with those numbers.

**Kadence block:** Muted teal background **#F0FDFA**, 4px left accent border **#14B8A6**, single action button or text link. **Visual weight: medium** — more prominent than Type A because the reader is deeper in the post and more invested.

**Full example:**
> "You've just seen how the avalanche method stacks payments against your highest-rate debt first. The Debt Payoff Tracker applies that exact logic to your actual balances — enter your debts, and it calculates the optimal payment order, your total interest saved vs minimum payments, and the exact month each debt hits zero. Your numbers, not hypothetical ones."
>
> [Get My Debt Payoff Tracker — Free]

**What makes it work:** "You've just seen how" acknowledges the work the reader did. "Applies that exact logic to your actual balances" bridges from theory to personal application. "Enter your debts" minimizes effort (the action is data entry, not concept learning). "Your numbers, not hypothetical ones" activates endowment effect.

### TYPE C — THE COMPLETION MOMENT CALLOUT

**Purpose:** Catch readers who completed the entire post — the highest-intent cohort. Type C is the natural answer to "what do I do with everything I just learned?"

**Placement rule:** **After the conclusion paragraph, before the author bio.** Non-negotiable position — every AF post gets a Type C callout here.

**Copy pattern:** Brief recognition of the post being complete + the logical next step framed as applying everything just learned to their specific numbers + full value stack in compressed form (2–3 components named) + trust anchor.

**Kadence block:** Deep charcoal background **#1E293B** with warm amber accent text **#F59E0B** for the headline, white body text **#F8FAFC**, 12px border radius. **Visual weight: high** — the most prominent callout in the post, designed to stand out as a clear "final destination."

**Full example:**
> "You now know the difference between avalanche and snowball, how to calculate your total interest cost, and how to find an extra $200–$500/month in your existing budget. The Debt Payoff Tracker takes everything you just learned and runs it on your specific numbers — your balances, your rates, your extra payment capacity. It calculates your optimal payoff order, your timeline for each debt, and the total dollars you save. Enter your info once; update monthly in 5 minutes.
>
> Completely free. You'll get 3 setup emails, then one email per week. Unsubscribe anytime."
>
> [Get My Debt Payoff Tracker — Free]

**What makes it work:** "You now know" validates the reader's time investment. Listing three specific things proves the callback is real, not generic. "Takes everything you just learned and runs it on your specific numbers" bridges knowledge to application. Three specific tool outputs named — not vague. "Enter your info once; update monthly in 5 minutes" is an ongoing effort minimizer. Trust anchor as separate line — clean, specific, no hype.

## Rules for All Three Callout Types

1. **One of each, maximum.** Never two Type A callouts in the same post. Types A and B can coexist; Type C always appears.
2. **Same lead magnet across all three.** Do not promote different offers within the same post. The reader sees the same tool described from three different angles (stakes / application / completion), not three different products.
3. **Each callout must reference the preceding section.** Generic CTA copy that could appear in any post is prohibited. The transition bridge must name something specific from the content directly above it — a number, a method name, a scenario.
4. **No back-to-back stacking.** Never place two callouts back-to-back without intervening body text. Trust-visual adjacency rule (§5.1) applies — Type C callouts must never be placed adjacent to trust-critical charts or comparison tables.
5. **Visual hierarchy escalates.** Type A (amber, 4px border) is the gentle nudge. Type B (teal, 4px border) is the invested-reader prompt. Type C (dark background, high contrast) is the final call. Escalating visual weight mirrors the reader's escalating commitment.
6. **3-callout-per-article cap is the authority rule.** Section 4.10's 3-CTA Rule and §4.13's Pre-Publish QA both reference this cap; this section is the source of truth.

## CTA Protocol — Zero-Asset Phase (No Lead Magnet, No Newsletter)

When no lead magnet and no newsletter exist yet, apply this to all 3 CTA positions:

- **Type A (Stakes Moment — amber callout, ~25–35% in):** Internal-link CTA. Same amber block, same structure. Copy pattern: one sentence acknowledging the specific cost/problem just calculated above → one sentence offering the pillar post as "the complete breakdown" → one trust reducer. The transition bridge MUST reference a specific number or scenario from the section directly above it — never generic.
- **Type B (How-To Moment — teal callout, ~55–70% in):** Internal-link CTA. Same teal block. Copy pattern: one sentence recapping what the reader just learned → one sentence offering a sibling spoke post as "the next step in applying this" → name 2–3 specific things the linked post covers.
- **Type C (Completion Moment — dark charcoal callout, end of post):** "Read Next" block. Same dark charcoal block. List the 2 most logical next posts for this reader. Copy pattern: *"You now know [3 specific things from THIS post]. The next two reads that complete this picture:"* → two post titles with one-line descriptions of what each one adds.

### Mandatory — Placeholder Comment System (Zero-Asset Phase only)

On the line directly above every CTA block, insert this HTML comment:

```
<!-- FUTURE CTA: [Post Topic] | Slot: [A / B / C] | Upgrade to: [Lead Magnet / Newsletter] when ready -->
```

The comment must be specific. Example:

```
<!-- FUTURE CTA: Debt Avalanche | Slot: C | Upgrade to: Debt Payoff Tracker lead magnet when ready -->
```

Do NOT leave a generic comment. The upgrade target must be named. (This is the only authorized HTML-comment placeholder in any AF draft and is exempt from §0-G item 1's "no placeholder text" rule.)

---

## 7-B — The Emotional Arc System: 4 Stages Per Post

*Pre-writing requirement. The Emotional Arc Template must be completed BEFORE drafting — never retrofitted. Determines intro tone, recognition target, urgency calculation, and CTA placement. Cross-referenced from §7-A Type A placement ("after the H2 containing the loss-aversion calculation — Stage 3 of the Emotional Arc").*

### Stage 1 — Reader Starts (The Arrival State)

- **Reader emotional condition on landing:** What combination of emotion / urgency / confusion are they carrying when they type the search query and click? **Researched, not guessed** — check Reddit threads (what words do they use?), People Also Ask (what does the framing reveal?), and the search query itself (`how to stop` = distress; `how to start` = aspiration; `what is` = confusion; `best way to` = decision mode).
- **Writer's job (Intro + Answer Block):** Match the emotional tone of the arrival state. Not cheerful, not clinical — whichever register accurately reflects where the reader is. Anxious → acknowledge without amplifying. Confused → signal clarity is coming. Skeptical → earn attention before claims.
- **Word count:** Intro 150–200 + Answer Block 40–60.
- **Failure modes:** False cheerfulness mismatching state ("Hey! Welcome! Budgeting is SO fun!" when reader just overdrew); information dump before emotional matching; over-acknowledging anxiety to the point of amplifying it.

### Stage 2 — Recognition (The "This Is Me" Moment)

- **Target shift:** "Let me see if this is useful" → "This writer understands my actual situation." Liking-activation moment — where the reader begins to trust the author, not just the information.
- **Writer's job (H2 #1 + H2 #2 — problem establishment + stakes):** Create specific recognition moments using dollar amounts, scenarios, and phrases drawn from reader personas + Reddit pain-point research.
- **Specificity ladder:**
  - **Weak:** "You might have some debt." (Matches no one specifically.)
  - **Medium:** "If you have credit card debt, you know how stressful it can be." (Generic.)
  - **Strong:** "$8,000 across three cards at different rates you haven't added up lately — one at 19%, one at 22%, one store card at 26% that you only opened for the 15% discount on a couch." (Lived understanding.)
- **Word count:** H2 #1 + H2 #2 combined 600–900.
- **Failure modes:** Generic problem descriptions; academic framing (informative but emotionally flat); register mismatch (too cheerful or too catastrophizing).

### Stage 3 — Peak Urgency (The Gap Amplification Moment)

- **Target shift:** Recognition → motivation. Reader understands what the problem is costing them specifically, in numbers, right now. **Type A Stakes Moment callout fires here.**
- **Writer's job (H2 #3 / "what this costs you" section):** Deploy the loss-aversion mechanism. Calculate cost in dollars per month, per year, over 5 years. Make the math so specific the reader can do the same calculation for themselves — or recognize that the offered tool does it.
- **Word count:** 300–500.
- **Failure modes:** Vague urgency ("this is costing more than you think!" — how much?); manufactured fear without calculation (YMYL violation, destroys trust); skipping the math because it feels aggressive (the math IS the service — showing $8,000 @ 22% costs $146/mo in interest is generosity, not aggression).
- **Type A callout placement:** Immediately after the cost-calculation section.

### Stage 4 — Close (Path Bridging + Conversion)

- **Target shift:** "I understand the problem and feel the urgency" → "I can see the specific path forward and it feels achievable." Must feel like **relief, not pressure**.
- **Writer's job (H2 #4 onward + conclusion + all 3 CTAs):** Deliver method / framework / tool with enough specificity that the reader can see themselves using it. Stage 4 is the reciprocity engine — bulk of value delivered here, justifying CTA asks. End with path-bridging language: name the specific first action, why it's the right starting point (not random), and the time it takes.
- **Word count:** Remaining body + conclusion (varies by post type — see §5.6).
- **Failure modes:** Reverting to urgency language during instruction (whiplash from relief to fear); complexity theater (making the method sound harder than it is); generic inspirational close ("You've got this!") instead of a specific first action ("Open the tracker. Enter your three highest-rate balances. 90 seconds.").
- **Type B callout placement:** After the primary instructional H2.
- **Type C callout placement:** After the conclusion paragraph, before author bio.

### Emotional Arc Pre-Writing Template (10–15 min — required before outlining)

```
TARGET KEYWORD: [keyword]

READER ARRIVAL STATE:
[2–3 sentences describing reader's emotional state at moment of search.]

STAGE 1 — TONE TARGET:
[Specific tone instruction for the intro. e.g., "Acknowledge financial anxiety without
amplifying it. Signal that specific numbers and a clear plan are coming. Do not be cheerful.
Do not be clinical. Be the calm friend who has been through this."]

STAGE 2 — RECOGNITION TARGET:
[Specific scenario / dollar amount / phrase that creates the strongest recognition moment
for this reader persona.]

STAGE 3 — URGENCY CALCULATION:
[Specific cost per month / per year / over 5 years — calculated from real data.]

TYPE A CALLOUT POSITION:
[After which H2? Lead magnet referenced?]

STAGE 4 — RELIEF FRAMING:
[What does the solution feel like when it lands for this specific reader? Specific first action?]

TYPE B CALLOUT POSITION: [After which H2?]
TYPE C CALLOUT: [What specific post content does it reference?]
```

**How to use:**
1. Complete BEFORE outlining the post. The arc determines outline structure, not vice versa.
2. Share the completed template with editors during review — editor checks whether the draft delivers each stage's promise.
3. During QA, verify each stage's target was hit (intro tone matches Stage 1; Stage 2 contains the specific recognition scenario; Stage 3 includes the calculated urgency number; callouts at specified positions).
4. Store completed templates alongside the post. When the post comes up for refresh (§5.9), the arc template tells the refreshing writer what the original emotional structure was — preserve it while updating the data.

---

## 7-C — Quick Reference Cheat Sheets

*High-frequency in-session decision aids. Open in a side tab while writing.*

### 7-C.1 — Voice Consistency Cheat Sheet (6-Attribute Sentence Test)

Before publishing any sentence, test against all six:

| Attribute | Test Question | Fix If It Fails |
|---|---|---|
| Conversational Expert | "Would a smart friend say this over coffee?" | Remove academic phrasing. Shorten sentences. Add "you." |
| Judgment-Free | "Could a reader in debt feel shamed by this?" | Remove `should have` / `you need to` / `obviously`. Reframe as possibility, not obligation. |
| Action-Biased | "Does this paragraph end with something the reader can DO?" | Add a concrete next step. Replace theory with instruction. |
| Numbers-First | "Is there a specific dollar amount, percentage, or timeframe within 2 sentences?" | Add one. Vague = untrusted in YMYL. |
| Emotionally Honest | "Does this acknowledge the real feeling behind the financial question?" | Add one sentence of emotional context before the tactical advice. |
| ELI12 Compliant | "Would a smart 12-year-old understand every word?" | Replace jargon with plain term. Add parenthetical translation on first use. |

### 7-C.2 — Top 20 Jargon Translations (ELI12 First-Use Reference)

*Every finance term gets a parenthetical translation on first appearance per §4.1 ELI12 Rule 2. Use these defaults; vary wording naturally to avoid repetition across posts.*

| Jargon | ELI12 Translation |
|---|---|
| APR | The total yearly cost of borrowing, shown as a percentage |
| Compound interest | Earning interest on your interest (your money makes money that makes more money) |
| Asset allocation | How you split your money between different types of investments |
| Amortization | How each payment splits between what you owe (principal) and the cost of borrowing (interest) |
| Liquidity | How quickly you can turn something into cash without losing value |
| Diversification | Not putting all your eggs in one basket — spreading money across different investments |
| Equity | The part of something you actually own (home value minus what you still owe) |
| Index fund | A basket of stocks that automatically copies the whole market (or a chunk of it) |
| Expense ratio | The annual fee an investment fund charges, shown as a percentage of your money |
| Rebalancing | Adjusting your investments back to your target split when they drift |
| Capital gains | Profit from selling an investment for more than you paid |
| Tax-advantaged | An account where the government gives you a tax break for saving (like a 401k or Roth IRA) |
| Vesting | The timeline before your employer's retirement contributions become permanently yours |
| Premium | The monthly price you pay for insurance, whether or not you use it |
| Deductible | The amount you pay out of pocket before insurance starts covering costs |
| Credit utilization | How much of your available credit you are using, shown as a percentage |
| Debt-to-income ratio | Your monthly debt payments divided by your monthly gross income |
| Emergency fund | Money set aside specifically for unexpected expenses — job loss, car repair, medical bill |
| Net worth | Everything you own minus everything you owe |
| Sinking fund | Money you save in advance for a known future expense (car repair, holiday gifts, annual insurance) |

### 7-C.3 — Decision Tree 1: Choosing Post Format (from §6.3)

*Map reader's primary intent → post format + word count target. Use at the Article Brief stage to set Field 5 (Writing Style) and Field 7 (Target Word Count).*

```
START: What is the reader's primary intent?

├── "How do I do X?" (procedural)
│   → How-To / Tutorial Format
│   → Numbered steps, worked examples, visual per major step
│   → Target: 2,500–4,000 words
│
├── "What is X?" (definitional)
│   → Explainer Format
│   → Definition → Why it matters → How it works → Examples → FAQ
│   → Target: 2,000–3,000 words
│
├── "Which X is better?" (comparison)
│   → Versus / Comparison Format (apply §4.5-B spec)
│   → Framework → Option A → Option B → Decision criteria → "Choose A if / Choose B if"
│   → Target: 2,500–3,500 words
│
├── "What are the best X?" (listicle)
│   → Ranked List Format
│   → Criteria disclosed → Items ranked with explanation → Summary table
│   → Target: 2,500–4,500 words
│
└── "Everything about X" (comprehensive)
    → Ultimate Guide / Pillar Post Format
    → TOC → Multiple H2 clusters → FAQ → Related resources
    → Target: 4,000–6,000+ words (consider hub-and-spoke if >5,000)
```

### 7-C.4 — Decision Tree 2: Choosing Visual Approach

```
START: What data or concept needs visualization?

├── A process or sequence
│   → Flowchart or numbered step visual (Kadence: Row Layout w/ numbered Info Boxes)
│
├── A comparison between 2–3 options
│   → Comparison table (2-column "Attribute | Value" for 2 options)
│   → Or Tabs Block (one tab per option) for detailed comparisons
│
├── A trend over time
│   → Line chart (single metric) or stacked area (composition over time)
│   → Setup-Chart-Interpretation format (§5.4)
│
├── A budget or allocation breakdown
│   → Horizontal bars sorted descending (>5 categories)
│   → 100% stacked bar or simple pie (2–3 categories with dramatic contrast)
│
├── A cascading chain of financial decisions
│   → Money Dominoes visual (horizontal flow, 3–5 nodes — §5.2)
│
├── A single powerful number
│   → Single-Big-Number callout (32px+ number, short caption — Featured Stat Info Box)
│
└── Exact numbers readers will reference / verify
    → Table (not chart) — Advanced Table with mobile-fit class
```

### 7-C.5 — Decision Tree 3: CTA Strategy Selection

```
START: What is the post's primary conversion goal?

├── Email list growth (default for most posts)
│   → Mid-article CTA: Content-specific lead magnet (template, checklist, calculator)
│   → End-of-post CTA: General newsletter signup
│   → Sidebar CTA: Evergreen lead magnet
│
├── Affiliate revenue (product-relevant posts only)
│   → CTA placement: AFTER the comparison/recommendation section, never before
│   → Styling: clearly distinct from editorial callouts (different border, explicit "affiliate" label)
│   → Never adjacent to trust visuals (charts, data tables)
│   → Maximum 2 affiliate CTAs per post
│
├── Internal traffic (hub-and-spoke linking)
│   → In-content contextual links (2–3 per 1,000 words)
│   → End-of-section "Related" callout boxes
│   → End-of-post "Read Next" section
│
└── Social sharing (viral-potential posts)
    → Tweetable/shareable stat callouts (1–2 per post)
    → Pinterest-optimized images (2:3 ratio pins — §4.12 + §5.8)
    → "Share this with someone who needs it" micro-CTA
```

---

# SECTION 8 — CONVERSION COPYWRITING SOP

## 8.1 The Six Cialdini Levers

**Lever 1 — Reciprocity**
- **Trigger:** Every post, before any CTA appears.
- **Execution Rule:** Give away your best thinking in the post body. The lead magnet extends what the post teaches — it applies the framework to the reader's specific numbers. It never withholds what the post should have taught.
- **Copy Pattern:** Post teaches the 50/30/20 framework → Lead magnet applies it to the reader's actual paycheck → "If the free stuff is this good, the template must be incredible."

---

**Lever 2 — Social Proof**
- **Trigger:** Any CTA, lead magnet description, or product claim.
- **Execution Rule:** Never use subscriber counts. Use specific-person + specific-result + specific-timeframe. When you have no testimonials, use published research to normalize the problem.
- **Copy Pattern (strong):** "After using this template, Sarah — a 28-year-old teacher making $42,000 — paid off $12,400 in credit card debt in 14 months."
- **Copy Pattern (research-based):** "57% of Americans can't cover a $1,000 emergency expense (Bankrate, 2024)." *(signals: you are not alone)*

---

**Lever 3 — Authority**
- **Trigger:** Any claim, recommendation, or statistic.
- **Execution Rule:** Cite Federal Reserve, IRS, CFPB, or BLS by name in visible text — not just as a link. Precision in the lead magnet description signals expertise.
- **Copy Pattern (weak):** "Download our free financial template."
- **Copy Pattern (strong):** "Download the Debt Payoff Tracker — a Google Sheet with 4 tabs that calculates your avalanche vs snowball payoff timeline, total interest saved, and monthly payment schedule for up to 12 debts."

---

**Lever 4 — Liking**
- **Trigger:** Intro, first 300 words, any personal-experience sentence.
- **Execution Rule:** Use the reader's actual language sourced from Reddit, comments, and emails. No false warmth.
- **Copy Pattern (banned):** "Hey friend! I'm SO excited you're here!"
- **Copy Pattern (correct):** "If you're reading this because your student loan payment went up and the math doesn't work anymore, this post is for you."

---

**Lever 5 — Scarcity / Urgency (Genuine Only)**
- **Trigger:** Any CTA adjacent to a loss-framing calculation.
- **Execution Rule:** No countdown timers. No "limited time offer." Calculate the specific dollar cost of one month's delay and state it. The math is the urgency.
- **Copy Pattern:** "Every month you carry the $8,000 balance at 22% APR, you pay $146 in interest alone. That's $1,752 per year — money that disappears into the bank's revenue instead of your savings. The Debt Payoff Tracker calculates your exact payoff timeline, including what happens if you start this month vs next month."

---

**Lever 6 — Commitment / Micro-Commitment Ladder**
- **Trigger:** CTA offer selection; funnel sequencing decisions.
- **Execution Rule:** Match the ask to the reader's current commitment level. "Download the free template" beats "Join our community" for uncertain readers.
- **Ladder:** Read post (free) → Download template (email) → Use template with real numbers → Open email sequence → Click link → Tripwire purchase ($7–$27) → Flagship product

---

## 8.1 Behavioral Economics — Execution Rules

**Loss Aversion (Kahneman/Tversky 2:1 Rule)**
- **Trigger:** Any financial concept that can be framed as gain OR loss.
- **Execution Rule:** Always write loss-first, then offer the resolution as the gain. Loss must be calculable, verifiable, and proportional — never exaggerated.
- **Copy Pattern (loss-framed):** "Every month without a high-yield savings account, you're losing $15–$40 in interest you could be earning on the money you already have. At current rates (4.5%+ APY), $10,000 sitting in a regular checking account costs you roughly $375 per year in missed interest."
- **Copy Pattern (gain-framed — weaker):** "A high-yield savings account could earn you $375 per year on a $10,000 balance."

---

**Status Quo Bias**
- **Trigger:** Any CTA or first-action instruction.
- **Execution Rule:** Frame the cost of the status quo in vivid, specific dollar terms. Then make the first action trivially small by comparison.
- **Copy Pattern:** "You're currently paying $146/month in interest on that credit card — $1,752 this year alone. The Debt Payoff Tracker takes 90 seconds to set up: enter your balance, rate, and minimum payment. It calculates everything else."

---

**Paradox of Choice — One-CTA-Per-Post Rule**
- **Execution Rule:** One CTA per post. Every decision point reduced to a binary with a clear recommended option.
- **Copy Pattern:** "If your interest rate is above 7%, use avalanche. If it's below 4%, consider investing first. Between 4–7%, either works — here's how to decide."

---

**Anchoring**
- **Execution Rule:** Anchor the product price against the cost of the problem it solves — never against a fake original price.
- **Copy Pattern (correct):** "The Complete Debt Payoff Kit is $97. The average American with $8,000 in credit card debt at 22% APR pays $2,700 per year in interest alone. If this kit helps you pay off even 6 months faster, you save $1,350 — a 14x return on a $97 investment."
- **Copy Pattern (banned):** "Originally $297, now just $97!" *(deceptive if product was never sold at $297)*

---

**Endowment Effect**
- **Execution Rule:** Write about the lead magnet as if the reader already has it and is using it.
- **Copy Pattern:** "Once you've got the Emergency Fund Calculator open, plug in your rent first — that's usually the biggest number and it sets the baseline for everything else. Then add utilities, groceries, and your minimum debt payments. The calculator auto-generates your monthly target and shows you exactly how many months to reach 3 months, then 6 months of coverage."

---

## 8.1 Financial Shame Neutralization — 4-Step Framework

*Apply when topic carries shame signals: debt, missed payments, zero savings, not knowing basics.*

**Step 1 — Normalize as systemic gap, not personal failure:**
"Nobody taught you this. It's not in the school curriculum. It's not in the employee handbook. The financial industry profits from confusion. If you don't know how amortization works, that's not a character flaw — it's a curriculum failure."

**Step 2 — Separate problem from person:**
"Your debt is a math problem. It has inputs (balance, rate, payment) and outputs (timeline, total cost). It is not a reflection of your intelligence, discipline, or worth as a human being."

**Step 3 — Create a forward identity:**
"You're here reading this, which means you're the kind of person who decided to figure it out. That decision — the one you already made by clicking this link — is the hardest part."

**Step 4 — Offer first action only after shame is neutralized:**
"The Debt Payoff Tracker asks for three numbers: your balance, your interest rate, and your monthly payment. Enter those three numbers and it does the rest. That's the whole first step."

**Banned CTA:** "Stop letting your debt control your life! Take charge today with our Debt Freedom Blueprint!"

**Correct CTA:** "When you're ready to see the full picture without judgment, the Debt Payoff Tracker lays out every number — balance, interest, timeline — in one place. No motivational speeches. Just math that's finally on your side."

---

## 8.2 The Four-Stage Desire Sequence

Build in this order. Each stage depends on the previous. Skip one and the CTA falls flat.

**Stage 1 — Problem Vividness**
- **Execution Rule:** Use a specific moment in the reader's week where the problem shows up in lived detail. Not abstract.
- **Copy Pattern:** "It's Thursday. Payday is tomorrow. You have $47 in your checking account. Your kid's school just sent home a permission slip for a $25 field trip. The gas light came on this morning. You need groceries but you're doing the mental math on whether you can stretch the pasta and canned sauce one more night. You're not bad with money — you're doing impossible arithmetic with not enough numbers."

**Stage 2 — Contrast Vivification**
- **Execution Rule:** Show the specific, achievable contrast. Not "financial freedom." Achievable contrast, not aspirational contrast.
- **Copy Pattern:** "It's Thursday. Payday is tomorrow. You have $1,200 in your checking account and $3,400 in a savings account you haven't touched. The field trip permission slip gets signed without mental math. You fill up the gas tank without checking the price per gallon. You buy groceries for the week — including the good cheese — and you don't think about it again until next Thursday."

**Stage 3 — Gap Amplification**
- **Execution Rule:** Convert the gap between Stage 1 and Stage 2 into specific dollars and time. Apply loss aversion.
- **Copy Pattern:** "Your credit card balance is $6,200 at 22% APR. At minimum payments, you'll pay $4,800 in interest over the next 5 years — nearly 80% of the original balance, paid again, to the bank, for the privilege of borrowing your own future income. That's $80/month that could be going into a savings account earning 4.5% instead of a credit card bill earning the bank 22%."

**Stage 4 — Path Bridging**
- **Execution Rule:** Name the first specific action, why it's the right starting point, what happens immediately after. Urgency from Stage 3 must resolve into agency, not anxiety.
- **Copy Pattern:** "The first step is entering three numbers into the Debt Payoff Tracker: your balance ($6,200), your rate (22%), and your current monthly payment ($180). The tracker calculates two things instantly: how long payoff takes at your current payment, and how much faster it goes if you add $50, $100, or $200/month. You'll see the exact month your balance hits zero — and the exact dollar amount you save in interest for every extra dollar you add. The whole setup takes 90 seconds."

---

## 8.3 The Six Silent Objections — Dissolution Patterns

| Objection | Dissolution Copy Pattern |
|---|---|
| "My situation is too specific — this won't apply to me." | Name specific complications the tool handles: "The tracker handles multiple debts at different rates, variable income months, and mid-year rate changes." Then name who it ISN'T for: "This won't work if you're self-employed with variable quarterly income." *(Exclusion converts — it signals honesty.)* |
| "I've tried this before and it didn't work." | Name the mechanism of previous failure: "Most budgeting apps fail because they track what you already spent instead of telling you what you can spend. That's like weighing yourself after Thanksgiving — informative, but too late to change anything." |
| "I don't want to give my email and get spammed." | State exact post-opt-in cadence: "After you download the tracker, you'll get a 3-email setup sequence over the next week that walks you through using it. After that, you'll get one email per week when a new post goes live. That's it. No daily emails. No affiliate promotions. No selling your email to third parties. Unsubscribe link in every email." |
| "I'll do it later." | Calculate the dollar cost of one month's delay: "Every month you carry the $6,200 balance at 22% APR costs you $113 in interest. That's $113 that could go toward paying down principal instead. If you set up the tracker today instead of next month, you save $113." |
| "This is probably just trying to sell me something." | Acknowledge monetization directly: "Yes, Adulting Finance makes money. Here's how: the content is free because the products convert better when readers trust the advice first. That model only works if the advice is actually good. So there's no incentive to steer you wrong — if the free content isn't genuinely useful, nobody buys anything and the site doesn't survive. The business model and your interests are aligned." |
| "I can't afford to spend money on this right now." | Explicitly separate free from paid: "The Debt Payoff Tracker is completely free. No credit card required. No 'free trial' that auto-charges. You download it, you own it, you use it forever. There is a paid version — the Complete Debt Payoff Kit — that includes additional tools and a video walkthrough. But you don't need it to get the result I described above. The free tracker does everything this post taught you." |

**Inline Objection Patterns:**
- **"Even If":** "[Desired outcome], even if [most common barrier]." → "Build a $1,000 emergency fund in 90 days, even if you're living paycheck to paycheck." *(Only use when the barrier is genuinely not disqualifying.)*
- **Acknowledge-and-Reframe:** Validate prior failure → Externalize failure to methodology → Position new tool as structurally different. → "If you've tried paying off debt before and quit after a few months, that's completely understandable — most debt payoff plans fail because they're built on willpower instead of systems."
- **"Reason Why":** Never state a recommendation without a mechanism. → "The 50/30/20 rule works because it creates a hard ceiling on your fixed expenses — and it's that ceiling, not the savings percentage, that determines whether you can build an emergency fund."

---

## 8.4 The CTA Copywriting System — 5 Required Components

Every CTA must contain all five. Missing one = conversion leak.

**Component 1 — Transition Bridge**
Connect to specific content just consumed. Generic CTAs convert at a fraction of contextual ones.
- **Banned:** "Want to learn more? Download our free template!"
- **Required:** References specific dollar amount, section, or scenario from the preceding content.

**Component 2 — Specific Benefit Statement**
Name what the reader gets, not what the tool has.
- **Banned:** "Download our free emergency fund calculator."
- **Required:** "The Emergency Fund Calculator takes those six numbers you just identified — rent, utilities, groceries, insurance, transport, and minimum debt payments — and builds your exact monthly target. Not a generic '3-6 months of expenses' rule. Your specific target, based on your specific floor, updated when any number changes."

**Component 3 — Effort Minimizer**
State the actual effort specifically. "It only takes a minute!" is not credible.
- **Banned:** "It only takes a minute!"
- **Required:** "The setup takes 90 seconds — you're entering six numbers from the calculation you already did in this post. The calculator does the rest: monthly target, timeline to 3 months of coverage, timeline to 6 months, and the exact weekly savings amount that gets you there."

**Component 4 — Trust Anchor**
- **Free opt-in:** "You'll get a 3-email setup sequence over the next week, then one email when new posts go live. No daily blasts. No affiliate spam. Unsubscribe in every email."
- **Paid product:** "30-day full refund. No forms. No 'reason required' field. No questions. If it doesn't work for your situation, you get your money back — and you keep the templates."

**Component 5 — Action Button**
- Rule 1: First-person possessive: "Get My Emergency Fund Calculator" beats "Get Your…" or "Submit."
- Rule 2: Completion language: "Yes, Give Me the Template" beats "Download."

---

**Value Stacking Formula (for paid products)**

Three-part structure per component: Name it → What it does → What it eliminates.

> "Here's everything inside the Complete Debt Payoff Kit:
>
> The Debt Payoff Tracker (a Google Sheet that calculates your optimal payment allocation across up to 12 debts — so you never have to manually figure out which debt gets the extra payment this month).
>
> The Interest Cost Calculator (enter any balance and rate, and it shows you the exact total cost over 1, 3, 5, and 10 years — so you stop guessing what your debt actually costs and start seeing the real numbers).
>
> The Payoff Accelerator Scenarios (pre-built models showing what happens if you add $50, $100, $200, or $500/month to your payments — so you can find the sweet spot between aggressive payoff and actually being able to live your life).
>
> The Monthly Check-In Template (a 5-minute monthly review that keeps you on track without turning debt payoff into a second job — so you update once a month and move on)."

**Price anchoring against problem cost:**
> "The Complete Debt Payoff Kit is $97. If you're carrying $8,000 in credit card debt at 22% APR, you're currently paying approximately $1,368 per year in interest. If this kit helps you pay off your debt even 6 months faster, you save $684 — a 7x return on $97. And unlike the interest, the $97 is a one-time cost. The kit is yours forever."

---

## 8.5 Email Sequence Architecture — 6-Email Welcome Sequence

| Email | Day | Subject Line Architecture | Body Structure |
|---|---|---|---|
| 1 — Delivery | 0 | "Your [Lead Magnet Name] is ready — plus one thing to do before you open it" | (1) Download link above the fold immediately. (2) Unexpected usage tip: "Before you open it, one thing: most people make a mistake in row 7 — they enter their minimum payment instead of what they actually pay. If you're paying even $10 over the minimum, enter the real number. It changes the timeline more than you'd expect." (3) Sequence preview: "Over the next week, I'll send you 3 short emails that help you get the most out of the tracker. After that, you'll hear from me once a week when a new post goes live. That's it." |
| 2 — Deepest Problem | 2–3 | "I used to check my bank balance with one eye closed" | (1) Personal/reader-sourced crisis scenario. (2) Specific achievable contrast. (3) Gap in dollars and time. (4) Bridge to tool already downloaded. (5) Reply prompt: "Hit reply and tell me: what's the one number in your finances you've been avoiding looking at?" |
| 3 — Counterintuitive | 4–5 | "Why paying off your smallest debt first might cost you $3,400" | (1) Counterintuitive claim. (2) Show the math mechanism. (3) "Open your Debt Payoff Tracker and switch between the Avalanche and Snowball tabs. The difference in total interest paid is your personal version of this number." (4) Soft product mention (one sentence only). |
| 4 — Case Study | 6–7 | "$12,400 in 14 months on a teacher's salary" | Specific person (Sarah, 28, teacher) + specific situation ($12,400 across 3 cards, take-home $3,100/month) + specific approach (Debt Payoff Tracker, avalanche, $340/month found) + specific result (debt-free 14 months, $2,890 interest saved) + first direct product offer: "Sarah used the free tracker for the first 4 months, then upgraded to the Complete Debt Payoff Kit when she wanted the monthly check-in template and the accelerator scenarios." |
| 5 — Direct Pitch | 8–9 | "The Debt Payoff Kit: what's inside, what it costs, and whether it's right for you" | (1) Callback to sequence actions already taken. (2) Full value stack. (3) Three inline objections: "Is this just a fancier version of the free tracker?" / "Can I build this myself?" / "What if it doesn't work for my situation?" (4) Guarantee stated explicitly. (5) Single link: "Get My Complete Debt Payoff Kit — $97." |
| 6 — Last Chance | 10–11 | "Last email about the Debt Payoff Kit (and the number that made me write it)" | (1) "I'm going to stop talking about the Debt Payoff Kit after this email." (2) Most compelling loss frame: "$4,200 in interest over 3 years at minimum payments — $4,200 that doesn't reduce your balance by a single dollar." (3) Single link. (4) One-sentence guarantee. (5) "Either way, I'm glad you're here. The free tracker is yours forever. See you next week." |

**Subject Line Architectures — 7 Patterns:**

| Architecture | Format | Example |
|---|---|---|
| 1 — Specific Number | "[Dollar amount or %] you're [verb]ing without knowing it" | "$2,340 you're spending on subscriptions without realizing it" |
| 2 — Counterintuitive | "Why [thing everyone does] might be [unexpected negative consequence]" | "Why paying off your credit card every month might be hurting your credit score" |
| 3 — Mistake ID | "The [topic] mistake that's making you feel [emotional consequence]" | "The budgeting mistake that's making you feel like you're bad with money" |
| 4 — First-Person Story | "I used to [specific vulnerable behavior]" | "I used to check my bank balance with one eye closed" |
| 5 — Direct Value | "How to [specific outcome] without [primary barrier]" | "How to cut $300/month from your spending without a budget (and without noticing)" |
| 6 — Implied Answer | "Why does [frustrating experience] even when [expected positive condition]?" | "Why does saving feel impossible even when you're earning more than ever?" |
| 7 — Time-Sensitive Discovery | "What changed about [topic] this [time period]" | "What changed about high-yield savings accounts this month" |

*A/B testing: minimum 500 opens before declaring a winner. Test different architectures, not minor word variations.*

---

## 8.6 Product Page Architecture — 10 Sections in Order

| Section | Position | Primary Job | Key Rule |
|---|---|---|---|
| 1 — Headline + Subheadline | Top | State the transformation, not the product name | "Pay Off Your Debt Faster Than You Thought Possible — With Math, Not Motivation" + "Even if" subheadline handling top 2 objections |
| 2 — Problem Section | 10–15% | Use the reader's own language from Reddit/emails | Specific moment of pain, not abstract condition: "You know that feeling when you open the credit card app and the number is higher than last month — even though you made a payment?" |
| 3 — Agitation Section | 15–25% | Deploy loss aversion with specific dollars, time, opportunity cost | "At 22% APR on an $8,000 balance, minimum payments cost you $4,200 in interest over the next 3 years — $4,200 you earned, that left your bank account, and that didn't reduce your balance by a single penny." |
| 4 — Bridge: Who Is This For | 25–30% | Build trust through explicit exclusion | Name who it IS for AND who it ISN'T for. "This is NOT designed for: mortgage-only debt, business debt, or situations where you need legal debt relief." Exclusion signals honesty. |
| 5 — Value Stack | 30–50% | Component-by-component evaluation + anchoring | Three-part formula per component: Name it → What it does → What it eliminates. End: "Together, these tools replace the guesswork, the midnight anxiety math, and the spreadsheet you'd have to build from scratch." |
| 6 — Social Proof | 50–60% | Specific outcome narrative matching current reader persona | "'I paid off $12,400 in 14 months on a $42,000 salary. The tracker showed me my payoff date on day one.' — Sarah, 28, teacher, Atlanta" |
| 7 — Objection Section | 60–70% | Inline objection handling — 3 to 5 objections woven into flow | "You might be thinking: 'Can't I just build this in Google Sheets myself?' Absolutely. If you're comfortable with spreadsheet formulas, you can build something similar in 8–12 hours." |
| 8 — The Offer | 70–80% | Price anchored against cost of problem | "$97 vs. $4,200 in interest on the average credit card balance. If the Kit saves you even 3 months of interest, you've made back $350 — a 3.6x return." |
| 9 — The Guarantee | 80–85% | Personal promise language, not legal policy | "Try the entire Kit for 30 days. If it doesn't work for your situation — for any reason — email me and I'll refund every penny. No forms. No 'reason required' dropdown. No questions." |
| 10 — The Close | 85–100% | Action button + compressed value restatement | "[Get My Complete Debt Payoff Kit — $97] / Full refund within 30 days. No questions." |

---

## 8.7 The Specificity Upgrade — 3 Rules

| Rule | Banned | Required |
|---|---|---|
| Replace relative adjectives with numbers | "A lot of people struggle with budgeting." | "58% of Americans don't follow a monthly budget (Debt.com, 2024)." |
| Replace outcome descriptions with scenario descriptions | "Improve your credit score." | "Move from 620 to 680 in six months — which is the threshold where most lenders offer better rate terms. On a $25,000 car loan, that one jump saves you approximately $2,100 in interest over 5 years." |
| Replace generic nouns with named specifics | "A tool to track your spending." | "A Google Sheet that pulls from your actual bank categories and color-codes overspending in real time — red for over budget, green for under, yellow for within $20 of the limit." |

---

## 8.8 Conversion Architecture Map — Techniques by Post Position

| Post Position | Active Persuasion Techniques |
|---|---|
| Introduction (0–10%) | Reciprocity · Liking via ELI12 · Job-type matching (Relief / Progress / Clarity / Identity) · Problem Vividness (Stage 1) |
| Problem/Stakes (10–30%) | Loss aversion at data points · Social proof via research · Authority via named citations · Contrast Vivification (Stage 2) |
| Core Teaching (30–70%) | Reciprocity deepened · Authority via precision · Curiosity gaps at section transitions · Gap Amplification (Stage 3) · Path Bridging (Stage 4) |
| Conclusion + Post-Content (70–100%) | Commitment/consistency · Final loss framing (one sentence) · Path bridging completion (single first action named) |
| CTA Position 1 — Stakes Moment (30–40%) | Small commitment ask · Partial reciprocity earned · Objections 1 + 3 handled · Curiosity gap opened · Effort minimizer |
| CTA Position 2 — How-To Moment (55–70%) | Full desire sequence complete · All 6 silent objections addressed · Value stack · Endowment effect activation |
| CTA Position 3 — Completion Moment (end) | Highest-intent cohort · Softer tone · Final loss framing · Completion language |

**Welcome Email Sequence Technique Map:**

| Email | Primary Technique | Secondary Techniques |
|---|---|---|
| 1 — Delivery | Reciprocity (overdeliver with unexpected insight) | Trust anchor · Specificity (usage tip) |
| 2 — Deepest Problem | Full desire sequence (4 stages) | Liking (personal story) · Commitment (reply prompt) |
| 3 — Counterintuitive | Authority (original analysis) | Curiosity gap · Soft product mention |
| 4 — Case Study | Social proof (specific narrative) | Liking (relatable person) · First product offer |
| 5 — Direct Pitch | Commitment/consistency (callback to prior actions) | Value stack · 3 inline objections · Guarantee |
| 6 — Last Chance | Loss aversion (12-month cost of status quo) | Genuine scarcity (sequence ending) · Warm close |

---

## 8.9 Conversion Copywriting QA Checklist

**Persuasion Foundations**
- [ ] Reciprocity: Reader received genuine value before the ask?
- [ ] Social proof: At least one specific outcome statement or research-based normalization stat?
- [ ] Authority: Copy cites at least one named institutional source or shows calculation-level expertise?
- [ ] Liking: Copy uses the reader's language (Reddit-sourced phrases, conversational register)?
- [ ] Scarcity/Urgency: All urgency genuine (calculated from real math, not countdown timers or "limited spots")?
- [ ] Commitment: Ask matches reader's current position on the micro-commitment ladder?

**Behavioral Economics**
- [ ] Loss aversion: Cost of inaction stated in specific dollars before the gain is offered?
- [ ] Loss framing is honest: Calculable, verifiable, and proportional — not exaggerated?
- [ ] Status quo bias addressed: First action framed as smaller than the cost of doing nothing?
- [ ] Choice reduction: One CTA per post (not competing offers)?
- [ ] Anchoring: Price or effort anchored against cost of the problem (not a fake original price)?
- [ ] Endowment effect: Lead magnet described as if the reader already has it and is using it?

**Audience Psychology**
- [ ] Shame neutralization: Copy normalizes the situation before teaching the solution?
- [ ] No blame language: Zero instances of "should have," "need to," "obviously," or "just"?
- [ ] Forward identity: Copy creates a "person who decided to change it" frame?
- [ ] Escape valve: Option for overwhelmed readers to take a smaller step?
- [ ] Emotional acknowledgment: Copy names the feeling before offering the fix?

**Desire Sequence**
- [ ] Problem vividness: Specific, sensory scenario (not abstract problem description)?
- [ ] Contrast vivification: "After" state specific and achievable (not aspirational)?
- [ ] Gap amplification: Cost of gap stated in dollars and time?
- [ ] Path bridging: First step named specifically with effort estimate?

**Objection Handling**
- [ ] "Too specific for me" addressed?
- [ ] "Tried before" addressed?
- [ ] "Don't want spam" addressed (exact cadence stated)?
- [ ] "I'll do it later" addressed (delay cost calculated)?
- [ ] "Just selling me something" addressed?
- [ ] "Can't afford it" addressed (free and paid explicitly separated)?

**CTA Anatomy**
- [ ] Transition bridge references specific content from preceding section?
- [ ] Specific benefit names reader's outcome (not tool's features)?
- [ ] Effort minimizer stated credibly and specifically?
- [ ] Trust anchor states exact expectations (email cadence, refund terms)?
- [ ] Action button uses first-person possessive ("Get My…")?

**Specificity Test**
- [ ] Every relative adjective replaced with a number?
- [ ] Every outcome description replaced with a scenario description?
- [ ] Every generic noun replaced with a named specific?
- [ ] At least one dollar amount within 2 sentences of every major claim?
- [ ] Lead magnet described with enough specificity that reader can picture using it?

---

## 8.10 Emotional Trigger Word Reference

**Usage Rules:**
1. Never stack more than 2 trigger phrases in the same sentence.
2. Every trigger word must be factually accurate. "Proven" requires proof. "Exact" requires calculation. "Free" means free.
3. Trigger words amplify good copy — they do not rescue bad copy.
4. Test trigger words in subject lines and button text first.
5. Rotate phrases across emails and CTAs to prevent reader habituation.

| Category | Word/Phrase | Use When | Example |
|---|---|---|---|
| **1 — Precision/Credibility** | Exact | The number is calculated, not estimated | "Your exact payoff date" |
| | Specific | The guidance applies to a defined situation | "Specific to your income and debt mix" |
| | Calculated | The result comes from math, not opinion | "Calculated from your actual balance and rate" |
| | Step-by-step | The process is sequential and complete | "A step-by-step monthly payment plan" |
| | Proven | Evidence (research or case study) exists | "A proven method used by 2,400+ readers" |
| | Data-backed | Institutional research supports the claim | "Data-backed strategies from Federal Reserve research" |
| | Measurable | The outcome can be tracked in numbers | "Measurable progress every month" |
| | Tested | The method has been used and verified | "Tested across 50+ debt payoff scenarios" |
| **2 — Ease/Accessibility** | In [specific time] | You have measured the time accurately | "Set up in 90 seconds" |
| | Without [primary barrier] | The tool genuinely removes this barrier | "Without building a spreadsheet from scratch" |
| | Even if [common limitation] | The limitation is honestly accounted for | "Even if you're starting from zero" |
| | All you enter is | The input is genuinely that simple | "All you enter is your balance, rate, and payment" |
| | The rest is automatic | The tool genuinely automates the rest | "The calculator does the rest" |
| | No [feared requirement] | The feared thing is genuinely not required | "No finance degree required" |
| | Already done | The reader completed relevant work in the post | "Using the numbers you already calculated" |
| **3 — Safety/Reversibility** | Free | Genuinely free with no hidden cost | "The template is completely free" |
| | No credit card required | There is no payment step in the opt-in | "No credit card required — just your email" |
| | Unsubscribe anytime | The unsubscribe mechanism works immediately | "Unsubscribe link in every email" |
| | Full refund | Refund policy is unconditional within the stated period | "Full refund within 30 days" |
| | No questions asked | The refund truly requires no justification | "No forms, no questions" |
| | Yours forever | The product does not expire or require a subscription | "Download once, yours forever" |
| | No strings | There are no hidden commitments | "No strings — the free version does everything this post describes" |
| **4 — Insider Access** | What most people miss | You've identified a genuine knowledge gap | "What most people miss about compound interest thresholds" |
| | The real reason | You're revealing a non-obvious mechanism | "The real reason your budget fails by week 3" |
| | What [authority] won't tell you | The gap is genuine, not conspiratorial | "What your bank won't tell you about overdraft fee alternatives" |
| | Behind the numbers | You're showing the math beneath a claim | "Behind the numbers: what 22% APR actually costs per day" |
| | The part nobody explains | You're filling a genuine explanatory gap | "The part nobody explains about Roth IRA income limits" |
| **5 — Genuine-Math Urgency** | Every month you wait | The cost of delay is calculable | "Every month you wait costs $146 in interest" |
| | By this time next year | The timeline makes the outcome tangible | "By this time next year, you'll have paid $1,752 in interest — or $0" |
| | Right now, your [X] is | The current state has a measurable cost | "Right now, your checking account is earning 0.01% while inflation runs at 3.2%" |
| | The difference between starting today and next month | The gap is calculable | "The difference: $146 and one month closer to done" |
| | While you're reading this | The cost is ongoing in real time | "While you're reading this, your $8,000 balance just accrued another $4.82 in interest" |
| **6 — Identity Aspiration** | The kind of person who | Reader has demonstrated intent through action | "You're the kind of person who reads the whole post — that's not common" |
| | Ready to | Reader has shown readiness signals | "If you're ready to see your real numbers" |
| | Decided to | Framing the action as a decision already made | "You've already decided to figure this out — the tracker makes it concrete" |
| | Building | Framing finance as construction, not deprivation | "You're building something here — a version of your money that works" |
| | Your plan | Activating ownership of the outcome | "Your plan, your numbers, your timeline" |
| | In control | The shift from reactive to proactive | "For the first time, you're in control of the math — not the other way around" |

---

# SECTION 6 — POST PRODUCTION WIREFRAME TEMPLATE

*Strip narrative commentary. Use as copy-pasteable structure. Adapt dollar amounts and keyword for each new post.*

---

## PRE-WRITING PHASE

```
[Competitor Audit] → Record average word count of top 5 competitors
→ Apply multiplier: ×1.20 medium gap / ×1.15 low gap / ×1.25 high gap
→ Set binding word count target in Article Brief before writing begins

Example: Top 5 avg 2,800 words × 1.20 = 3,360 → TARGET: 3,400 words

[Visual Benchmark] → Competitor avg visuals + 2 = your minimum
Example: avg 4 visuals → TARGET: 6 visuals minimum

[Title Scorecard] → Working title → Score against 10-point scorecard → Must hit 8/10 before advancing
Example: "How to Pay Off $30,000 in Student Loans Fast (Even on $45K)" → 8/10

[GEO Pre-Plan] → Name: lead statistic | named sources needed | definitional sentences required | direct answer placement
Example: Lead stat: Federal Reserve student loan balance data
Sources needed: Federal Reserve, Dept. of Education, BLS
Definitions required: debt avalanche, debt snowball, income-driven repayment
```

---

## POST STRUCTURE

| Section Type | Word Count Target | Verbatim Hook / Rule |
|---|---|---|
| **Introduction** | 150–200 words | Hook = named statistic with named source + stakes in dollars. *"The average student loan borrower owes $28,950 (Federal Reserve Bank of New York, Q4 2023). On a $45,000 salary — roughly $3,375/month take-home — that debt feels like a permanent roommate."* Promise = exact monthly plan, dollar by dollar. Roadmap = brief TOC reference only. |
| **YMYL Disclaimer Callout** | 40–60 words | Light yellow background, amber left border. Must include: topic scope + "not personalized financial advice" + "consult a financial advisor for your specific plan" + "all numbers current as of [Month Year]." |
| **H2: What $[X] in [Debt] Actually Costs You** | 400 words | GEO sentence required: cite federal rate + total cost calculation with named source. *"At 6.8% interest — the current federal student loan rate as of 2024 — a $30,000 loan on a standard 10-year repayment plan costs $41,440 total, meaning you pay $11,440 in interest alone (Federal Student Aid, Department of Education)."* Visual required: line chart showing minimum-payment timeline vs accelerated timeline. Setup-Chart-Interpretation format. Specific numbers in first 300 words (Trust Checkpoint 2). |
| **H2: The $[Salary] Budget Breakdown** | 500 words | Visual required: monthly budget table with actual dollar amounts. Apply 50/30/20: calculate $needs / $wants / $savings+debt from stated salary. Show specific line items where extra payment money comes from (not "cut expenses"). Money Dominoes callout required: name the chain reaction from one small cut to final investment outcome with dollar amounts at each node. |
| **H2: [Strategy A] vs [Strategy B] — Which Fits Your Psychology** | 500 words | GEO definitional sentence for each method. Visual required: comparison table (Strategy / Total Interest Paid / Time to First Account Closed / Time to Full Payoff / Best For). Emotional framing required: acknowledge this is math AND psychology. Decision rule required: name the specific condition that determines which option the reader should choose. |
| **H2: The Month-by-Month Payoff Plan** | 600 words | Visual required: worked-example table (months 1, 3, 6, 12, 24, 36, 48 — balance remaining / cumulative interest paid / cumulative principal paid). Real numbers from salary budget section above. Milestone celebration at month 12. Section-level caveat required: name the rate assumption and point to an external calculator for personalized numbers. |
| **H2: [X] Ways to Find an Extra $[Y]–$[Z]/Month** | 400 words | Numbered list. Each item must have a dollar estimate. NOT generic — must be specific with source. Visual required: horizontal bar chart of savings by strategy, sorted descending. |
| **H2: What Happens After Payoff — The Money Dominoes Chain** | 300 words | Visual required: flow diagram showing payoff → emergency fund → employer match → Roth IRA → taxable investing. Dollar amounts required at each node. Purpose: addresses "what's the point" motivation gap that keeps people from starting. |
| **FAQ Section** | 300 words (4 questions min) | Source questions from People Also Ask for target keyword. Each answer: direct answer in first sentence, then 2–3 sentences of context. Label **[FAQ SCHEMA REQUIRED]** above section heading in draft. |
| **Conclusion** | 150 words | Single next step ONLY — NOT a summary. Name the exact action, the exact tool or resource, and the time it takes. *"Open your loan servicer's website right now. Write down your balance, interest rate, and current monthly payment. Then come back here and calculate your accelerated timeline using the budget breakdown in Section 2. That's it — one action, today."* |

---

## POST-WRITING QA GATE

| Check | Standard |
|---|---|
| Voice consistency | All 6 ELI12 attributes verified |
| Jargon | No unexplained terms — all defined on first use |
| E-E-A-T | Author experience referenced, sources named, disclaimer present |
| GEO audit | 5+ statistics with named sources · 3+ "according to" attributions · definitional sentences for all key terms |
| Visual count | Competitor benchmark + 2 minimum |
| Reading level | Grade 7 (Hemingway App) |
| Mobile | All tables render without horizontal scroll at 375px. All charts legible at 375px. |

---

*End of AF Playbook Compressed Sections — v15 Compression Pass*
*Sections compressed: 4.1-A, 4.1-B, 4.1-C, 5.1–5.10 (Differentiation Protocol), Section 8, Section 6*
*Operational data preserved: 100% | Estimated word reduction from source: ~13,500 words*
