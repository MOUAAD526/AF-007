# Hero-Image Style Review — Designer + AI-Prompt Pass

Methodology: I'm grading each style on **(a) composition / hierarchy, (b) typography & contrast, (c) color & balance, (d) AI-prompt failure modes** (text-in-shape leakage, word breaks, empty boxes, hex-as-text, etc.), and giving you a concrete fix per item — both a **design fix** (what should change visually) and a **prompt fix** (what to add/remove/clamp in the generation prompt).

There are several recurring root causes I see across the whole set. Worth fixing globally first because they kill ~70% of the issues in one go:

### Global / cross-style issues (fix these once, half the styles improve)

1. **Empty containers/boxes/circles.** Whenever the prompt mentions a "card", "panel", "circle", "envelope", or similar shape with no content described, the model renders an empty primitive. **Fix:** never request an empty container. Either (a) describe what's *inside* it (icon, mini chart, percentage, tally marks, glyph), or (b) ask for it as a *background graphic element* with low opacity, off-canvas, or behind text — not as a foreground card.
2. **Hex codes leaking as text.** When you tell the model "use color #FDA050", it sometimes prints `$FDA,050` as if it were a dollar amount. **Fix:** never put a raw hex in a prompt next to numeric copy. Use named colors ("warm amber", "deep navy") or move hex codes to a separate "palette:" block and keep them away from the headline copy.
3. **Font-name leakage into visible text.** "Inter SAVINGS ACTION PLAN" (Style 2) means the model treated the font name as part of the badge text. **Fix:** isolate type instructions ("Typography: Inter Bold for headline") in a labeled block; never inline the font name adjacent to a string the model is supposed to render.
4. **No-text-in-shape ignored.** The model regularly stamps "ZERO" (or whatever the nearest semantic concept is) inside otherwise blank shapes. Negative instructions ("no text in shapes") are unreliable. **Fix:** instead of saying "no text", give the shapes a *positive* job — e.g. "fill each colored box with a small line-icon (cart, gas pump, house)". Empty shapes will always be filled with something; choose what.
5. **Word-break / hyphenation errors** ("trad eoff", "Coppins"). The text is being rasterized at a fixed canvas width, so a long line wraps mid-word. **Fix:** keep each headline line ≤ 18 characters, force line breaks with explicit `\n` or `<br>` markers in the prompt, and avoid words >9 chars in a single line. Pre-wrap the copy yourself rather than letting the model do it.
6. **Decorative footer bars / border lines.** Several styles end with a thick blue or orange bar at the very bottom edge — it's nearly always "leftover" from a prompt asking for a colored progress bar or accent stripe. **Fix:** if you want an accent stripe, anchor it to the *headline* (under the H1) — never to the canvas edge — or remove it entirely.
7. **Repeated headline / phrase doubling.** Style 6 prints `10/10/80 Rule` twice. The model is hallucinating from the prompt structure where the same value appears in both title and subtitle. **Fix:** make sure your title and subtitle have *different* copy in the prompt; if they're the same intent, drop one.

---

## Per-style review

### Style 1 — Zero Shock — PASS (with fixes)
**What works:** the oversized `$0` as a background graphic texture is a strong concept. Amber accent under the orange headline is on-brand. Left-side eyebrow → H1 → kicker hierarchy is correct.

**What's broken:**
- The `$0` glyph is **cropped on both sides** — top of the `$` is cut, the `0` exits the right edge. It looks like a sizing accident, not a deliberate bleed. A graphic-texture treatment should bleed *intentionally*, with one anchored side.
- The amber stripe is **way too thick** and sits awkwardly across the lower third — it cuts the `$0` at its waistline, looks like an underline that escaped. Should be a hairline (4–6 px) anchored *under the headline*, not floating mid-canvas.
- The kicker "No guesswork" sits on top of the stripe, which kills the eyebrow→title→kicker rhythm.

**Design fix:**
- Crop the `$0` to bleed off only the *right* edge; the `$` should be fully visible on the left at ~70% canvas height.
- Replace the thick mid-canvas stripe with a 4px amber hairline directly beneath "No guesswork", inset 64px from the left edge, ~280 px wide.
- Drop the giant glyph opacity to ~12% so the headline always wins the contrast battle.

