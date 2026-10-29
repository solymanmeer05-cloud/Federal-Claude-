# Platinum Education Outreach

Harvey emails organisations across the UK (housing associations, councils, charities, community centres, libraries, food banks, employment agencies, employers) on behalf of **Solyman, Student Consultant at Platinum Education**.

**The message:** Platinum Education is a consultancy that helps adults who didn't get the GCSEs or A-levels they hoped for get onto one of over 400 university courses across the UK, so they can change careers and their lives.

Harvey doesn't contact members of the public. People come to you when a partner they trust passes the word on.

## What's here

| File | What it is |
|---|---|
| [`partner_emails.md`](partner_emails.md) | The email sequence for partner organisations |
| [`reply_templates.md`](reply_templates.md) | Short answers to common replies |
| [`partner_toolkit.md`](partner_toolkit.md) | Poster, social posts and newsletter text for partners |
| [`texts_and_calls.md`](texts_and_calls.md) | Texts for people who enquired, phone scripts, enquiry form |
| [`../skills/uk_adult_learner_courses.md`](../skills/uk_adult_learner_courses.md) | The message and rules Harvey writes by |

## To get started

1. Put Platinum Education's company details in `compliance.postal_address` in `harvey.yaml` (your email and website are already set).
2. Connect your Outlook / Microsoft 365 mailbox (see `docs/microsoft365.md`): register the Harvey app, put `M365_CLIENT_ID` and `M365_TENANT_ID` in `.env`, then run `harvey microsoft auth` and `harvey microsoft test`. Add an email checker key (e.g. `REOON_API_KEY`) and say yes to the Precleared check in `harvey setup`.
3. Confirm signals (`harvey signals --confirm free`), then `harvey discover --estimate` and `harvey discover`.
4. `harvey run`, then approve emails in the dashboard Outbox.

Don't run `harvey train`: it would overwrite this setup.

## Keep in mind

- Never call it free (student finance is a loan), and don't offer referral fees or incentives.
- Only text or call members of the public after they enquire and agree to it.
- How Platinum Education is paid (university partner contracts) is only mentioned if someone asks.
- The government is scrutinising agents that recruit UK students, so keep your university partnership agreements on file.
