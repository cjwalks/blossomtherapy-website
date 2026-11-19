// Deletes form submissions from Netlify once they're old enough to have been
// emailed to the admin inbox. Runs daily at 2am Brisbane time (16:00 UTC; Brisbane has no daylight saving).
//
// Needs one environment variable, set in Netlify (scope: Functions):
//   NETLIFY_API_TOKEN  a Netlify personal access token
// Optional:
//   KEEP_HOURS         how long to keep submissions before deleting (default 24)
//
// Until NETLIFY_API_TOKEN is set, this does nothing. That's deliberate:
// only set it after confirming the notification emails arrive.

const API = "https://api.netlify.com/api/v1";

export default async (req, context) => {
  const token = Netlify.env.get("NETLIFY_API_TOKEN");
  if (!token) {
    console.log("NETLIFY_API_TOKEN not set; skipping cleanup.");
    return;
  }
  const keepHours = Number(Netlify.env.get("KEEP_HOURS") || 24);
  const cutoff = Date.now() - keepHours * 60 * 60 * 1000;
  const siteId = context.site?.id || Netlify.env.get("SITE_ID");
  const headers = { Authorization: `Bearer ${token}` };

  // Collect old submissions first, then delete (deleting while paging would shift pages).
  const old = [];
  for (let page = 1; page <= 50; page++) {
    const res = await fetch(`${API}/sites/${siteId}/submissions?per_page=100&page=${page}`, { headers });
    if (!res.ok) {
      console.error(`Listing submissions failed: ${res.status} ${await res.text()}`);
      return;
    }
    const batch = await res.json();
    for (const s of batch) {
      if (new Date(s.created_at).getTime() < cutoff) old.push(s.id);
    }
    if (batch.length < 100) break;
  }

  let deleted = 0;
  for (const id of old) {
    const res = await fetch(`${API}/submissions/${id}`, { method: "DELETE", headers });
    if (res.ok || res.status === 404) deleted++;
    else console.error(`Delete ${id} failed: ${res.status}`);
  }
  console.log(`Deleted ${deleted} of ${old.length} submissions older than ${keepHours}h.`);
};

export const config = {
  schedule: "0 16 * * *", // 2am Brisbane (UTC+10, no DST)
};
