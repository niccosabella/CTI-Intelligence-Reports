"""Offline behavioral model of Hunt 1; not a KQL execution test.

Uses only synthetic events and Python's standard library. No network access.
Run: python3 test_cti_hunt.py
"""
import csv
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
START = datetime.fromisoformat('2026-09-01T00:00:00+00:00')
END = datetime.fromisoformat('2026-11-01T00:00:00+00:00')
DOMAINS = ('cdn-gstat.com', 'sslcdnhost.com')
IP = '154.29.75.245'


def classify(row):
    timestamp = datetime.fromisoformat(row['Timestamp'].replace('Z', '+00:00'))
    if not START <= timestamp < END:
        return 'No match'
    raw = row['RemoteUrl'].strip().lower()
    try:
        host = (urlsplit(raw if '://' in raw else 'https://' + raw).hostname or '').rstrip('.')
    except ValueError:
        host = ''
    domain_match = any(host == domain or host.endswith('.' + domain) for domain in DOMAINS)
    ip_match = row['RemoteIP'] == IP
    if domain_match and ip_match:
        return 'Reported domain and IP'
    if domain_match:
        return 'Reported domain or subdomain'
    if ip_match:
        return 'Reported IP only: check hosting context'
    return 'No match'


def main():
    with (ROOT / 'synthetic_events.csv').open(newline='', encoding='utf-8') as source:
        rows = list(csv.DictReader(source))
    results = []
    for row in rows:
        actual = classify(row)
        passed = actual == row['Expected']
        results.append(dict(row, Actual=actual, Passed=passed))
        print(f"{'PASS' if passed else 'FAIL'} {row['Case']}: {actual}")
    with (ROOT / 'test_results.csv').open('w', newline='', encoding='utf-8') as target:
        writer = csv.DictWriter(target, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)
    failures = sum(not result['Passed'] for result in results)
    print(f'\n{len(results) - failures}/{len(results)} passed.')
    print('Synthetic Python behavior checks only. KQL syntax, parse_url behavior,')
    print('tenant schemas, telemetry coverage, and production detections remain unvalidated.')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
