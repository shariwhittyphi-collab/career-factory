"""Batch 2, part C: construction and production careers (Career Factory, October 2026)."""
from content_common import *

C = []


def add(name, slug, area, areaName, soc, subtitle, img, alts, wages, proj, tags, motivation, readiness, future,
        nextSteps, futureSteps, final, step, sections, pay, sourceNote, extra=(), group=None, hubGroup=None):
    c = dict(name=name, slug=slug, area=area, areaName=areaName, soc=soc, subtitle=subtitle,
             images=[img + '-1.jpg', img + '-2.jpg'], alts=alts, wages=wages, proj=proj, tags=tags,
             facets=facets_for(wages, proj), motivation=motivation, readiness=readiness,
             future=future + FUTURE_TAIL, nextSteps=nextSteps, futureSteps=futureSteps, final=final,
             group=group, hubGroup=hubGroup)
    c['recs'] = recs_for(name.lower(), step)
    c['sources'] = onet_sources(soc, extra)
    c['sourceNote'] = sourceNote
    c['sections'] = sections
    c['pay'] = pay_section(c, *pay)
    C.append(c)


def P(**k):
    k['from'] = k.pop('frm')
    return k


ON_SITE = '<p>Ask about written instructions, a buddy on your first jobs, extra practice time, or other support that helps you learn and work safely.</p>'

# ---------------------------------------------------------------- Construction Laborer
add('Construction Laborer', 'construction-laborer', 'skilled-trades', 'Skilled Trades', '47-2061.00',
    'Doing the hands-on work that gets every building project done',
    'construction-laborer',
    ['A construction laborer levels gravel inside wooden forms at a building site.',
     'A construction laborer carries a bundle of rebar across a job site.'],
    dict(p10=18.75, p25=21.96, p50=23.59, p75=29.17, p90=34.23, p50a=49070),
    P(y0=2024, y1=2034, frm=5150, to=5650, pct=10, open=480),
    ['construction', 'outdoor', 'hands-on', 'concrete', 'physical', 'apprenticeship'],
    ['I like physical work I can see at the end of the day.', 'I like working outside with a crew.', 'I want to start working without more school first.'],
    ['Lifting, carrying, and shoveling for much of a shift', 'Working outside in heat, cold, and wind', 'Following directions from a crew leader',
     'Wearing a hard hat, safety glasses, and other gear all day', 'Learning to use tools like saws, compactors, and jackhammers',
     'Getting up early and working long days in busy season', 'Measuring and marking where work goes', 'Speaking up when something looks unsafe'],
    [['a', 'Talk with a construction laborer about the work.'], ['b', 'Look into a laborer apprenticeship.'], ['c', 'Compare construction job ads near you.']],
    ['Ask someone who works construction what a normal day is like.', 'Look at laborer job ads in your area and what they ask for.',
     'Ask whether employers provide safety gear and training.', 'Ask about seasonal work, hours, and pay while learning.'],
    {'a': ['Ask a laborer what tasks fill most of the day.', 'Ask what gear they wear and what new people find hard.', 'Notice whether outdoor, physical work sounds good to you.'],
     'b': ['Search for construction apprenticeships at apprenticeship.gov.', 'Ask a contractor or union hall how apprentices apply.', 'Write down the age, school, and driver’s license rules.'],
     'c': ['Read five job ads and mark what they require.', 'Compare pay, hours, and whether the work stops in winter.', 'Ask which employers train beginners.']},
    'Every road, school, and house starts with a crew doing the heavy, hands-on work. Construction laborers learn on the job and can grow into a skilled trade. Showing up ready and working safely matters more than knowing everything on day one.',
    'Talking with someone who works on a construction crew is a useful next step.',
    [['Welcome', '<p>Before a building goes up, someone digs, carries, levels, and cleans. That crew member is often a construction laborer.</p>'
      '<p>This is physical, outdoor work on a team. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Construction Laborer?', '<p>You do the hands-on work that keeps a construction project moving. You help skilled workers, run small machines, and keep the site safe and clean.</p>{{IMAGE0}}'
      '<ul><li>Load and unload materials and carry them where they are needed.</li><li>Dig, shovel, and level ground and gravel.</li>'
      '<li>Help pour and finish concrete.</li><li>Run tools like compactors, saws, and jackhammers.</li>'
      '<li>Signal equipment operators and direct traffic around the site.</li><li>Clean up to remove hazards.</li></ul>'
      '<p><strong>The real picture:</strong> The work changes with each job. Roads, houses, farms, and oil field sites all need laborers, and in North Dakota much of the work is busiest from spring through fall.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every crew and job site is different.</p><ul>'
      '<li>Early morning: Meet the crew, put on safety gear, and hear the plan for the day.</li>'
      '<li>Morning: Unload a delivery of lumber and rebar and stack it where it goes.</li>'
      '<li>Midday: Help set forms and spread gravel before a concrete pour.</li>'
      '<li>Afternoon: Help finish the concrete and run a compactor.</li>'
      '<li>Before leaving: Clean tools and pick up the site so it is safe overnight.</li></ul>'
      '<p>Weather changes plans. Some days start before sunrise to beat the heat, and some jobs pause when it storms.</p>'],
     ['How You Learn the Job', '<p><strong>Most people learn on the job.</strong> Many employers hire people with a high school diploma or GED, and some do not require one. Read the actual job ad.</p><ul>'
      '<li><strong>On-the-job training:</strong> An experienced worker shows you the tools and safety rules.</li>'
      '<li><strong>Apprenticeship:</strong> Some contractors and the Laborers’ union offer construction craft laborer apprenticeships, where you are paid while you learn.</li>'
      '<li><strong>Safety training:</strong> Many employers ask for or provide OSHA 10-hour safety training.</li>'
      '<li><strong>Optional classes:</strong> North Dakota schools offering construction trades programs include Turtle Mountain College in Belcourt and Sitting Bull College in Fort Yates. Compare cost, length, and schedule.</li></ul>'
      + APPRENTICE_PAY],
     ['Training and Employer Requirements', '<p>North Dakota does not license construction laborers. Building contractors need a state contractor license, but that is the employer’s job, not yours. Ask each employer what you need to start.</p><ul>'
      '<li>Ability to lift and carry heavy materials, or ask about the job’s physical demands.</li><li>Steel-toed boots and some basic gear; ask what the employer provides.</li>'
      '<li>A driver’s license and reliable ride to job sites that move.</li><li>Safety training, which many employers provide.</li>'
      '<li>Drug testing for some employers.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask who trains new workers and what safety gear you will be given.</p>' + ON_SITE],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Experienced laborer:</strong> Run more equipment and take on harder tasks.</li>'
      '<li><strong>A skilled trade:</strong> Many laborers move into carpentry, concrete finishing, pipe laying, or equipment operation.</li>'
      '<li><strong>Crew leader or foreman:</strong> Lead a crew as experience grows.</li>'
      '<li><strong>Construction manager:</strong> With experience and sometimes more school, plan and run whole projects.</li></ul>'
      '<p>Ask people on the crew which paths are open where you live.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Seeing a project rise because of your work.</li><li>Working outside with a crew.</li>'
      '<li>Starting without a degree and learning on the job.</li><li>Many paths into skilled trades.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Hard physical work that can be tough on your body over time.</li>'
      '<li>Weather, including North Dakota winters.</li><li>Seasonal layoffs or long days in busy season.</li>'
      '<li>Travel to job sites far from home.</li></ul>'
      '<p>North Dakota projects about 10% growth in these jobs from 2024 to 2034, with about 480 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Does physical work on a team, outside, sound like a good fit for you?</p>']],
    ('North Dakota construction laborer pay — May 2025:',
     'Building contractors, road and bridge crews, oil field and energy projects, farms, and cities and counties.',
     'Outdoor job sites in all kinds of weather. Many jobs are full time in busy season, with early starts and some long days.',
     'Ask about base pay, overtime, winter work, travel pay, benefits, and what safety gear is provided.'),
    'Openings and pay can change with the construction season and the economy.',
    [['OSHA construction safety training', 'https://www.osha.gov/training/outreach/construction']],
    group='Construction Trades', hubGroup='Construction Trades')

