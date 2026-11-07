# APT29: Infrastructure Appendix

**Review date:** November 7, 2026

This appendix records observables identified in public vendor reporting. Campaign associations are attributed to the reporting organizations; they have not been independently corroborated through DNS, certificate, or registration analysis.

## Reported observables

| Defanged observable | Campaign context | Reported role | Source |
| --- | --- | --- | --- |
| `findcloudflare[.]com` | 2025 watering-hole investigation | Amazon identified actor-controlled infrastructure imitating Cloudflare verification pages and supporting device-code authentication lures. | [Amazon, August 29, 2025][A1] |
| `cloudflare[.]redirectpartners[.]com` | Same 2025 investigation | Amazon identified additional infrastructure following disruption, again associated with device-code authentication lures. | [Amazon, August 29, 2025][A1] |
| `cdn-gstat[.]com` | CaptiveCrunch, separately tracked 2026 activity | Microsoft included this domain in updated network hunting guidance for September/October 2026 activity attributed to Storm-2945, which Microsoft assesses as a Midnight Blizzard sub-cluster. | [Microsoft, October 5, 2026 update][A2] |

## Interpretation and limitations

- Publication and update dates do not establish registration dates or exact activity intervals for each observable.
- Current ownership, resolution, and actor control have not been verified. Historical associations may no longer apply.
- The 2025 and 2026 campaigns remain separate. These observables are not evidence for the January 2024 Microsoft intrusion analyzed in the profile.
- Shared hosting, DNS records, certificate relationships, and provider branding alone do not establish malicious ownership or actor attribution.
- The second observable is a hostname under `redirectpartners[.]com`; its reported role does not establish that every sibling hostname is malicious.

## References

- **A1:** CJ Moses, Amazon. [Amazon disrupts watering hole campaign by Russia's APT29][A1]. Published August 29, 2025; accessed November 7, 2026.
- **A2:** Microsoft Threat Intelligence. [CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft][A2]. Published July 31, 2026; updated October 5, 2026; accessed November 7, 2026.

[A1]: https://aws.amazon.com/blogs/security/amazon-disrupts-watering-hole-campaign-by-russias-apt29/
[A2]: https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
