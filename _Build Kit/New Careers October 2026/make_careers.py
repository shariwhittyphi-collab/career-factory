"""Assemble careers.json from the content files. Run: python make_careers.py <out>"""
import json, sys
import careers_a, careers_b, overrides
from content_common import RESEARCH_STEPS, UNDECIDED_STEPS
GROUPS = {'jobs-you-can-start-now': ('Offices and Banks', None), 'business-finance': ('Accounting and Taxes', 'Accounting and Taxes'),
          'healthcare': ('Support Services', 'Support Services'), 'education': ('Classroom Teachers', 'Classroom Teachers')}
out = []
for c in careers_a.C + careers_b.C:
    c = dict(c)
    c['group'], hg = GROUPS[c['area']]
    if hg: c['hubGroup'] = hg
    secs = []
    for t, b in c['sections']:
        secs.append([t, c['pay'] if b is None else b])
    c['sections'] = secs
    c['readiness'] = overrides.READINESS[c['slug']]
    c['futureSteps'] = dict(c['futureSteps'], research=RESEARCH_STEPS, undecided=UNDECIDED_STEPS)
    for slug, old, new in overrides.FIXES:
        if slug == c['slug']:
            hits = sum(b.count(old) for t, b in c['sections'])
            assert hits == 1, (slug, old[:40], hits)
            c['sections'] = [[t, b.replace(old, new)] for t, b in c['sections']]
    c['part2Intro'] = overrides.PART2_INTRO
    del c['pay']
    assert len(secs) == 8 and '{{IMAGE0}}' in secs[1][1] and '{{IMAGE1}}' in secs[2][1], c['name']
    blob = json.dumps(c)
    for bad in ['DVR', ' VR ', 'Sheri']:
        assert bad not in blob, (c['name'], bad)
    assert set(c['futureSteps']) == {'a', 'b', 'c', 'research', 'undecided'} and len(c['readiness']) == 8 and len(c['recs']) == 5
    out.append(c)
json.dump(out, open(sys.argv[1], 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(out), 'careers written')