# ---------------------------------------------------------------- Forklift Operator
add('Forklift Operator', 'forklift-operator', 'jobs-you-can-start-now', 'Jobs You Can Start Now', '53-7051.00',
    'Moving and stacking loads safely in warehouses, plants, and yards',
    'forklift-operator',
    ['A forklift operator lifts a wrapped pallet onto a warehouse rack.',
     'A forklift operator kneels to inspect a forklift tire before a shift.'],
    dict(p10=19.58, p25=21.65, p50=23.68, p75=27.07, p90=30.14, p50a=49260),
    P(y0=2024, y1=2034, frm=990, to=1060, pct=7, open=100),
    ['warehouse', 'forklift', 'equipment', 'shipping', 'manufacturing', 'hands-on'],
    ['I like driving and running equipment.', 'I like work with a clear goal for each shift.', 'I want to start working without more school first.'],
    ['Driving a machine carefully in tight spaces', 'Checking a machine for problems before each shift', 'Paying close attention to people walking nearby',
     'Following safety rules exactly, every time', 'Reading order numbers and labels to find the right load',
     'Working in a warehouse that may be hot, cold, or noisy', 'Sitting and climbing on and off a machine all day', 'Asking for help when a load looks unsafe'],
    [['a', 'Ask a forklift operator what the job is like.'], ['b', 'Ask employers how they train and certify operators.'], ['c', 'Compare warehouse job ads near you.']],
    ['Ask someone who works in a warehouse what a shift looks like.', 'Look at forklift and warehouse job ads in your area.',
     'Ask how employers train new operators.', 'Ask about shifts, pay, and support while learning.'],
    {'a': ['Ask what a normal shift looks like and how busy it gets.', 'Ask what new operators find hard.', 'Notice whether steady equipment work sounds good to you.'],
     'b': ['Ask employers whether they train new hires on a forklift.', 'Ask how long training lasts and how you are evaluated.', 'Write down which employers train beginners.'],
     'c': ['Read five job ads and mark what they require.', 'Compare day, night, and weekend shifts.', 'Compare pay, benefits, and how each employer trains.']},
    'Everything on a store shelf or a factory line was moved by someone along the way. Forklift operators keep goods moving safely. Careful driving and paying attention to people around you matter most, and employers train you to the safety rules.',
    'Asking a forklift operator about their shift is a useful next step.',
    [['Welcome', '<p>Pallets of food, parts, and supplies move through North Dakota warehouses every day. Forklift operators move them.</p>'
      '<p>This job mixes careful driving, safety, and steady work. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Forklift Operator?', '<p>You drive a forklift or similar machine to load, move, and stack materials. You work in warehouses, factories, lumber yards, and shipping docks.</p>{{IMAGE0}}'
      '<ul><li>Inspect the forklift before each shift.</li><li>Load and unload trucks and rail cars.</li>'
      '<li>Move pallets to the right shelf or work area.</li><li>Check labels and order numbers so the right load goes to the right place.</li>'
      '<li>Watch for people and obstacles while driving.</li><li>Record what was moved, sometimes with a handheld scanner.</li></ul>'
      '<p><strong>The real picture:</strong> Some jobs are mostly driving. In others, you also pick orders, wrap pallets, and help on the dock.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every warehouse runs on its own schedule.</p><ul>'
      '<li>Start of shift: Walk around the forklift and check tires, forks, horn, and brakes.</li>'
      '<li>Morning: Unload two trucks and put pallets away on high racks.</li>'
      '<li>Midday: Move materials to the production line as they are needed.</li>'
      '<li>Afternoon: Load outgoing orders onto trucks in the right order.</li>'
      '<li>End of shift: Park and charge or fuel the forklift and report any problems.</li></ul>'
      '<p>Busy days can feel fast. Safety always comes before speed.</p>'],
     ['How You Learn the Job', '<p><strong>Most people learn on the job.</strong> Many employers hire people with a high school diploma or GED, and some do not require one.</p><ul>'
      '<li><strong>Employer training:</strong> Federal safety rules require each operator to finish training and an evaluation before driving on their own. The training mixes classroom learning, hands-on practice, and a driving test at work.</li>'
      '<li><strong>Start nearby:</strong> A warehouse, stocker, or material mover job can lead to forklift work.</li>'
      '<li><strong>Refreshers:</strong> Operators are evaluated again at least every three years, or after an accident or near miss.</li></ul>'
      '<p>There is no state forklift license. A card from a class somewhere else does not replace your employer’s own training and evaluation, so ask before paying for a class.</p>'],
     ['Training and Employer Requirements', '<p>Requirements depend on the employer. Ask what you need to start.</p><ul>'
      '<li>Completion of the employer’s forklift training and evaluation.</li><li>Good eyesight, hearing, and attention to people nearby.</li>'
      '<li>Ability to climb on and off the machine and sometimes lift boxes.</li><li>Willingness to work shifts, which may include nights or weekends.</li>'
      '<li>Drug testing for some employers.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask who trains new operators and how much practice time you get.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Experienced operator:</strong> Drive other equipment, such as reach trucks or loaders.</li>'
      '<li><strong>Lead or trainer:</strong> Train new operators and lead a shift.</li>'
      '<li><strong>Warehouse or shipping supervisor:</strong> Run a dock or a whole shift.</li>'
      '<li><strong>Truck driving:</strong> Some operators go on to earn a commercial driver’s license.</li></ul>'
      '<p>Ask your employer which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Running equipment instead of lifting everything by hand.</li><li>Clear tasks with a finish line each shift.</li>'
      '<li>Starting without a degree.</li><li>Jobs in many industries.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Hot, cold, or noisy warehouses.</li><li>Night or weekend shifts.</li>'
      '<li>Pressure to move fast.</li><li>The risk of accidents if safety rules are not followed.</li></ul>'
      '<p>North Dakota projects about 7% growth in these jobs from 2024 to 2034, with about 100 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Do careful, steady driving and safety rules sound like a good fit for you?</p>']],
    ('North Dakota forklift operator pay — May 2025:',
     'Warehouses, distribution centers, factories, grain and farm supply businesses, lumber yards, and shipping companies.',
     'Usually indoors in a warehouse or plant, sometimes in outdoor yards. Shifts may include nights and weekends.',
     'Ask about base pay, shift pay, overtime, benefits, and how the employer trains and evaluates operators.'),
    'Pay figures are for industrial truck and tractor operators, which includes forklift operators.',
    [['OSHA powered industrial truck rules (29 CFR 1910.178)', 'https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.178']],
    group='Warehouse, Factory and Driving')

