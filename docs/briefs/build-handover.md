# The Growth Machine — Build Handover

**For Claude Code.** Save this as `CLAUDE.md` in the repository root. It is read
automatically at the start of every session and is the single source of truth for
this project.

Domain: **thegrowthmachine.co**
Last updated: 5 October 2026
Items marked **OPEN** are undecided — ask before assuming. Items marked **BLOCKED**
have no content yet and must not be invented (see §13).

---

## 1. What is being built

A standalone marketing site for The Growth Machine, a two-person fractional
executive firm. Static, fast, no CMS, no store, no login. Roughly ten pages.

The deliverable is a site that gets a qualified founder onto a 30-minute call.
Everything is subordinate to that.

---

## 2. The business

The Growth Machine sells **Andrew Price** and **Tarren Price** as fractional senior
operators. Not an agency. Not consultants who deliver a deck. Two named executives
who embed part-time and do the work.

**Andrew** — multiple-time founder, CEO and Chief Revenue Officer. Revenue, sales,
growth and commercial strategy, B2B and B2C. Acts as a fractional CRO/CCO or
co-founder-equivalent for companies that need that seat but cannot justify or afford
a full-time hire.

**Tarren** — ecommerce and FMCG personal care. Amazon, Shopify, Meta advertising.
Builds and reshapes ecommerce operations to lift revenue or margin.

Andrew and Tarren are the only employees. A bench of trusted specialists (UI/UX,
engineering, AI build) is engaged hourly, per contract, as needed.

---

## 3. The framework — revenue and margin

**This is the organising idea of the entire brand.** Not a menu label, not a service
category, not a page. It is the lens everything is seen through.

Growth has exactly two sources. Every lever that exists lands in one of them.

- **Revenue** — new ways to earn, better ways to earn, more from the same effort.
- **Margin** — money the business already makes and quietly loses on the way out.

This licenses a claim of total coverage without a single woolly word, and it is
board-legible. Founders and boards already think in these terms.

**The reframe. This is the homepage argument:**

> Everyone sells founders revenue. Half your growth is sitting in your margin and
> nobody is looking at it.

It attacks a default belief rather than a competitor, it is true, and it explains
why a CRO-level operator is the right call rather than an agency.

**Why it is credible here, and this is the real differentiator:** most fractional
CROs sell revenue because revenue is all they can do. This firm can claim both sides
because each principal genuinely owns one. Andrew has run revenue as a CRO; Tarren
has run margin inside ecommerce operations. Build the homepage around that pairing.

**Hard constraints:**

- Two axes. **Never a 2x2 matrix.** The moment it becomes a grid with four quadrant
  names it stops being a commercial insight and becomes a consulting slide.
- **"Inside-out" and "outside-in" are banned from all customer-facing copy.** The
  phrase was used with two conflicting meanings during briefing and is ambiguous to
  anyone who did not invent it. Revenue and margin need no explanation; do not put a
  spatial metaphor in front of something already clear.

---

## 4. Positioning

**Core promise:** the senior seat your business needs, filled part-time, by someone
who has actually held it.

**The method.** The "machine" is positioned as the *method* — the repeatable system
applied to every client — rather than a thing installed and handed over.

> **Consequence, and it drives layout.** A method can be copied and has no track
> record. Two named senior operators cannot be copied and do have one. So the method
> needs a distinctive name, and "Who you actually get" must sit **high** on the
> homepage. If the site reads process-first, the fractional pitch collapses into an
> agency pitch and loses on price.

**OPEN — method name.** Not "The Growth Machine Method". Candidates:

- *Both Sides of the Number* — names the revenue/margin idea directly
- *Find the leak, then the lever* — describes the actual sequence of work
- *Count both sides* — shortest, most repeatable

Each engagement also carries its own one-line principle. Proposals:

| Engagement | Principle |
|---|---|
| The Diagnostic | *Everything ranked by what it costs you* |
| The Fractional Seat | *In the business, not on a call* |
| The Build | *It has to still work after we leave* |

---

## 5. Audience — two paths, one hero

**Navigation forks by buyer. Revenue and margin is the lens, not the menu.**

People self-identify by what they *are* far faster than by what is *wrong* with
them — and mostly they do not know which side is broken, which is the entire reason
the Diagnostic exists.

