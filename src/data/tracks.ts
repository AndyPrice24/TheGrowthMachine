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
      cta: "How we'd work with you",
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
        text: "Or a brand ready for its next channel or product.",
      },
      {
        name: "Diagnose",
        lead: "We find where to focus first: your biggest opportunities and leaks.",
        points: [
          "What each order really earns, after ad spend, fees and returns",
          "Where shoppers buy, drop off and come back, channel by channel",
          "Your team, agencies and budget, and the next product or market worth backing",
        ],
      },
      {
        name: "Design",
        lead: "One plan for every channel, built on profit.",
        points: [
          "The few numbers that matter, and a ceiling on what a new customer can cost",
          "A sharper customer, offer and price, and a reason to come back",
          "Website, marketplaces and retail, in the order that pays first",
          "Launching new products and markets",
        ],
      },
      { name: "Execute", text: "We do the work with your team: creative, campaigns, your site and listings, retention, and the tools that run them, AI included." },
      { name: "Embed", text: "One set of numbers everyone trusts, agencies held to them, and a team that runs it without depending on anyone, us included." },
      {
        name: "What comes out",
        points: [
          "Orders that make money",
          "Customers who come back",
          "Every channel run as one business",
          "Numbers everyone can read",
          "Growth that runs on profit, not spend",
        ],
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
      title: "You sell to other businesses.",
      text: "A pipeline you can predict and numbers you can trust. At home, across Africa or overseas.",
      cta: "How we'd work with you",
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
          "A new market or product with no one to lead it",
        ],
        text: "Or a business ready for its next stage.",
      },
      {
        name: "Diagnose",
        lead: "We find where to focus first: your biggest opportunities and leaks.",
        points: [
          "How deals are really won, and who wins them",
          "Your channels, numbers, team and agencies: what's working and what isn't",
          "The next market or product worth backing, and what you have to get there with",
        ],
      },
      {
        name: "Design",
        lead: "One revenue plan, sales and marketing together, in the order that pays first.",
        points: [
          "The few numbers that matter, each with an owner",
          "Your best-fit customers, message and pricing",
          "The sales process and channels to win them",
          "Launching new products and markets",
        ],
      },
      { name: "Execute", text: "We do the work with your team: pipeline, campaigns, the sales process, and the tools that run them, AI included." },
      { name: "Embed", text: "A forecast the board can trust, playbooks your team owns, the hires you'll need and when, and an engine that runs without depending on anyone, us included." },
      {
        name: "What comes out",
        points: [
          "A pipeline you can predict",
          "Numbers you can trust",
          "Sales that no longer depend on you",
          "A new market or product, launched and growing",
          "Revenue that grows faster than your costs",
        ],
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
