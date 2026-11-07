# APT29: Cloud Identity Threat Profile

**Review date:** November 7, 2026  
**Evidence scope:** Selected reporting from January 2024 through the October 5, 2026 source update  
**Collection cutoff:** November 7, 2026  
**Audience:** SOC Director at a representative U.S. defense contractor using Microsoft 365 and Entra ID

An independent public-source assessment of cloud identity threats to a representative U.S. defense contractor.

**Intelligence requirement:** Is APT29 a threat to us, and what should we do about it?

**Focus:** Cloud identity exposure in Microsoft 365 and Entra ID.

## Executive summary

APT29 is likely relevant to a representative U.S. defense contractor because public reporting documents defense-sector targeting and cloud account abuse. The SOC Director should first close legacy account protection gaps and review application access to email, then restrict unnecessary device-code authentication and validate identity-to-mailbox monitoring. Sensitive correspondence could be exposed if accounts or application permissions are compromised. [S2] [S3] [S5]

This is an assessment of relevance, not evidence of organization-specific targeting or compromise. Selected reporting includes a 2026 campaign update, while the detailed cloud intrusion case is historical. The effectiveness of existing defenses cannot be evaluated without organizational telemetry and configuration evidence. [S8]

## About APT29

### Names and tracking scope

Public reporting associates several names with APT29. A shared association does not establish that each vendor tracks precisely the same activity. Campaign descriptions retain each source’s original designation.

| Name | Reporting organization or usage | Interpretation | Source |
| --- | --- | --- | --- |
| APT29 | MITRE ATT&CK identifier G0016; used in government and industry reporting | Primary label used in this profile | [S1] |
| Midnight Blizzard | Microsoft | Microsoft's designation; Microsoft explicitly relates it to APT29 | [S2] |
| NOBELIUM | Microsoft | Earlier Microsoft designation identified alongside Midnight Blizzard | [S2] |
| Cozy Bear | CrowdStrike; also used by other sources | Associated designation; preserve campaign context | [S1] |
| The Dukes | F-Secure, ESET, and government reporting | Historical associated designation | [S1] |
| UNC2452 | FireEye/Mandiant | Appears in SolarWinds investigation reporting; do not automatically extend that cluster label to all APT29 activity | [S1] |

Additional names listed in MITRE's associated-group table are recorded below. These associations do not establish identical tracking scope. [S1]

| Associated name | Source organization identified by MITRE | Context |
| --- | --- | --- |
| IRON RITUAL | Sophos | Associated tracking designation |
| IRON HEMLOCK | Secureworks | Associated tracking designation |
| NobleBaron | SentinelOne | Associated tracking designation |
| Dark Halo | Volexity | SolarWinds-related reporting |
| YTTRIUM | Microsoft | Historical designation |
| CozyDuke | CrowdStrike | Historical designation |
| SolarStorm | Palo Alto Networks Unit 42 | SolarWinds-related reporting |
| Blue Kitsune | PwC | Associated tracking designation |
| UNC3524 | Mandiant | Associated cluster; retain original source context |

This inventory follows the reviewed MITRE entry rather than claiming a universal list. Microsoft additionally identifies Storm-2945 and Storm-2372 as sub-clusters, not synonyms for all APT29 activity. [S8]

### Actor overview

APT29 is a state-linked espionage actor attributed to Russia's SVR. Public reporting describes intelligence collection, valid-account abuse, and manipulation of cloud authentication and application access. Its specializations relevant here are obtaining access to identities and using that access to reach email. [S1] [S2]

Assessment: The selected evidence suggests substantial operational capability: the actor combines account attacks, permission abuse, and concealment rather than depending on one entry method. This describes demonstrated behavior, not a measured budget or a claim that every campaign is equally sophisticated. [S2] [S3]

### Attribution

MITRE records U.S. and U.K. government attribution to Russia's Foreign Intelligence Service (SVR). This profile reports that attribution; it does not claim to have independently established sponsorship. [S1]

## Targeting and relevance

### Documented targets

The October 2024 joint government advisory identifies defense, technology, and finance among targeted sectors. It distinguishes deliberate intelligence targets, including cleared defense contractors, from opportunistic victims whose vulnerable systems can support further operations. Its geographic scope extends beyond North America and Europe. [S3]

Microsoft's separate October 2024 RDP phishing investigation documented government, higher education, defense, and NGO targets, especially in the U.K., Europe, Australia, and Japan. Targeting is not proof that every recipient was compromised. [S4]

### Relevance to the scenario

Assessment: Its defense-sector role makes it relevant to documented targeting. Its cloud identities could provide access to sensitive correspondence or relationships. Actual exposure depends on its data, privileges, controls, and partners; sector membership alone does not establish targeting or compromise. [S2] [S3]

### Campaign context