| Path | Buyer | Led by | Vocabulary |
|---|---|---|---|
| **A · Ecommerce** | Founder or GM of a DTC / FMCG brand | Tarren | COGS, AOV, CAC, marketplace fees, retention, contribution |
| **B · Startups & scale-ups** | Founder or CEO needing a commercial exec | Andrew | Pipeline, GTM, sales motion, pricing, board |

Shared brand, shared engagements, different evidence and different metrics. Both
paths are read through revenue and margin.

**OPEN — Path B label and route.** `/startups` is the working recommendation.
"Growth" is too vague and collides with the company name.

---

## 6. Offer — three engagement types

Not six service pillars. Two people offering six services reads as an agency
pretending to be bigger than it is, which is the one credibility failure that cannot
be recovered from in fractional work.

**1 · The Diagnostic**
Fixed scope, fixed fee, paid. Output is a ranked list of leaks in two columns,
revenue and margin, each with a number against it and an estimate of effort to fix.
The front door to everything else.
*Paid, not free — a paid diagnostic qualifies; a free audit attracts tyre-kickers.*
This is where §3 stops being a claim and becomes a deliverable.

**2 · The Fractional Seat**
Embedded and ongoing. A CRO, CCO or ecommerce lead inside the business N days a
month. The core product.

**3 · The Build**
A defined project with a handover — a system, an AI tool, a revenue function stood
up and left running. Where the specialist bench gets used.

**Pricing is not shown.** The call is the qualifier.

---

## 7. The bench — how it appears

**Mechanism only. No names, no photos, no team grid.**

A short paragraph inside *How We Work*. Shape of the claim:

> We are two. When a job needs a discipline we don't have, we bring in a specialist
> we've actually worked with, at their rate, and you see the number before we commit
> it. We don't mark up other people's time.

Why not a team page: "we have a network of experts" is unfalsifiable, every
freelancer says it, and buyers discount it to zero. A staffing *policy* is concrete,
verifiable by behaviour, and the no-markup line differentiates against every agency
that quietly doubles a subcontractor's rate.

Never write "expertise across the board" or any variant. The honest framing is
**we are the brains, the bench is the hands.**

---

## 8. Sitemap and page architecture

```
/                          Home
/ecommerce                 Path A landing
/startups                  Path B landing            [label OPEN]
/how-we-work               Engagement hub + staffing model + method
/how-we-work/diagnostic
/how-we-work/fractional-seat
/how-we-work/build
/who-we-are                Andrew and Tarren in depth
/work                      Proof                     [BLOCKED — §13]
/contact                   Book a call
```

Header nav: Home · How We Work (dropdown of three) · Who We Are · Work · Contact,
plus two CTAs at different temperatures — one low-commitment, one high.

### 8.1 Home, in order

1. **Hero** — one promise, one CTA. No carousel, no stat bar, no logo wall.
2. **The reframe** — §3. Comes before the fork because it applies to both buyers.
3. **The fork** — two cards, Ecommerce and Startups. High on the page. A visitor
   must be able to self-select in about four seconds.
4. **The problem** — the seat you need filled and cannot justify full-time.
5. **How we work** — three engagement cards linking out.
6. **Who you actually get** — Andrew and Tarren, named, with track record.
   Deliberately above proof, because of §4.
7. **Proof** — **BLOCKED**.
8. **Qualification + CTA** — capacity is genuinely limited; say so, then book a call.

### 8.2 Path pages

Same skeleton as Home. The problem, examples, metrics and proof are rewritten in
that buyer's language. **Fork the framing, never the offer** — the three engagement
types are identical on both paths.

### 8.3 Engagement detail page — fixed anatomy, all three

1. Benefit headline plus one paragraph on what it actually is
2. Who it is for, and explicitly who it is not for
3. What's included — around six bullets
4. **The method** — the named principle from §4. An opinion, not a process diagram.
5. **What you'll see** — cadence, reporting, and what to expect at month 1 / 3 / 6.
   Expectation-setting is a trust device. Write it in full sentences, not a table of
   vague promises.
6. The other two engagements as cross-links
7. CTA — book a 30-minute call

---

## 9. Design system

### 9.1 Colour

The wordmark is black and white everywhere. The **gear is the only place colour
lives in the identity**, which is what licenses that colour as the site accent.

