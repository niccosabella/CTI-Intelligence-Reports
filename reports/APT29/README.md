# APT29: Cloud Identity Threat Analysis

## Overview

This project examines APT29’s cloud identity operations and their relevance to a representative U.S. defense contractor using Microsoft 365 and Entra ID.

It combines a threat actor profile with a passive infrastructure investigation. Findings distinguish source-reported campaign associations, observed infrastructure relationships, analytical judgments, and unresolved candidates.

## Reports

- [Threat Actor Profile](assessment.md) — Actor background, targeting, Diamond Model analysis, five ATT&CK mappings, and defensive priorities.
- [Infrastructure Investigation](infrastructure-investigation.md) — Registration, certificate, and passive DNS evidence; a Mermaid infrastructure map; and proposed KQL hunting queries.

## Research Objectives

- Document actor names, attribution, targeting, and operational capabilities.
- Analyze a reported cloud intrusion using the Diamond Model.
- Map documented behaviors to MITRE ATT&CK techniques.
- Investigate infrastructure relationships using existing third-party records.
- Distinguish reported campaign infrastructure from unconfirmed candidates.
- Develop evidence-based SOC hunting recommendations.

## Scope and Methodology

The threat actor profile uses selected reporting from 2024 through an October 2026 source update, with a collection cutoff of November 7, 2026.

The infrastructure investigation was conducted on November 7, 2026, EST, with recorded UTC lookups extending into November 8. Research used ICANN Lookup, certificate transparency records, VirusTotal, Shodan, and the accessible Censys host view.

Only existing third-party records were consulted. No direct visits, probes, or new scans of suspect infrastructure were performed.

Historical infrastructure associations do not establish current ownership or control. Shared hosting and common registration services are treated as investigative leads rather than proof of campaign membership.

## SOC Hunting Queries

The infrastructure report includes two proposed KQL hunts using `DeviceNetworkEvents`:

- Source-reported campaign domains and IP infrastructure.
- Unconfirmed neighboring domains, evaluated separately.

The queries have not been validated against organizational telemetry. Historical hunting requires sufficient data retention, and matches require investigation rather than automatic attribution or blocking.

## Disclosure

This project represents independent research for educational and professional development purposes. It does not represent an official assessment from any employer or government organization. No employer information or private incident telemetry was used.