# ---------------------------------------------------------------- Maintenance and Repair Worker
add('Maintenance and Repair Worker', 'maintenance-and-repair-worker', 'skilled-trades', 'Skilled Trades', '49-9071.00',
    'Fixing a little of everything so buildings and machines keep working',
    'maintenance-repair-worker',
    ['A maintenance worker replaces a faucet part under a sink.',
     'A maintenance worker on a stepladder changes a ceiling light fixture in a school hallway.'],
    dict(p10=17.44, p25=20.06, p50=23.96, p75=28.68, p90=32.91, p50a=49840),
    P(y0=2024, y1=2034, frm=3680, to=3980, pct=8, open=380),
    ['maintenance', 'repair', 'building', 'tools', 'hands-on', 'troubleshooting'],
    ['I like figuring out why something does not work.', 'I like using tools and fixing things.', 'I like a job where every day is a little different.'],
    ['Figuring out why something stopped working', 'Using hand and power tools', 'Climbing ladders and working in tight spaces',
     'Reading a manual or a simple drawing', 'Doing small plumbing, painting, and carpentry jobs', 'Talking with tenants, staff, or students about a problem',
     'Keeping a list of work orders and finishing them', 'Knowing when a job needs a licensed electrician or plumber'],
    [['a', 'Talk with a maintenance worker about their day.'], ['b', 'Take a class in a basic repair skill.'], ['c', 'Compare maintenance job ads near you.']],
    ['Ask a building or plant maintenance worker what a normal day is like.', 'Look at maintenance job ads in your area.',
     'Notice which skills the ads list most.', 'Ask about training, pay, and support while learning.'],
    {'a': ['Ask what kinds of repairs come up most.', 'Ask what they wish they had learned first.', 'Notice whether a mix of repairs sounds good to you.'],
     'b': ['Look for a short class in basic plumbing, electrical safety, or HVAC.', 'Practice small repairs at home with someone experienced.', 'Write down the tools you can already use.'],
     'c': ['Compare jobs at schools, apartments, hospitals, and factories.', 'Compare pay, hours, and on-call duty.', 'Ask which employers train beginners.']},
    'Schools, apartments, hospitals, and plants all need someone who keeps things working. Maintenance workers learn many skills over time, one repair at a time. Curiosity and careful, safe work matter most.',
    'Talking with a maintenance worker is a useful next step.',
    [['Welcome', '<p>A leaky faucet, a broken door, a light that will not come on. Someone has to fix them, and in many buildings that person is the maintenance worker.</p>'
      '<p>This job mixes many small trades. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Maintenance and Repair Worker?', '<p>You keep buildings, equipment, and grounds in working order. You do routine upkeep and fix problems as they come up.</p>{{IMAGE0}}'
      '<ul><li>Do routine upkeep, like changing filters, belts, and fluids.</li><li>Find out why something stopped working.</li>'
      '<li>Repair doors, locks, fixtures, and drywall.</li><li>Do small plumbing and painting jobs.</li>'
      '<li>Order parts and supplies.</li><li>Keep records of the work you finished.</li></ul>'
      '<p><strong>The real picture:</strong> A school job, an apartment job, and a factory job are very different. Some work is mostly building repairs; some is mostly machines.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every building has its own list.</p><ul>'
      '<li>Morning: Check the work orders and plan the route.</li>'
      '<li>Later: Replace a faucet part and fix a sticking door.</li>'
      '<li>Midday: Change air filters in the heating system.</li>'
      '<li>Afternoon: Answer an urgent call about a leak.</li>'
      '<li>Before leaving: Write down what was finished and order a part for tomorrow.</li></ul>'
      '<p>Plans change when something urgent breaks. Some jobs include being on call.</p>'],
     ['How You Learn the Job', '<p><strong>Many people learn on the job,</strong> often after a high school diploma or GED. Many employers like to see a certificate or experience in a trade.</p><ul>'
      '<li><strong>On-the-job training:</strong> An experienced worker teaches the building’s systems.</li>'
      '<li><strong>Apprenticeship:</strong> Building and industrial maintenance apprenticeships pay you while you learn.</li>'
      '<li><strong>Short classes:</strong> Courses in HVAC, plumbing basics, or electrical safety can help you get hired.</li>'
      '<li><strong>Start nearby:</strong> Janitor, groundskeeper, or helper jobs can lead to maintenance work.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>There is no general state license for maintenance work. Some tasks are licensed: in North Dakota, electrical wiring work needs a state electrical license, and plumbing has its own rules. Ask exactly what your job will include.</p><ul>'
      '<li>Comfort with hand and power tools.</li><li>Ability to climb ladders, lift, and work in tight spaces, or ask about the physical demands.</li>'
      '<li>A driver’s license for jobs that cover several buildings.</li><li>A background check for jobs in schools or health care.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask which repairs you will do yourself and which go to licensed trades.</p>' + ON_SITE],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Lead maintenance worker:</strong> Take on harder repairs and train others.</li>'
      '<li><strong>Facilities supervisor or manager:</strong> Run maintenance for a building or campus.</li>'
      '<li><strong>A licensed trade:</strong> Electrician, plumber, or HVAC technician through an apprenticeship.</li>'
      '<li><strong>Industrial maintenance:</strong> Specialize in factory machines.</li></ul>'
      '<p>Ask people where you work which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Fixing things and seeing them work again.</li><li>A different mix of tasks every day.</li>'
      '<li>Jobs in almost every town.</li><li>Skills you can use at home, too.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>On-call duty, nights, or weekend emergencies.</li><li>Dirty, cramped, or hot spaces.</li>'
      '<li>Lifting and climbing.</li><li>Many people asking for help at once.</li></ul>'
      '<p>North Dakota projects about 8% growth in these jobs from 2024 to 2034, with about 380 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Do you enjoy figuring out and fixing a little of everything?</p>']],
    ('North Dakota maintenance and repair worker pay — May 2025:',
     'Schools, apartment buildings, hospitals and clinics, factories, hotels, and cities and counties.',
     'Inside and outside buildings, often moving from task to task. Some jobs include on-call or weekend duty.',
     'Ask about base pay, on-call pay, overtime, benefits, and whether the employer pays for classes.'),
    'Pay figures are for general maintenance and repair workers.',
    [['North Dakota electrical licensing law (NDCC 43-09)', 'https://ndlegis.gov/cencode/t43c09.pdf']],
    group='Industrial & Electrical Repair', hubGroup='Industrial & Electrical Repair')