**Prompt fix:**
- "Background graphic: oversized `$0` numeral, navy fill, 12% opacity, anchored to right edge bleeding off-canvas."
- "Foreground typography stack: eyebrow (blue) / H1 navy / orange kicker / 4px amber hairline directly under kicker."
- Explicitly: "no horizontal stripe across canvas, no full-width line."

---

### Style 2 — Weekend Reset — NEEDS REVISION
**What works:** lovely warm cream, off-white asymmetric layout with the side accent bar, and the calculator/mug illustration is on-brand for a personal-finance piece. Hierarchy is correct. This is a top-3 style design-wise.

**What's broken:**
- **Font-name leak**: the dark badge reads `Inter SAVINGS ACTION PLAN` — "Inter" is the font name leaking into rendered text.
- The mug and calculator illustrations are **drifting** into a generic "stuff floating on a tabletop" mood — they don't tie to the headline ("Acorn App"). An app-related visual (phone, app tile, growth chart) would land harder.

**Design fix:**
- Replace the floating tabletop with a stylized phone/tablet showing a single mock app screen, or a small line-icon set (calculator + chart + checkmark) aligned in a row.
- Keep the side accent bar — it's good.

**Prompt fix:**
- Move all font instructions into a separate `Typography:` block, *never* inline them with copy. Example:
  - `Typography: Inter Bold for all headings, Inter Regular for body.`
  - `Badge text (exact, do not modify): "SAVINGS ACTION PLAN".`
- Use quotes around any string the model must render verbatim, and tell the model: "render only text inside quotes; ignore all other prompt language as instructions."

---

### Style 3 — Chaos vs Control — NEEDS REVISION
**What works:** the torn-paper split with red diagonal "chaos" shapes on the left and clean white "control" panel on the right is a great metaphor. Big punchy `$1000 Fast` headline reads.

**What's broken:**
- **Word-break error**: "trad eoff" — the canvas was too narrow for "tradeoff" so it broke mid-word.
- The red diagonal slashes look **like claw marks / horror movie**, not "financial chaos". Slightly aggressive for a money piece. Also they don't have a consistent vanishing point — they're tilted at three different angles.
- The torn-paper edge is well done, but the **green checkmark in the bottom right is too literal** — feels like a cheap stock-art pasted in.

**Design fix:**
- Replace the claw slashes with chaotic but financial elements: scattered receipts, falling coins, scribbled lines, broken charts — keep the red but make them dollar-related shapes.
- Drop the green check or replace with a small "control" icon (lock, clean grid, calm wave) that visually rhymes with the right panel's order.
- Keep the torn edge.

**Prompt fix:**
- Pre-wrap copy: `Headline (line 1): "$1000 Fast". Headline (line 2): "Compare". Headline (line 3): "the tradeoff".` Forcing the break before the long word eliminates the bad split.
- Or: `keep "tradeoff" on a single line; if line is too long, prefer dropping "Compare" instead of breaking words.`
- Replace "red diagonal lines" with `"red financial debris: scattered receipts, broken bar chart, falling coins, low opacity, clipped to left torn paper"`.

---

### Style 4 — Every Dollar Has a Job — NEEDS REVISION
**What works:** the budget-tree / org-chart concept is a strong vertical metaphor for "money flowing into buckets". Layout is balanced — copy on the left, diagram on the right. Color-coded buckets look clean.

**What's broken:**
- **Hex-leak**: top card reads `$FDA,050`. The model read a color hex (`#FDA050` or similar warm amber) and rendered it as a dollar amount. This is a known prompt bug.
- **Negative-space failure**: the three colored buckets all read `ZERO`. You told the AI "no text in shapes" and it inserted "ZERO" as a placeholder.
- The single small green box hanging below the tree looks like a leftover / orphan node. Either unify the structure (two rows of three) or delete it.

**Design fix:**
- Top card: actual income figure, e.g. `$5,050` in white on navy.
- Three buckets: replace `ZERO` text with **icons + dollar value + small label** (e.g. blue: 🏠 $1,500 Rent / orange: ⛽ $300 Gas / green: 💰 $250 Save). Now each bucket has a job.
- Drop the orphan green box, or extend the tree so each bucket flows into a sub-allocation.

