# Blossom Therapy & Supports website

A static site (plain HTML/CSS) that's ready for Netlify. It doesn't need a build step.

## Deploy (Netlify free)
1. Create a Netlify account using the business email, not a personal one.
2. Go to Sites > Add new site > Deploy manually, then drag this whole folder in.
3. Check the free *.netlify.app preview URL on a phone.
4. When it's approved: Domain management > add blossomtherapyandsupport.com.au, then follow Netlify's DNS steps at the registrar. **Don't change MX (email) records.**

## Search the files for these markers
- `HALAXY EMBED` — paste the Halaxy form embed code here, then delete the fallback email button. There are 5 of these:
  - Home picker: Client intake
  - Home picker: Carer intake
  - Home picker: Referrer form
  - Services page: Group waitlist
  - Referrals page: Referrer form
- `CONFIRM` — facts to check before launch
- `TODO` — waiting on photos, bios or information
- `LATER` — where the online booking link goes when booking is switched on

## Before cancelling GoDaddy
The referral PDF and the 4 resource PDFs are still linked from GoDaddy's servers. Download them into `assets/files/` and update the links first, or they'll break when GoDaddy is cancelled.

## Editing
Edit the HTML files directly, then drag the folder into Netlify again to redeploy. Each deploy uses 15 of the 300 free monthly credits, so batch your changes.