# ---------------------------------------------------------------- Painter
add('Painter', 'painter', 'skilled-trades', 'Skilled Trades', '47-2141.00',
    'Preparing and painting walls, buildings, and structures with care',
    'painter',
    ['A painter rolls gray paint onto a living-room wall.',
     'A painter brushes paint along window trim from a short scaffold.'],
    dict(p10=17.71, p25=22.75, p50=26.38, p75=29.16, p90=37.64, p50a=54870),
    P(y0=2024, y1=2034, frm=610, to=640, pct=5, open=50),
    ['painting', 'construction', 'hands-on', 'detail', 'indoor', 'outdoor'],
    ['I like careful work that looks good when it is done.', 'I like using my hands.', 'I like seeing a big change by the end of a job.'],
    ['Taping, covering, and protecting floors and furniture', 'Scraping, sanding, and patching before painting', 'Working on ladders and scaffolding',
     'Painting straight, clean edges', 'Standing, reaching, and bending for much of the day', 'Wearing a mask or respirator when needed',
     'Talking with customers about colors and plans', 'Asking how to handle old paint that may contain lead'],
    [['a', 'Talk with a painter about the work.'], ['b', 'Practice prep and painting on a small project.'], ['c', 'Compare painting job ads and apprenticeships.']],
    ['Ask a painter what a normal day is like.', 'Look at painter job ads in your area.', 'Ask about safety gear and ladder training.',
     'Ask about pay, seasons, and support while learning.'],
    {'a': ['Ask how much of the job is prep work.', 'Ask what new painters find hard.', 'Notice whether careful, detailed work sounds good to you.'],
     'b': ['Help paint a room with someone experienced.', 'Practice taping and cutting in a straight edge.', 'Notice how long good prep takes.'],
     'c': ['Read job ads from painting contractors.', 'Search for painter apprenticeships at apprenticeship.gov.', 'Compare pay, hours, and winter work.']},
    'A good paint job protects a building and makes people proud of it. Painters learn on the job, one careful step at a time. Patient prep work and safety matter as much as the painting itself.',
    'Talking with a painter is a useful next step.',
    [['Welcome', '<p>Fresh paint changes how a room or building feels. Behind every clean edge is a painter who did careful prep work first.</p>'
      '<p>This job mixes detail, patience, and physical work. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Painter?', '<p>You prepare and paint walls, ceilings, trim, and outside surfaces of homes and buildings.</p>{{IMAGE0}}'
      '<ul><li>Cover floors and furniture and tape off edges.</li><li>Fill cracks and holes, then sand and scrape.</li>'
      '<li>Apply primer, paint, and stain with brushes, rollers, or sprayers.</li><li>Set up ladders and scaffolding safely.</li>'
      '<li>Read work orders and match colors.</li><li>Clean up tools and the work area.</li></ul>'
      '<p><strong>The real picture:</strong> Much of the job is preparation. Painting outside is seasonal in North Dakota, while inside work goes on all year.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every job is different.</p><ul>'
      '<li>Morning: Move furniture, lay drop cloths, and tape trim.</li>'
      '<li>Later: Patch holes and sand the walls smooth.</li>'
      '<li>Midday: Prime the patched spots.</li>'
      '<li>Afternoon: Cut in edges with a brush and roll the walls.</li>'
      '<li>Before leaving: Clean brushes and rollers and check the work in good light.</li></ul>'
      '<p>Some days are spent high on a ladder outside. Others are quiet indoor work.</p>'],
     ['How You Learn the Job', '<p><strong>Most painters learn on the job.</strong> Many employers hire people with a high school diploma or GED, and some do not require one.</p><ul>'
      '<li><strong>On-the-job training:</strong> An experienced painter teaches prep, tools, and safety.</li>'
      '<li><strong>Apprenticeship:</strong> Painter apprenticeships pay you while you learn.</li>'
      '<li><strong>Safety training:</strong> Ladder, scaffold, and respirator training are common.</li>'
      '<li><strong>Lead-safe training:</strong> Work on homes built before 1978 follows federal lead-safe rules, and the company must be certified. Workers are trained in lead-safe work practices.</li></ul>'
      + APPRENTICE_PAY],
     ['Training and Employer Requirements', '<p>North Dakota does not license painters. Painting contractors need a state contractor license for larger jobs, and that is the employer’s responsibility. Ask what you need to start.</p><ul>'
      '<li>Ability to climb ladders, stand, and reach for long periods, or ask about the physical demands.</li><li>Comfort wearing a mask or respirator when needed.</li>'
      '<li>A driver’s license for travel to job sites.</li><li>Lead-safe training if the employer works on older homes.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask who trains new painters and what safety gear is provided.</p>' + ON_SITE],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Experienced painter:</strong> Take on spraying, special finishes, or commercial jobs.</li>'
      '<li><strong>Crew leader:</strong> Lead a painting crew.</li>'
      '<li><strong>Estimator:</strong> Measure jobs and figure costs.</li>'
      '<li><strong>Your own business:</strong> Some painters start their own company, which needs a contractor license and insurance.</li></ul>'
      '<p>Ask painters near you which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>A clear before and after.</li><li>Careful, detailed hands-on work.</li>'
      '<li>Starting without a degree.</li><li>Inside work in winter and outside work in summer.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Ladders and heights.</li><li>Paint fumes, dust, and old lead paint.</li>'
      '<li>Slow seasons and layoffs.</li><li>Standing and reaching all day.</li></ul>'
      '<p>North Dakota projects about 5% growth in these jobs from 2024 to 2034, with about 50 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Does patient, careful work that looks good when it is done sound like you?</p>']],
    ('North Dakota painter pay — May 2025:',
     'Painting contractors, building contractors, schools and hospitals, property managers, and self-employment.',
     'Inside homes and buildings, and outside on ladders and scaffolding. Outdoor work is seasonal.',
     'Ask about base pay, winter work, overtime, benefits, and what safety gear is provided.'),
    'Pay figures are for construction and maintenance painters.',
    [['North Dakota lead-safe renovation information — ND Department of Environmental Quality', 'https://deq.nd.gov/WM/Lead/renovation.aspx']],
    group='Construction Trades', hubGroup='Construction Trades')

