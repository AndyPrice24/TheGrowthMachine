/*
 * The two audiences the homepage splits into after "The awkward stage".
 *
 * One page, three addresses (decided 9 October 2026): `/` shows the shared
 * opening and stops at the choice; `/b2b` and `/ecommerce` show the same
 * opening, then everything below the choice written for that audience.
 * Outbound emails link straight to a track, so a prospect never has to
 * answer a question Andrew already knows the answer to.
 *
 * Everything here that differs between the two is copy. The machine artwork
 * is shared; only the words beside it change.
 */
import type { StepCopy } from "../components/MachineRun.astro";

export type TrackId = "b2b" | "ecommerce";

export interface Track {
  id: TrackId;
  path: string;
  meta: { title: string; description: string };
  card: { kicker: string; title: string; text: string; cta: string; switchTo: string };
  machine: StepCopy[];
  inOut: { inward: string; outward: string };
  /* who is introduced first in "Who you actually get" */
  leads: "andrew" | "tarren";
}

export const tracks: Record<TrackId, Track> = {
  ecommerce: {
    id: "ecommerce",
    path: "/ecommerce",
    meta: {
      title: "Fractional CMO and Ecommerce Lead | The Growth Machine",
      description:
        "Fractional CMO and ecommerce leadership for consumer brands, from people who've founded and run their own. Sharper customer, stronger offer, data-led spend.",
    },
    card: {
      kicker: "Ecommerce and consumer brands",
      title: "You sell online, on Amazon or into retail.",
      text: "Sharper customer, stronger offer. Data-led decisions on channels, creative and budget, so you scale what pays.",
      cta: "For ecommerce brands",
      switchTo: "Switch to ecommerce",
    },
    /* Rebuilt from 35 LinkedIn job ads (October 2026): the reasons consumer
       brands hire, ranked, are running several channels at once, not being
       able to see what's working, repeat customers, margin, and agencies to
       hold to account. Paid acquisition is framed as a discipline, not a
       complaint. */
    machine: [
      {
        name: "What comes in",
        points: [
          "Ad spend doing all the work",
          "Traffic that doesn't convert",
          "Customers who buy once",
          "Channels nobody runs as one",
          "Numbers no one can explain",
        ],
        text: "Or a brand ready for its next channel.",
      },
      { name: "Diagnose", text: "We find out what each order really earns, by channel, product and customer, after fees, returns and ad spend." },
      { name: "Design", text: "Sharper customer, stronger offer, and a plan for each channel built on what it actually earns." },
      { name: "Execute", text: "We do the work with your team: creative, campaigns, your site and listings, retention, and the tools that run them, AI included." },
      { name: "Embed", text: "One set of numbers everyone trusts, agencies held to them, and a team that runs it without depending on anyone, us included." },
      {
        name: "What comes out",
        points: ["Orders that make money", "Customers who come back", "Growth that runs on profit, not spend"],
      },
    ],
    inOut: {
      inward:
        "Where margin slips between the ad and the doorstep: fees, returns, stock, agencies nobody holds to account, and numbers no one can explain. We fix them, and build the tools that keep them fixed.",
      outward:
        "Who your customer really is, a sharper offer, creative and channels that pay their way, customers who come back, and the next channel: Amazon, retail or overseas.",
    },
    leads: "tarren",
  },
  b2b: {
    id: "b2b",
    path: "/b2b",
    meta: {
      title: "Fractional CRO, CMO and GTM for B2B | The Growth Machine",
      description:
        "Fractional CRO, CMO and GTM leadership for B2B, SaaS and service businesses, from people who've founded and run their own. We judge growth by profit.",
    },
    card: {
      kicker: "B2B, SaaS and service businesses",
      title: "You need a CRO, CMO or GTM lead, but not full-time.",
      text: "A pipeline you can predict and numbers you can trust. At home, across Africa or overseas.",
      cta: "For B2B businesses",
      switchTo: "Switch to B2B",
    },
    /* Rebuilt from 32 LinkedIn job ads and a web scan of fractional postings
       (October 2026): the four main B2B reasons to hire, in order, are a
       pipeline you can predict, numbers you can trust, a sales engine that
       does not run through the founder, and new markets or launches. */
    machine: [
      {
        name: "What comes in",
        points: [
          "A pipeline you can't predict",
          "Numbers nobody trusts",
          "Sales that still run through the founder",
          "A new market with no one to lead it",
        ],
        text: "Or a business ready for its next stage.",
      },
      { name: "Diagnose", text: "We find out what's really working: every channel, deal and number, ranked by what it's worth to you." },
      { name: "Design", text: "We decide who you sell to, what you say and what you charge, and build the plan around a few numbers that matter." },
      { name: "Execute", text: "We do the work with your team: pipeline, campaigns, the sales process, and the tools that run them, AI included." },
      { name: "Embed", text: "A forecast the board can trust, playbooks your team owns, and an engine that runs without depending on anyone, us included." },
      {
        name: "What comes out",
        points: ["A pipeline you can predict", "Numbers you can trust", "Revenue that grows faster than headcount"],
      },
    ],
    inOut: {
      inward:
        "Numbers nobody trusts, systems bolted on as you grew, spend no one can prove is working, and decisions that still wait for you. We fix them, and build the tools that keep them fixed.",
      outward:
        "Who you sell to and what you say, the pipeline that wins them, and the next market: at home, across Africa or overseas.",
    },
    leads: "andrew",
  },
};

/* the order the cards appear in, on every version of the page */
export const trackOrder: TrackId[] = ["ecommerce", "b2b"];