```css
--torch:     #FF2715;  /* accent. OKLCH L 0.64 · C 0.246 · H 30° */
--ink:       #0A0A0A;  /* primary dark ground */
--ink-pure:  #000000;  /* full-bleed hero and logo grounds only */
--paper:     #FFFFFF;
--grey-900:  #141414;
--grey-800:  #1C1C1C;
--grey-700:  #2B2B2B;  /* borders on dark */
--grey-500:  #6A6A6A;
--grey-300:  #9A9A9A;
--grey-100:  #E8E6E5;  /* borders on light, very slightly warm */
```

Neutrals carry a faint warm bias so they sit with Torch rather than against it.
Do not substitute a pure computational grey.

**Accent contrast — hard rules, not guidelines.**

| Ground | Ratio | Permitted use |
|---|---|---|
| On black | 5.24:1 | Anything, including small text and links |
| On white | 3.78:1 | Graphics, rules, buttons, large numerals, headings ≥24px |

On white surfaces the accent colours **objects, not small text**. Orange body links
on white fail the 4.5:1 text threshold. Use `--ink` for text and let the accent
carry buttons, rules, the gear and large numerals.

Torch was selected from a two-round trial. Round one eliminated every accent that
survives only one ground; round two established that Torch is near the maximum
saturation achievable while clearing both. **Do not substitute a brighter orange** —
brighter fails on white and is also less saturated, because the sRGB gamut narrows
toward white.

Semantic colours (success, warning, error) are separate from the accent and are not
yet defined. Add them when the contact form exists.

### 9.2 Typography

One family, extreme weight contrast — taken from the logo's own logic.

```
Display   Archivo Black          headlines, engagement names, large numerals
Body      Archivo 400/500/600    running text, UI
Data      IBM Plex Mono 400/500  metrics, figures, technical eyebrows
```

- Eyebrows and labels: 0.6875rem, weight 600, letter-spacing 0.22em, uppercase
- Headlines: `text-wrap: balance`, letter-spacing −0.015em to −0.02em
- Running text near 65 characters
- `font-variant-numeric: tabular-nums` wherever digits align. There will be a lot of
  digits on this site — that is the point of §3.

Self-host the fonts rather than hotlinking, for performance and privacy.

**PROVISIONAL** until the vector logo arrives — the wordmark may be a specific
typeface worth matching rather than approximating with Archivo Black.

### 9.3 Layout and motion

- **Alternating black and white full-bleed sections.** This is the site's rhythm and
  the structural reason the accent had to survive both grounds.
- Flex and grid with `gap`. No per-element margins for sibling spacing.
- Wide content gets its own `overflow-x: auto`. The body never scrolls sideways.
- Mobile first. 16px side gutters minimum.
- **The signature moment — the machine.** Two inputs, one output: revenue entering
  one side, margin the other, feeding a single mechanism, profit coming out. A
  left-to-right scroll sequence. The logo carries no in/out idea, so the site must.
  Build this once, properly, and keep everything else quiet.
- The gear rotates. Sparingly — page load and the machine sequence. Not on every
  hover on every card.
- Respect `prefers-reduced-motion` everywhere. The machine sequence must degrade to
  a static composition that still communicates two-in-one-out.

### 9.4 Components

Header with dual CTAs · hero · reframe block · fork card · engagement card · the
machine sequence · bio block · proof card · staffing-model paragraph · method
callout · expectations block (month 1/3/6) · qualification block · CTA band · footer.

Fourteen components. Build them as components, not as per-page markup.

---

## 10. Copy rules

- Specific beats clever. Numbers beat adjectives.
- Everything frames through revenue or margin. If a claim fits neither, cut it.
- Name engagements as outcomes, not job titles.
- Every engagement carries a named method — an opinion, not a process.
- **Never** write "inside-out", "outside-in", or any spatial variant.
- **Never** render revenue/margin as a 2x2 grid or name quadrants.
- Never claim a network, a roster, or "expertise across the board".
- Never imply more people than exist. Two employees. Say two.
- Expectation-setting is a trust device, not a caveat. Write it in full sentences.
- No stock language: no "unlock", "supercharge", "10x", "secret weapon", "bespoke".
- British English.

---

## 11. Technical specification

### 11.1 Stack

**Astro**, static output. Rationale: ships almost no JavaScript by default, which
suits a content site where Core Web Vitals and SEO matter; content collections map
cleanly onto the three engagement pages and two path pages; trivial to deploy as
static files. No React or other framework unless something genuinely needs it — the
machine sequence does not, it needs an IntersectionObserver and about forty lines of
vanilla JS.

