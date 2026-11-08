# APT29 infrastructure: MISP and OpenCTI workflow

## Objective

Convert an existing passive infrastructure investigation into structured, traceable intelligence for historical SOC hunting. This home-lab exercise uses public research and synthetic events; no employer data or corporate telemetry was used.

Supporting investigation: [Cloud Identity Infrastructure: APT29-Associated Domain Investigation](infrastructure-investigation.md).

## MISP evidence curation

Created event 1684, **APT29 — Source-reported infrastructure supporting cloud identity research**, with organisation-only distribution, ongoing analysis, and undefined threat level. The event was left unpublished during this exercise.

Recorded five attributes:

| Type | Value | Purpose |
|---|---|---|
| domain | `cdn-gstat.com` | Source-reported infrastructure |
| domain | `sslcdnhost.com` | Source-reported infrastructure |
| ip-dst | `154.29.75.245` | Historical destination infrastructure |
| link | Microsoft CaptiveCrunch article | Original reporting cited by the investigation |
| link | GitHub infrastructure investigation | Supporting analysis and limitations |

Infrastructure attributes retain source references, historical observations, and current-control limitations. IDS flags were left unchecked and correlation remained enabled. Added the MITRE ATT&CK Groups **APT29 — G0016** cluster and an Event Report summarizing purpose, evidence, recommended use, and limitations.

Unconfirmed neighboring domains were excluded from this event's source-reported infrastructure set. Actor associations follow the original reporting; they are not independent attribution findings.

## OpenCTI ingestion and review

The existing MISP connector imported the event as a report attributed to CTI-LAB. Its graph contained three indicators, two domain observables, one IPv4 observable, and APT29, with nine imported relationships: three `based-on`, three `indicates`, and three `related-to` connections.

The MISP Event Report was accessible as a Note under the imported report's Overview. The report's Content view showed its title as the description rather than the full investigation summary.

Added two `resolves-to` relationships between existing observables:

| Source | Target | Historical record date |
|---|---|---|
| `cdn-gstat.com` | `154.29.75.245` | September 26, 2026 |
| `sslcdnhost.com` | `154.29.75.245` | September 30, 2026 |

Relationship descriptions preserve dates, source references, and limits. Start and stop timestamps were intentionally left unset because the reviewed evidence did not preserve exact observation times or continuous intervals. These records do not establish simultaneous hosting, common ownership, current resolution, or current actor control.

The resulting graph contains the original seven entities and two additional DNS relationships.

## Import validation findings

Inspected the imported `cdn-gstat.com` indicator and the installed connector's source code.

| Finding | Evidence and interpretation |
|---|---|
| Exact-domain pattern | `[domain-name:value = 'cdn-gstat.com']`; the pattern itself does not match subdomains. |
| Detection disabled | The indicator showed Detection: No and processing status disabled. Connector code copies MISP `to_ids` into `x_opencti_detection`. |
| Record dates differ from activity dates | Connector code assigns indicator `valid_from` from the MISP attribute timestamp. It does not represent the September DNS observation. |
| Lifecycle applies | The panel displayed an initial score of 40, a revocation threshold of 20, and a projected threshold crossing in approximately two months. This is consistent with the displayed January 2027 validity end, but does not prove the full derivation. |
| Confidence requires review | Imported information displayed “Confirmed by other sources.” The origin of that rating was not established. It must not be read as independent confirmation of attribution or current control. |
| Unpublished ingestion occurred | The unpublished MISP event was present in OpenCTI. The bundled sample documents `import_only_published` defaulting to false and `create_indicators` defaulting to true. Full effective configuration was not established. |

The connector's source maps `import_to_ids_no_score` into its internal `default_attribute_score`. The displayed initial score of 40 was not conclusively traced to an effective runtime setting. Neither confidence nor `valid_until` was explicitly assigned in the connector files searched; this does not exclude assignment by libraries or the platform.

A validation Note was attached to the indicator. No connector configuration was changed during this review.

## Synthetic matching checks

An AI-assisted standalone Python model was executed locally against 18 synthetic cases. All 18 passed their predefined expected results. The model covers the intended matching behavior of the investigation's first historical KQL hunt, including:

- Exact domain and subdomain matches.
- Full URL parsing, mixed case, whitespace, trailing dots, and ports.
- Rejection of prefix/suffix lookalikes and domains appearing only in URL paths or user information.
- Separate domain-and-IP, domain-only, and IP-only match classifications.
- Exclusion of unconfirmed candidate domains unless the reported IP independently matches.
- Inclusive September 1 and exclusive November 1, 2026 boundaries.

Files: [test script](test_cti_hunt.py), [synthetic cases](synthetic_events.csv), and [execution results](test_results.csv).

Run with Python 3, with both input files in the same directory:

```bash
python3 test_cti_hunt.py
```

This is a Python behavioral test, not execution or validation of the actual KQL. Python URL parsing may differ from KQL `parse_url`. KQL syntax, tenant schemas, telemetry coverage, production performance, and detection effectiveness remain unvalidated. No Sentinel or Defender access was available. The second candidate-domain hunt was not tested by this script. Synthetic timestamps are fixtures, not evidence of real activity.

## Operational boundaries and remaining work

- Keep historical research distinct from current blocking recommendations.
- Review confidence and initial-score provenance before operational use.
- Apply explicit downstream export criteria; Detection: No alone does not demonstrate that every possible consumer will exclude the record.
- Keep MISP's distribution model distinct from OpenCTI markings and access controls; ingestion does not establish equivalent access restrictions.
- Execute and validate the actual KQL in an authorized Kusto environment when available.
- Compare the manually created analysis report with the connector-imported report before deciding whether both are useful; no duplicate report was deleted during this exercise.

## Skills demonstrated

Evidence curation, source provenance, MISP attribute and galaxy modeling, connector validation, OpenCTI graph modeling, temporal uncertainty handling, indicator lifecycle interpretation, and synthetic testing of hunting logic.

## Disclosure

AI assisted with workflow guidance, analysis, documentation, and the Python test harness. Findings distinguish observed UI behavior and inspected code from unresolved defaults and analytical interpretation. No claim of newly discovered APT29 infrastructure or production detection validation is made.
