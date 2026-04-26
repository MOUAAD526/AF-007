# ADULTING FINANCE — COMPLETE DESIGN SYSTEM GUIDE
## The Single Source of Truth for Every Visual Decision
## Version 1.0 | March 2026
## Load this document at the start of every LLM session that involves design, visuals, or content production.

---

# HOW TO USE THIS DOCUMENT

This is the master design reference for Adulting Finance. Every time you work with an AI tool — whether that is Claude, ChatGPT, Gemini, Midjourney, or Nanabanana — paste the relevant sections of this document into your prompt context before giving any design instructions. The more of this document the AI has access to, the more consistent and on-brand the output will be.

The document is organized into nine sections. Sections 1 through 4 cover the foundational brand identity: colors, typography, spacing, and core rules. Sections 5 through 7 cover how those foundations apply to specific output types: blog visuals, hero banners, and Pinterest pins. Section 8 covers the CSS implementation for WordPress. Section 9 is a quick-reference prompt header you can copy-paste at the start of any AI session.

Read the entire document once to understand the system. After that, use it as a reference — you do not need to read it front to back every time.

---
---

# SECTION 1: BRAND IDENTITY FOUNDATION

## 1.1 What Adulting Finance Is

Adulting Finance is a personal finance blog written for adults aged 22 to 35 who feel like they missed the money class everyone else attended. The brand voice is ELI12 — Explain Like I'm 12 — which means plain language, specific dollar amounts, no assumed knowledge, and an empathetic tone that treats the reader as smart but uninformed rather than careless.

The editorial philosophy is: money decisions create life consequences. Every visual, every design choice, and every prompt you give an AI tool should serve that mission. The design should feel trustworthy, approachable, and premium — like a smart friend who happens to know finance, not like a bank or a discount coupon site.

## 1.2 The Aesthetic Reference

The closest visual references for Adulting Finance are Morning Brew's editorial graphics, Sendlane's marketing cards, and Bloomberg Businessweek's cover typography. The common thread across all three is white-dominant clean surfaces, bold confident typography, color used sparingly for meaning rather than decoration, and generous white space that signals quality.

What Adulting Finance is NOT: it is not NerdWallet (too corporate and affiliate-farm), not Dave Ramsey (too preachy and dated), not a generic WordPress finance blog (too template-heavy), and not a YouTube finance channel (too hype-heavy and clickbait-adjacent). The design system exists specifically to look different from all of these.

---
---

# SECTION 2: THE COLOR SYSTEM

## 2.1 The Official Palette

Every color decision in every visual, every callout block, every infographic, and every hero banner must come from this palette. No colors outside this list are permitted without explicit documentation of the exception and why it was made.

**Primary Colors — these four carry the brand identity:**

Dodger Blue `#3686FF` is your primary action color. It appears on links, CTA buttons, category eyebrow labels, the Type B callout accent, and bar charts when the data itself is neutral. It signals information, action, and trust.

Energy Orange `#FDA050` is your primary emotional accent. It appears on variable expense bars in budget visuals, the Type A callout accent, headline accent lines in hero banners, and any design moment where you want warmth, urgency, or human approachability. It is the amber-gold that runs through your brand.

Black Out `#222222` is your primary dark surface. It appears on all headings, dark backgrounds in split-panel layouts, the Type C completion block background, and fixed expense bars in budget visuals. It is warmer than pure black and feels premium rather than harsh.

White `#FFFFFF` is your primary background. All blog post content areas, all infographic canvases, and all card surfaces default to pure white unless there is a specific reason for a different background.

**Secondary Colors — these carry semantic meaning:**

Green Haze `#01AC36` signals success, growth, and positive financial outcomes. It appears exclusively on savings category bars, the zero-balance final row in tables, success states, and any design moment celebrating a financial win.

Red `#FF343C` signals danger, warning, and financial problems. It appears on budget floor lines in charts, over-budget warning states, and any design moment communicating risk or a problem that needs to be solved.

Grey `#808080` is your neutral muted tone. It appears on body copy, secondary labels, and supporting text that needs to recede visually.

Irrigo Purple `#9A4CFB` is a reserved accent that should be used extremely rarely — only when a visual needs a fourth color for categorical distinction. Do not use it in standard blog post visuals.

Tropical Blue `#D8E6FA` is your lightest accent, used exclusively for very light background tints in callout boxes and info containers.

**Derived Surface Colors — these are not in the official palette but are derived from it:**

Page Background `#F8FAFC` is a near-white surface used for the overall page background and for data visualization containers. It is cooler and cleaner than the cream off-whites sometimes seen in finance blogs.

Section Background `#F4F7FF` is a very light blue tint derived from Dodger Blue. It is used for the Answer Block background, the Type B callout background, and any info container that needs subtle differentiation from pure white.

Light Border `#E8EDFB` is used for all card borders, table dividers, and grid lines. It has a slight blue tint that keeps the UI feeling cohesive with the Dodger Blue accent system.

Caption Text `#9CA3AF` is used for all captions, source lines, small labels, and secondary supporting information.

Muted Text `#6B7280` is the standard body text color for all article content.

## 2.2 How to Use Colors Together

The most important color rule in this system is restraint. At maximum, any single visual should use three colors from the palette — one dark neutral, one light background, and one accent. Hero banners can use up to four colors only when each color serves a distinct semantic purpose.