Use whatever Astro major version is current at build time. Plain CSS with custom
properties, or Tailwind if preferred — but the tokens in §9.1 are the source of
truth either way, defined once and referenced everywhere. No hardcoded hex values
in components.

### 11.2 Repository structure

```
/
├── CLAUDE.md                 this file
├── src/
│   ├── components/           the fourteen components in §9.4
│   ├── layouts/
│   ├── pages/                routes mirroring §8
│   ├── content/              engagement and path page content as MD/MDX
│   └── styles/tokens.css     §9.1 and §9.2, defined once
├── public/
│   ├── fonts/                self-hosted Archivo + IBM Plex Mono subsets
│   └── brand/                logo lockup, standalone gear mark, favicons, OG images
└── README.md                 how to run, build and deploy
```

### 11.3 Performance budget

- Lighthouse 95+ on all four categories, mobile, for every page
- Largest Contentful Paint under 2.0s on a simulated 4G connection
- Total JavaScript under 30KB gzipped across the site
- No layout shift on font load — preload the subsets, use `font-display: swap`

### 11.4 SEO

- One primary keyword per page. Do **not** chase the brand name (see §12.3).
- Unique `<title>` ≤60 characters and meta description 150–160 on every page
- OG and Twitter card images per page, generated from the brand assets
- `sitemap.xml` and `robots.txt` generated at build
- JSON-LD: `Organization` on the homepage, `Service` on each engagement page,
  `Person` for Andrew and Tarren on `/who-we-are`
- Semantic headings, one `h1` per page, logical order, no skipped levels

### 11.5 Accessibility

Target WCAG 2.1 AA.

- The accent contrast rules in §9.1 are the most likely place to fail. Enforce them.
- Visible keyboard focus on every interactive element. Do not remove outlines
  without replacing them with something at least as visible.
- The dropdown nav must be keyboard operable and escape-dismissible.
- `prefers-reduced-motion` honoured by the machine sequence and the gear.
- Run an axe pass before deploy.

### 11.6 Analytics and privacy

Use a cookieless, privacy-first analytics provider (Plausible, Fathom, or
Cloudflare Web Analytics). Rationale: no cookie banner, which removes a consent
interstitial from a site whose only job is to get someone onto a call. Do not add
Google Analytics or Meta Pixel without an explicit decision, because either one
drags consent requirements back in.

### 11.7 Booking and contact

**OPEN.** The primary CTA is "Book a 30-minute call". Decide between an embedded
scheduler (Calendly, Cal.com, SavvyCal) and a plain form. If a scheduler is
embedded, lazy-load it so it does not cost the performance budget on first paint.
A fallback `mailto:` is not acceptable as the only path.

---

## 12. Domain and deployment

### 12.1 The domain

**thegrowthmachine.co** — already registered. Canonical form is lowercase.

**OPEN — registrar.** Needed before DNS can be configured. Where the domain was
bought determines where the records are edited.

### 12.2 Recommended hosting

**Cloudflare Pages.** Static hosting, free tier is more than adequate, global edge,
automatic TLS, preview deployments per branch, and if the domain's nameservers move
to Cloudflare the connection is a single click with no manual records. Cloudflare
Web Analytics is then available at no cost and with no cookie banner.

Vercel or Netlify are equally valid. The process below works for any of them.

### 12.3 Important — the .com is taken and active

`thegrowthmachine.com` is a live business: a CRM and marketing automation platform
for Managed Service Providers, operated under Marketopia. Verified 5 October 2026.

Three consequences for this build:

1. **Do not target the brand name in SEO.** Ranking for "the growth machine" against
   an established .com in an adjacent B2B marketing space is an expensive fight for
   traffic that mostly is not looking for us. Target service and problem terms
   instead: fractional CRO, fractional chief revenue officer, ecommerce margin
   consultant, fractional commercial director, and the problem-led variants.
2. **Email hygiene matters.** Anyone typing the address from memory may default to
   `.com` and reach another company. Always render the full address in text, never
   abbreviate the domain, and set up SPF, DKIM and DMARC properly from day one so
   mail from `.co` is not treated as a spoof of the better-known `.com`.
3. **Trademark is worth ten minutes of professional advice.** Different class of
   offering — services versus software — and coexistence is common, but this is a
   question for a lawyer, not for a build document.

### 12.4 Connection process

Run this **after** the site builds and passes locally, not before.

1. **Push to a Git remote.** GitHub is fine. Keep `main` as the production branch.
2. **Create the hosting project** and connect the repository. Build command and
   output directory per the Astro adapter in use. Confirm the preview URL renders
   correctly before touching DNS.