# ---------------------------------------------------------------- Roofer
add('Roofer', 'roofer', 'skilled-trades', 'Skilled Trades', '47-2181.00',
    'Building and repairing the roofs that keep weather out',
    'roofer',
    ['A roofer in a safety harness nails shingles on a house roof.',
     'A roofer rolls out underlayment on a flat commercial roof.'],
    dict(p10=22.14, p25=23.08, p50=28.72, p75=34.68, p90=42.00, p50a=59740),
    P(y0=2024, y1=2034, frm=350, to=380, pct=9, open=30),
    ['roofing', 'construction', 'outdoor', 'heights', 'hands-on', 'physical'],
    ['I like physical work outside.', 'I am comfortable with heights.', 'I like seeing a job finished at the end of the day.'],
    ['Working on a roof, high above the ground', 'Wearing a safety harness and tying off', 'Carrying heavy bundles up ladders',
     'Working in summer heat and wind', 'Kneeling and bending for long stretches', 'Cutting shingles and metal to fit',
     'Working fast with a crew while staying safe', 'Saying no to unsafe work'],
    [['a', 'Talk with a roofer about the work.'], ['b', 'Learn about fall protection and roofing apprenticeships.'], ['c', 'Compare roofing job ads near you.']],
    ['Ask a roofer what a normal day is like.', 'Look at roofing job ads in your area.', 'Ask how employers train new roofers to work safely at heights.',
     'Ask about the season, pay, and winter work.'],
    {'a': ['Ask what the hardest part of the job is.', 'Ask what safety gear the crew uses.', 'Notice whether heights and heat sound okay to you.'],
     'b': ['Search for roofer apprenticeships at apprenticeship.gov.', 'Ask employers whether they provide fall-protection training.', 'Write down what each program requires.'],
     'c': ['Read five roofing job ads.', 'Compare pay, season length, and winter work.', 'Ask which employers train beginners.']},
    'A good roof protects everything under it, and North Dakota weather keeps roofers busy. Roofers learn on the job with a crew. Working safely at heights matters more than anything else.',
    'Talking with a roofer is a useful next step.',
    [['Welcome', '<p>Hail, wind, and snow are hard on roofs. Roofers build and repair them so homes and businesses stay dry.</p>'
      '<p>This is physical work at heights, usually outside. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Roofer?', '<p>You install, repair, and replace roofs on houses and other buildings.</p>{{IMAGE0}}'
      '<ul><li>Tear off old roofing and clear the work area.</li><li>Lay underlayment and waterproofing.</li>'
      '<li>Install shingles, metal, or flat-roof systems.</li><li>Cut and fit shingles and flashing around chimneys and vents.</li>'
      '<li>Inspect roofs for damage.</li><li>Clean up nails and debris.</li></ul>'
      '<p><strong>The real picture:</strong> Work depends on the season and the weather. After a hailstorm, crews can be very busy.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every crew works differently.</p><ul>'
      '<li>Early morning: Set up ladders, anchors, and harnesses before the heat.</li>'
      '<li>Morning: Tear off old shingles and load them into a dumpster.</li>'
      '<li>Midday: Lay new underlayment and flashing.</li>'
      '<li>Afternoon: Nail down new shingles row by row.</li>'
      '<li>Before leaving: Clean up nails with a magnet and cover any open areas.</li></ul>'
      '<p>Rain or high wind can stop work for the day.</p>'],
     ['How You Learn the Job', '<p><strong>Most roofers learn on the job.</strong> Many employers hire people with a high school diploma or GED, and some do not require one.</p><ul>'
      '<li><strong>On-the-job training:</strong> An experienced roofer teaches tools, materials, and safe work at heights.</li>'
      '<li><strong>Apprenticeship:</strong> Roofer apprenticeships pay you while you learn.</li>'
      '<li><strong>Fall protection:</strong> Training in harnesses, anchors, and ladder safety is part of the job.</li></ul>'
      + APPRENTICE_PAY],
     ['Training and Employer Requirements', '<p>North Dakota does not license individual roofers. Roofing contractors need a state contractor license for jobs over $4,000, with proof of insurance and workers’ compensation coverage. State law also bars roofing contractors from promising to cover a customer’s insurance deductible.</p><ul>'
      '<li>Comfort working at heights.</li><li>Ability to lift and carry heavy bundles, or ask about the physical demands.</li>'
      '<li>A driver’s license and a reliable ride to job sites.</li><li>Fall-protection training, which employers should provide.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask how the crew protects workers from falls.</p>' + ON_SITE],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Experienced roofer:</strong> Work on metal, flat, or specialty roofs.</li>'
      '<li><strong>Crew leader or foreman:</strong> Run a crew.</li>'
      '<li><strong>Estimator or inspector:</strong> Measure roofs and plan jobs.</li>'
      '<li><strong>Your own business:</strong> With a contractor license and insurance.</li></ul>'
      '<p>Ask roofers near you which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Outdoor, active work with a crew.</li><li>Finishing a whole roof in a few days.</li>'
      '<li>Starting without a degree.</li><li>Pay that rises with skill.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Heights and the risk of falls.</li><li>Hot sun and hard physical work.</li>'
      '<li>Seasonal work and winter layoffs.</li><li>Busy stretches after storms.</li></ul>'
      '<p>North Dakota projects about 9% growth in these jobs from 2024 to 2034, with about 30 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Do heights and hard outdoor work sound like something you would enjoy?</p>']],
    ('North Dakota roofer pay — May 2025:',
     'Roofing contractors, general contractors, and self-employment.',
     'Outdoors on roofs, in heat and wind. Work is seasonal, with long days after storms.',
     'Ask about base pay, season length, winter work, overtime, benefits, and safety training.'),
    'Openings and pay can change with the weather and the construction season.',
    [['North Dakota contractor licensing law (NDCC 43-07)', 'https://ndlegis.gov/cencode/t43c07.pdf'],
     ['North Dakota residential roofing contractor law (NDCC 26.1-39.2)', 'https://ndlegis.gov/cencode/t26-1c39-2.pdf']],
    group='Construction Trades', hubGroup='Construction Trades')