Amazon's August 2025 report adds a newer example: compromised websites redirected visitors into a device-code authentication lure intended to authorize attacker-controlled devices. Amazon described the campaign as opportunistic; it does not establish defense-specific targeting. [S5]

Microsoft's October 5, 2026 update reports renewed CaptiveCrunch activity by Storm-2945 on September 29, involving hospitality networks and cloud authentication lures. This adds current-year evidence without establishing defense-specific targeting in that campaign. [S8]

The cases below remain separate. The source set does not establish a typical dwell time; reporting dates are not treated as access durations.

### Selected activity timeline

| Date or reporting period | Distinct case | Relevance | Source |
| --- | --- | --- | --- |
| January 2024 disclosure | Microsoft cloud intrusion | Test account compromise followed by application-based email access | [S2] |
| October 22, 2024 onward, as reported October 29 | RDP attachment phishing | Defense organizations among the targets | [S4] |
| August 29, 2025 publication | Watering-hole investigation | Device-code lures and two saved domains | [S5] |
| September 29, 2026 activity; October 5 update | CaptiveCrunch resumption | Additional evidence of cloud identity exposure through traveler-focused operations | [S8] |

## Diamond Model: Microsoft cloud intrusion disclosed January 2024

### Case evidence

The table describes one historical case using Microsoft's firsthand reporting. It does not describe an intrusion into the representative organization. [S2]

| Element | Attribute | Evidence and limits | Source |
| --- | --- | --- | --- |
| Adversary | Origin | Russia-based actor attributed to the SVR; attribution is reported rather than independently established here. | [S2] |
| Adversary | Motivation | Intelligence collection supporting Russian foreign policy interests. | [S2] |
| Adversary | Activity | Microsoft identified Midnight Blizzard as responsible for the selected cloud intrusion. | [S2] |
| Victim | Targeting | Microsoft's legacy test environment and corporate email accounts in this case. | [S2] |
| Victim | Locations | Victim tenant and mailbox locations are not established by the evidence extracted here; broader actor geography is not substituted for case evidence. | [S2] |
| Victim | Systems | Cloud identities, OAuth applications, and Exchange Online. | [S2] |
| Capabilities | IN | Password spraying compromised a test account without MFA. | [S2] |
| Capabilities | THROUGH | Application privileges enabled additional identities, applications, and mailbox permission grants. | [S2] |
| Capabilities | OUT | Application-based access to corporate email through Exchange Web Services. | [S2] |
| Infrastructure | Attack infrastructure | Residential proxy networks obscured connections to the tenant and Exchange Online; individual endpoints are not attributed here. | [S2] |
| Infrastructure | Support infrastructure | Separate staging or management systems are not identified in the evidence extracted for this case. | [S2] |

### Defensive implication

Assessment: Investigate the connection between account access, application permissions, and mailbox activity. A password reset alone may leave application-based access unresolved. Residential proxies also make source-IP blocklists insufficient. [S2]

## Tactics, techniques, and procedures

### Operational sequence: January 2024 cloud case

- **IN:** Password spraying obtained an account lacking MFA.
- **THROUGH:** Existing application privileges enabled additional accounts, applications, and permission grants.
- **OUT:** Application-based Exchange access enabled email collection.

This sequence summarizes the selected case rather than a mandatory pattern for every APT29 operation. [S2]

### Tools and access mechanisms

OAuth applications and Exchange Web Services are legitimate mechanisms abused in this case. Residential proxies obscured connections. The evidence does not require a named malware family to explain the access path; the selected five mappings focus on identity and email behavior. [S2]

### Five ATT&CK mappings

These are analyst mappings of behavior Microsoft reported in January 2024, checked against MITRE definitions on November 7, 2026. They are not a claim that Microsoft assigned these exact IDs. [S2]

