# AF WRITING PLAYBOOK — COMPRESSED PRODUCTION REFERENCE
**Version:** v15 Compression Pass | **Format:** Operational Rules + Swipe Files Only
**Purpose:** Load this alongside the core playbook. All pedagogical narrative removed. 100% of operational data preserved.

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


# Section 4.2 reader personas

**Restore at minimum:**
- The two-layer persona model: reader persona and voice persona must both be selected before drafting.
- The four reader personas: Overwhelmed Starter, Debt-Stressed Adult, First-Gen Builder, Optimizing Grower.
- For each persona, keep: life situation, emotional state, what keeps them reading, what makes them bounce, vocabulary swaps, and any non-negotiable writing constraint.
- The rule that one primary reader persona must be chosen before drafting, with up to one or two secondary personas only if needed.
- The persona decision-tree rule that selection must be logged in the Article Brief.

**Why it matters:**
Without this block, the compressed file tells the writer to choose persona but does not preserve the actual persona system used to make that choice.

# Section 4.3 post anatomy and visual placement rules

**Restore at minimum:**
- The 9-component post anatomy map.
- Word-count targets and jobs for each component: title/H1, meta description, introduction plus answer block, table of contents, body sections, visuals, conclusion, CTA block, author bio.
- The mandatory 3-part conclusion structure: single takeaway, 24-hour action, thesis connection.
- The first-meaningful-visual rule, visual density rule, callout-box budget, chart setup-chart-interpretation sequence, monetization-distance rule, and one-dominant-element-per-viewport rule.
- The visual placement map by post type.

**Why it matters:**
This is the missing bridge between structure rules and actual on-page article assembly.

# Section 4.4 title mastery system 

**Restore at minimum:**
- The two-title workflow: SEO title tag and on-page H1 are separate assets.
- The load rule for the Hooks and Title Formulas companion file.
- The hard gate that every session must produce at least 10 title options before approval.
- The requirement to use at least 5 different hook categories before scoring titles.
- The 7 title formulas summary.
- The 10-point title scorecard and the minimum publish threshold.
- The title A/B testing workflow and tracking fields.

**Why it matters:**
The compressed file is strong on drafting, but title generation is still a required pre-draft gate in the full playbook.

## Patch 04 — restore Section 4.5 intro frameworks and writing-style system

**Insert after:** `Section 4.4`

**Restore at minimum:**
- The 5 intro frameworks and the intent-to-framework matrix.
- The five AF writing styles: Tutorial, Story/Narrative, Contrarian, Data-Led, Money Dominoes.
- For each style, keep: what it is, title signals, intro framework, section architecture, word-count range, emotional register, tone-dial settings, FAQ placement, and what makes the style distinct.
- The title test and tiebreaker rule used to identify the correct style before drafting.
- The content-pairs system linking ELI12 posts with Adult Systems posts.
- The 1 Rule 1 Tool format.
- Section 4.5-B comparison and review post writing spec.
- Section 4.5-C format translation table.

**Why it matters:**
This block determines how the article should be built before the first paragraph is written.

# Section 4.6 heading hierarchy and FAQ ending rule

**Restore at minimum:**
- Character-count ranges for H1, H2, H3, and H4.
- The 3-question test every heading must pass.
- Primary-keyword, secondary-keyword, and related-term placement rules in headings.
- H2 cadence and H4 restraint rules.
- Heading formatting rules.
- The mandatory FAQ action-sentence rule: every FAQ answer must end with a specific action the reader can take within 24 hours.

**Why it matters:**
These are production-level controls that affect scanability, featured-snippet readiness, and behavioral usefulness.

# Section 4.7 on-page SEO implementation rules

**Restore at minimum:**
- The on-page SEO checklist used after drafting.
- Exact placement rules for the primary keyword across title, H1, intro, H2s, meta, slug, and image alt where appropriate.
- The answer-block and direct-answer formatting rules used for featured snippets and AI overviews.
- Any Rank Math or CMS field requirements that are part of publication readiness.
- The rules that separate reader-first phrasing from forced keyword repetition.

**Why it matters:**
The compressed file keeps broad SEO/GEO logic, but the full playbook also contains page-level implementation rules needed for publishing.

# Section 4.8 E-E-A-T, YMYL, and disclaimer implementation

**Restore at minimum:**
- Required trust signals that must appear in or around the article.
- Rules for where and how disclaimers should appear when the topic requires them.
- Any author-bio, review, sourcing, and update-signaling requirements tied to YMYL safety.
- Any rules that distinguish educational explanation from personalized financial advice.

**Why it matters:**
Section 0 preserves the top-level compliance logic, but the article-level implementation details still need to be present in the compressed file.

#Section 4.9 internal linking architecture

**Restore at minimum:**
- The internal-linking rules for pillar-to-cluster and pair-post connections.
- The live-link versus planned-link rule.
- Anchor-text and placement rules.
- Minimum internal-link expectations by post type where defined.
- Any rule that prevents adding links as generic navigation instead of contextual help.

**Why it matters:**
The compressed output contract asks for internal-link recommendations, but the deeper linking logic is still in the full playbook.

# Section 4.10 CTA and monetization architecture

**Restore at minimum:**
- CTA role by post layer and post type.
- The micro-conversion path when a reader is not ready for a hard conversion CTA.
- CTA sequencing rules tied to emotional stage.
- Product, lead magnet, and affiliate separation rules.
- Any exceptions for comparison posts and high-trust affiliate layouts.

**Why it matters:**
The compressed file keeps CTA examples, but the strategy layer that decides which CTA belongs where is still needed.

# Section 4.11 workflow and asset-production rules


**Restore at minimum:**
- The workflow stages between draft, review, approval, and publish.
- Any required companion assets, production records, or handoff requirements not already repeated in Section 0.
- Asset-output rules for visuals, briefs, ledgers, scorecards, and publication packages.
- Any notes for multi-session continuity beyond the basic session sequence.

**Why it matters:**
This turns the compressed file from a writing guide into an operational production reference.

# Section 4.12 Pinterest SEO and pin-production rules

**Restore at minimum:**
- Pinterest-specific metadata and keyword rules.
- Pin title, description, and visual-asset expectations.
- Any packaging rules that connect the blog post to Pinterest distribution.

**Why it matters:**
If the compressed file is meant to support the full production system, distribution rules cannot live only in the large playbook.

# Section 4.13 final checklist and QA rules

**Restore at minimum:**
- Final editorial checklist.
- Publication-readiness checklist.
- Any score thresholds, fail conditions, or sign-off rules not fully duplicated in Section 0.
- Any post-specific QA checks for links, metadata, schema, visuals, disclaimers, and CTA integrity.

**Why it matters:**
Section 0 defines the session gates, but the detailed verification list is still needed at the last pass.
---

# SECTIONS 5.1–5.10 — THE AF CORE DIFFERENTIATION PROTOCOL

> **⚑ Apply this framing to every production decision across Sections 5.1–5.10.**
>
> AF optimizes for comprehension over affiliate clicks. Mega-sites (NerdWallet, Bankrate, Investopedia) structure content for affiliate conversion — highlighted winner columns, product comparison tables as hero content, urgency timers, dark patterns. AF **never uses highlighted winner columns or dark patterns.** Every first visual is a teaching visual (decision tree, worked example, framework summary), never a product card. Every chart includes a "do nothing" baseline row so the reader sees the cost of inaction. Every visual is built for the reader's scenario, not an idealized one. Depth comes from original calculations, Money Dominoes chains, and real-number scenarios — not filler that serves affiliate purposes. Every paragraph must teach, prove, or move the reader toward a decision. Content refresh means a genuine content upgrade, not a date-stamp change. ELI12 voice and consistent AF frameworks (Money Dominoes, ELI12) are structural advantages mega-sites cannot replicate at scale without abandoning their business model.

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
