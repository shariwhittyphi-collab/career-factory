"""Rebuild the two rural additions in the web edition and portable hubs.
Run from any directory with Python 3; no third-party packages are required.
Existing careers and their embedded assessments are preserved byte for byte.
"""
from pathlib import Path
import base64,html,json,re

here=Path(__file__).resolve().parent
repo=here.parents[1]
site=repo/'Career Assessments Web'
careers=json.loads((here/'careers.json').read_text(encoding='utf8'))
template=(here/'assessment-template.html').read_text(encoding='utf8')

def tools(id):
    return f'''<div class="tool-row" role="group" aria-label="Section tools"><button type="button" class="tool-btn" data-label="&#128266; Listen" aria-pressed="false" onclick="listenSection(this,'{id}')">&#128266; Listen</button><button type="button" class="tool-btn" onclick="printSection('{id}')">&#128424;&#65039; Print this part</button></div>'''

def radios(name,question,answers):
    return '<div class="assessment-question"><fieldset><legend>'+html.escape(question)+'</legend><div class="radio-group">'+''.join(f'<label class="radio-option"><input type="radio" name="{name}" value="{html.escape(v)}"> {html.escape(label)}</label>' for v,label in answers)+'</div></fieldset></div>'

def build(c):
    mot=dict(zip(['love','hands','path'],c['motivation']))
    mot.update(salary='I am curious about pay and job stability.',recommend='Someone suggested I look at it.',explore='I am still exploring my options.')
    sections=list(c['sections'])
    sections.append(('Part 1: What Interests You?',radios('motivation','What makes you curious about this work?',mot.items())))
    sections.append(('Part 2: Things You Could Try','<p>Think about what sounds comfortable and what you would like help learning. You do not need these skills already.</p>'+''.join(radios('readiness'+str(i),str(i)+'. '+q,[('yes','Yes'),('unsure','Unsure'),('no','No')]) for i,q in enumerate(c['readiness'],1))))
    sections.append(('Part 3: A Small Next Step',radios('future','What would you like to do next?',c['future'])+'<div class="assessment-question"><label for="comments">Any thoughts or questions? (Optional)</label><textarea id="comments" rows="4" placeholder="Optional..."></textarea></div>'))
    blocks=[]
    for i,(title,body) in enumerate(sections,1):
        for image in range(2):
            idx=c['images'][image]
            b64=base64.b64encode((here/f'images/career-{idx}.jpg').read_bytes()).decode()
            body=body.replace('{{IMAGE'+str(image)+'}}',f'<figure class="img-slot"><img src="data:image/jpeg;base64,{b64}" alt="{html.escape(c["alts"][image])}" width="1400" height="933"><figcaption>Illustration of the work. People and scenes are AI-generated.</figcaption></figure>')
        buttons='' if i==1 else '<button class="btn-secondary" onclick="prevSection()">Back</button>'
        buttons+=('<button class="btn-primary" onclick="generateReport()">See My Reflections</button>' if i==11 else '<button class="btn-primary" onclick="nextSection()">'+('Let’s Begin' if i==1 else 'Continue')+'</button>')
        blocks.append(f'<div class="section'+(' active' if i==1 else '')+f'" id="section{i}"><h2 tabindex="-1"><span class="section-number" aria-hidden="true">{i}</span>{html.escape(title)}</h2>'+tools('section'+str(i))+body+'<div class="button-group">'+buttons+'</div></div>')
    data={'name':c['name'],'scores':dict(love=9,hands=9,path=8,salary=6,recommend=4,explore=3),'motLabels':mot,'futureLabels':dict(c['future']),'recs':c['recs'],'nextSteps':c['nextSteps'],'futureSteps':c['futureSteps'],'finalWords':c['final'],'readinessItems':c['readiness']}
    sources=f'''<div class="srcsec" id="sources" data-section-name="sources">{tools('sources')}<h2>Sources &amp; Learn More</h2><p>Career facts and figures were checked October 4, 2026. The sample day and reflection questions are original illustrations, not an employer schedule or a validated aptitude test.</p><ul>
    <li><a href="https://www.onetonline.org/link/summary/{c['soc']}">O*NET OnLine — occupation information</a></li>
    <li><a href="https://www.onetonline.org/link/localwages/{c['soc']}?st=ND">North Dakota pay — BLS May 2025, via O*NET</a></li>
    <li><a href="https://www.onetonline.org/link/localtrends/{c['soc']}?st=ND">North Dakota outlook — Projections Central 2024–2034, via O*NET</a></li>
    <li><a href="https://www.gooseneckimp.com/careers">Gooseneck — employer information and current openings</a></li>
    <li><a href="https://www.rdoequipment.com/careers/access-your-future-internship-programs/high-school-programs">RDO — high school programs</a></li></ul>
    {('<p>Precision-ag pay and outlook figures describe the broader Agricultural Technicians group, SOC 19-4012.00. They are not separate estimates for precision-ag workers or a particular employer.</p><ul><li><a href="https://www.lrsc.edu/programs/precision-agriculture-certificate">Lake Region State College — 15-credit certificate</a></li><li><a href="https://catalog.ndscs.edu/agriculture/associate-in-applied-science/precision-agriculture-technician">NDSCS — 62-credit associate degree and paid internship</a></li><li><a href="https://www.ndsu.edu/agricultural-biosystems-engineering/agricultural-technology">NDSU — Agricultural Technology</a></li></ul>' if c['area']=='science' else '<p>Parts-sales figures include multiple industries. They are not a dealership wage offer.</p>')}
    <p>Openings and program requirements can change. Confirm local availability, pay, schedule, transport, school arrangements, and training support with the employer.</p></div>'''
    nav='<nav class="dvr-nav" aria-label="Career navigation"><a href="index.html">All careers in this area</a><a href="../index.html">Explore all careers</a><a href="../student-opportunities.html">Student opportunities</a></nav>'
    raw=template.replace('{{NAME}}',c['name']).replace('{{SUBTITLE}}',c['subtitle']).replace('{{SECTIONS}}','\n'.join(blocks)).replace('{{DATA}}',json.dumps(data,ensure_ascii=False)).replace('{{SOURCES}}',sources)
    return raw.replace('{{NAVIGATION}}',nav),raw.replace('{{NAVIGATION}}','').replace('../student-opportunities.html','https://shariwhittyphi-collab.github.io/career-factory/student-opportunities.html')

