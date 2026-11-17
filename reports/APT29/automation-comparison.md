# Automating the APT29 Infrastructure Investigation

**Research date:** November 17, 2026  
**Purpose:** Compare automated passive lookups with the earlier manual investigation and reduce stale IP-neighbor pivots.

## Summary

I ran an existing passive domain-pivot tool against `cdn-gstat[.]com`, compared its output with my manual infrastructure investigation, and added an optional `--days` filter.

The tool reproduced the four passive DNS observations previously collected manually. Its safeguards also illustrated two tradeoffs: a busy-IP rule suppressed useful campaign-period neighbors, while a relative “same week” label included a relationship from 2020. My change addresses stale resolution pivots; it does not establish maliciousness or solve the busy-IP coverage limitation.

## Code and attribution

- [My tool fork](https://github.com/niccosabella/cti-portfolio-tools)
- [Date-filter implementation and tests](https://github.com/niccosabella/cti-portfolio-tools/commit/ea3871537b3c99a9d804b1cbf1833a6202d880c9)
- [Original MIT-licensed tool](https://github.com/CTIJen/cti-portfolio-tools)
- [Manual infrastructure investigation](infrastructure-investigation.md)

The original tool supplies registration, certificate, passive DNS, and IP-neighbor collection. My contribution adds resolution-age filtering, eight unit tests, and usage documentation.

## Method

The runs used Python 3.15.2 on Windows. API credentials were supplied through a session environment variable rather than embedded in code. Requests went to existing third-party registration, certificate, and VirusTotal records; no suspect infrastructure was visited or scanned.

The starting domain remained `cdn-gstat[.]com`. SAN expansion was disabled with `--rounds 0 --max-domains 1`. Registration and certificate records were collected first, followed by VirusTotal resolutions and bounded IP-neighbor lookups.

## Manual versus automated results

| Finding | Comparison and interpretation |
| --- | --- |
| Four DNS observations | The script reproduced the manually recorded dates and IPs: `1.1.1[.]1` on October 1, `154.29.75[.]245` on September 26, `185.53.179[.]128` on September 17, and `209.58.186[.]193` on December 27, 2020. |
| Certificate records | Four records were returned across the successful queries, including September 2026 records and older 2020–2021 history. Old certificates do not establish continuity of actor control. |
| Partial crt.sh failures | Exact-domain and wildcard queries failed independently in different runs. One failed query did not mean all certificate collection failed. |
| Busy-IP suppression | The script reported 40+ associations and omitted neighbors for three addresses, including the campaign-associated IP. Manual inspection of that IP had exposed `sslcdnhost[.]com` and two unconfirmed candidates. |
| Historical “same week” result | `www.cdn-gstat[.]com` matched a December 2020 resolution. The label described proximity between records, not recent campaign activity. |
| Server and fingerprint data | Shodan/Censys investigation remained outside the script. Earlier access limitations still prevented JARM or JA4X conclusions. |

Registrar and nameserver rows are registration context, not actor-identification evidence. Their date field uses the domain creation date; it does not prove when those assignments began.

The busy-IP count reflects returned historical associations, not proven simultaneous hosting. The examined API function requests up to 40 records without pagination, so its output is not an exhaustive history.

## Change: optional UTC resolution-age filtering

`--days N` restricts the resolutions processed to UTC calendar dates from today through N days ago, inclusive. The check runs before saving a resolution or requesting its IP neighbors.

```powershell
py .\pivot_out.py 'cdn-gstat[.]com' --rounds 0 --max-domains 1 --days 90
```

- Omitting the option preserves the original behavior.
- Zero includes only today's resolutions; negative values are rejected.
- Missing, malformed, and future dates are excluded when the filter is enabled.
- Certificates and registration records are not filtered.
- Neighbor dates remain subject to the existing relative `--window` logic; they are not independently filtered by `--days`.

The purpose is to bound a current-infrastructure investigation and avoid requests on stale resolution branches. Historical investigations may appropriately omit the filter or use a different research scope.

## Validation

The original nine unit tests passed before changes. Eight new tests cover default behavior, recent and old dates, the inclusive boundary, a date beyond the boundary, zero-day behavior, invalid or missing dates, and future dates.

```text
Ran 17 tests
OK
```

Tests use a fixed reference date so results do not drift with the calendar. They validate date-selection behavior, not the accuracy or availability of external APIs.

| Live run | Findings | Interpretation |
| --- | --- | --- |
| Without VT credentials | 7 | Registration and certificate rows only |
| VT enabled, neighbors skipped | 11 | Added four resolutions |
| Neighbors enabled, no age filter | 17 | Included the old resolution and three historical neighbors |
| Neighbors enabled, `--days 90` | 13 | Printed an explicit skip for the December 2020 resolution |

The four-row reduction is consistent with excluding the old resolution and its three neighbors. The terminal skip message directly confirms exclusion of that resolution; API-request counts were not instrumented. Zero same-week neighbors in the filtered run does not mean the recent IPs have none: busy-IP suppression still applies.

## Limitations and lessons

Automation makes repeated collection easier but does not replace campaign analysis. Shared IPs, common registrars, and certificate issuers remain leads rather than attribution proof. A historical association does not establish current control.

The date filter does not correct busy-IP suppression, incomplete API coverage, intermittent certificate services, or missing fingerprint data. It also depends on the run date; future reruns can legitimately exclude records included in this run.

## Disclosure

I performed the local runs, edits, tests, and Git commits with guidance.
