# APT29 infrastructure research ledger

Status: three selected source-reported observables preserved; no passive pivots performed yet.

Source: CJ Moses, Amazon, [Amazon disrupts watering hole campaign by Russia's APT29](https://aws.amazon.com/blogs/security/amazon-disrupts-watering-hole-campaign-by-russias-apt29/), published August 29, 2025; reviewed November 7, 2026.

| Observable | Type | Reported relationship | Evidence status | Exact activity interval | Current status |
| --- | --- | --- | --- | --- | --- |
| `findcloudflare[.]com` | Domain | Source identifies actor-controlled infrastructure imitating Cloudflare verification | Reported by Amazon; not independently corroborated here | Unknown | Not checked |
| `cloudflare[.]redirectpartners[.]com` | Hostname | Source identifies additional infrastructure following disruption | Reported by Amazon; not independently corroborated here | Unknown | Not checked |

Selected Part 2 seed: `findcloudflare[.]com`.

Publication date is not a registration date, first-seen date, or last-seen date. Historical attribution does not establish current control. No IP addresses, certificates, or fingerprints have been collected yet. The later section preserves an additional domain from a separate 2026 campaign.

## Passive pivot record template

For each future result record:

- Query and seed observable, defanged in published prose.
- Provider, exact result URL or export reference, and lookup timestamp in UTC.
- Dataset coverage and access limitations.
- Historical first/last observation dates, where available.
- Returned observable and relationship: DNS resolution, certificate SAN, issuer, fingerprint, or registration record.
- Source-reported fact versus our inference.
- Alternative explanations such as shared hosting, wildcard certificates, reassignment, or benign service use.
- Corroboration and confidence rationale.
- Next passive research step.

Do not infer APT29 control from shared infrastructure alone. Keep the 2025 campaign separate from the January 2024 Microsoft intrusion. No direct browsing, scanning, TLS probing, or authentication against suspect infrastructure is part of this exercise.

## Current-year candidate: separate campaign

Observable: `cdn-gstat[.]com`. Microsoft's CaptiveCrunch update includes this domain in network hunting guidance for September/October 2026 activity. Current ownership and exact per-domain activity dates remain unverified.

Source: [Microsoft CaptiveCrunch report](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/), October 5, 2026 update; reviewed November 7, 2026.

This is an alternative seed if the older watering-hole domain produces insufficient passive history. Do not merge the campaign clusters without evidence.
