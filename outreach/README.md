# UK Adult Learner Outreach

Harvey is set up to find **organisations** across the UK (housing associations, councils, charities, community centres, libraries, food banks, employment agencies, employers) and ask them to tell the adults they support about part-time, student-finance-funded courses.

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

## Before you run it

1. **Send as the provider.** Fill in `persona` in `harvey.yaml` with a real member of the course provider's staff and the provider's name. Harvey won't run while it says "Your Company".
2. **Get the copy approved.** Have the provider's marketing or compliance lead sign off the course facts, subject list and student finance wording.
3. **Add your details.** Put the registered company or charity name, number and address in `compliance.postal_address`.
   Turn on the Precleared check (the setup wizard asks; or set `compliance.precleared` to `enabled: true`, `sender_country: "GB"`, `address_source: "published"`, `prospect_country: "GB"`).
4. **Connect a mailbox.** Use a work mailbox on the provider's domain (`harvey gmail auth` or `harvey microsoft auth`), plus an email verification key. Warm it up for 2–4 weeks before cold sending.
5. **Train on your site:** `harvey train https://your-provider-site` writes the course details into `skills/product_knowledge.md`.
6. **Find partners:** confirm the signals Harvey records (dashboard → Signals, or `harvey signals --confirm free`), then `harvey discover --estimate` shows the searches and cost first. Five partner types (community centres, libraries, charities, food banks, employment agencies) work on the free OpenStreetMap source; the rest need a web search source.
7. **Run it:** `harvey run`, then approve emails in the dashboard Outbox.

## Ground rules

- No referral fees or per-enrolment payments to partners, and no incentives to students. The UK government has said it sees no legitimate role for domestic agents in recruiting UK students, and franchised providers are under closer scrutiny.
- Never describe the courses as free. Student finance is a loan, repaid only above the earnings threshold.
- Don't collect or receive anyone's personal details without their own consent. Text or call members of the public only after they enquire and opt in.
- B2B email to named staff at organisations is lawful in the UK with a clear opt-out. Harvey adds the opt-out, honours it permanently, and, once you switch it on, runs a Precleared UK PECR check on each new address.