**Prompt fix:**
- Move palette out of the inline copy. Instead of `colors: #FDA050, #2563EB, #16A34A`, write:
  - `Palette (do not render as text): warm amber, royal blue, success green, deep navy.`
- For the buckets:
  - `Bucket 1 (blue): icon=house, label="Rent", value="$1,500".`
  - `Bucket 2 (amber): icon=gas pump, label="Gas", value="$300".`
  - `Bucket 3 (green): icon=piggy bank, label="Save", value="$250".`
- Top card: `Header card text (exact): "$5,050"`.
- "No text inside shapes" doesn't work; **always describe what is inside instead.**

---

### Style 5 — Premium Dark Cover — NEEDS REVISION
**What works:** rich navy background, a faint horizon line, eyebrow + H1 + kicker stack reads cleanly. The orange "No guesswork" CTA pops perfectly.

**What's broken:**
- **Floating empty circle** on the right with a single orange dot. Reads as either "moon", "loading spinner", or "blank avatar". It contributes nothing semantic.
- The thick orange bar at the bottom edge is the same "footer stripe" issue as Style 1 — it looks like a stuck progress bar.

**Design fix:**
- Replace the empty circle with one of:
  - **Concentric ring chart** (3 nested circles) showing 100/30/7 envelope split.
  - **A stylized envelope icon** (since the headline is "100 Envelope Challenge").
  - **A tally/grid of 100 small dots** arranged in a circle, with a few amber-filled to suggest progress.
- Remove the bottom-edge orange stripe entirely. The eyebrow/headline stack is enough hierarchy on its own.

**Prompt fix:**
- Replace `"large dark circle on right with single orange dot"` with `"100-dot grid on right side, 7 dots filled amber, 93 dots dark navy outline, arranged in a 10x10 square, low-key, decorative not dominant"`.
- Add: `"no decorative bars or lines along canvas edges; keep edges clean."`

---

### Style 6 — The Missing Money — NEEDS REVISION (your call of "PASS" is too generous)
**What works:** the giant brown question-mark watermark is a strong concept for a piece called "The Missing Money". Cinematic.

**What's broken:**
- **Repeated line**: `10/10/80 Rule` then `10/10/80 made clear` — visual stutter. Kills credibility.
- **Contrast is poor**: the brown question-mark watermark sits behind white text, but it's at the same value as the surrounding navy in places — text reads OK but the `?` dot at the bottom of the canvas competes with the orange "Real clarity".
- The amber underline beneath `Real clarity` is **the right idea** but it's the same exact width as the headline above, which is too much; should be ~50% width and centered.
- **Vertical rhythm is off**: too much empty space above the eyebrow, too little below the kicker. Looks bottom-heavy because of the question-mark dot.

**Design fix:**
- Make the headline a single line: `10/10/80 Rule` OR `10/10/80 made clear` — pick one. If the rule needs explanation, use `10/10/80 Rule` as H1 and a small `Save 10. Invest 10. Live on 80.` as a one-line subtitle.
- Drop the `?` watermark to ~8% opacity; right now it's around 18% and competes.
- Center the headline block vertically (move it up ~80 px) so the `?` dot has room to breathe and doesn't crowd "Real clarity".
- Trim the amber underline to the width of "Real clarity" only.

**Prompt fix:**
- `Headline (single line): "10/10/80 Rule"`. `Subtitle: "Save 10. Invest 10. Live on 80."` Don't repeat the phrase.
- `Background watermark: oversized "?" glyph, 8% opacity, brown #6B4C2A, anchored center but allowed to bleed top and bottom; do not overlap headline text bounding box.`

---

### Style 7 — The 48 Hours — NEEDS MAJOR REVISION (your "very bad" is correct)
**What works:** the concept of using "48 HOURS" as a graphic typographic background is strong on paper.

**What's broken:**
- The `48 HOURS` typography is **so dominant** it has eaten the canvas. The actual headline ("Coppins headline with breathing room") is jammed into the bottom-left corner with no breathing room — ironic given the placeholder copy literally says "with breathing room".
- The orange `HOURS` overlaps the navy `48`'s second `8` and the result reads like overlapping LP jacket art — confusing, not striking.
- "Coppins" is a **placeholder name leak**, similar pattern to "Inter" leaking into Style 2 (placeholder text leaked from the prompt template).
- The huge translucent navy `O` at bottom-right is a third typographic element competing with the other two.

