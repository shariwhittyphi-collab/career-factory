"""Build the October 2026 new careers into the web edition and the portable hubs.

Run from any directory with Python 3; no third-party packages are required:
    python "_Build Kit/New Careers October 2026/build.py"

What it does, for every career in careers.json:
  * writes Career Assessments Web/<area>/<slug>.html from the shared Rural Additions template
  * embeds the same assessment (minus the site navigation bar) in the area's portable hub
  * adds a card to the area menu page and the hub menu, in the named group
  * adds or refreshes the career's entry in search-index.json
  * refreshes the career counts on the area pages, hubs, homepage and README

It refuses to build unless both images for every career exist as JPEGs, because the
Career Factory rule is that no career ships without its two images. Use
prepare_images.py first to size Chadwick's images to 1200 x 800 and under 600 KB.

Running it again is safe: existing careers are left byte for byte, and new careers are
replaced rather than duplicated.
"""
from pathlib import Path
import base64, html, json, re, sys


def rd(p):
    """Read text keeping the file's own line endings (CRLF or LF)."""
    with open(p, encoding='utf8', newline='') as f:
        return f.read()


def wr(p, text):
    """Write text using the line endings the file already has (new files follow the template)."""
    p = Path(p)
    model = p if p.exists() else repo / '_Build Kit' / 'Rural Additions' / 'assessment-template.html'
    with open(model, 'rb') as f:
        crlf = b'\r\n' in f.read(200000)
    text = text.replace('\r\n', '\n')
    if crlf:
        text = text.replace('\n', '\r\n')
    with open(p, 'w', encoding='utf8', newline='') as f:
        f.write(text)


here = Path(__file__).resolve().parent
repo = here.parents[1]
site = repo / 'Career Assessments Web'
template = rd(repo / '_Build Kit' / 'Rural Additions' / 'assessment-template.html')
careers = json.loads(rd(here / 'careers.json'))
image_dirs = [here / 'images', repo / '_Build Kit' / 'Rural Additions' / 'images']
CHECKED = 'October 10, 2026'
# The report wording and accessibility fixes shared with the rest of the site.
sys.path.insert(0, str(repo / '_Build Kit' / 'Soften Reports October 2026'))
from soften import soften

HUBS = {
    'jobs-you-can-start-now': 'Jobs_You_Can_Start_Now_Career_Assessments.html',
    'healthcare': 'Healthcare_Career_Assessments.html',
    'education': 'Education_Career_Assessments.html',
    'business-finance': 'Business_and_Finance_Career_Assessments.html',
}
NEW_GROUPS = {  # groups that do not exist yet: (area, title) -> (insert after group, colour, icon)
    ('jobs-you-can-start-now', 'Offices and Banks'): ('Stores, Desks and Customer Service', '#0b6b74', '&#128450;'),
}


def find_image(name):
    for d in image_dirs:
        p = d / name
        if p.exists():
            return p
    return None


missing = [(c['name'], f) for c in careers for f in c['images'] if not find_image(f)]
if missing:
    print('Not built. These images are missing (save them in "_Build Kit/Rural Additions/images"):')
    for name, f in missing:
        print('   ', name, '->', f)
    sys.exit(1)


def tools(id):
    return f'''<div class="tool-row" role="group" aria-label="Section tools"><button type="button" class="tool-btn" data-label="&#128266; Listen" aria-pressed="false" onclick="listenSection(this,'{id}')">&#128266; Listen</button><button type="button" class="tool-btn" onclick="printSection('{id}')">&#128424;&#65039; Print this part</button></div>'''


def radios(name, question, answers):
    return ('<div class="assessment-question"><fieldset><legend>' + html.escape(question) + '</legend><div class="radio-group">'
            + ''.join(f'<label class="radio-option"><input type="radio" name="{name}" value="{html.escape(v)}"> {html.escape(label)}</label>' for v, label in answers)
            + '</div></fieldset></div>')