The most reliable combinations for any design output are these three: first, `#222222` dark surface with `#FDA050` amber accent and `#FFFFFF` white background gives you the warm premium editorial feel that defines the brand. Second, `#FFFFFF` white background with `#3686FF` blue accent and `#222222` dark text gives you the clean modern informational feel. Third, `#0F172A` deep navy background with `#FDA050` amber accent and `#F8FAFC` near-white text gives you the dark premium fintech feel used in hero banners and the Type C completion block.

Never use Energy Orange and Dodger Blue at equal visual weight in the same design. One must be dominant and the other must be an accent. Orange carries the emotional warmth. Blue carries the functional trust. When both fight for attention, the design feels like a template.

## 2.3 Color by Use Case — The Quick Reference

For budget infographic bars, the assignment is fixed: `#222222` for fixed expenses, `#FDA050` for variable expenses, `#01AC36` for savings and goals. These assignments are consistent across every post, every visual, and every chart. Changing them for variety is not permitted because readers build pattern recognition — they begin to associate the colors with the category types across multiple posts.

For callout blocks, the assignment is: Type A Stakes callout uses `#FDA050` as the left border accent and `#FFF8F0` as the background. Type B How-To callout uses `#3686FF` as the left border accent and `#F4F7FF` as the background. Type C Completion callout uses `#222222` as the full background with `#3686FF` as the headline accent color.

For hero banners and featured images, use either the dark split-panel approach (left panel `#222222` or `#0F172A`, right panel `#FFFFFF`) or the full light approach (`#FFFFFF` or `#F7F4EE` full background). Do not create hero banners with fully saturated color backgrounds — the brand reads as editorial, not promotional.

## 2.4 What Is Banned

Never use any gradient in any visual. Never use any drop shadow heavier than `0 2px 8px rgba(0,0,0,0.06)` — and even that should be used only for fintech card elements that genuinely need depth. Never use `#0D1117` as a background color — it was used in an earlier version of the system and is now retired. Never use saturated orange outside the `#FDA050` hex — any orange that reads as "neon" or "construction cone" is wrong. Never burn a URL, blog name, or source attribution into a design graphic — source lines go in captions below images, not inside the image file itself.

---

## 2.5 The AF Blue Series — Extended Palette

The AF Blue Series is a 10-color monochromatic ramp added in Version 2.0. It extends the original palette for a wider range of visual styles — specifically for posts about credit, banking, investing, insurance, and any content where the reader needs to feel calm, safe, and confident rather than motivated or alarmed.

The Blue Series is organized into three tiers. A strict rule governs its use: **one tier per design**. Never mix colors from different tiers in the same visual. Mixing makes the ramp look like an accident rather than an intentional system.