**Design fix:**
- Pick **one** typographic background — either `48` cropped to bleed top-left, OR `HOURS` running across the bottom — not both layered.
- Headline area should be **minimum 40% of canvas**, anchored top-left or bottom-left, with at least 64 px of clear space all around.
- Reduce background type opacity to ~15% navy / no orange overlay.
- Replace placeholder "Coppins headline with breathing room" with a real testable headline.

**Prompt fix:**
- `Background typographic graphic (single element only): "48" in extra-bold, navy, 18% opacity, anchored top-right, bleeding off canvas.`
- `Foreground stack (must dominate): eyebrow "FAST MONEY PLAN", H1 (real headline, max 4 words per line), kicker "No guesswork".`
- Strip the prompt of any placeholder names ("Coppins", "Inter", "Lorem") — these *will* leak.
- `Foreground area must occupy at least 50% of canvas with 64px padding; background graphic must not overlap foreground bounding box.`

---

### Style 8 — The Magazine Cover — PASS (legit best in show)
**What works:** warm cream background, ghosted `$` glyph at low opacity behind the type, dark navy badge ("ADULT MONEY GUIDE") with amber underline, then a clear H1 → number → orange kicker stack. Editorial, calm, trustworthy. Type is large but not screaming. **This is the template the others should look up to.**

**Minor improvements:**
- The amber underline under the badge is good, but slightly too short — extend it ~10% so it reaches the right edge of "GUIDE".
- The `$` watermark is positioned just right (right side, partial bleed). Could go even lower-opacity (~10%) to add more elegance.

**Use this as the master template** and reverse-engineer it: the layout grid (badge → headline → number → kicker), the warm cream + navy + amber palette, the ghosted-glyph background, and the no-decoration rule (no stripes, no orphan shapes) are all working in concert.

---

### Style 9 — Empty boxes on right (no image attached, working from your note)
Same root cause as Style 4/15: prompt asked for "cards" or "boxes" with no content. **Prompt fix:** describe contents — icons, mini-charts, tiny percentages, glyphs. Never request an empty container.

---

### Style 10 — PASS (no image attached)
Hold the line. No changes recommended without seeing it.

---

### Style 11 — Deep Ocean Trust — PASS (your 5.5/10 is fair)
**What works:** unified dark navy panel, banded horizontal depth gradient, clean type stack with the orange "No guesswork" kicker. No empty shapes. The horizontal banding is a clever solution to the previous "floating circle" problem.

**What's broken:**
- It feels **flat and dated** — like a corporate insurance brochure from ~2013. The bands don't have enough distinction (the three navy values are too close together to read as deliberate stripes). At a glance you see one solid panel.
- No graphic anchor. There's an eyebrow, a headline, and a kicker — and then literal empty space below. Compare with Style 8 which has the ghosted `$` doing background work.
- The orange hairline at the very bottom is the same "footer stripe" issue. Drop it.

**Design fix:**
- Either (a) drop in a low-opacity `$` or `?` watermark like Style 8 to give the canvas a graphic anchor, or (b) increase the contrast between the depth bands so they read as deliberate horizontal layers (lighten the top band ~10%, darken the bottom band ~10%).
- Add a small icon — thermometer or AC unit — at low opacity behind/beside the headline since the topic is "AC Temperature".
- Remove the bottom orange hairline.

**Prompt fix:**
- `Background: deep navy with three distinct horizontal depth bands, top band lightest, bottom band darkest, 8% lightness delta between bands.`
- `Background graphic anchor (low opacity 12%): stylized thermometer or snowflake glyph, right side, partially bleeding off canvas.`
- `No edge stripes or footer bars.`

---

### Style 12 — Cerulean Clarity — PASS (with fix)
**What works:** clean two-panel split, big `$278` on the left in white-on-blue, eyebrow / H1 / kicker stack on the right. Good information hierarchy — number on one side, narrative on the other. The thin lighter-blue band between panels is a nice editorial touch.

