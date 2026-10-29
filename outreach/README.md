# UK Adult Learner Outreach

Harvey is set up for **Solyman, Student Consultant at Platinum Education**, an independent education consultancy. It finds **organisations** across the UK (housing associations, councils, charities, community centres, libraries, food banks, employment agencies, employers) and asks them to tell the adults they support about part-time, student-finance-funded courses.

It doesn't scrape social media or contact members of the public. People reach you because a partner they trust told them about you, or because they saw your poster or an ad and enquired.

## What's here

| File | What it is |
|---|---|
| [`partner_emails.md`](partner_emails.md) | Cold email sequences for each kind of partner organisation |
| [`reply_templates.md`](reply_templates.md) | How to answer partners' replies and questions |
| [`partner_toolkit.md`](partner_toolkit.md) | Poster, leaflet, social posts, newsletter text and staff briefing for partners |
| [`texts_and_calls.md`](texts_and_calls.md) | Text messages for enquirers who opted in, phone scripts and consent wording |
| [`../skills/uk_adult_learner_courses.md`](../skills/uk_adult_learner_courses.md) | The rules and facts Harvey uses when writing |
| [`../harvey.yaml`](../harvey.yaml) | Who Harvey targets, where (29 UK cities) and how it sends |

## Read this first: agents and UK students

Platinum Education recruits UK students for course providers, so it is a domestic recruitment agent. That is the area the government is cracking down on:

- In March 2025 the government said it can "see no legitimate role for domestic agents in the recruitment of UK students" and that it would act on agents straight away. The Department for Education has been investigating agents' use, and the Office for Students has found weak oversight where franchised providers use them.
- New rules on franchised courses tie their eligibility for student finance to registration with the Office for Students (for larger delivery partners, from 2028–29).

I couldn't confirm whether a formal ban on paying domestic agents has come in yet. Before scaling this up, get in writing from each provider you work with that their arrangement with Platinum Education is allowed under current Department for Education and Office for Students rules, and keep that on file. If a provider stops using agents, stop naming them.

## Before you run it

1. **Check who you're sending as.** `persona` in `harvey.yaml` is set to Solyman, Student Consultant, Platinum Education. Change `persona.email` to your real work address. Every email says plainly that Platinum Education is an independent consultancy, not the college.
2. **Name only providers you have a written agreement with,** and get each one to approve how its courses are described. Fill in how Platinum Education is paid in `reply_templates.md` ("Are you an agent?") and in `harvey.yaml` (`objection_responses`), honestly.
3. **Add your company details.** Put Platinum Education's registered name, company number and registered office address in `compliance.postal_address`.
   Turn on the Precleared check (the setup wizard asks; or set `compliance.precleared` to `enabled: true`, `sender_country: "GB"`, `address_source: "published"`, `prospect_country: "GB"`).
4. **Connect a mailbox.** Use your Platinum Education work mailbox (`harvey gmail auth` or `harvey microsoft auth`), plus an email verification key. Warm it up for 2–4 weeks before cold sending.
5. **Fill in the courses by hand** in the "Courses and providers" section of `skills/uk_adult_learner_courses.md`. Don't run `harvey train`: it overwrites the company name, product description and every targeting setting in this setup with a generic sales setup.
6. **Find partners:** confirm the signals Harvey records (dashboard → Signals, or `harvey signals --confirm free`), then `harvey discover --estimate` shows the searches and cost first. Five partner types (community centres, libraries, charities, food banks, employment agencies) work on the free OpenStreetMap source; the rest need a web search source.
7. **Run it:** `harvey run`, then approve emails in the dashboard Outbox.

## Ground rules

- Always say you're from Platinum Education, an independent consultancy. Never present as the college, a university, Student Finance, Jobcentre Plus or a charity. Tell students they can apply to the college directly.
- No referral fees to partners and no incentives to students. Never charge students, fill in their student finance application or ask for their login details.
- Never describe the courses as free. Student finance is a loan, repaid only above the earnings threshold.
- Don't collect or receive anyone's personal details without their own consent. Text or call members of the public only after they enquire and opt in.
- B2B email to named staff at organisations is lawful in the UK with a clear opt-out. Harvey adds the opt-out, honours it permanently, and, once you switch it on, runs a Precleared UK PECR check on each new address.
