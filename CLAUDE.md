# The Growth Machine

Marketing site for The Growth Machine, a two-person fractional executive firm
(Andrew Price and Tarren Price). Domain: **thegrowthmachine.co**.

**Status: the brief is being reconciled.** Two source briefs exist and they
disagree on the core argument, the offer, the look and parts of the stack.
Until this file is replaced with the merged brief, build nothing that depends
on an unsettled decision: no page copy, no design tokens, no components.

## Source briefs

- `docs/briefs/build-handover.md`: the build handover. It has the revenue and
  margin positioning, strict rules and the technical spec.
- `docs/briefs/website-developer-handover-v1.pdf`: the developer handover v1.
  It has page-by-page copy, wireframes, art direction and the photography brief.

Neither one wins by default. Every conflict between them is decided by the
owners and recorded here.

## Settled

- **This repo is completely separate from Groove (MGN8).** Nothing here
  touches that repo, and nothing there touches this one.
- **The name is final:** The Growth Machine. The domain is `thegrowthmachine.co`,
  always written in full and in lowercase. `thegrowthmachine.com` belongs to
  an unrelated company.
- **Stack: Astro, static output.** The build handover specifies it and the
  PDF names no stack. Whether content is edited through a CMS is still open.

## Rules both briefs agree on

- **Never invent proof.** No client names, logos, quotes, percentages or
  results, not even as placeholders. Fake proof that reaches production is
  the one failure this site cannot recover from.
- **Never invent credentials.** Bios, titles, companies, dates and outcomes
  come from Andrew and Tarren.
- **Two people. Say two.** Never imply a team, a roster or a network.
- **No pricing on the site.** The call is the qualifier.
- **No newsletter pop-up and no chat widget** at launch.
- **No stock language:** unlock, supercharge, 10x, secret weapon, bespoke,
  innovative solutions, holistic synergies, end-to-end.

## Working rules

- Astro is on v7, which is newer than most training data. Check
  `node_modules/astro/` and the dev server's warnings before relying on a
  convention from memory.
- Every page must build and pass `npm run check` before it is pushed.