# ---------------------------------------------------------------- Sheet Metal Worker
add('Sheet Metal Worker', 'sheet-metal-worker', 'skilled-trades', 'Skilled Trades', '47-2211.00',
    'Building and installing ductwork, roofs, and metal parts for buildings',
    'sheet-metal-worker',
    ['A sheet metal worker bends steel on a shop brake to form ductwork.',
     'A sheet metal worker on a lift fastens round ductwork near a ceiling.'],
    dict(p10=23.11, p25=23.51, p50=31.34, p75=38.91, p90=40.74, p50a=65180),
    P(y0=2024, y1=2034, frm=390, to=420, pct=6, open=30),
    ['sheet metal', 'HVAC', 'construction', 'apprenticeship', 'fabrication', 'hands-on'],
    ['I like building things out of metal.', 'I like math I can use with my hands.', 'I want to earn pay while I learn a trade.'],
    ['Measuring and doing math for cuts and bends', 'Reading drawings and plans', 'Cutting, bending, and joining metal',
     'Working on lifts and ladders', 'Wearing gloves, glasses, and hearing protection', 'Lifting and fitting heavy duct sections',
     'Going to classes while working an apprenticeship', 'Asking a journeyworker when you are not sure'],
    [['a', 'Talk with a sheet metal worker or apprentice.'], ['b', 'Look into the sheet metal apprenticeship.'], ['c', 'Compare sheet metal and HVAC job ads.']],
    ['Ask a sheet metal worker what a normal day is like.', 'Look up the sheet metal apprenticeship for North and South Dakota.',
     'Brush up on measuring and basic math.', 'Ask about pay while learning.'],
    {'a': ['Ask whether they work mostly in a shop or on job sites.', 'Ask what apprentices learn first.', 'Notice whether metal work sounds good to you.'],
     'b': ['Read the apprenticeship requirements for age, school, and physical fitness.', 'Ask how pay rises as you finish hours.', 'Write down the application steps.'],
     'c': ['Read ads from HVAC and sheet metal contractors.', 'Compare shop work and field work.', 'Compare pay, benefits, and training.']},
    'Heating and cooling systems, roofs, and gutters all depend on sheet metal work. It is a skilled trade you can learn through a paid apprenticeship. Careful measuring and safe work matter most.',
    'Talking with a sheet metal apprentice is a useful next step.',
    [['Welcome', '<p>The ducts that carry warm air through a school in January were built and installed by sheet metal workers.</p>'
      '<p>This trade mixes math, metal, and building. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Sheet Metal Worker?', '<p>You make and install products from thin metal, such as heating and cooling ducts, roof flashing, and gutters.</p>{{IMAGE0}}'
      '<ul><li>Read drawings and measure carefully.</li><li>Cut, bend, and shape metal in a shop.</li>'
      '<li>Join seams by riveting, welding, or soldering.</li><li>Install ducts in buildings, often from lifts.</li>'
      '<li>Install metal roofing and flashing.</li><li>Repair and maintain systems.</li></ul>'
      '<p><strong>The real picture:</strong> Some days are in a fabrication shop. Others are on a construction site.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every job site is different.</p><ul>'
      '<li>Morning: Review the drawings with the crew.</li>'
      '<li>Later: Cut and bend sheet metal into duct sections in the shop.</li>'
      '<li>Midday: Load sections and take them to the job site.</li>'
      '<li>Afternoon: Hang and fasten ductwork from a scissor lift.</li>'
      '<li>Before leaving: Clean up scraps and mark tomorrow’s start point.</li></ul>'
      '<p>Apprentices also spend some evenings or blocks of time in class.</p>'],
     ['How You Learn the Job', '<p><strong>Most sheet metal workers learn through an apprenticeship.</strong> You work for pay during the day and take classes.</p><ul>'
      '<li><strong>North and South Dakota apprenticeship:</strong> The Sheet Metal Workers’ joint apprenticeship program has training in Bismarck and Minot and in Fargo and Grand Forks. Applicants must be at least 18 with a high school diploma or GED. Applications are taken year round.</li>'
      '<li><strong>Pay while learning:</strong> Apprentice pay rises in steps as you finish work hours, until you reach full journeyworker pay.</li>'
      '<li><strong>Other routes:</strong> Some HVAC contractors train helpers on the job.</li></ul>'
      + APPRENTICE_PAY],
     ['Training and Employer Requirements', '<p>North Dakota does not have a separate state license for sheet metal workers. Contractors need a state contractor license. Ask employers what they require.</p><ul>'
      '<li>Age 18 or older and a high school diploma or GED for the apprenticeship.</li><li>Basic math and measuring skills.</li>'
      '<li>Ability to lift, climb, and work on lifts, or ask about the physical demands.</li><li>A driver’s license for travel to job sites.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask how apprentices are supported in class and on the job.</p>' + ON_SITE],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Journeyworker:</strong> Finish the apprenticeship and earn full trade pay.</li>'
      '<li><strong>Foreman:</strong> Lead crews on big projects.</li>'
      '<li><strong>Specialist:</strong> HVAC testing and balancing, architectural metal, or welding.</li>'
      '<li><strong>Estimator or project manager:</strong> Plan jobs with experience.</li></ul>'
      '<p>Ask people in the trade which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Paid training instead of school debt.</li><li>Building real things from flat metal.</li>'
      '<li>Strong pay for experienced workers.</li><li>A mix of shop and job-site work.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Sharp edges, noise, and lifting.</li><li>Heights and lifts.</li>'
      '<li>Travel to job sites.</li><li>Several years of apprenticeship before full pay.</li></ul>'
      '<p>North Dakota projects about 6% growth in these jobs from 2024 to 2034, with about 30 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Does building with metal while you earn and learn sound good to you?</p>']],
    ('North Dakota sheet metal worker pay — May 2025:',
     'HVAC and sheet metal contractors, roofing contractors, and manufacturers.',
     'Fabrication shops and construction sites, sometimes on lifts. Mostly full time.',
     'Ask about apprentice pay steps, overtime, benefits, and class schedules.'),
    'Apprentice pay usually starts below these figures and rises as you complete hours.',
    [['Sheet Metal Workers JATC of North & South Dakota — apprenticeship information (ND CTE)', 'https://www.cte.nd.gov/sites/www/files/documents/Students/ApprenticeshipOpportunity_JATC_SheetMetal.pdf']],
    group='Construction Trades', hubGroup='Construction Trades')