def build(c):
    mot = dict(zip(['love', 'hands', 'path'], c['motivation']))
    mot.update(salary='I am curious about pay and job stability.', recommend='Someone suggested I look at it.', explore='I am still exploring my options.')
    sections = [list(s) for s in c['sections']]
    sections.append(['Part 1: What Interests You?', radios('motivation', 'What makes you curious about this work?', mot.items())])
    sections.append(['Part 2: Things You Could Try', c['part2Intro']
                     + ''.join(radios('readiness' + str(i), str(i) + '. ' + q, [('yes', 'Sounds comfortable'), ('unsure', 'Not sure yet'), ('no', 'Not for me')]) for i, q in enumerate(c['readiness'], 1))])
    sections.append(['Part 3: A Small Next Step', radios('future', 'What would you like to do next?', c['future'])
                     + '<div class="assessment-question"><label for="comments">Any thoughts or questions? (Optional)</label><textarea id="comments" rows="4" placeholder="Optional..."></textarea></div>'])
    assert len(sections) == 11, c['name']
    blocks = []
    for i, (title, body) in enumerate(sections, 1):
        for n in range(2):
            b64 = base64.b64encode(find_image(c['images'][n]).read_bytes()).decode()
            body = body.replace('{{IMAGE' + str(n) + '}}', f'<figure class="img-slot"><img src="data:image/jpeg;base64,{b64}" alt="{html.escape(c["alts"][n])}" width="1200" height="800"><figcaption>Illustration of the work. People and scenes are AI-generated.</figcaption></figure>')
        buttons = '' if i == 1 else '<button class="btn-secondary" onclick="prevSection()">Back</button>'
        buttons += ('<button class="btn-primary" onclick="generateReport()">See My Reflections</button>' if i == 11
                    else '<button class="btn-primary" onclick="nextSection()">' + ('Let’s Begin' if i == 1 else 'Continue') + '</button>')
        blocks.append(f'<div class="section' + (' active' if i == 1 else '') + f'" id="section{i}"><h2 tabindex="-1"><span class="section-number" aria-hidden="true">{i}</span>{html.escape(title)}</h2>'
                      + tools('section' + str(i)) + body + '<div class="button-group">' + buttons + '</div></div>')
    data = {'name': c['name'], 'scores': dict(love=9, hands=9, path=8, salary=6, recommend=4, explore=3), 'motLabels': mot,
            'futureLabels': dict(c['future']), 'recs': c['recs'], 'nextSteps': c['nextSteps'], 'futureSteps': c['futureSteps'],
            'finalWords': c['final'], 'readinessItems': c['readiness']}
    links = ''.join(f'<li><a href="{html.escape(u)}">{html.escape(t)}</a></li>' for t, u in c['sources'])
    sources = (f'<div class="srcsec" id="sources" data-section-name="sources">{tools("sources")}<h2>Sources &amp; Learn More</h2>'
               f'<p>Career facts and figures were checked {CHECKED}. The sample day and reflection questions are original illustrations, not an employer schedule or a validated aptitude test.</p>'
               f'<ul>{links}</ul><p>{html.escape(c["sourceNote"])}</p>'
               '<p>Openings, pay, and program requirements can change. Confirm local availability, pay, schedule, and training support with the employer or school.</p></div>')
    nav = '<nav class="dvr-nav" aria-label="Career navigation"><a href="index.html">All careers in this area</a><a href="../index.html">Explore all careers</a><a href="../student-opportunities.html">Student opportunities</a></nav>'
    raw = (template.replace('{{NAME}}', c['name']).replace('{{SUBTITLE}}', c['subtitle']).replace('{{SECTIONS}}', '\n'.join(blocks))
           .replace('{{DATA}}', json.dumps(data, ensure_ascii=False)).replace('{{SOURCES}}', sources))
    return soften(raw.replace('{{NAVIGATION}}', nav)), soften(raw.replace('{{NAVIGATION}}', ''))


def matching_close(s, open_at):
    """Index of the </div> that closes the <div> starting at open_at."""
    depth, i = 0, open_at
    for m in re.finditer(r'<div\b|</div>', s[open_at:]):
        depth += 1 if m.group() == '<div' else -1
        if depth == 0:
            return open_at + m.start()
    raise ValueError('unbalanced div')


