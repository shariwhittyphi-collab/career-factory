#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
refresh_check.py — annual data freshness check for careerfactorynd.org

WHAT THIS DOES
  Pulls the current North Dakota wage and projection figures from O*NET for all
  193 careers, compares them against what the site currently publishes, and
  writes a review report of what changed. It does NOT edit anything. You read
  the report, decide what matters, then make the edits.

  Report-only is deliberate. A median that moves 40% usually means the fetch
  broke, not that the economy did. A human should see that before it ships.

WHEN TO RUN IT
  * Late March / April each year  — new BLS wage vintage (sometimes slips to June)
  * Mid-2027, then every 2 years  — new Projections Central cycle (2026-2034 next)
  * Any time https://www.onetonline.org/help/online/datasources shows a new vintage

WHERE TO RUN IT
  On a normal machine with internet. It will NOT run inside Claude's sandbox —
  the egress proxy blocks onetonline.org for scripts.

      pip install requests
      python3 refresh_check.py --index out/search-index.json --out refresh_report

WHERE THE EDIT GOES WHEN SOMETHING CHANGED
  Two different places, because the site was built in two eras:
    * 170 careers live in the build-kit dicts (bk/tech/*.py) as W([hourly],[annual]).
      Edit the dict, re-run build + passes, push.
    * 23 careers are hand-built HTML with no dict (the early healthcare batch plus
      GIS Technologist). Edit the published HTML directly. The report marks these.
"""
import argparse, json, os, re, sys, time

ONET = 'https://www.onetonline.org/link/{kind}/{soc}?st=ND'
UA   = 'careerfactorynd.org data refresh (contact: site owner)'

# Careers with no build-kit dict — edits must be made in the HTML directly.
HANDBUILT = {
 '31-1131','29-2011','31-9091','29-1292','29-2032','29-2042','29-2061','29-2035',
 '31-9092','29-2099.01','29-2033','29-1161','31-2011','29-2057','29-2043','31-9097',
 '31-2021','29-2034','29-1141','29-1126','29-2055','29-2056','15-1299.02'}

# How big a move has to be before it is worth a human looking.
WAGE_PCT   = 2.0    # percent change in median hourly
GROWTH_PP  = 1.0    # percentage points change in projected growth
OPENINGS_PCT = 10.0 # percent change in annual openings


def fetch(url, session, tries=3):
    last = None
    for i in range(tries):
        try:
            r = session.get(url, timeout=30, headers={'User-Agent': UA})
            if r.status_code == 200:
                return r.text
            last = f'HTTP {r.status_code}'
        except Exception as e:
            last = f'{type(e).__name__}: {e}'
        time.sleep(1.5 * (i + 1))
    return None


def _nd_section(html, window):
    """Isolate the North Dakota row. Returns None if it cannot be found.

    This MUST fail rather than fall back to the whole page. An earlier version
    returned the full text when the ND anchor was missing, which silently picked
    up the United States figures and reported them as North Dakota's. A wrong
    number that looks right is far worse than a gap, because nothing flags it.
    """
    if not html:
        return None
    txt = re.sub(r'<[^>]+>', ' ', html)
    txt = re.sub(r'\s+', ' ', txt)
    i = txt.find('North Dakota')
    if i < 0:
        return None
    seg = txt[i + len('North Dakota'): i + len('North Dakota') + window]
    # Stop at the next geography so we never bleed into the US row.
    for marker in ('United States', 'U.S.', 'Nationwide'):
        j = seg.find(marker)
        if j > 0:
            seg = seg[:j]
    return seg


def parse_wages(html):
    """Return ND hourly (and annual) percentiles, or {} if the ND row is absent."""
    seg = _nd_section(html, 400)
    if seg is None:
        return {}
    hourly = [float(x.replace(',', '')) for x in re.findall(r'\$([\d,]+\.\d{2})', seg)][:5]
    annual = [int(x.replace(',', '')) for x in re.findall(r'\$([\d,]{5,})(?!\.\d)', seg)][:5]
    out = {}
    if len(hourly) >= 5:
        out['hourly'] = hourly
    if len(annual) >= 5:
        out['annual'] = annual
    # Some occupations publish annual-only (teachers are paid on contract, not
    # by the hour). Annual alone is a valid, complete answer for those.
    return out


def parse_trends(html):
    """Return ND employment now/then, percent change, annual openings."""
    seg = _nd_section(html, 300)
    if seg is None:
        return {}
    clean = [int(n.replace(',', '')) for n in re.findall(r'([\d,]+)', seg)
             if n.replace(',', '').isdigit()]
    pct = re.search(r'(-?\d+)%', seg)
    out = {}
    if len(clean) >= 2:
        out['employment'] = clean[0]
        out['projected'] = clean[1]
    if pct:
        out['pct'] = float(pct.group(1))
    elif re.search(r'no change', seg, re.I):
        out['pct'] = 0.0
    if len(clean) >= 3:
        out['openings'] = clean[-1]
    return out


def pct_change(old, new):
    if old in (None, 0) or new is None:
        return None
    return (new - old) / old * 100.0


def compare(row, w, t):
    """Return list of (field, old, new, note) that moved more than the thresholds."""
    found = []
    # Hourly, where the occupation publishes it.
    old_h = row.get('medianHourly')
    new_h = w.get('hourly', [None]*5)[2] if w.get('hourly') else None
    c = pct_change(old_h, new_h)
    if c is not None and abs(c) >= WAGE_PCT:
        found.append(('median hourly', old_h, new_h, f'{c:+.1f}%'))

    # Annual. This matters on its own for the 11 teacher pages, which are paid
    # on a yearly contract and publish NO hourly figure at all — if we only
    # compared hourly, a teacher salary change would never be reported.
    old_a = row.get('medianAnnual')
    new_a = w.get('annual', [None]*5)[2] if w.get('annual') else None
    if old_h is None or new_h is None:
        c = pct_change(old_a, new_a)
        if c is not None and abs(c) >= WAGE_PCT:
            label = ('median annual (contract pay)'
                     if row.get('payBasis') == 'annual-contract' else 'median annual')
            found.append((label, old_a, new_a, f'{c:+.1f}%'))

    old_g, new_g = row.get('ndGrowthPct'), t.get('pct')
    if old_g is not None and new_g is not None and abs(new_g - old_g) >= GROWTH_PP:
        found.append(('ND growth %', old_g, new_g, f'{new_g-old_g:+.1f} pp'))
    elif old_g is None and new_g is not None:
        found.append(('ND growth %', None, new_g, 'now published (was missing)'))

    old_o, new_o = row.get('ndOpeningsPerYear'), t.get('openings')
    c = pct_change(old_o, new_o)
    if c is not None and abs(c) >= OPENINGS_PCT:
        found.append(('annual openings', old_o, new_o, f'{c:+.1f}%'))
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--index', default='out/search-index.json')
    ap.add_argument('--out', default='refresh_report')
    ap.add_argument('--limit', type=int, default=0, help='only check the first N (smoke test)')
    ap.add_argument('--delay', type=float, default=1.0, help='seconds between requests; be polite')
    ap.add_argument('--mock', help='JSON file of fake fetch results, for testing the logic offline')
    a = ap.parse_args()

    careers = json.load(open(a.index, encoding='utf-8'))['careers']
    if a.limit:
        careers = careers[:a.limit]

    # NB: test by `a.mock is not None`, never by truthiness — an empty mock file
    # loads as {} which is falsy, and the script would silently start hitting the
    # live site instead of running offline. That bug was real; keep this explicit.
    use_mock = a.mock is not None
    mock = json.load(open(a.mock, encoding='utf-8')) if use_mock else {}
    session = None
    if not use_mock:
        try:
            import requests
        except ImportError:
            sys.exit('needs requests:  pip install requests')
        session = requests.Session()

    changed, unchanged, failed = [], 0, []
    for i, row in enumerate(careers, 1):
        soc = row['soc']
        if use_mock:
            w = mock.get(soc, {}).get('wages', {})
            t = mock.get(soc, {}).get('trends', {})
        else:
            wh = fetch(ONET.format(kind='localwages', soc=soc), session)
            time.sleep(a.delay)
            th = fetch(ONET.format(kind='localtrends', soc=soc), session)
            time.sleep(a.delay)
            w, t = parse_wages(wh), parse_trends(th)

        if not w and not t:
            failed.append((soc, row['name']))
            continue
        diffs = compare(row, w, t)
        if diffs:
            changed.append((row, diffs))
        else:
            unchanged += 1
        if not use_mock and i % 20 == 0:
            print(f'  ...{i}/{len(careers)}', file=sys.stderr)

    # If a large share failed to parse, the problem is almost certainly that O*NET
    # changed its page layout — not that those careers vanished. Say so loudly,
    # because a half-broken report is more dangerous than no report.
    fail_rate = len(failed) / max(1, len(careers)) * 100
    broken = fail_rate >= 20
    banner = []
    if broken:
        banner = ['> ## STOP — do not act on this report', '>',
                  f'> {len(failed)} of {len(careers)} careers ({fail_rate:.0f}%) could not be read.',
                  '> That is too many to be a coincidence. O*NET has almost certainly changed',
                  '> its page layout, which means the figures that *did* parse may also be wrong.',
                  '> Open one of the failing URLs in a browser, compare it to what parse_wages()',
                  '> and parse_trends() expect, and fix the parser before trusting any of this.', '']

    lines = banner + ['# Career Factory — data refresh check', '',
             f'Checked **{len(careers)}** careers against current O*NET North Dakota data.', '',
             f'- changed: **{len(changed)}**',
             f'- unchanged: {unchanged}',
             f'- could not read: {len(failed)}', '',
             f'Thresholds: wages {WAGE_PCT}%, growth {GROWTH_PP}pp, openings {OPENINGS_PCT}%.', '']
    if changed:
        lines += ['## Careers to review', '']
        for row, diffs in sorted(changed, key=lambda x: x[0]['name']):
            where = ('**hand-built HTML** — edit the page directly'
                     if row['soc'].replace('.00','') in HANDBUILT or row['soc'] in HANDBUILT
                     else 'build-kit dict')
            lines.append(f"### {row['name']}  ({row['areaName']})")
            lines.append(f"SOC {row['soc']} · {where} · `{row['url']}`")
            lines.append('')
            lines.append('| field | published | current | change |')
            lines.append('|---|---|---|---|')
            for f, o, n, note in diffs:
                lines.append(f'| {f} | {o} | {n} | {note} |')
            lines.append('')
    if failed:
        lines += ['## Could not read', '',
                  'Check these by hand — a parse failure usually means O*NET changed its page layout.', '']
        lines += [f'- {n} ({s})' for s, n in failed] + ['']

    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    open(a.out + '.md', 'w', encoding='utf-8').write('\n'.join(lines))
    json.dump({'changed': [{'soc': r['soc'], 'name': r['name'],
                            'diffs': [{'field': f, 'old': o, 'new': n, 'note': d} for f, o, n, d in ds]}
                           for r, ds in changed],
               'failed': [{'soc': s, 'name': n} for s, n in failed],
               'unchanged': unchanged, 'failRatePct': round(fail_rate,1),
               'parserProbablyStale': broken},
              open(a.out + '.json', 'w', encoding='utf-8'), indent=1)
    if broken:
        print(f'WARNING: {fail_rate:.0f}% of pages failed to parse — the parser is probably stale.',
              file=sys.stderr)
    print(f'{len(changed)} changed, {unchanged} unchanged, {len(failed)} unreadable')
    print(f'wrote {a.out}.md and {a.out}.json')


if __name__ == '__main__':
    main()