**TIER 1 — DEEP BLUES (Dark backgrounds and anchor surfaces)**
These replace the original dark background variants (#0F172A, #0D1B2A) in blue-dominant compositions. They are more distinctly blue — the viewer immediately knows they are looking at something blue, not just dark.

- Deep Space Blue `#012a4a` — darkest, anchor backgrounds
- Yale Blue `#013a63` — primary dark surface in Blue Series designs
- Yale Blue 2 `#01497c` — secondary dark surface, card backgrounds
- Yale Blue 3 `#014f86` — subheader backgrounds, chips

**TIER 2 — MID BLUES (Accent colors, borders, data elements)**
Deeper and more sophisticated than Dodger Blue (#3686FF). Use for section accents, card borders, and decorative lines on light backgrounds.

- Rich Cerulean `#2a6f97` — strong accent, corporate blue feel
- Cerulean `#2c7da0` — primary accent in calm/trust designs
- Air Force Blue `#468faf` — secondary accent, lighter and approachable

**TIER 3 — LIGHT BLUES (Background tints and surface washes only)**
These are surface colors only. Never use as text color — contrast is insufficient. Pair with Tier 1 deep blue text or `#222222` for readable text on these surfaces.

- Steel Blue `#61a5c2` — visible surface color, card faces
- Sky Blue Light `#89c2d9` — background washes, panel fills
- Light Blue `#a9d6e5` — barely-there tint, near-white blue

**Blue Series Combination Rules (all mandatory):**

1. One tier per design — Tier 1 OR Tier 2 OR Tier 3. Never mix.
2. `#FDA050` Energy Orange is always present as the warm accent in any Blue Series design. It prevents cold/clinical feel.
3. On Tier 1 dark backgrounds: use `#FFFFFF` for headlines, `rgba(255,255,255,0.65)` for body copy, `#FDA050` for key numbers. Never use `#3686FF` on Tier 1 — the two blues fight each other.
4. On white or Tier 3 surfaces: use Tier 2 colors for borders and accent elements.
5. Never combine Blue Series Tier 1 with original dark backgrounds in the same design — they look like a mistake.
6. Never use Tier 3 colors as text — only as surface and background fills.

---
---

# SECTION 3: THE TYPOGRAPHY SYSTEM

## 3.1 The Font Pairing

Adulting Finance uses two fonts. Poppins handles all headings, display numbers, and prominent labels. Inter handles all body text, captions, supporting labels, and data annotations. Both are free on Google Fonts and should be loaded via Google Fonts API in your WordPress theme.

Poppins was chosen because its geometric letterforms feel modern and confident without being cold. The rounded geometry carries warmth that suits the ELI12 editorial voice. Inter was chosen because it is the most readable sans-serif at small sizes on screens and has excellent tabular numeral support — critical for a finance blog that shows a lot of numbers in tables and charts.

If either font is unavailable in a design tool, the fallback chain is `-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`. Never substitute a serif font, a display font, or a hand-lettered font anywhere in the system.

## 3.2 The Type Scale

The type scale is built around a clear hierarchy with five distinct levels, each with a specific role.

The Display level uses Poppins Bold at 36 to 40 pixels for desktop article H1 headings and at 120 to 260 pixels for hero banner headlines. Display type is always `#222222` unless it appears on a dark background, in which case it is `#FFFFFF` or `#FDA050` for the accent line.

The Heading level uses Poppins Bold at 28 pixels for H2 section headings, Poppins SemiBold at 22 pixels for H3 subheadings, and Poppins SemiBold at 18 pixels for H4 labels. All heading colors are `#222222` in light contexts.

The Body level uses Inter Regular at 18 pixels for all article content with a line-height of 1.7. This larger-than-standard body size is intentional — the ELI12 audience includes many mobile-first readers, and 18 pixels maintains comfortable readability on smaller screens without requiring zoom.

The Label level uses Inter SemiBold at 11 pixels, all-caps, with letter-spacing of 0.10em. This is used for category eyebrow labels, section headers in infographics, and small descriptive annotations. The color is always either `#3686FF` (blue, for primary labels) or `#9CA3AF` (gray, for secondary labels).

The Caption level uses Inter Regular at 12 to 13 pixels with `#9CA3AF` color. This is used for source lines below charts, image captions, and any supporting metadata.

## 3.3 Typography Rules

Only two font weights should appear in any single visual: one regular weight (400) for supporting text and one bold weight (600 or 700) for emphasis. Never use weight 800 or 900 in visuals — Poppins Black can be used in hero banners for the dominant headline or number, but it should not appear in standard body infographics.

All monetary amounts in any visual — whether in a bar label, a table cell, or a chart annotation — use Inter Bold or Poppins Bold with tabular numeral rendering. This ensures dollar amounts align cleanly in columns without the irregular spacing that comes from proportional numerals.

Headlines in hero banners should be a maximum of 7 words. If the headline requires more than 7 words, it needs to be rewritten, not made smaller. A smaller headline is always worse than a shorter headline.

---
---

# SECTION 4: SPACING, LAYOUT, AND VISUAL RULES

## 4.1 The Spacing System

The spacing system uses a base unit of 4 pixels. Every gap, margin, and padding in every visual should be a multiple of 4. The practical working values are 8 pixels for tight internal gaps like the space between an icon and its label, 12 pixels for small padding within compact components, 16 pixels for standard component padding, 20 pixels for comfortable card padding, 24 pixels for section padding inside containers, 32 pixels for the gap between separate components, 40 pixels for larger section separations, and 48 pixels or more for major layout zones.

The reason for this system is visual rhythm. When every spatial relationship in a design is a multiple of the same base unit, the design feels intentional and precise rather than arbitrary. Readers cannot always articulate why a design feels premium or cheap, but much of that feeling comes from consistent spatial relationships.

## 4.2 Border Radius

Border radius follows a consistent scale across all elements. Small elements like badges, tags, and pills use 4 to 6 pixels for a slightly rounded feel. Standard buttons, input fields, and small cards use 8 pixels. Standard cards and callout blocks use 12 pixels. Large cards and feature containers use 16 pixels. Hero elements and large section containers use 20 to 24 pixels. Full pill shapes (for eyebrow labels and CTA badges) use a border-radius equal to half the element height.

The most important rule about border radius is consistency — if your callout blocks use 12 pixels, your data viz containers should also use 12 pixels, and your related post cards should also use 12 pixels. Inconsistent border radii across a page create a feeling of visual disorder even when readers cannot identify why.

## 4.3 The Four Visual Functions

Every visual element in every blog post must serve one of four functions. Understanding these functions helps you decide what to include, what to cut, and what to prioritize when you are building a post.

Teaching visuals explain a concept, show a process, or make data understandable. The paycheck waterfall infographic and the weekend timeline graphic are teaching visuals. Trust visuals prove claims with sourced data. The budget summary table and bar charts with cited statistics are trust visuals. Pacing visuals give the reader a visual breath between dense text sections. A simple comparison card between two scenarios is a pacing visual. Conversion visuals move the reader toward a next step. The three CTA callout blocks are conversion visuals.

A visual that does not fit any of these four functions should be cut. "It looks nice" is not a function. "It fills space" is not a function. Every visual earns its place by serving one of these four specific purposes.

## 4.4 What Is Banned in Every Visual

No illustrations or cartoons of any kind. No stock photography of people. No 3D rendering or beveled depth effects. No gradient fills inside bars, cards, or backgrounds — the one exception is a very faint ambient radial glow at 6 to 8 percent opacity maximum in dark hero banners where it creates depth without being a visible gradient. No heavy drop shadows — the maximum is `0 2px 8px rgba(0,0,0,0.06)`. No icons inside data visualization bars. No URLs burned inside graphics. No source attributions with the blog name inside graphics — the blog name never appears inside an image file. No CSS spec text or design annotation text of any kind inside exported images. No watermarks.

## 4.5 The Placement Rules for Blog Post Visuals

The first meaningful visual in every blog post must appear within the top 20 percent of the article. This is based on Nielsen Norman Group research showing that 57 percent of viewing time occurs above the fold. The opening section must contain an answer-supporting visual before the second subheading. This single rule has the highest impact on time-on-page metrics of any structural decision.

Every post needs a minimum of four visuals with a maximum of six. The density target is one visual per 400 to 700 words. No two callout blocks should appear back-to-back without substantial body text between them. CTA callout blocks must never be placed adjacent to trust visuals like charts or data tables — the proximity between promotional and credibility content degrades both.

---
---

# SECTION 5: THE BLOG POST VISUAL SYSTEM

## 5.1 The Six Standard Visual Types

Every blog post on Adulting Finance draws from a consistent library of six visual types. Understanding each type's specifications means you can give precise instructions to any design tool without reinventing the specifications each time.

**The Paycheck Waterfall Infographic** is a vertical teaching visual that appears in the top 20 percent of tutorial and how-to posts. It shows income flowing down through color-coded category bars (fixed in `#222222`, variable in `#FDA050`, savings in `#01AC36`) until reaching a green `$0.00 Left to Assign` box at the bottom. The dimensions are 740 pixels wide by 860 pixels tall for desktop, with a mobile version at 375 pixels wide by 780 pixels tall. It is produced as a PNG file, compressed to under 150KB, and served as WebP. It is wrapped in a `.af-data-viz` Kadence container on the page.

**The Timeline Graphic** is a two-column teaching visual used for posts that involve a Saturday/Sunday or Day 1/Day 2 structure. The left column has an `#FDA050` amber header and the right column has a `#3686FF` blue header. Each column contains numbered task rows with time estimates. Dimensions are 740 pixels wide by 320 pixels tall desktop, stacking to a single column on mobile. It can be built either as a PNG or natively in Kadence Row Layout with two Info Box blocks.

**The Data Summary Table** is a trust visual built natively as a Kadence Advanced Table block — never as an image. It uses a dark navy `#222222` header row, section headers in `#F4F7FF` with `#3686FF` label text, alternating striped data rows, and a final `$0 ✓` row in `#F0FDF4` background with `#01AC36` bold green text. It always includes the `.af-comparison-table` CSS class and must be configured for mobile-responsive stacking.

**The Decision Tree Flowchart** is a teaching visual for sections with multiple branching scenarios. It uses an entry pill in `#222222` at the top, scenario nodes in `#F4F7FF` with `#3686FF` text, and color-coded action nodes where red (`#FFF5F5` background, `#FF343C` border) indicates problems, green (`#F0FDF4` background, `#01AC36` border) indicates positive actions, and blue (`#F4F7FF` background, `#3686FF` border) indicates neutral information. Connector lines are 1.5 pixels in `#D8E6FA`. Dimensions are 740 pixels wide by 500 pixels tall.

**The Bar Chart** is a trust visual for data-led sections. Bars are `#3686FF` Dodger Blue by default unless the bars carry the budget category color coding. All bars start at zero — truncated axes are never permitted. The chart title states the takeaway, not the topic. Every chart includes a setup paragraph before it and an interpretation paragraph after it. The source attribution appears as a caption below the chart image, not burned into the image itself.

**The Comparison Card** is a pacing visual built natively in Kadence as a two-column Row Layout. The left column uses `#FEF2F2` background with `#FF343C` left border accent. The right column uses `#F0FDF4` background with `#01AC36` left border accent. This is always a native block build, never an image.

## 5.2 The Three CTA Callout Blocks

Every blog post contains exactly three CTA callout blocks positioned at approximately 30 to 35 percent (Type A), 55 to 70 percent (Type B), and end of post (Type C) of the post's total length. Each has specific visual specifications that must be consistent across all posts.

The Type A Stakes Callout uses background `#FFF8F0` with a left border accent of `4px solid #FDA050`. The border radius is 12 pixels on the right corners and 0 on the left corners — this flat-left-edge treatment is the standard for all left-border callout blocks in the system. The CSS class is `.kb-callout-stakes`.

The Type B How-To Callout uses background `#F4F7FF` with a left border accent of `4px solid #3686FF`. Same border radius treatment. CSS class is `.kb-callout-howto`.

The Type C Completion Callout uses background `#222222` (Black Out) with white body text `#FFFFFF` and headline text in `#3686FF` (Dodger Blue). Nested link cards inside this block use background `#333333` with `#3686FF` link text. Border radius is 16 pixels on all corners — unlike the other two callouts, this is a full-bleed card, not a left-border accent. CSS class is `.kb-callout-completion`.

Above every CTA callout block, an HTML comment must be inserted using this format: `<!-- FUTURE CTA: [Post Topic] | Slot: [A/B/C] | Upgrade to: [specific lead magnet or newsletter] when ready -->`. This comment system exists so that when lead magnets are eventually built, every CTA location across all published posts can be found and updated systematically.

## 5.3 The Answer Block

The Answer Block is a featured snippet target that appears after the introduction and before the first H2 in every post. It provides a direct 40 to 60 word answer to the post's primary question. The visual specification is background `#F4F7FF`, left border `4px solid #3686FF`, border radius 12 pixels on the right corners, padding 20 pixels desktop and 16 pixels mobile, CSS class `.kb-answerbox`. The headline inside the block uses Poppins Bold at 15 pixels in `#222222`. The body text uses Inter Regular at 16 pixels in `#6B7280`.

This block is the most important structural element for Google featured snippets and AI Overview extraction. It should never be reworded after publishing without careful consideration, because once it is indexed it may be extracted verbatim by AI systems.

---
---

# SECTION 6: THE HERO BANNER SYSTEM

## 6.1 Required Assets Per Post

Every blog post requires two image assets produced before publication: the featured image and three Pinterest pins. These are completely separate files with different dimensions, different compositions, and different purposes.

The featured image is `1200 × 630px`, exported as JPG at high quality, compressed to under 200KB using ShortPixel or Squoosh before uploading to WordPress. It serves as the blog header, the Open Graph image for social sharing previews, the Twitter Card image, and the Google Discover thumbnail. Getting this wrong means every social share of the post shows a broken or low-quality preview.

The three Pinterest pins are each `1000 × 1500px`, exported as PNG. They follow the staggered publishing schedule: Pin A on publish day, Pin B on day 7, and Pin C on day 14. They are never embedded in the post body — they are uploaded directly to Pinterest or your Pinterest scheduler.

## 6.2 Hero Banner Design Principles

A premium hero banner has one dominant idea, one dominant visual object, and one dominant promise. The most common failure mode is including too many text elements — an eyebrow, a long headline, a subtitle, a description, a URL, and a source line all fighting for attention simultaneously. The rule is: eyebrow label, headline of maximum 7 words, one payoff line, and one dominant visual object. Nothing else.

The headline should create either a curiosity gap, a tension statement, a time promise, or a shock number. "How to Make a Zero-Based Budget" is informational but not click-generating. "Your Budget Should End at $0" creates cognitive tension. "Most Budgets Fail. This One Doesn't." creates contrarian curiosity. "Build Your Budget This Weekend" creates a time-bound promise. All of these are stronger hooks than a descriptive title.

The four proven layout structures for AF hero banners are the split panel (dark left, white right, accent divider), the full dark cover (one dominant large number or headline on dark navy), the warm editorial (cream off-white full canvas, large type-dominant layout), and the card composition (white canvas with a centered premium fintech card as the visual object).

## 6.3 Hero Banner Specification for Nanabanana

When giving design instructions to Nanabanana or any image generation tool, always specify these six things explicitly in this order: canvas dimensions in exact pixels, background color with the exact hex code, font names (Poppins and Inter), all text content with exact sizes and colors, all geometric element dimensions and colors, and the export format. Never leave any of these to the tool's interpretation — the more specific the prompt, the more consistent the output.

Always end every hero banner prompt with the Critical Rules block: no URL on canvas, no CSS spec text, no shadows except where specifically permitted, no gradients except the one permitted ambient glow, and a reminder that the image must be legible at half-size (600 × 315px).

## 6.4 The 4K Master Workflow

All hero banners and Pinterest pins should be designed at 4K resolution (3840 × 2016px for the featured image master and 2000 × 3000px for the Pinterest pin master) and then exported at the final web dimensions. Designing at 4K gives you flexibility for cropping, repurposing, and future format adaptations without quality loss. The web exports are always: `1200 × 630px` JPG for the blog and `1000 × 1500px` PNG for Pinterest.

---
---

# SECTION 7: THE PINTEREST PIN SYSTEM

## 7.1 The Three-Pin Strategy

Every post gets three visually distinct Pinterest pins, each designed around a different emotional hook. Pin A is title-focused and serves as the primary traffic driver. Pin B is data or number-focused and appeals to readers who respond to statistics and proof. Pin C is benefit or outcome-focused and appeals to readers who want to know what transformation they will experience.

The three pins must be genuinely different compositions with different headline copy, different visual emphasis, and different color balance. A color swap of the same layout is not a distinct pin — it is the same design twice and Pinterest's algorithm treats it accordingly.

## 7.2 Pinterest Pin Visual Rules

All three pins use the same brand color palette and typography as the blog visuals, but Pinterest composition follows different principles than blog content. The hook line at the very top of the pin must be legible at 236 pixels wide — the standard Pinterest feed column width on mobile. If text is too small to read at that width, it will not stop the scroll.

The top 30 percent of every pin is the most important real estate. The dominant visual hook — whether a large number, a bold statement, or a strong color block — must appear in this zone. Readers scrolling a Pinterest feed see the top of each pin before the bottom, so the hook must communicate the core promise before they scroll past.

No blog name or URL should appear burned into the pin graphic. Domain attribution is handled by Pinterest's platform attribution when the pin links back to the post.

---
---

# SECTION 8: THE WORDPRESS CSS IMPLEMENTATION

## 8.1 How to Install

All CSS below should be pasted into WordPress Admin → Appearance → Customize → Additional CSS, or into your child theme's `style.css` file. Using a child theme stylesheet is preferred for production sites because it survives theme updates. Always clear your site cache after pasting new CSS.

The Google Fonts import should go at the very top of your CSS, before any other rules. If your theme already loads Poppins or Inter, remove the import to avoid loading them twice.

## 8.2 The Complete CSS

```css
/* ═══════════════════════════════════════════
   ADULTING FINANCE — COMPLETE DESIGN SYSTEM CSS
   Version 1.0 | March 2026
   Paste this entire block into Additional CSS
   ═══════════════════════════════════════════ */

/* Google Fonts — load Poppins and Inter */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;900&family=Inter:wght@300;400;500;600;700&display=swap');

/* ─────────────────────────────────────
   GLOBAL TYPOGRAPHY
   ───────────────────────────────────── */

h1, h2, h3, h4, h5, h6 {
  font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 700;
  color: #222222;
  line-height: 1.25;
}

body, p, li, td, input, select, textarea {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight: 400;
  color: #6B7280;
  line-height: 1.7;
  font-size: 18px;
}

/* ─────────────────────────────────────
   LINKS — Clean, no underlines by default
   ───────────────────────────────────── */

a {
  color: #3686FF;
  text-decoration: none;
  transition: color 0.15s ease;
}

a:hover {
  color: #2563EB;
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 3px;
}

a:visited {
  color: #3686FF;
}

/* Links inside dark completion blocks */
.kb-callout-completion a {
  color: #3686FF;
  font-weight: 600;
  text-decoration: none;
}

.kb-callout-completion a:hover {
  color: #60A5FA;
  text-decoration: underline;
  text-underline-offset: 2px;
}

/* ─────────────────────────────────────
   RELATED POST CARDS
   ───────────────────────────────────── */

.related-posts-card,
.af-read-next-card {
  background: #FFFFFF;
  border: 1px solid #E8EDFB;
  border-radius: 12px;
  padding: 20px 24px;
  margin-bottom: 12px;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.related-posts-card:hover,
.af-read-next-card:hover {
  border-color: #3686FF;
  box-shadow: 0 2px 12px rgba(54, 134, 255, 0.08);
}

.related-posts-card .category-label,
.af-read-next-card .post-category {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  color: #3686FF;
  text-decoration: none;
  margin-bottom: 8px;
  display: block;
}

.related-posts-card .card-title a,
.af-read-next-card .post-title a {
  font-family: 'Poppins', sans-serif;
  color: #222222;
  text-decoration: none;
  font-size: 17px;
  font-weight: 700;
  line-height: 1.35;
}

.related-posts-card .card-title a:hover,
.af-read-next-card .post-title a:hover {
  color: #3686FF;
}

.related-posts-card .card-description,
.af-read-next-card .post-description {
  color: #9CA3AF;
  font-size: 14px;
  line-height: 1.6;
  margin-top: 6px;
  text-decoration: none;
}

/* ─────────────────────────────────────
   ANSWER BLOCK
   ───────────────────────────────────── */

.kb-answerbox {
  background-color: #F4F7FF;
  border-left: 4px solid #3686FF;
  border-radius: 0 12px 12px 0;
  padding: 20px 24px;
  margin: 28px 0;
}

.kb-answerbox strong,
.kb-answerbox b {
  font-family: 'Poppins', sans-serif;
  color: #222222;
  font-size: 15px;
  font-weight: 700;
  display: block;
  margin-bottom: 8px;
}

.kb-answerbox p {
  color: #6B7280;
  font-size: 16px;
  line-height: 1.7;
  margin: 0;
}

/* ─────────────────────────────────────
   YMYL DISCLAIMER
   ───────────────────────────────────── */

.af-ymyl-disclaimer {
  background-color: #FFFBF0;
  border-left: 4px solid #FDA050;
  border-radius: 0 8px 8px 0;
  padding: 16px 20px;
  margin: 24px 0;
}

.af-ymyl-disclaimer p {
  font-size: 14px;
  color: #6B7280;
  line-height: 1.6;
  margin: 0;
}

/* ─────────────────────────────────────
   TYPE A — STAKES CALLOUT (Orange)
   ───────────────────────────────────── */

.kb-callout-stakes {
  background-color: #FFF8F0;
  border-left: 4px solid #FDA050;
  border-radius: 0 12px 12px 0;
  padding: 20px 24px;
  margin: 32px 0;
}

.kb-callout-stakes p,
.kb-callout-stakes li {
  color: #6B7280;
  font-size: 16px;
  line-height: 1.7;
}

.kb-callout-stakes strong {
  font-family: 'Poppins', sans-serif;
  color: #222222;
  font-weight: 700;
}

.kb-callout-stakes a {
  color: #B45309;
  font-weight: 600;
  text-decoration: none;
}

.kb-callout-stakes a:hover {
  text-decoration: underline;
  text-underline-offset: 2px;
}

/* ─────────────────────────────────────
   TYPE B — HOW-TO CALLOUT (Blue)
   ───────────────────────────────────── */

.kb-callout-howto {
  background-color: #F4F7FF;
  border-left: 4px solid #3686FF;
  border-radius: 0 12px 12px 0;
  padding: 20px 24px;
  margin: 32px 0;
}

.kb-callout-howto p,
.kb-callout-howto li {
  color: #6B7280;
  font-size: 16px;
  line-height: 1.7;
}

.kb-callout-howto strong {
  font-family: 'Poppins', sans-serif;
  color: #222222;
  font-weight: 700;
}

.kb-callout-howto a {
  color: #3686FF;
  font-weight: 600;
  text-decoration: none;
}

.kb-callout-howto a:hover {
  text-decoration: underline;
  text-underline-offset: 2px;
}

/* ─────────────────────────────────────
   TYPE C — COMPLETION CALLOUT (Dark)
   ───────────────────────────────────── */

.kb-callout-completion {
  background-color: #222222;
  border-radius: 16px;
  padding: 32px 36px;
  margin: 40px 0;
}

.kb-callout-completion .completion-headline,
.kb-callout-completion > p:first-child strong {
  font-family: 'Poppins', sans-serif;
  color: #3686FF;
  font-size: 20px;
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 16px;
  display: block;
}

.kb-callout-completion p {
  color: #FFFFFF;
  font-size: 16px;
  line-height: 1.7;
  margin-bottom: 20px;
}

.kb-callout-completion .next-read-card {
  background: #333333;
  border-radius: 10px;
  padding: 16px 20px;
  margin-top: 12px;
  border: 1px solid #444444;
}

.kb-callout-completion .next-read-card a {
  font-family: 'Poppins', sans-serif;
  color: #3686FF;
  font-weight: 600;
  text-decoration: none;
  font-size: 15px;
  display: block;
}

.kb-callout-completion .next-read-card a:hover {
  color: #60A5FA;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.kb-callout-completion .next-read-card p {
  color: #9CA3AF;
  font-size: 13px;
  line-height: 1.5;
  margin-top: 4px;
  margin-bottom: 0;
}

/* ─────────────────────────────────────
   DATA VIZ CONTAINER
   ───────────────────────────────────── */

.af-data-viz {
  background-color: #FFFFFF;
  border: 1px solid #E8EDFB;
  border-radius: 12px;
  padding: 28px;
  margin: 32px 0;
  overflow-x: hidden;
}

.af-data-viz figcaption,
.af-data-viz .chart-caption {
  text-align: center;
  font-size: 12px;
  color: #9CA3AF;
  margin-top: 16px;
  font-style: italic;
  line-height: 1.5;
}

/* ─────────────────────────────────────
   COMPARISON TABLE
   ───────────────────────────────────── */

.af-comparison-table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'Inter', sans-serif;
  font-size: 15px;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #E8EDFB;
}

.af-comparison-table th {
  background-color: #222222;
  color: #FFFFFF;
  padding: 14px 20px;
  text-align: left;
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  font-size: 13px;
}

.af-comparison-table .section-header td {
  background-color: #F4F7FF;
  color: #3686FF;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 11px;
  letter-spacing: 0.10em;
  text-transform: uppercase;
  padding: 10px 20px;
}

.af-comparison-table tr:nth-child(even) {
  background-color: #F8FAFC;
}

.af-comparison-table tr:nth-child(odd) {
  background-color: #FFFFFF;
}

.af-comparison-table td {
  padding: 14px 20px;
  border-bottom: 1px solid #F1F5F9;
  color: #6B7280;
}

.af-comparison-table td:first-child {
  color: #222222;
  font-weight: 500;
}

.af-comparison-table td:last-child {
  text-align: right;
  font-weight: 700;
  color: #222222;
  font-variant-numeric: tabular-nums;
}

.af-comparison-table .zero-row td {
  background-color: #F0FDF4;
  color: #01AC36;
  font-weight: 700;
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  border-top: 2px solid #01AC36;
  padding: 16px 20px;
}

/* Mobile responsive */
@media (max-width: 767px) {
  .af-comparison-table thead { display: none; }
  .af-comparison-table tr {
    display: block;
    margin-bottom: 8px;
    border: 1px solid #E8EDFB;
    border-radius: 8px;
    overflow: hidden;
  }
  .af-comparison-table td {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 16px;
  }
  .af-comparison-table td::before {
    content: attr(data-label);
    font-weight: 600;
    color: #9CA3AF;
    font-size: 12px;
  }
}
```

---
---

# SECTION 9: THE AI PROMPT HEADER

## 9.1 How to Use This Header

Copy the block below and paste it at the very beginning of any AI prompt session that involves visual design, image generation, callout block writing, or infographic production for Adulting Finance. The AI will use it as context for every request in that session. You do not need to paste the entire design system document every time — this compressed header captures the essential rules in a format that fits within most prompt windows.

## 9.2 The Compressed Prompt Header

```
You are working on design and visual content for Adulting Finance, a personal finance blog for adults aged 22–35. Before producing any visual output, internalize these rules:

BRAND IDENTITY: Editorial, trustworthy, warm. Like Morning Brew crossed with Bloomberg Businessweek. Clean white surfaces, bold Poppins headings, minimal color use.

OFFICIAL COLORS — ORIGINAL PALETTE:
Primary Blue:    #3686FF — links, CTAs, category labels, bar charts
Primary Orange:  #FDA050 — variable bars, warm accents, headline highlights
Black Out:       #222222 — headings, dark surfaces, fixed expense bars
White:           #FFFFFF — all backgrounds
Success Green:   #01AC36 — savings bars, zero balance, positive states
Warning Red:     #FF343C — danger states, budget floor lines
Muted Text:      #6B7280 — all body copy
Caption Text:    #9CA3AF — source lines, small labels
Light Border:    #E8EDFB — card borders, dividers
Section BG:      #F4F7FF — answer blocks, info callouts
Page BG:         #F8FAFC — subtle page/container background

AF BLUE SERIES — Extended Palette (3 tiers, one tier per design only):
TIER 1 dark BGs:  #012a4a · #013a63 · #01497c · #014f86
TIER 2 accents:   #2a6f97 · #2c7da0 · #468faf
TIER 3 surfaces:  #61a5c2 · #89c2d9 · #a9d6e5
Blue Series rule: amber (#FDA050) is ALWAYS present as the warm accent.
Never mix tiers. Never use Tier 3 as text color. Never mix Blue Series Tier 1
with original dark backgrounds (#0F172A, #0D1B2A) in the same design.

FONTS: Poppins (headings, display numbers, 700 weight) + Inter (body, labels, 400–600 weight)

BUDGET CATEGORY COLORS — NEVER CHANGE THESE:
Fixed expenses:    #222222 (Black Out)
Variable expenses: #FDA050 (Energy Orange)
Savings & goals:   #01AC36 (Green Haze)
Zero result:       #01AC36 with #F0FDF4 background

ABSOLUTE BANS:
❌ No gradients anywhere
❌ No cartoon illustrations or stock photos of people
❌ No drop shadows heavier than 0 2px 8px rgba(0,0,0,0.06)
❌ No URLs, blog names, or spec text inside image files
❌ No font weights above 700 except in hero banner display numbers
❌ No colors outside the official palette without explicit approval
❌ No background color #0D1117 — this is retired
❌ No mixing Blue Series tiers in a single design
❌ No Blue Series Tier 3 colors used as text

CALLOUT BLOCKS:
Type A (Stakes):     bg #FFF8F0, left border 4px solid #FDA050, class .kb-callout-stakes
Type B (How-To):     bg #F4F7FF, left border 4px solid #3686FF, class .kb-callout-howto
Type C (Completion): bg #222222, headline color #3686FF, body text white, class .kb-callout-completion

INFOGRAPHIC SPECS:
All blog post infographics: 740px wide, white background #FFFFFF
All hero banners: 1200×630px export (4K 3840×2016 master)
All Pinterest pins: 1000×1500px PNG
Data viz containers: white bg, 1px border #E8EDFB, 12px border-radius, 28px padding

Every visual must serve one of four functions: Teaching, Trust, Pacing, or Conversion.
First visual in every post must appear within the top 20% of the article.
Every chart requires a setup paragraph before it and an interpretation paragraph after it.
Hero banner headlines: maximum 7 words. One dominant idea. One dominant visual object.
Final headline line always in #FDA050 amber. Never place full SEO title on a banner.
```

---
---

# SECTION 10: THE PRODUCTION CHECKLIST

## 10.1 Per-Post Asset Checklist

This checklist should be completed before every post is published. It covers all design and visual elements that must be present and correct before the publish button is pressed.

Beginning with the featured image, confirm that it has been designed at 4K master resolution and exported at exactly `1200 × 630px` as a JPG, that it has been compressed to under 200KB using ShortPixel or Squoosh, that the alt text has been set in WordPress and includes the primary keyword, and that the Open Graph preview has been validated using Facebook Sharing Debugger or an equivalent tool.

For the post body visuals, confirm that Visual 1 (the Paycheck Waterfall or equivalent teaching visual) appears before the second H2 heading — this is the top 20 percent rule. Confirm that all PNG images have been compressed to under 150KB and are being served as WebP. Confirm that native Kadence table and comparison card blocks have been built with the correct CSS classes. Confirm that all three CTA callout blocks (Type A, Type B, Type C) are present with HTML placeholder comments above each one. Confirm that no two callout blocks appear back-to-back without body text between them.

For the Pinterest assets, confirm that all three pins have been prepared and scheduled in your Pinterest tool: Pin A for publish day, Pin B for day 7, Pin C for day 14.

For the CSS implementation, confirm that the complete CSS from Section 8 has been pasted into WordPress Additional CSS, that the site cache has been cleared after the CSS was added, and that you have done a mobile preview at 375 pixels width to confirm all tables and visuals render without horizontal scroll.

## 10.2 Version History

This document was created in March 2026 as Version 1.0. When any element of the brand system changes — a new color is added, a font is changed, a CSS rule is updated, a new visual type is introduced — update the version number and add a changelog entry here so that anyone working with this document knows what is current.

Version 1.0 — March 2026 — Initial complete system. Replaces all previous partial design documents. Colors derived from official palette. Aesthetic references: Sendlane. Type C callout accent changed from amber to Dodger Blue. Background #0D1117 retired. Font system updated to Poppins + Inter.

Version 2.0 — March 2026 — AF Blue Series added (10-color ramp, 3 tiers). Section 2.5 added. Section 9 prompt header updated with Blue Series rules. 16-style banner system added to companion Prompt Style Guide.

---

*Adulting Finance Design System Guide — Version 1.0 — March 2026*
*This document is the single source of truth for all design decisions.*
*Load Section 9 (The AI Prompt Header) at the start of every LLM design session.*
*Update the version number whenever any rule changes.*