def section_bounds(s, title):
    """Return (start, end) of the field-section whose title is `title`."""
    t = s.find('>' + title + '</h2>')
    if t < 0:
        t = s.find('>' + title.replace('&', '&amp;') + '</h2>')
    if t < 0:
        return None
    start = s.rfind('<div class="field-section">', 0, t)
    end = matching_close(s, start) + len('</div>')
    return start, end


def add_card(s, c, card, group):
    """Insert `card` at the end of the group's careers-grid (creating the group if needed)."""
    b = section_bounds(s, group)
    if b is None:
        after, colour, icon = NEW_GROUPS[(c['area'], group)]
        a = section_bounds(s, after)
        head = (f'<div class="field-section">\n            <div class="field-header" style="border-color: {colour};">\n'
                f'                <div class="field-icon" style="background-color: {colour};" aria-hidden="true">{icon}</div>\n'
                f'                <h2 class="field-title" style="color: {colour};">{group}</h2>\n'
                f'                <span class="career-count">0 careers</span>\n            </div>\n'
                f'            <div class="careers-grid">\n            </div>\n        </div>\n        ')
        s = s[:a[1]] + '\n        ' + head.rstrip() + s[a[1]:]
        b = section_bounds(s, group)
    start, end = b
    grid_close = matching_close(s, s.index('<div class="careers-grid">', start))
    s = s[:grid_close] + '    ' + card + '\n            ' + s[grid_close:]
    start, end = section_bounds(s, group)
    n = s[start:end].count('class="career-card"')
    seg = re.sub(r'<span class="career-count">\d+ careers?</span>', f'<span class="career-count">{n} career{"s" if n != 1 else ""}</span>', s[start:end], count=1)
    return s[:start] + seg + s[end:]


def area_total(area):
    return sum(x['area'] == area for x in data['careers'])


# ------------------------------------------------------------------ pages, hubs, menus
for c in careers:
    web, portable = build(c)
    wr(site / c['area'] / f"{c['slug']}.html", web)

    key = c['name'] + ' Career Assessment'
    hub = repo / HUBS[c['area']]
    s = rd(hub)
    m = re.search(r'var ASSESSMENTS_DATA = (\{.*?\});', s, re.S)
    blob = m[1]
    pair = json.dumps(key) + ': ' + json.dumps(base64.b64encode(portable.encode()).decode())
    if key in json.loads(blob):
        blob = re.sub(re.escape(json.dumps(key)) + r'\s*:\s*"[A-Za-z0-9+/=]+"', lambda _: pair, blob)
    else:
        blob = blob.rstrip()[:-1].rstrip() + ',\n    ' + pair + '\n}'
    s = s[:m.start(1)] + blob + s[m.end(1):]
    menu_end = s.index('var ASSESSMENTS_DATA')
    if f"openAssessment('{key}')" not in s[:menu_end]:
        card = (f'<button class="career-card" onclick="openAssessment(\'{key}\')">\n                    <div class="career-title">{html.escape(c["name"], quote=False)}</div>\n'
                f'                    <div class="career-description">{html.escape(c["subtitle"], quote=False)}</div>\n                </button>')
        head, tail = s[:menu_end], s[menu_end:]
        if c.get('hubGroup'):
            head = add_card(head, c, card, c['hubGroup'])
        else:  # flat hub menu: add to the end of the one grid
            g = head.index('<div class="careers-grid">', head.index('<div id="menu">'))
            close = matching_close(head, g)
            head = head[:close] + card + head[close:]
        s = head + tail
    wr(hub, s)

    p = site / c['area'] / 'index.html'
    s = rd(p)
    if f'href="{c["slug"]}.html"' not in s:
        card = (f'<a class="career-card" href="{c["slug"]}.html">\n                    <div class="career-title">{html.escape(c["name"], quote=False)}</div>\n'
                f'                    <div class="career-description">{html.escape(c["subtitle"], quote=False)}</div>\n                </a>')
        s = add_card(s, c, card, c['group'])
        wr(p, s)