**What's broken:**
- The **thick blue line at the very bottom** is the same canvas-edge stripe issue you flagged. Drop it.
- The right panel is *very* white — needs at least one accent (a small icon, an underline, or a callout chip). Right now the eyebrow is the only piece of color besides the headline.
- "Choose calmly" has slightly inconsistent kerning vs the headline — not a deal-breaker but visible.

**Design fix:**
- Remove the bottom blue stripe.
- Add a small amber hairline under "SAVINGS DECISION GUIDE" (matching Style 8's badge pattern).
- Optionally: a tiny suitcase or plane glyph at ~12% opacity on the right panel since topic is "Travel Savings".

**Prompt fix:**
- `No bottom edge stripe.`
- `Right panel: eyebrow with 4px amber hairline below it, then H1, then orange kicker, plus 12% opacity travel-related glyph anchored bottom-right.`

---

### Style 13 — Blueprint — NEEDS REVISION
**What works:** the blueprint grid background is a strong concept for a "saving for a house" piece — visual metaphor matches subject.

**What's broken:**
- **Right card is literally a blue rectangle with one orange dot.** Empty container problem. The dot looks like a typo, not a design choice.
- The grid lines are good but very uniform — a real blueprint has a denser sub-grid (every 5 squares) and faint axis labels.
- "Saving for a House" text is fine but could use a small house glyph in the empty card area.

**Design fix:**
- Fill the right card with a **stylized house floor plan** — a blueprint of a small home: rectangles for rooms, dotted door swings, dimension lines. This is on-theme and replaces the empty box with content.
- Add a denser secondary grid (every 5 lines lighter, every 25 lines slightly stronger) for authenticity.
- Possibly add a tiny "scale 1:50" label or compass rose in a corner.

**Prompt fix:**
- Replace "blue card with orange dot on right" with `"stylized architectural floor plan of a small house, line drawing style, white-on-blueprint, occupying right 40% of canvas, includes 2-3 rectangular rooms, door swings, and dimension annotations."`
- `Background: blueprint grid, 25 vertical / 18 horizontal main lines, every 5th line slightly bolder, white at 25% opacity on deep blueprint blue.`
- `No empty rectangles.`

---

### Style 15 — The Showdown — NEEDS REVISION
**What works:** clean cream canvas, three product-comparison cards on the right, clear "Choose calmly" CTA. The colored top bars give visual variety.

**What's broken:**
- **Three cards are empty white boxes with colored top bars** — the comparison concept is broken without content. Same empty-container failure as Styles 4, 9, 13.
- Headlines on the left are **too small relative to the cards** — eye goes to the cards first, but then there's nothing to read in them, so it bounces back to the headline. Hierarchy inversion.
- Lack of any iconography or numerical data in the cards.

**Design fix:**
- Each card should have: **(1) name** ("Brand A"), **(2) icon**, **(3) price**, **(4) one-line USP**. Make it a real micro-comparison.
- Bump headline size by ~20% so it reads as the page's primary focal point.
- Use blue/orange/green only as the *top accent bar*, but apply a tiny tint of the same color to the price line inside each card (subtle). This visually unifies card content with header.

**Prompt fix:**
- `Three comparison cards on right (each card MUST contain): icon at top, brand label "Brand A/B/C", large price "$15", "$22", "$8", and a one-line tagline ("Cheapest pack", "Best per kg", "Bulk only"). No empty cards permitted.`
- `Headline must be at least 1.4x the height of card text.`

---

### Style 16 — The Real Story — NEEDS REVISION
**What works:** soft cream background, dark badge, side accent rule, big quote-style headline. The editorial mood is right for "Real Money Story".

**What's broken:**
- **Empty cream circle** on the right — same floating-shape problem.
- **Literal quotation marks** rendered into the headline text: `'Withdraw Savings Feel less stuck'` and `Next step'`. The model interpreted the prompt's `"...quoted headline..."` directive as part of the content.
- The kicker `Next step'` has only one quote because the closing quote leaked but the opening one didn't — the asymmetry is jarring.
- "Withdraw Savings / Feel less stuck" reads like two unrelated lines mashed together. Not a coherent quote.

**Design fix:**
- Replace the empty cream circle with **a portrait silhouette** (since this is supposedly a "Real Money Story" — a person), or with a stylized speech-bubble icon, or a small chart.
- Decide: do you want quote marks at all? If yes, render them as a **single decorative oversized "❝" glyph** in amber at the top-left (a magazine pull-quote treatment). If no, strip them entirely.
- Rewrite the headline so it's a real one-liner — e.g. `"How I withdrew $5K and stopped feeling stuck."`

**Prompt fix:**
- Don't put the headline copy in quotes inside the prompt — the model renders the quotes literally. Use a labeled block:
  - `Headline (render this exact text, do not include any quotation marks): How I withdrew $5K and stopped feeling stuck`
- `Decorative element: large amber "❝" glyph in top-left, no closing quote, used purely as a visual accent.`
- Replace the empty circle with `"abstract grayscale portrait silhouette of a person from chest up, low contrast against cream background, occupies right 25% of canvas"` or `"low-opacity speech bubble glyph"`.

---

### Style 17 — Empty boxes on right (no image attached)
Same fix as Styles 4 / 9 / 13 / 15: every container needs content. Define icons + values for each box in the prompt. Don't ask for empty cards.

---

### Style 18 — Same empty-box pattern (no image attached)
Same fix. This is by far the most common single failure across the 19 styles — I'd estimate it's responsible for ~60% of the "needs revision" verdicts. Worth a global prompt-template patch.

---

### Style 19 — The Rule — PASS (with fixes)
**What works:** unified dark navy canvas, headline + orange kicker + amber underline, then a horizontal stacked bar chart underneath. The bar visualization actually communicates the 50/30/20 (or whatever ratio) rule cleanly. Much better than a split panel.

**What's broken:**
- **Thick blue stripe at the very bottom edge** — the now-recurring "footer bar" bug. Drop it.
- The stacked bar has 4 segments but no labels or percentages; viewer can't read the rule. Add tiny labels on or above each segment ("50%", "30%", "15%", "5%" or similar).
- "Money Saving Chart $5,050" reads as two glued-together phrases. Should be `Money Saving Chart` as eyebrow OR `$5,050` as the H1 — not both as same-weight headline text. (This is an issue you'd flagged for Style 19.)

**Design fix:**
- Remove the bottom-edge blue stripe.
- Convert "Money Saving Chart" into a small eyebrow above and `$5,050` becomes the actual H1.
- Add segment labels (small white % or category names) on or above each bar segment.
- Optionally add a thin amber callout line pointing to one specific segment ("← keep this").

**Prompt fix:**
- `Eyebrow: "MONEY SAVING CHART".`
- `H1: "$5,050".`
- `Kicker: "Real clarity" in amber.`
- `Below kicker: stacked horizontal bar chart, 4 segments (amber 40%, blue 25%, green 20%, dark-navy 15%), each segment labeled with its percentage in small white type.`
- `No edge stripes; no footer bar.`

---

## Priority order for fixes (if you do them in waves)

1. **Wave 1 — global prompt template fixes** (1 prompt edit, fixes ~half the styles): kill empty containers, isolate hex codes, isolate font names, ban edge stripes, pre-wrap headlines.
2. **Wave 2 — Style 7 rebuild**: this is the only style that's structurally broken (composition, not just AI artifacts).
3. **Wave 3 — Styles 4, 13, 15, 16**: empty-box / placeholder-text fixes via the new global template.
4. **Wave 4 — Styles 1, 5, 11, 12, 19**: minor decorative cleanup (drop edge stripes, replace floating circles with content-bearing graphics).
5. **Wave 5 — Style 6**: rewrite copy to remove the doubled headline, then dial back watermark opacity.

## Master template recommendation

Style 8 is the clear template winner. Its formula:

- Warm cream OR deep navy canvas (pick one of the two backgrounds for every variant; consistency).
- **Eyebrow badge** (dark pill or framed text) with **amber underline**.
- **H1** in navy/white, max 3 words per line, max 2 lines.
- **Number/value line** (when relevant) at H1 weight or larger.
- **Orange kicker** (single line, action-oriented: "No guesswork", "Real clarity", "Choose calmly").
- **Background watermark glyph** at 10–12% opacity, anchored to a single edge with deliberate bleed.
- **No edge stripes. No empty containers. No floating shapes.**

If you bake this skeleton into your prompt template and the per-style variants only swap the watermark glyph + the topic copy, you'll get consistency and dodge the failures above in one pass.