for c in careers:
    web,portable=build(c)
    (site/c['area']/f"{c['slug']}.html").write_text(web,encoding='utf8')
    hub=repo/('Science_Career_Assessments.html' if c['area']=='science' else 'Jobs_You_Can_Start_Now_Career_Assessments.html')
    s=hub.read_text(encoding='utf8'); key=c['name']+' Career Assessment'
    m=re.search(r'var ASSESSMENTS_DATA = (\{.*?\});',s,re.S)
    encoded=base64.b64encode(portable.encode()).decode()
    blob=m[1]
    pair=json.dumps(key)+': '+json.dumps(encoded)
    if key in json.loads(blob):
        blob=re.sub(re.escape(json.dumps(key))+r'\s*:\s*"[A-Za-z0-9+/=]+"',lambda _:pair,blob)
    else:
        blob=blob.rstrip()[:-1].rstrip()+',\n    '+pair+'\n}'
    s=s[:m.start(1)]+blob+s[m.end(1):]
    if c['name'] not in s[:s.index('var ASSESSMENTS_DATA')]:
        card=f'<button class="career-card" onclick="openAssessment(\'{key}\')"><div class="career-title">{c["name"]}</div><div class="career-description">{c["subtitle"]}</div></button>'
        if c['area']=='science':
            at=s.index('<button class="career-card" onclick="openAssessment(\'Agricultural Technician')
            s=s[:at]+card+'\n                '+s[at:]
            s=s.replace('Explore 7 In-Demand Science Careers in North Dakota','Explore 8 science careers in North Dakota').replace('<span class="career-count">2 careers</span>','<span class="career-count">3 careers</span>',1)
        else:
            at=s.index('<div class="careers-grid">',s.index('<div id="menu">'))+len('<div class="careers-grid">')
            s=s[:at]+card+s[at:]
            s=s.replace('22 careers to explore','23 careers to explore')
    if c['area']=='science': s=s.replace('In-Demand Science Career Assessments','Science Careers to Explore')
    hub.write_text(s,encoding='utf8')
    p=site/c['area']/'index.html'; s=p.read_text(encoding='utf8')
    if f'{c["slug"]}.html' not in s:
        card=f'<a class="career-card" href="{c["slug"]}.html"><div class="career-title">{c["name"]}</div><div class="career-description">{c["subtitle"]}</div></a>'
        at=s.index('<a class="career-card" href="'+('agricultural-technician' if c['area']=='science' else 'cashier')+'.html">')
        s=s[:at]+card+'\n                '+s[at:]
        s=s.replace('Explore 7 In-Demand Science Careers in North Dakota','Explore 8 science careers in North Dakota')
        s=s.replace('Explore 22','Explore 23')
        if c['area']=='science':
            s=s.replace('<span class="career-count">2 careers</span>','<span class="career-count">3 careers</span>',1)
        else:
            before,after=s.split('Stores, Desks and Customer Service',1)
            after=after.replace('<span class="career-count">5 careers</span>','<span class="career-count">6 careers</span>',1)
            s=before+'Stores, Desks and Customer Service'+after
        p.write_text(s,encoding='utf8')

index=site/'search-index.json'; data=json.loads(index.read_text(encoding='utf8'))
for c in careers:
    entry={k:c[k] for k in ['name','subtitle','area','areaName','soc','medianHourly','medianAnnual','entryHourly','topHourly','ndGrowthPct','ndOpeningsPerYear','ndEmployment','tags']}
    entry.update(url=c['area']+'/'+c['slug']+'.html',payBasis='hourly',ndProjectionStatus='ok',facets=['20-to-30','growing-fast' if c['area']=='science' else 'steady'],published=True)
    for k in ['payLabel','growthLabel']:
        if k in c: entry[k]=c[k]
    data['careers']=[x for x in data['careers'] if x['url']!=entry['url']]+[entry]
data['totalCareers']=data['publishedCareers']=len(data['careers'])
for area in data['areas']: area['count']=sum(c['area']==area['slug'] for c in data['careers'])
data['note']='Original index generated by mkindex.py; rural additions refreshed by _Build Kit/Rural Additions/build.py.'
index.write_text(json.dumps(data,indent=1,ensure_ascii=False)+'\n',encoding='utf8')
print('Built both rural careers, area menus, portable hubs, and the 195-career search index.')