# ------------------------------------------------------------------ search index
index = site / 'search-index.json'
data = json.loads(rd(index))
for c in careers:
    w, pj = c['wages'], c['proj']
    annual = c.get('payBasis') == 'annual-contract'
    entry = dict(name=c['name'], subtitle=c['subtitle'], area=c['area'], areaName=c['areaName'], url=c['area'] + '/' + c['slug'] + '.html',
                 soc=c['soc'], medianHourly=None if annual else w['p50'], medianAnnual=w['p50a'],
                 payBasis='annual-contract' if annual else 'hourly', entryHourly=None if annual else w['p10'], topHourly=None if annual else w['p90'],
                 ndGrowthPct=pj['pct'], ndOpeningsPerYear=pj['open'], ndEmployment=pj['from'], ndProjectionStatus='ok',
                 facets=c['facets'], tags=c['tags'], published=True)
    if c.get('growthLabel'):
        entry['growthLabel'] = c['growthLabel']
    data['careers'] = [x for x in data['careers'] if x['url'] != entry['url']] + [entry]
data['totalCareers'] = data['publishedCareers'] = len(data['careers'])
for area in data['areas']:
    area['count'] = sum(x['area'] == area['slug'] for x in data['careers'])
data['note'] = 'Original index generated by mkindex.py; rural additions refreshed by _Build Kit/Rural Additions/build.py; October 2026 additions by _Build Kit/New Careers October 2026/build.py.'
wr(index, json.dumps(data, indent=1, ensure_ascii=False) + '\n')
total = len(data['careers'])

# ------------------------------------------------------------------ counts
TAGLINES = {
    'jobs-you-can-start-now': (r'(<p class="tagline">)\d+ North Dakota jobs you can start without a degree', r'\g<1>{n} North Dakota jobs you can start without a degree',
                               r'(<p class="tagline">)\d+ careers to explore in North Dakota', r'\g<1>{n} careers to explore in North Dakota'),
    'healthcare': (r'(<p class="tagline">)Explore \d+ (?:In-Demand )?Healthcare Careers in North Dakota', r'\g<1>Explore {n} Healthcare Careers in North Dakota', None, None),
    'education': (r'(<p class="tagline">)Explore \d+ (?:In-Demand )?Education Careers in North Dakota', r'\g<1>Explore {n} Education Careers in North Dakota', None, None),
    'business-finance': (r'(<p class="tagline">)Explore \d+ (?:In-Demand )?Business and Finance Careers in North Dakota', r'\g<1>Explore {n} Business and Finance Careers in North Dakota', None, None),
}
home = site / 'index.html'
hs = rd(home)
for area in sorted({c['area'] for c in careers}):
    n = area_total(area)
    idx_pat, idx_rep, hub_pat, hub_rep = TAGLINES[area]
    p = site / area / 'index.html'
    wr(p, re.sub(idx_pat, idx_rep.format(n=n), rd(p), count=1))
    hub = repo / HUBS[area]
    s = rd(hub)
    s = re.sub(hub_pat or idx_pat, (hub_rep or idx_rep).format(n=n), s, count=1)
    wr(hub, s)
    hs = re.sub(r'(href="' + re.escape(area) + r'/index\.html"[\s\S]*?<span class="area-count">)\d+ careers', r'\g<1>' + str(n) + ' careers', hs, count=1)



hs = re.sub(r'(<strong data-total>)\d+(</strong>)', r'\g<1>' + str(total) + r'\g<2>', hs)
wr(home, hs)

readme = repo / 'README.md'
r = rd(readme)
r = re.sub(r'\*\*\d+ careers across 12 areas\.\*\*', f'**{total} careers across 12 areas.**', r)
for a in data['areas']:
    r = re.sub(r'(\| ' + re.escape(a['name']) + r' \| )\d+( \|)', r'\g<1>' + str(a['count']) + r'\g<2>', r)
r = re.sub(r'(\| \*\*Total\*\* \| \*\*)\d+(\*\* \|)', r'\g<1>' + str(total) + r'\g<2>', r)
wr(readme, r)

print(f'Built {len(careers)} new careers. The site now lists {total} careers.')