# ---------------------------------------------------------------- Butcher and Meat Cutter
add('Butcher and Meat Cutter', 'butcher-and-meat-cutter', 'jobs-you-can-start-now', 'Jobs You Can Start Now', '51-3021.00',
    'Cutting, trimming, and packaging meat in stores and processing plants',
    'meat-processing-worker',
    ['A meat cutter in a mesh glove trims a cut of beef on a steel table.',
     'A meat cutter packages trimmed cuts on a processing line.'],
    dict(p10=10.76, p25=17.37, p50=19.27, p75=22.75, p90=27.48, p50a=40080),
    P(y0=2024, y1=2034, frm=590, to=590, pct=1, open=70,
      note='The job counts are rounded to the nearest 10, so the small change does not show in them.'),
    ['meat', 'food', 'grocery', 'hands-on', 'knife skills', 'agriculture'],
    ['I like working with my hands.', 'I like food and how it is prepared.', 'I want to start working without more school first.'],
    ['Using sharp knives and saws carefully', 'Working in a cold room for much of a shift', 'Standing at a table or line for long stretches',
     'Following food safety and cleaning rules exactly', 'Wearing gloves, a hairnet, and protective gear', 'Lifting boxes and large cuts of meat',
     'Helping customers who ask for special cuts', 'Asking for help when you are not sure how to cut something'],
    [['a', 'Talk with a butcher or meat cutter.'], ['b', 'Look into a meat cutting certificate.'], ['c', 'Compare grocery and processing job ads.']],
    ['Ask a meat counter worker what a normal day is like.', 'Look at butcher and meat cutter job ads in your area.',
     'Ask how employers teach knife safety.', 'Ask about pay, hours, and support while learning.'],
    {'a': ['Ask what new workers learn first.', 'Ask how cold the work area is and how long shifts are.', 'Notice whether this kind of hands-on food work sounds good to you.'],
     'b': ['Read about the meat cutting programs at NDSCS in Wahpeton and Dickinson State University.', 'Compare length, cost, and hands-on time.', 'Ask whether employers prefer a certificate.'],
     'c': ['Compare grocery store, locker plant, and processing plant jobs.', 'Compare pay, shifts, and benefits.', 'Ask which employers train beginners.']},
    'North Dakota raises a lot of livestock, and someone has to prepare that meat safely for families. Many butchers learn on the job, and a short certificate can help. Careful knife work and strict cleanliness matter most.',
    'Talking with a butcher or meat cutter is a useful next step.',
    [['Welcome', '<p>The steaks, roasts, and ground beef at a grocery store or a local locker plant were cut and wrapped by butchers and meat cutters.</p>'
      '<p>This job mixes knife skills, food safety, and steady hands-on work. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Butcher and Meat Cutter?', '<p>You cut, trim, and package meat so it is ready to sell and cook. You work at grocery store meat counters, local meat markets and locker plants, and processing plants.</p>{{IMAGE0}}'
      '<ul><li>Cut, trim, bone, and grind meat.</li><li>Wrap, weigh, and label packages.</li>'
      '<li>Prepare special cuts that customers order.</li><li>Check meat when it arrives and store it properly.</li>'
      '<li>Set up the display case so it looks good.</li><li>Clean and sanitize tools and work areas.</li></ul>'
      '<p><strong>The real picture:</strong> A small-town meat market, a grocery store, and a large plant are very different jobs. Plants often have one task on a line; small shops do a bit of everything.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every shop runs differently.</p><ul>'
      '<li>Morning: Put on protective gear, check deliveries, and plan the day’s cuts.</li>'
      '<li>Later: Cut steaks and roasts and grind beef.</li>'
      '<li>Midday: Wrap, weigh, and label packages for the case.</li>'
      '<li>Afternoon: Prepare a custom order and help customers at the counter.</li>'
      '<li>Before leaving: Clean and sanitize every surface and tool.</li></ul>'
      '<p>Fall hunting season and holidays can bring busy stretches.</p>'],
     ['How You Learn the Job', '<p><strong>Most people learn on the job.</strong> Many employers hire people with a high school diploma or GED. Training can take from a few weeks to about a year.</p><ul>'
      '<li><strong>On-the-job training:</strong> An experienced cutter teaches knife safety, cuts, and food safety.</li>'
      '<li><strong>Short certificate:</strong> North Dakota State College of Science in Wahpeton and Dickinson State University offer meat cutting certificates.</li>'
      '<li><strong>Start nearby:</strong> A meat department clerk or packaging job can lead to cutting.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>We did not find a North Dakota license for individual butchers. Meat processing businesses are licensed and inspected by the North Dakota Department of Agriculture. Ask each employer what you need to start.</p><ul>'
      '<li>Food safety training, which employers often provide.</li><li>Comfort working in cold rooms.</li>'
      '<li>Ability to stand and lift for long periods, or ask about the physical demands.</li><li>Willingness to wear protective gear like mesh gloves.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask how the employer teaches knife safety and how much practice time you get.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Experienced meat cutter:</strong> Handle custom and specialty cuts.</li>'
      '<li><strong>Meat department manager:</strong> Run a store’s meat counter.</li>'
      '<li><strong>Lead or supervisor:</strong> Lead a line in a processing plant.</li>'
      '<li><strong>Your own shop:</strong> Some butchers run a local meat market or locker plant.</li></ul>'
      '<p>Ask people in the trade which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Hands-on work with a clear result.</li><li>Learning a craft that people value.</li>'
      '<li>Starting without a degree.</li><li>Jobs in many towns.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Cold work areas.</li><li>Sharp tools and the risk of cuts.</li>'
      '<li>Repetitive motions that can strain hands and wrists.</li><li>Weekend and holiday hours.</li></ul>'
      '<p>North Dakota projects the number of these jobs to stay about the same from 2024 to 2034, with about 70 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Does careful, hands-on food work sound like a good fit for you?</p>']],
    ('North Dakota butcher and meat cutter pay — May 2025:',
     'Grocery stores, meat markets and locker plants, and meat processing plants.',
     'Cold, clean work rooms and store counters. Many jobs include weekends.',
     'Ask about base pay, shifts, benefits, and how the employer trains new cutters.'),
    'Pay figures are for butchers and meat cutters. Workers on processing plant lines may be counted under a different job title.',
    [['North Dakota Meat and Poultry Inspection Program — ND Department of Agriculture', 'https://www.ndda.nd.gov/divisions/grain-livestock/meat-inspection']],
    group='Food and Restaurants')