3. **Decide the canonical host.** Recommendation: apex `thegrowthmachine.co` as
   canonical, with `www` 301-redirecting to it. Be consistent — canonical tags,
   sitemap and internal links must all use the same form.
4. **Add the custom domain in the host's dashboard.** It will issue the exact DNS
   records required. **Use the values it gives you.** Do not copy IP addresses or
   CNAME targets from documentation, blog posts or memory; providers change them.
5. **Add the records at the registrar** (or move nameservers to Cloudflare, which
   replaces this step). Typically an `A` or `ALIAS`/`ANAME` record at the apex and a
   `CNAME` for `www`.
6. **Wait for propagation**, usually minutes, occasionally hours. Verify with
   `dig thegrowthmachine.co +short` and `curl -sI https://thegrowthmachine.co`.
7. **Confirm TLS** has issued and that `http://` and the non-canonical host both
   redirect to `https://` on the canonical host. Check all four combinations.
8. **Set up email** separately from site hosting. Decide the provider, then add MX,
   SPF, DKIM and DMARC records. See §12.3 point 2.
9. **Post-launch:** submit the sitemap to Google Search Console, verify the property,
   confirm analytics is recording, and re-run Lighthouse against the live domain
   rather than localhost.

---

## 13. Rules of engagement for this build

**Do not invent proof.** There is no client list, no case study, no testimonial and
no published number. If a section needs proof, build it as a visibly empty component
with a `TODO` and tell Andrew. Never generate placeholder client names, logos,
quotes, percentages or results, not even as lorem — on a site whose entire credibility
rests on track record, fake proof that survives to production is a catastrophic
failure, and plausible fake proof is harder to spot than obvious fake proof.

**Do not invent credentials.** Andrew and Tarren's bios must come from them. Job
titles, company names, dates and outcomes are facts, not copy.

**Ask before resolving anything marked OPEN.** There are six. None of them should be
guessed.

**Keep the component count down.** Fourteen components is the target. If a page
seems to need a fifteenth, the answer is usually that an existing one needs a variant.

---

## 14. Suggested build sequence

| Phase | Work | Gate |
|---|---|---|
| 1 | Repo, Astro, tokens, fonts, base layout, header and footer | Tokens render; nav keyboard-operable |
| 2 | Component library built in isolation against real copy | All fourteen exist and are responsive |
| 3 | Home, with proof as a visible empty slot | Lighthouse 95+ mobile |
| 4 | The machine sequence | Works, and degrades under reduced-motion |
| 5 | How We Work hub and the three engagement pages | Anatomy in §8.3 identical across all three |
| 6 | Both path pages | Framing forked, offer identical |
| 7 | Who We Are, Contact, booking integration | Booking path works end to end |
| 8 | SEO, schema, OG images, sitemap, analytics | Validated, no console errors |
| 9 | Accessibility pass | axe clean, manual keyboard walkthrough |
| 10 | Deploy and connect the domain per §12.4 | All four host/protocol combinations resolve correctly |
| 11 | Proof | **Blocked until content exists** |

---

## 15. Open items

| # | Item | Needed for |
|---|---|---|
| 1 | **Proof** — nameable clients, publishable numbers, quotes | `/work`, Home §8.1.7, both path pages. The single biggest determinant of whether this site converts. |
| 2 | Vector logo (SVG/AI/EPS) | Final typography match, large-format rendering |
| 3 | Standalone gear mark | Favicon, OG, mobile nav. The full lockup will not survive small sizes. |
| 4 | Method name | §4, engagement pages |
| 5 | Path B label and route | Nav and routing |
| 6 | Domain registrar | §12.4 steps 5 and 8 |
| 7 | Booking tool choice | §11.7 |
| 8 | Andrew and Tarren bios and credentials | `/who-we-are`, Home §8.1.6 |

Also untested: the G/R ligature in the wordmark at roughly 40px in a nav bar. Check
it before committing to the lockup at that size.

---

## 16. Reference and provenance

Structural reference was scale-house.co — hub-and-spoke architecture, outcome-named
services, named methods, expectation-setting as trust, scarcity as qualification,
two CTA temperatures. **Structure only.** Their visual design is not a reference and
must not be imitated.

Accent selection: two published trials, round one covering nine accents across three
families, round two covering seven oranges. Torch (#FF2715) selected in round two.
