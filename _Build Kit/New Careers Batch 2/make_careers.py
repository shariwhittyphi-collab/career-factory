"""Assemble careers.json for Batch 2 from careers_c.py and careers_d.py. Run: python make_careers.py careers.json"""
import json, sys
import careers_c, careers_d  # careers_d adds its careers to the same list
from content_common import RESEARCH_STEPS, UNDECIDED_STEPS
PART2_INTRO = '<p>For each activity, choose whether it sounds comfortable to try. You do not need these skills already, and you can ask for support.</p>'
out = []
for c in careers_c.C:
    c = dict(c)
    if not c.get('hubGroup'):
        c.pop('hubGroup', None)
    c['sections'] = [[t, c['pay'] if b is None else b] for t, b in c['sections']]
    c['futureSteps'] = dict(c['futureSteps'], research=RESEARCH_STEPS, undecided=UNDECIDED_STEPS)
    c['part2Intro'] = PART2_INTRO
    del c['pay']
    secs = c['sections']
    assert len(secs) == 8 and '{{IMAGE0}}' in secs[1][1] and '{{IMAGE1}}' in secs[2][1], c['name']
    blob = json.dumps(c)
    for bad in ['DVR', ' VR ', 'Sheri', 'vocational rehab']:
        assert bad not in blob, (c['name'], bad)
    assert set(c['futureSteps']) == {'a', 'b', 'c', 'research', 'undecided'} and len(c['readiness']) == 8 and len(c['recs']) == 5
    assert len(c['motivation']) == 3 and len(c['future']) == 5 and len(c['nextSteps']) == 4 and c['group'], c['name']
    out.append(c)
assert len({c['slug'] for c in out}) == len(out) == 16
json.dump(out, open(sys.argv[1], 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(out), 'careers written')