# ---------------------------------------------------------------- Production Supervisor
add('Production Supervisor', 'production-supervisor', 'management', 'Management', '51-1011.00',
    'Leading the people on a factory or plant floor to work safely and well',
    'production-supervisor',
    ['A production supervisor reviews a chart on a tablet with a machine operator.',
     'A production supervisor leads a start-of-shift meeting with workers.'],
    dict(p10=25.21, p25=29.18, p50=36.71, p75=42.94, p90=62.11, p50a=76350),
    P(y0=2024, y1=2034, frm=1730, to=1840, pct=7, open=180),
    ['manufacturing', 'supervisor', 'leadership', 'production', 'safety', 'plant'],
    ['I like leading a team.', 'I like solving problems that keep work moving.', 'I want to grow from the plant floor into leadership.'],
    ['Leading a short meeting at the start of a shift', 'Giving clear directions and feedback', 'Solving problems when a machine or schedule goes wrong',
     'Checking that people follow safety rules', 'Keeping records of hours, output, and quality', 'Working out a conflict between two workers',
     'Walking the plant floor for much of a shift', 'Asking for help from other departments'],
    [['a', 'Talk with a production supervisor.'], ['b', 'Take on a lead role at work.'], ['c', 'Look into supervision classes.']],
    ['Ask a supervisor how they moved into leadership.', 'Look at production supervisor job ads in your area.',
     'Ask your employer about lead or trainer roles.', 'Ask about pay, shifts, and leadership training.'],
    {'a': ['Ask what a normal shift looks like.', 'Ask what was hardest when they started leading people.', 'Notice whether leading a team sounds good to you.'],
     'b': ['Offer to train a new coworker.', 'Ask to help with safety meetings.', 'Write down what you learn about leading people.'],
     'c': ['Read about the operations management and supervision programs at Bismarck State College and the University of North Dakota.', 'Compare short courses and degrees.', 'Ask whether your employer pays for classes.']},
    'Every factory shift needs someone who keeps people safe, work moving, and quality high. Many supervisors started on the floor themselves. Clear communication and fairness matter as much as knowing the machines.',
    'Talking with a production supervisor is a useful next step.',
    [['Welcome', '<p>When a plant runs well, someone is making sure the right people are on the right jobs, safely. That person is the production supervisor.</p>'
      '<p>This job mixes leadership, problem solving, and the plant floor. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Production Supervisor?', '<p>You lead a team of production workers in a factory or plant. You plan the work, keep people safe, and solve problems during the shift.</p>{{IMAGE0}}'
      '<ul><li>Plan schedules and assign jobs to meet production goals.</li><li>Enforce safety and cleanliness rules.</li>'
      '<li>Check products and equipment for problems.</li><li>Keep records of hours, output, and quality.</li>'
      '<li>Train new workers and give feedback.</li><li>Work with maintenance, shipping, and other departments.</li></ul>'
      '<p><strong>The real picture:</strong> You are responsible for both people and numbers. Some days are calm; others bring breakdowns and short staffing.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every plant runs on its own schedule.</p><ul>'
      '<li>Start of shift: Lead a short huddle about safety, goals, and staffing.</li>'
      '<li>Morning: Walk the floor and check that each line is running.</li>'
      '<li>Midday: Work with maintenance to fix a machine that went down.</li>'
      '<li>Afternoon: Coach a new worker and review quality checks.</li>'
      '<li>End of shift: Record output and pass notes to the next supervisor.</li></ul>'
      '<p>Plants that run around the clock need supervisors on every shift.</p>'],
     ['How You Learn the Job', '<p><strong>Many supervisors start on the floor.</strong> About a third of people in this job say a high school diploma is what it needs, along with experience. Some employers want college classes or a degree.</p><ul>'
      '<li><strong>Grow from within:</strong> Machine operators and assemblers often become leads, then supervisors.</li>'
      '<li><strong>Leadership training:</strong> Many employers offer supervisor training.</li>'
      '<li><strong>Optional education:</strong> Bismarck State College and the University of North Dakota offer operations management and supervision programs.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>No state license is needed. Requirements depend on the employer. Ask what you need.</p><ul>'
      '<li>Experience in production or a related job.</li><li>Knowledge of safety rules for the plant.</li>'
      '<li>Comfort with computers for schedules and reports.</li><li>Willingness to work shifts, which may include nights or weekends.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask what leadership training and support new supervisors get.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Senior supervisor:</strong> Lead several lines or a whole shift.</li>'
      '<li><strong>Production or plant manager:</strong> Run the whole operation.</li>'
      '<li><strong>Safety or quality specialist:</strong> Focus on one area you enjoy.</li>'
      '<li><strong>Training:</strong> Teach new workers and leads.</li></ul>'
      '<p>Ask leaders where you work which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Leading and helping people grow.</li><li>Solving problems on the spot.</li>'
      '<li>Strong pay that grows with experience.</li><li>A path from the floor into management.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Pressure from goals and deadlines.</li><li>Handling conflicts and discipline.</li>'
      '<li>Night, weekend, or rotating shifts.</li><li>Being called when something breaks.</li></ul>'
      '<p>North Dakota projects about 7% growth in these jobs from 2024 to 2034, with about 180 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Does leading a team on a busy plant floor sound good to you?</p>']],
    ('North Dakota production supervisor pay — May 2025:',
     'Food processing plants, equipment manufacturers, energy and ethanol plants, and other factories.',
     'Plant floors and offices. Shifts may include nights and weekends.',
     'Ask about base pay, shift pay, bonuses, benefits, and leadership training.'),
    'Pay figures are for first-line supervisors of production and operating workers.',
    group='Plants, Projects and Science', hubGroup='Plants, Projects and Science')