| ATT&CK technique | Reported behavior | Suggested defender observable | Sources |
| --- | --- | --- | --- |
| [T1110.003: Password Spraying](https://attack.mitre.org/techniques/T1110/003/) | Low-volume password spraying compromised a test account without MFA. | Correlated sign-in failures across accounts and time, followed by success; avoid relying on high-volume thresholds alone. | [S2], linked MITRE definition |
| [T1078.004: Cloud Accounts](https://attack.mitre.org/techniques/T1078/004/) | The actor used the compromised cloud account to gain initial access. | Successful sign-ins inconsistent with the account's normal device, network, or usage pattern. | [S2], linked MITRE definition |
| [T1136.003: Cloud Account](https://attack.mitre.org/techniques/T1136/003/) | A new user account was created to grant consent to malicious applications. | Account creation followed by application consent; examine initiating identity and approved change context. | [S2], linked MITRE definition |
| [T1098.002: Additional Email Delegate Permissions](https://attack.mitre.org/techniques/T1098/002/) | Malicious applications received full_access_as_app mailbox permissions. | Application permission grants and consent changes enabling broad mailbox access. | [S2], linked MITRE definition |
| [T1114.002: Remote Email Collection](https://attack.mitre.org/techniques/T1114/002/) | Malicious applications authenticated to Exchange Online to access corporate email. | Unusual application mailbox access, EWS activity, or changes in access volume and mailbox scope. | [S2], linked MITRE definition |

### Telemetry and interpretation

The observable column contains proposed investigation leads, not telemetry we collected or tested detections. Sign-in, directory audit, application, and mailbox records must be available and retained; visibility varies by configuration and licensing. Legitimate administration can produce similar events. Correlate identities, application IDs, timestamps, permissions, and change records before concluding activity is malicious.

### Mapping rationale

The supporting behavior is granting mailbox access, not merely creating an application or adding its secret. MITRE's APT29 entry includes application permissions under this technique. Application-only access should not be described as ordinary user-delegated OAuth consent. The historical permission name is preserved as reported; current defensive configuration requires separate validation. [S1] [S2]

## Historical infrastructure

### Reported observables

Amazon reported two domains in its August 29, 2025 investigation of an APT29 watering-hole campaign. Its investigation described compromised websites redirecting visitors to infrastructure that imitated Cloudflare verification and lured users into authorizing attacker-controlled devices through Microsoft's device-code flow. These are historical source-reported associations, not independently verified current ownership. [S5]

| Defanged observable | Source-reported role | Time context | Current status |
| --- | --- | --- | --- |
| `findcloudflare[.]com` | Actor-controlled redirect destination imitating Cloudflare verification | Report published August 29, 2025; exact registration and activity interval not established here | Not checked |
| `cloudflare[.]redirectpartners[.]com` | Additional infrastructure observed after disruption, again directing users toward device-code authentication lures | Report published August 29, 2025; exact activity dates not established here | Not checked |

### Research starting point

Selected starting point: `findcloudflare[.]com`. It is directly identified in the source and provides a domain for passive certificate, DNS, and registration-history research. A useful pivot result is not guaranteed. The second observable is a subdomain of `redirectpartners[.]com`; shared parentage or hosting alone would not establish maliciousness of sibling names.

These observables belong to the 2025 campaign, separate from the Diamond Model case. Provider branding in a lure does not establish provider compromise; Amazon reported no compromise of AWS systems. [S5]

### Research method

`cdn-gstat[.]com` is an additional current-year research candidate from Microsoft’s updated network hunting guidance. It is associated with the separate CaptiveCrunch case; current control is unverified. [S8]

The companion [infrastructure ledger](infrastructure-notes.md) records research provenance. Record lookup time, dataset coverage, historical observation dates, exact relationships, and alternative explanations. Treat shared certificates, hosting, or DNS as leads rather than automatic actor attribution. Keep observables defanged in published prose. Research will use third-party records rather than direct connections to suspect infrastructure.

## Defensive priorities

### Prioritized actions

These are proposed priorities for the representative organization, not findings from an environment assessment. Owners and completion evidence make the recommendations reviewable.

| Priority | Recommended action and rationale | Suggested owner | Evidence of completion | Basis |
| --- | --- | --- | --- | --- |
| 1 | Inventory legacy/test tenants and inactive user accounts; remove unnecessary access and enforce phishing-resistant MFA for human identities. The reported initial compromise involved a test account without MFA. | Identity team | Account inventory, documented exceptions, and validated authentication-policy coverage | [S2] [S3] |
| 2 | Review application identities, consent, credentials, and mailbox permissions. Remove unjustified grants and scope legitimate applications to required resources. Human MFA does not govern app-only access in the same way. | Identity and messaging teams | Application owners assigned; excessive grants removed; access scope verified | [S2] [S7] |
| 3 | Establish a baseline for legitimate device-code use, then restrict unnecessary use through Conditional Access. Assess policy impact in report-only mode and document required exceptions before enforcement. | Identity team | Usage baseline, policy-impact review, and approved exceptions | [S5] [S6] |
| 4 | Verify collection and retention of user and service-principal sign-ins, directory changes, application consent, and mailbox activity. Validate correlated investigation logic with authorized test activity. | SOC | Log-coverage inventory and documented results from controlled validation | [S2]; proposed validation workflow |

### Human and application identities

Protecting human sign-ins does not eliminate malicious application permissions or all authorization abuse. Service-principal controls require separate design; Microsoft documents workload-identity Conditional Access with specific scope and licensing requirements. Device-code policies address a different authentication pathway. [S6] [S7]

### Response considerations

Proposed response: preserve relevant evidence and scope the incident across accounts, applications, permissions, and accessed mailboxes. Contain affected identities, sessions, application credentials, and unauthorized grants as appropriate to the findings. Verify that access is removed rather than treating a user password reset as complete remediation. No incident response actions have been performed in this exercise.

## Intelligence gaps and assessment limits

### Unresolved questions

- Organizational exposure: account inventories, application grants, sensitive data, control coverage, and partner access are hypothetical or unknown.
- Current activity: the latest included source update is October 5, 2026. The profile is selective and does not establish activity against this representative organization or continuous activity through the collection cutoff.
- Infrastructure: exact activity intervals, historical resolutions, certificates, and current control of the saved domains are unverified.
- Detection effectiveness: proposed observables have not been tested; logging, retention, licensing, and normal administrative behavior affect visibility.
- Dwell time and impact: this source set does not establish a typical dwell time or a loss estimate for the representative organization.
- Attribution: public government and vendor assessments are cited; underlying attribution evidence has not been independently examined.

## Source evaluation and method

| Source set | Value to this assessment | Limitation |
| --- | --- | --- |
| MITRE [S1] | Normalizes names and links behavior to original references | A synthesis, not independent confirmation of each underlying report |
| Microsoft [S2], [S4], [S8] | Firsthand investigations, technical observations, and campaign context | Visibility and attribution reflect Microsoft's evidence; telemetry was not independently examined |
| Joint government advisory [S3] | Sector targeting and broader operational context | Public evidence does not expose the full attribution basis |
| Amazon [S5] | Campaign investigation and explicit infrastructure associations | Domain roles remain source-reported; current ownership is unknown |
| Microsoft documentation [S6], [S7] | Implementation context for proposed controls | Product guidance is not evidence of APT29 behavior or proof a control works in this scenario |

Source authority and claim support are evaluated separately. Independent corroboration is not assumed merely because two publications repeat the same attribution. Unknown details remain gaps instead of being filled with assumptions.

This assessment uses an illustrative organizational scenario and public reporting; no organization-specific telemetry was examined. Reported facts are attributed to their sources; scenario implications, mappings, observables, and priorities are analytical work. Sources may reference the same underlying investigations, so repeated reporting is not counted as independent corroboration. No victim telemetry, direct infrastructure probing, or tested detection results are presented.

AI assisted with research organization and drafting. No employment-related or nonpublic operational information was used.

## References

Core collection: MITRE [S1], the government advisory [S3], and vendor investigations [S2], [S5], [S8]. The separate RDP case [S4] supplies additional targeting context; [S6] and [S7] are implementation references.

- [S1] MITRE ATT&CK. [APT29, G0016](https://attack.mitre.org/groups/G0016/). Accessed November 7, 2026.
- [S2] Microsoft Threat Intelligence. [Midnight Blizzard: Guidance for responders on nation-state attack](https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/). January 25, 2024. Accessed November 7, 2026.
- [S3] FBI, NSA, CNMF, NCSC-UK. [Update on SVR Cyber Operations and Vulnerability Exploitation](https://www.ic3.gov/CSA/2024/241010.pdf). October 10, 2024. Accessed November 7, 2026.
- [S4] Microsoft Threat Intelligence. [Midnight Blizzard conducts large-scale spear-phishing campaign using RDP files](https://www.microsoft.com/en-us/security/blog/2024/10/29/midnight-blizzard-conducts-large-scale-spear-phishing-campaign-using-rdp-files/). October 29, 2024. Accessed November 7, 2026.
- [S5] CJ Moses, Amazon. [Amazon disrupts watering hole campaign by Russia's APT29](https://aws.amazon.com/blogs/security/amazon-disrupts-watering-hole-campaign-by-russias-apt29/). August 29, 2025. Accessed November 7, 2026.
- [S6] Microsoft Learn. [Block authentication flows with Conditional Access policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows). Accessed November 7, 2026.
- [S7] Microsoft Learn. [Conditional Access for workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity). Accessed November 7, 2026.

- [S8] Microsoft Threat Intelligence. [CaptiveCrunch: Midnight Blizzard targets travelers worldwide for malware delivery and credential theft](https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/). July 31, 2026; updated October 5, 2026. Accessed November 7, 2026.

[S8]: https://www.microsoft.com/en-us/security/blog/2026/07/31/captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-malware-delivery-and-credential-theft/
[S1]: https://attack.mitre.org/groups/G0016/
[S2]: https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/
[S3]: https://www.ic3.gov/CSA/2024/241010.pdf
[S4]: https://www.microsoft.com/en-us/security/blog/2024/10/29/midnight-blizzard-conducts-large-scale-spear-phishing-campaign-using-rdp-files/
[S5]: https://aws.amazon.com/blogs/security/amazon-disrupts-watering-hole-campaign-by-russias-apt29/
[S6]: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows
[S7]: https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity

