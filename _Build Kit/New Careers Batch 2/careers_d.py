"""Batch 2, part D: human services, public safety, and community careers (Career Factory, October 2026)."""
from content_common import *
from careers_c import add, P, ON_SITE, C as _ALL

_start = len(_ALL)

# ---------------------------------------------------------------- Correctional Officer
add('Correctional Officer', 'correctional-officer', 'social-services', 'Social Services and Public Safety', '33-3012.00',
    'Keeping jails and prisons safe for staff and the people who live there',
    'correctional-officer',
    ['A correctional officer watches a grid of camera views at a control desk.',
     'A correctional officer walks a corridor carrying a radio.'],
    dict(p10=22.88, p25=23.77, p50=25.22, p75=29.39, p90=30.23, p50a=52460),
    P(y0=2024, y1=2034, frm=1070, to=1000, pct=-6, open=90),
    ['corrections', 'public safety', 'law enforcement', 'security', 'shift work', 'communication'],
    ['I want to help keep people safe.', 'I like clear rules and structure.', 'I want a job with paid training and benefits.'],
    ['Following strict rules and procedures every time', 'Staying calm when someone is angry or upset', 'Talking respectfully with people from many backgrounds',
     'Watching closely and noticing small changes', 'Writing clear reports about what happened', 'Working nights, weekends, or holidays',
     'Standing and walking for much of a shift', 'Calling for backup instead of handling everything alone'],
    [['a', 'Talk with a correctional officer about the work.'], ['b', 'Learn about state and county hiring.'], ['c', 'Compare corrections job ads.']],
    ['Ask someone who works in corrections what a normal shift is like.', 'Look at state and county correctional officer job ads.',
     'Ask how new officers are trained and supported.', 'Ask about shifts, pay, and benefits.'],
    {'a': ['Ask what surprised them most when they started.', 'Ask how they handle stress after a hard shift.', 'Notice whether this kind of structured, people-focused work sounds right.'],
     'b': ['Read the ND Department of Corrections and Rehabilitation careers page.', 'Look at county jail job postings near you.', 'Write down the age, background check, and training steps.'],
     'c': ['Compare state prisons and county jails.', 'Compare pay, shifts, and benefits.', 'Ask about training length and support for new officers.']},
    'Correctional officers keep a facility safe and orderly, and the way they treat people matters to everyone inside. North Dakota hires people with a high school diploma and pays them while they train. Calm, fair, respectful communication is the most important skill.',
    'Talking with a correctional officer is a useful next step.',
    [['Welcome', '<p>Inside every jail and prison, officers keep things safe and running, around the clock. They also shape the daily lives of the people who live there.</p>'
      '<p>This job mixes security, structure, and people skills. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Correctional Officer?', '<p>You keep order and safety in a jail or prison. You supervise residents, follow security procedures, and respond when something goes wrong.</p>{{IMAGE0}}'
      '<ul><li>Supervise residents during daily activities.</li><li>Count residents and check locks, doors, and gates.</li>'
      '<li>Search areas for items that are not allowed.</li><li>Screen visitors and control entrances.</li>'
      '<li>Write reports about incidents and daily activity.</li><li>Help residents get to programs, meals, and appointments.</li></ul>'
      '<p><strong>The real picture:</strong> Most of the job is talking, watching, and following routines. Being fair and consistent prevents many problems.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every facility runs on its own schedule.</p><ul>'
      '<li>Start of shift: Get a briefing from the officers going off duty.</li>'
      '<li>Morning: Do a count and walk a housing unit.</li>'
      '<li>Midday: Supervise meals and movement to programs.</li>'
      '<li>Afternoon: Watch cameras at a control station and screen visitors.</li>'
      '<li>End of shift: Write reports and brief the next shift.</li></ul>'
      '<p>Most shifts are routine, and some are tense. Officers work as a team and call for help when needed.</p>'],
     ['How You Learn the Job', '<p><strong>A high school diploma or GED is what most jobs ask for.</strong> The North Dakota Department of Corrections and Rehabilitation says it trains new officers and pays them while they train.</p><ul>'
      '<li><strong>Paid training:</strong> New officers learn security, communication, first aid, and how to calm tense situations.</li>'
      '<li><strong>County jails:</strong> North Dakota law requires jail staff who work directly with residents to complete training approved by the state Peace Officer Standards and Training board.</li>'
      '<li><strong>Optional education:</strong> Minot State University offers a corrections and criminal justice program.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>Requirements depend on the employer. Ask each one what you need.</p><ul>'
      '<li>A high school diploma or GED.</li><li>A minimum age; county jails often require age 18, and some employers require 21.</li>'
      '<li>A background check, drug test, and sometimes a physical or fitness test.</li><li>Completion of the employer’s training program.</li>'
      '<li>Willingness to work rotating shifts, including nights and holidays.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask how long training lasts and what support new officers get, including help after a hard shift.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Senior officer or trainer:</strong> Train new staff.</li>'
      '<li><strong>Sergeant, lieutenant, or supervisor:</strong> Lead a shift.</li>'
      '<li><strong>Case manager or programs:</strong> Help residents prepare to return to the community.</li>'
      '<li><strong>Related careers:</strong> Probation officer, police officer, or 911 dispatcher.</li></ul>'
      '<p>Ask officers where you would work which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Paid training and steady public-sector benefits.</li><li>Clear rules and teamwork.</li>'
      '<li>Starting with a high school diploma.</li><li>A chance to treat people with dignity in a hard place.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Stress and exposure to conflict.</li><li>Nights, weekends, holidays, and mandatory overtime.</li>'
      '<li>The emotional weight of the work.</li><li>Support for officers’ mental health.</li></ul>'
      '<p>North Dakota projects about a 6% drop in these jobs from 2024 to 2034, but there are still about 90 openings a year as people retire or change jobs.</p>'
      '<p><strong>A question for yourself:</strong> Can you see yourself staying calm, fair, and steady in a structured, sometimes tense place?</p>']],
    ('North Dakota correctional officer pay — May 2025:',
     'State prisons run by the ND Department of Corrections and Rehabilitation, county and regional jails, and juvenile facilities.',
     'Inside secure facilities, with rotating shifts around the clock.',
     'Ask about base pay, shift pay, overtime, benefits, retirement, and paid training.'),
    'Pay figures are for correctional officers and jailers.',
    [['ND Department of Corrections and Rehabilitation — careers', 'https://www.docr.nd.gov/careers'],
     ['North Dakota correctional facility law (NDCC 12-44.1)', 'https://ndlegis.gov/cencode/t12c44-1.pdf']],
    group='Public Safety', hubGroup='Public Safety')

# ---------------------------------------------------------------- Substance Abuse Counselor
add('Substance Abuse Counselor', 'substance-abuse-counselor', 'social-services', 'Social Services and Public Safety', '21-1011.00',
    'Helping people work toward recovery from alcohol and drug problems',
    'substance-abuse-counselor',
    ['A counselor listens to a client in a calm counseling office.',
     'A counselor leads a small group discussion in a community room.'],
    dict(p10=20.80, p25=26.66, p50=33.00, p75=37.17, p90=41.65, p50a=68630),
    P(y0=2024, y1=2034, frm=1260, to=1500, pct=20, open=130),
    ['counseling', 'addiction', 'recovery', 'mental health', 'helping', 'license'],
    ['I want to help people through hard times.', 'I am a good listener.', 'I want a career with a license and room to grow.'],
    ['Listening closely without judging', 'Talking with people who are struggling or upset', 'Leading a group conversation',
     'Writing careful notes and treatment plans', 'Keeping what people share private', 'Setting healthy limits with clients',
     'Studying for a license exam after college', 'Asking a supervisor for help with a hard situation'],
    [['a', 'Talk with a substance abuse counselor.'], ['b', 'Look into addiction counseling programs.'], ['c', 'Learn the North Dakota license steps.']],
    ['Ask a counselor what a normal week is like.', 'Look at addiction counseling programs in North Dakota.',
     'Read the license steps on the ND Board of Addiction Counseling Examiners site.', 'Ask about pay and support during clinical training.'],
    {'a': ['Ask what drew them to the work.', 'Ask how they take care of themselves.', 'Notice whether this kind of work sounds right for you.'],
     'b': ['Compare programs at Minot State University, the University of Mary, and Nueta Hidatsa Sahnish College.', 'Ask about cost, length, and online options.', 'Ask how each program arranges clinical training.'],
     'c': ['Read the coursework, clinical training, and exam requirements.', 'Write down questions for the board or a school advisor.', 'Ask a counselor how long the process took them.']},
    'Recovery changes lives, families, and whole communities, and North Dakota needs more counselors to help. The path takes college, supervised training, and a state license. Patience, honesty, and respect for each person matter most.',
    'Talking with a licensed addiction counselor is a useful next step.',
    [['Welcome', '<p>When someone decides to change their relationship with alcohol or drugs, a counselor is often part of that journey.</p>'
      '<p>This career mixes listening, planning, and hope. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Substance Abuse Counselor?', '<p>You help people who struggle with alcohol, drugs, or other addictive behaviors. You meet with people one-on-one and in groups, and you work with their families and other providers.</p>{{IMAGE0}}'
      '<ul><li>Meet with clients to understand their needs and goals.</li><li>Write treatment plans with each person.</li>'
      '<li>Lead individual and group sessions.</li><li>Track progress and adjust plans.</li>'
      '<li>Work with doctors, nurses, social workers, and courts.</li><li>Step in to help when someone is in crisis.</li></ul>'
      '<p><strong>The real picture:</strong> Recovery is rarely a straight line. Counselors celebrate progress and keep going through setbacks.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every program works differently.</p><ul>'
      '<li>Morning: Review notes and meet with the team about new clients.</li>'
      '<li>Later: Meet one-on-one with two clients.</li>'
      '<li>Midday: Lead a group session.</li>'
      '<li>Afternoon: Update treatment plans and call a client’s doctor.</li>'
      '<li>Before leaving: Finish notes and plan tomorrow.</li></ul>'
      '<p>Some days are hopeful and others are heavy. Supervision and teamwork help counselors keep going.</p>'],
     ['How You Learn the Job', '<p><strong>This career takes college and a state license.</strong> North Dakota licensed addiction counselors complete board-approved college coursework, at least 960 hours of supervised clinical training, and a national exam.</p><ul>'
      '<li><strong>North Dakota programs:</strong> Minot State University and the University of Mary offer bachelor’s programs in addiction counseling. Nueta Hidatsa Sahnish College in New Town offers an associate program.</li>'
      '<li><strong>Clinical training:</strong> You practice under supervision in an approved program.</li>'
      '<li><strong>Another route:</strong> Licensed professional counselors in North Dakota need a master’s degree in counseling; some also treat addiction.</li>'
      '<li><strong>Start nearby:</strong> Recovery support, peer support, or human service assistant jobs can be a first step.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>To practice as a licensed addiction counselor in North Dakota, you need a license from the North Dakota Board of Addiction Counseling Examiners. Confirm the exact education rules with the board before you choose a program.</p><ul>'
      '<li>Board-approved college coursework.</li><li>At least 960 hours of supervised clinical training.</li>'
      '<li>Passing the board-approved exam.</li><li>A background check for most jobs.</li>'
      '<li>Continuing education to keep the license.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask schools how they help students find clinical training placements.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Experienced counselor:</strong> Specialize in youth, families, or co-occurring mental health needs.</li>'
      '<li><strong>Clinical supervisor:</strong> Train and supervise new counselors.</li>'
      '<li><strong>Program director:</strong> Lead a treatment program.</li>'
      '<li><strong>More education:</strong> A master’s degree can lead to a professional counselor license.</li></ul>'
      '<p>Ask counselors near you which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Helping people rebuild their lives.</li><li>Strong demand in North Dakota.</li>'
      '<li>A licensed profession with room to grow.</li><li>Teamwork with other helpers.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Emotional weight and burnout.</li><li>Lots of paperwork.</li>'
      '<li>Clients who relapse or stop coming.</li><li>Years of school and training before full licensure.</li></ul>'
      '<p>North Dakota projects about 20% growth in these jobs from 2024 to 2034, with about 130 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Can you listen without judging and keep caring when change is slow?</p>']],
    ('North Dakota substance abuse counselor pay — May 2025:',
     'Treatment centers, hospitals, human service centers, tribal health programs, correctional facilities, and private practices.',
     'Offices and group rooms, sometimes with evening hours. Some counselors work by video.',
     'Ask about base pay, supervision for your license, caseload size, benefits, and help with continuing education.'),
    'Pay and outlook figures are for substance abuse, behavioral disorder, and mental health counselors as one group.',
    [['ND Board of Addiction Counseling Examiners — clinical training', 'https://www.ndbace.org/training-continuing-education/clinical-training/'],
     ['North Dakota addiction counselor law (NDCC 43-45)', 'https://ndlegis.gov/cencode/t43c45.pdf']],
    group='Helping People and Families', hubGroup='Helping People and Families')

# ---------------------------------------------------------------- Psychiatric Technician
add('Psychiatric Technician', 'psychiatric-technician', 'healthcare', 'Healthcare', '29-2053.00',
    'Supporting the daily care of people in mental health treatment',
    'psychiatric-technician',
    ['A psychiatric technician walks calmly beside a patient down a hospital hallway.',
     'A psychiatric technician records observations at a nurses’ station.'],
    dict(p10=18.44, p25=18.90, p50=19.21, p75=22.39, p90=26.81, p50a=39960),
    P(y0=2024, y1=2034, frm=210, to=240, pct=16, open=20),
    ['mental health', 'healthcare', 'patient care', 'hospital', 'helping', 'behavioral health'],
    ['I want to help people during hard times.', 'I stay calm when others are upset.', 'I want to work in healthcare without years of school first.'],
    ['Talking calmly with someone who is upset or confused', 'Noticing small changes in how a person acts', 'Helping with daily care like meals and hygiene',
     'Taking vital signs like pulse and blood pressure', 'Writing clear notes about what you saw', 'Following safety plans exactly',
     'Working nights, weekends, or holidays', 'Asking a nurse for help right away when something changes'],
    [['a', 'Talk with a psychiatric technician or mental health worker.'], ['b', 'Look into a mental health technician program.'], ['c', 'Compare hospital and treatment center job ads.']],
    ['Ask someone who works in behavioral health what a shift is like.', 'Read about the program at Williston State College.',
     'Look at mental health technician job ads.', 'Ask about training, shifts, and support.'],
    {'a': ['Ask what the best and hardest parts are.', 'Ask how the team keeps everyone safe.', 'Notice whether this kind of care sounds right for you.'],
     'b': ['Read about the psychiatric and mental health technician certificate and associate degree at Williston State College.', 'Compare cost and length.', 'Ask whether employers train on the job.'],
     'c': ['Compare hospitals, treatment centers, and residential programs.', 'Compare pay, shifts, and benefits.', 'Ask what de-escalation training they provide.']},
    'People in mental health treatment need steady, kind care every day. Psychiatric technicians provide much of it, side by side with nurses and therapists. Patience, calm, and respect matter most.',
    'Talking with someone who works on a behavioral health unit is a useful next step.',
    [['Welcome', '<p>On a mental health unit, technicians spend more time with patients than almost anyone else on the team.</p>'
      '<p>This job mixes caregiving, observation, and calm communication. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Psychiatric Technician?', '<p>You care for people who are getting treatment for mental illness or developmental disabilities. You work under nurses and doctors as part of a team.</p>{{IMAGE0}}'
      '<ul><li>Help patients with daily care and activities.</li><li>Watch for changes in mood or behavior and report them.</li>'
      '<li>Take vital signs.</li><li>Encourage social, work, and recreation skills.</li>'
      '<li>Help lead group activities as directed.</li><li>Help keep everyone safe using approved calming techniques.</li></ul>'
      '<p><strong>The real picture:</strong> Job titles vary. You may see mental health technician, behavioral health technician, or direct care associate.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every unit runs on its own schedule.</p><ul>'
      '<li>Start of shift: Hear a report on each patient from the last shift.</li>'
      '<li>Morning: Help with breakfast and check vital signs.</li>'
      '<li>Midday: Help lead a group activity.</li>'
      '<li>Afternoon: Spend time talking with patients and watching for changes.</li>'
      '<li>End of shift: Write notes and report to the nurse.</li></ul>'
      '<p>Most of the day is steady and caring. Sometimes a patient becomes very upset, and the team works together to keep everyone safe.</p>'],
     ['How You Learn the Job', '<p><strong>Paths vary.</strong> Some employers hire people with a high school diploma and train them; others want a certificate or college classes.</p><ul>'
      '<li><strong>North Dakota program:</strong> Williston State College offers a psychiatric and mental health services technician certificate and associate degree.</li>'
      '<li><strong>On-the-job training:</strong> Employers teach safety, de-escalation, and their own procedures.</li>'
      '<li><strong>Start nearby:</strong> Certified nurse aide or direct support professional jobs can lead to this work.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>We did not find a North Dakota license for psychiatric technicians. Requirements depend on the employer. Ask each one what you need.</p><ul>'
      '<li>A high school diploma or GED, and sometimes a certificate.</li><li>CPR certification and de-escalation training.</li>'
      '<li>A background check.</li><li>Willingness to work shifts, including nights and weekends.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask what safety training you get and how staff support each other after a hard shift.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Lead technician:</strong> Train new staff.</li>'
      '<li><strong>Nursing:</strong> Many technicians go on to become LPNs or RNs.</li>'
      '<li><strong>Counseling or social work:</strong> With more college.</li>'
      '<li><strong>Activities or recreation therapy:</strong> Focus on groups and activities.</li></ul>'
      '<p>Ask people on your unit which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Making a real difference in someone’s hardest days.</li><li>Teamwork with nurses and therapists.</li>'
      '<li>A way into healthcare.</li><li>Learning a lot about mental health.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Emotional stress.</li><li>The risk of being hurt when a patient is very upset.</li>'
      '<li>Nights, weekends, and holidays.</li><li>Pay that starts lower than some healthcare jobs.</li></ul>'
      '<p>North Dakota projects about 16% growth in these jobs from 2024 to 2034, with about 20 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Can you stay calm and kind with someone who is having a very hard day?</p>']],
    ('North Dakota psychiatric technician pay — May 2025:',
     'Hospitals with behavioral health units, the State Hospital and other state facilities, residential treatment centers, and group homes.',
     'Hospital units and treatment facilities, with shifts around the clock.',
     'Ask about base pay, shift pay, benefits, safety training, and help paying for nursing school.'),
    'Many similar jobs use other titles, such as mental health technician or direct care associate, and may be counted under other job groups.',
    group='Therapy & Rehabilitation', hubGroup='Therapy & Rehabilitation')

# ---------------------------------------------------------------- Social and Human Service Assistant
add('Social and Human Service Assistant', 'social-and-human-service-assistant', 'social-services', 'Social Services and Public Safety', '21-1093.00',
    'Connecting people with the services and support they need',
    'human-service-assistant',
    ['A human service assistant helps a client fill out a form at an agency desk.',
     'A human service assistant loads groceries into a client’s car at a food pantry.'],
    dict(p10=17.92, p25=18.88, p50=22.24, p75=26.10, p90=31.81, p50a=46260),
    P(y0=2024, y1=2034, frm=1330, to=1490, pct=12, open=160),
    ['human services', 'case management', 'community', 'helping', 'social work', 'nonprofit'],
    ['I want to help people get what they need.', 'I like solving practical problems.', 'I want to work in my community.'],
    ['Helping someone fill out forms and applications', 'Explaining services in plain words', 'Listening to people who are stressed or upset',
     'Keeping careful records', 'Keeping what people share private', 'Calling other agencies to find help',
     'Driving to visit people at home or in the community', 'Asking a supervisor when a situation is beyond your role'],
    [['a', 'Talk with someone who works at a community agency.'], ['b', 'Volunteer with a local program.'], ['c', 'Look into human services classes.']],
    ['Ask someone at a community agency what a normal day is like.', 'Look at human service job ads in your area.',
     'Volunteer at a food pantry, shelter, or community program.', 'Ask about training, pay, and support.'],
    {'a': ['Ask what kinds of problems people bring in.', 'Ask what new staff find hard.', 'Notice whether this work sounds good to you.'],
     'b': ['Find a local program that needs volunteers.', 'Notice how staff talk with people.', 'Write down what you enjoyed.'],
     'c': ['Compare human services programs at North Dakota colleges.', 'Compare cost, length, and online options.', 'Ask whether employers help pay for classes.']},
    'When people need food, housing, or help getting services, human service assistants help them find a way. Many start with a certificate or associate degree and grow from there. Respect, patience, and follow-through matter most.',
    'Talking with someone who works at a community agency is a useful next step.',
    [['Welcome', '<p>Applying for help can be confusing and stressful. Human service assistants help people find their way through it.</p>'
      '<p>This job mixes helping, organizing, and problem solving. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Social and Human Service Assistant?', '<p>You help people get services like food, housing, health care, and job help. You often work alongside social workers and case managers.</p>{{IMAGE0}}'
      '<ul><li>Meet with people to learn what they need.</li><li>Help fill out applications and gather papers.</li>'
      '<li>Connect people with programs and agencies.</li><li>Keep records and write reports.</li>'
      '<li>Visit people at home or in the community.</li><li>Follow up to see how things are going.</li></ul>'
      '<p><strong>The real picture:</strong> Job titles vary: case aide, family support worker, outreach worker, or program assistant.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every agency is different.</p><ul>'
      '<li>Morning: Check messages and meet with a supervisor about new cases.</li>'
      '<li>Later: Help a family apply for food assistance.</li>'
      '<li>Midday: Help at the food pantry.</li>'
      '<li>Afternoon: Call agencies to find housing help for a client.</li>'
      '<li>Before leaving: Update case notes.</li></ul>'
      '<p>Some days you see quick wins. Other problems take weeks to solve.</p>'],
     ['How You Learn the Job', '<p><strong>Paths vary.</strong> Some employers want a bachelor’s degree, and others hire people with an associate degree, some college, or experience.</p><ul>'
      '<li><strong>North Dakota programs:</strong> Human services programs are offered at Bismarck State College, United Tribes Technical College, the University of Mary, Valley City State University, Nueta Hidatsa Sahnish College, Turtle Mountain College, Sitting Bull College, and Rasmussen University in Fargo.</li>'
      '<li><strong>On-the-job training:</strong> Agencies teach their programs and record systems.</li>'
      '<li><strong>Start nearby:</strong> Volunteering or front-desk work at an agency can open the door.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>We did not find a North Dakota license for this job. Requirements depend on the employer. Ask what you need.</p><ul>'
      '<li>A high school diploma, and often some college or a degree.</li><li>A background check.</li>'
      '<li>A driver’s license for home and community visits.</li><li>Comfort with computers and record keeping.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask about caseload size and how supervisors support new staff.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Case manager:</strong> Handle more complex cases.</li>'
      '<li><strong>Social worker:</strong> With a social work degree and license.</li>'
      '<li><strong>Program coordinator:</strong> Run a community program.</li>'
      '<li><strong>Specialist:</strong> Focus on youth, older adults, housing, or disability services.</li></ul>'
      '<p>Ask people in your agency which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Helping your own community.</li><li>Seeing problems get solved.</li>'
      '<li>Many kinds of agencies to choose from.</li><li>Growing demand in North Dakota.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Heavy caseloads and paperwork.</li><li>Stress from people’s hard situations.</li>'
      '<li>Pay that may start modest.</li><li>Rules that limit what you can do.</li></ul>'
      '<p>North Dakota projects about 12% growth in these jobs from 2024 to 2034, with about 160 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Do you enjoy solving practical problems so people get the help they need?</p>']],
    ('North Dakota social and human service assistant pay — May 2025:',
     'Human service zones and county agencies, nonprofits, tribal programs, shelters, and community action agencies.',
     'Offices, homes, and community settings. Some jobs include evenings.',
     'Ask about base pay, caseload, mileage pay, benefits, and help paying for school.'),
    'Pay figures are for social and human service assistants.',
    group='Helping People and Families', hubGroup='Helping People and Families')

# ---------------------------------------------------------------- Community Health Worker
add('Community Health Worker', 'community-health-worker', 'social-services', 'Social Services and Public Safety', '21-1094.00',
    'Helping neighbors understand their health and find care',
    'community-health-worker',
    ['A community health worker goes over a handout with a client at a kitchen table.',
     'A community health worker hands out pamphlets at a community health fair.'],
    dict(p10=21.54, p25=22.18, p50=28.66, p75=35.33, p90=36.64, p50a=59610),
    P(y0=2024, y1=2034, frm=90, to=100, pct=10, open=10),
    ['health', 'community', 'outreach', 'public health', 'helping', 'education'],
    ['I want to help people in my community stay healthy.', 'I like talking with people.', 'I want to connect people with care.'],
    ['Talking with people in their homes and in the community', 'Explaining health information in plain words', 'Listening to people’s worries and goals',
     'Helping people make and keep appointments', 'Keeping careful records', 'Keeping health information private',
     'Driving to visits around town or the county', 'Knowing when to refer someone to a nurse or doctor'],
    [['a', 'Talk with a community health worker.'], ['b', 'Learn about North Dakota CHW certification.'], ['c', 'Look at CHW and outreach job ads.']],
    ['Ask a community health worker what a normal week is like.', 'Read about North Dakota’s CHW certification.',
     'Look at community health and outreach job ads.', 'Ask about training and support.'],
    {'a': ['Ask who they help and how.', 'Ask what training helped them most.', 'Notice whether this work sounds right for you.'],
     'b': ['Read the four certification pathways on the ND Health and Human Services site.', 'Find a CHW training program.', 'Ask employers whether they require certification.'],
     'c': ['Compare public health, clinic, and tribal health jobs.', 'Compare pay, travel, and hours.', 'Ask which employers train new workers.']},
    'Community health workers are trusted helpers who bridge the gap between people and health care. North Dakota now certifies them, which helps pay for their services. Trust, respect, and knowing your community matter most.',
    'Talking with a community health worker is a useful next step.',
    [['Welcome', '<p>Sometimes the most helpful health worker is someone from the neighborhood who knows how to explain things and where to find help.</p>'
      '<p>This job mixes outreach, education, and support. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Community Health Worker?', '<p>You help people understand their health and connect with care and services. You often work in the community you come from.</p>{{IMAGE0}}'
      '<ul><li>Visit people at home or meet them in the community.</li><li>Explain health information in plain words.</li>'
      '<li>Help people manage conditions like diabetes day to day.</li><li>Connect people with clinics and services.</li>'
      '<li>Follow up to see how things are going.</li><li>Keep records of visits.</li></ul>'
      '<p><strong>The real picture:</strong> Titles vary, such as community health representative, outreach worker, or patient navigator.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every program works differently.</p><ul>'
      '<li>Morning: Plan home visits and check messages.</li>'
      '<li>Later: Visit a client to talk about managing blood sugar.</li>'
      '<li>Midday: Help another client schedule a clinic visit and find a ride.</li>'
      '<li>Afternoon: Staff a table at a community event.</li>'
      '<li>Before leaving: Record visits and plan follow-ups.</li></ul>'
      '<p>Much of the day is spent on the road and with people, not at a desk.</p>'],
     ['How You Learn the Job', '<p><strong>North Dakota began certifying community health workers in October 2025.</strong> Certification creates a way for North Dakota Medicaid to pay for their services.</p><ul>'
      '<li><strong>Certification pathways:</strong> A CHW training program plus a 200-hour internship; Indian Health Service community health representative training; 1,000 hours of supervised CHW work within three years; or certification from another state.</li>'
      '<li><strong>College:</strong> Some employers want a degree in public health or a related field. North Dakota options include UND, NDSU, Dickinson State University, the University of Jamestown, and Turtle Mountain College.</li>'
      '<li><strong>On-the-job training:</strong> Employers teach their programs and community resources.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>Ask each employer whether they require North Dakota CHW certification. Certified CHWs renew with 12 hours of continuing education, including 2 on legal and ethical topics.</p><ul>'
      '<li>Strong ties to the community you will serve.</li><li>A driver’s license and reliable car for visits.</li>'
      '<li>A background check.</li><li>Comfort keeping health information private.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask how the employer trains and supervises CHWs.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Senior CHW or team lead:</strong> Train and support new CHWs.</li>'
      '<li><strong>Health educator:</strong> With more education.</li>'
      '<li><strong>Nursing or social work:</strong> Many CHWs go on to college.</li>'
      '<li><strong>Program coordinator:</strong> Run a community health program.</li></ul>'
      '<p>Ask people in public health near you which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Helping your own community.</li><li>Time out with people instead of at a desk.</li>'
      '<li>A growing field with new certification.</li><li>Seeing people get healthier.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Few jobs in some areas.</li><li>Travel and mileage.</li>'
      '<li>Jobs that depend on grant funding.</li><li>The emotional weight of people’s struggles.</li></ul>'
      '<p>North Dakota projects about 10% growth in these jobs from 2024 to 2034. It is a small field, with about 10 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Would you like to be the trusted person who helps neighbors find care?</p>']],
    ('North Dakota community health worker pay — May 2025:',
     'Public health units, clinics and hospitals, tribal health programs, and nonprofits.',
     'Homes, community places, and offices, with a lot of driving.',
     'Ask about base pay, mileage, whether the job is grant funded, benefits, and training.'),
    'Pay figures are for community health workers. Few workers are counted in North Dakota, so figures may change a lot from year to year.',
    [['North Dakota community health worker certification — ND Health and Human Services', 'https://www.hhs.nd.gov/regulation-licensure-and-certification/comm-hlth-worker']],
    group='Helping People and Families', hubGroup='Helping People and Families')

# ---------------------------------------------------------------- 911 Dispatcher
add('911 Dispatcher', '911-dispatcher', 'social-services', 'Social Services and Public Safety', '43-5031.00',
    'Answering emergency calls and sending help where it is needed',
    'dispatcher',
    ['A 911 dispatcher wearing a headset types at a console with several monitors.',
     'A 911 dispatcher speaks into a headset while keying a radio.'],
    dict(p10=22.97, p25=23.88, p50=28.82, p75=29.45, p90=30.37, p50a=59940),
    P(y0=2024, y1=2034, frm=300, to=320, pct=6, open=30),
    ['911', 'dispatch', 'public safety', 'emergency', 'communication', 'computer'],
    ['I want to help people in an emergency.', 'I stay calm under pressure.', 'I like fast-paced work with a computer and phone.'],
    ['Staying calm when a caller is panicking', 'Asking clear questions quickly', 'Typing while listening and talking',
     'Following a script and set procedures', 'Keeping track of several things at once', 'Working nights, weekends, and holidays',
     'Sitting at a console for a long shift', 'Asking a coworker for help on a hard call'],
    [['a', 'Ask a 911 dispatcher about the work.'], ['b', 'Learn the hiring steps for a dispatch center.'], ['c', 'Practice typing and multitasking.']],
    ['Ask whether your local dispatch center offers sit-alongs or tours.', 'Look at dispatcher job ads in North Dakota.',
     'Practice typing for speed and accuracy.', 'Ask about training, shifts, and support.'],
    {'a': ['Ask what a normal shift is like.', 'Ask how they cope after a hard call.', 'Notice whether this work sounds right for you.'],
     'b': ['Read job postings and write down the background check, hearing, and drug screening steps.', 'Ask how long training lasts.', 'Ask whether they train in emergency medical dispatch.'],
     'c': ['Take a free typing test online.', 'Practice listening and typing at the same time.', 'Write down what was hard.']},
    'When someone calls 911, the dispatcher is the first person who helps. North Dakota dispatch centers train new hires, including how to give medical instructions. A calm voice and clear thinking matter most.',
    'Talking with a 911 dispatcher is a useful next step.',
    [['Welcome', '<p>The first voice people hear in an emergency belongs to a 911 dispatcher.</p>'
      '<p>This job mixes calm communication, quick thinking, and teamwork. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a 911 Dispatcher?', '<p>You answer emergency and non-emergency calls and send police, fire, and ambulance crews where they are needed.</p>{{IMAGE0}}'
      '<ul><li>Answer calls and find out where the caller is.</li><li>Ask questions to learn what is happening.</li>'
      '<li>Decide which calls are most urgent.</li><li>Send the right crews by radio and computer.</li>'
      '<li>Give callers instructions until help arrives.</li><li>Record details of every call.</li></ul>'
      '<p><strong>The real picture:</strong> Many calls are not emergencies. Some are frightening. Dispatchers handle both, often at the same time.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every center is different.</p><ul>'
      '<li>Start of shift: Get a briefing on what is happening in the area.</li>'
      '<li>Morning: Handle a car crash call and send crews.</li>'
      '<li>Midday: Answer non-emergency calls and track units by radio.</li>'
      '<li>Afternoon: Give a caller medical instructions until the ambulance arrives.</li>'
      '<li>End of shift: Finish records and brief the next dispatcher.</li></ul>'
      '<p>Quiet stretches can change in seconds.</p>'],
     ['How You Learn the Job', '<p><strong>Most centers hire people with a high school diploma or GED and train them.</strong></p><ul>'
      '<li><strong>Required training:</strong> North Dakota law requires each 911 center to give dispatchers initial and ongoing training.</li>'
      '<li><strong>Medical instructions:</strong> Dispatchers who give medical instructions before help arrives must finish an approved emergency medical dispatch course.</li>'
      '<li><strong>On the job:</strong> New dispatchers train with an experienced dispatcher before working alone.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>North Dakota sets hiring rules for 911 centers. Ask each center for its full list.</p><ul>'
      '<li>Fingerprinting and a nationwide background check, with no felony conviction.</li><li>Drug screening and a hearing test before hiring.</li>'
      '<li>Initial and ongoing training from the center.</li><li>An emergency medical dispatch course to give medical instructions.</li>'
      '<li>Willingness to work rotating 24/7 shifts.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask how the center supports dispatchers after hard calls.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Senior dispatcher or trainer:</strong> Train new dispatchers.</li>'
      '<li><strong>Shift supervisor:</strong> Lead a team.</li>'
      '<li><strong>911 center manager:</strong> Run a dispatch center.</li>'
      '<li><strong>Related careers:</strong> EMT, firefighter, or police officer.</li></ul>'
      '<p>Ask dispatchers near you which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Helping people at the most important moment.</li><li>Teamwork with first responders.</li>'
      '<li>Paid training and steady public jobs.</li><li>Fast-paced, never-boring work.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Stress and upsetting calls.</li><li>Nights, weekends, holidays, and overtime.</li>'
      '<li>Long shifts at a console.</li><li>Support for dispatchers’ mental health.</li></ul>'
      '<p>North Dakota projects about 6% growth in these jobs from 2024 to 2034, with about 30 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Can you stay calm and clear when someone else is in crisis?</p>']],
    ('North Dakota 911 dispatcher pay — May 2025:',
     'City and county 911 centers, state radio, and some hospitals and ambulance services.',
     'Dispatch centers with computers and radios, staffed 24 hours a day.',
     'Ask about base pay, shift pay, overtime, benefits, and support after hard calls.'),
    'Pay figures are for public safety telecommunicators. Outlook figures are for police, fire, and ambulance dispatchers.',
    [['North Dakota 911 law, including dispatcher requirements (NDCC 57-40.6)', 'https://ndlegis.gov/cencode/t57c40-6.pdf']],
    group='Public Safety', hubGroup='Public Safety')

# ---------------------------------------------------------------- Recreation Worker
add('Recreation Worker', 'recreation-worker', 'jobs-you-can-start-now', 'Jobs You Can Start Now', '39-9032.00',
    'Leading activities, games, and programs that help people have fun and stay active',
    'recreation-worker',
    ['A recreation worker sets up cones and balls on a park field.',
     'A recreation worker leads a chair exercise class for older adults.'],
    dict(p10=10.70, p25=14.61, p50=17.94, p75=22.69, p90=25.96, p50a=37310),
    P(y0=2024, y1=2034, frm=960, to=1040, pct=8, open=210),
    ['recreation', 'parks', 'activities', 'youth', 'seniors', 'sports'],
    ['I like helping people have fun.', 'I like being active.', 'I want a job with people instead of a desk.'],
    ['Leading a game or activity for a group', 'Explaining rules clearly and patiently', 'Keeping a group safe and on track',
     'Being active and on your feet', 'Working with children, teens, or older adults', 'Giving first aid if someone gets hurt',
     'Working evenings, weekends, or summers', 'Asking a supervisor for help with a difficult situation'],
    [['a', 'Talk with a recreation worker.'], ['b', 'Volunteer at a park, camp, or senior center.'], ['c', 'Look at seasonal recreation job ads.']],
    ['Ask someone at a park district or senior center about their job.', 'Look at recreation job ads in your area.',
     'Ask about CPR and first aid training.', 'Ask about hours, seasons, and pay.'],
    {'a': ['Ask what a normal day is like.', 'Ask what groups they enjoy most.', 'Notice whether this work sounds fun to you.'],
     'b': ['Volunteer with a youth sports program, camp, or senior activity.', 'Notice what parts you enjoyed.', 'Write down what you learned.'],
     'c': ['Read seasonal job ads for summer programs.', 'Compare part-time and full-time jobs.', 'Ask which require CPR or lifeguard training.']},
    'Parks, camps, and community centers help people of every age stay active and connected. Many recreation workers start part time. Energy, patience, and keeping people safe matter most.',
    'Talking with a recreation worker is a useful next step.',
    [['Welcome', '<p>Summer programs, community events, and senior center classes all need someone to plan the fun and keep it safe.</p>'
      '<p>This job mixes activity, leadership, and people skills. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Recreation Worker?', '<p>You plan and lead activities like sports, games, crafts, and fitness classes in parks, camps, and community centers.</p>{{IMAGE0}}'
      '<ul><li>Set up equipment and spaces.</li><li>Lead games, sports, crafts, and classes.</li>'
      '<li>Plan activities that fit each group.</li><li>Enforce safety rules.</li>'
      '<li>Give first aid when needed.</li><li>Keep attendance and supply records.</li></ul>'
      '<p><strong>The real picture:</strong> Many jobs are part time or seasonal. Full-time jobs often involve more planning and leadership.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every program is different.</p><ul>'
      '<li>Morning: Set up the field for a youth soccer program.</li>'
      '<li>Later: Lead drills and games.</li>'
      '<li>Midday: Lead a chair exercise class at the senior center.</li>'
      '<li>Afternoon: Plan next week’s activities.</li>'
      '<li>Before leaving: Put away equipment and write down attendance.</li></ul>'
      '<p>Weather and turnout can change the plan.</p>'],
     ['How You Learn the Job', '<p><strong>Many part-time jobs need only a high school diploma, and some take teens.</strong> Full-time jobs often want a college degree in recreation or a related field.</p><ul>'
      '<li><strong>On-the-job training:</strong> Employers teach their programs and safety rules.</li>'
      '<li><strong>Certifications:</strong> CPR and first aid are common. Pool jobs need lifeguard certification.</li>'
      '<li><strong>Start nearby:</strong> Volunteering or summer camp jobs build experience.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>We did not find a North Dakota license for recreation workers. Requirements depend on the employer. Ask what you need.</p><ul>'
      '<li>CPR and first aid certification.</li><li>A background check for work with children or vulnerable adults.</li>'
      '<li>Ability to be active and on your feet.</li><li>Willingness to work evenings, weekends, or summers.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask what training is provided and how staff handle emergencies.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Program leader:</strong> Plan and run whole programs.</li>'
      '<li><strong>Recreation coordinator:</strong> Lead staff and budgets.</li>'
      '<li><strong>Recreation therapy:</strong> With a degree, help people heal through activities.</li>'
      '<li><strong>Parks and recreation manager:</strong> Run a park district.</li></ul>'
      '<p>Ask your supervisor which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Fun, active work.</li><li>Making a difference for kids or older adults.</li>'
      '<li>Starting part time without a degree.</li><li>Summer jobs outdoors.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Lower pay in many part-time jobs.</li><li>Seasonal work.</li>'
      '<li>Evenings and weekends.</li><li>Managing behavior in large groups.</li></ul>'
      '<p>North Dakota projects about 8% growth in these jobs from 2024 to 2034, with about 210 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Do you enjoy leading activities and helping others have a good time?</p>']],
    ('North Dakota recreation worker pay — May 2025:',
     'Park districts, cities, YMCAs, camps, senior centers, nursing homes, and after-school programs.',
     'Parks, gyms, camps, and community centers. Many jobs are part time or seasonal.',
     'Ask about hourly pay, hours per week, season length, and whether full-time work is available.'),
    'Pay figures include many part-time and seasonal workers.',
    group='Care, Safety and Investigation')

# ---------------------------------------------------------------- Library Technician
add('Library Technician', 'library-technician', 'education', 'Education', '25-4031.00',
    'Helping people find books, information, and computers at the library',
    'library-technician',
    ['A library technician scans returned books at a circulation desk.',
     'A library technician reshelves books from a cart in a quiet aisle.'],
    dict(p10=16.78, p25=17.45, p50=18.87, p75=21.87, p90=24.08, p50a=39240),
    P(y0=2024, y1=2034, frm=400, to=410, pct=1, open=70),
    ['library', 'books', 'customer service', 'computer', 'organizing', 'education'],
    ['I like books and organizing information.', 'I like helping people find what they need.', 'I want a calm indoor job.'],
    ['Helping people at a front desk', 'Putting books in exact order', 'Learning a library computer system',
     'Helping someone use a computer or printer', 'Answering questions politely and patiently', 'Pushing carts and reaching high and low shelves',
     'Working some evenings or Saturdays', 'Asking a librarian when you are not sure'],
    [['a', 'Talk with a library worker.'], ['b', 'Volunteer at a library.'], ['c', 'Look at library job ads.']],
    ['Ask library staff what their day is like.', 'Look at library assistant and technician job ads.', 'Practice basic computer and customer service skills.',
     'Ask about training, pay, and hours.'],
    {'a': ['Ask what tasks fill most of the day.', 'Ask what new staff learn first.', 'Notice whether library work sounds right for you.'],
     'b': ['Ask your local library about volunteering.', 'Help with shelving or events.', 'Write down what you enjoyed.'],
     'c': ['Compare public, school, and college library jobs.', 'Compare pay, hours, and benefits.', 'Ask which require college classes.']},
    'Libraries help people learn, apply for jobs, and find a quiet place to read. Library technicians keep everything organized and help people use it. Patience and careful organizing matter most.',
    'Talking with library staff is a useful next step.',
    [['Welcome', '<p>From story time to job applications, libraries help whole communities. Library technicians keep them running.</p>'
      '<p>This job mixes organizing, computers, and customer service. Explore what it feels like before deciding whether it interests you.</p>'
      '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
     ['What is a Library Technician?', '<p>You help librarians run the library. You check materials in and out, help visitors, and keep everything organized.</p>{{IMAGE0}}'
      '<ul><li>Check books and other materials in and out.</li><li>Answer simple questions and help people find things.</li>'
      '<li>Help visitors use computers, printers, and online resources.</li><li>Process new books and materials.</li>'
      '<li>Sort and shelve materials.</li><li>Help with programs and events.</li></ul>'
      '<p><strong>The real picture:</strong> Titles vary, such as library assistant, library associate, or circulation clerk.</p>'],
     ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every library is different.</p><ul>'
      '<li>Morning: Check in returned books and sort them.</li>'
      '<li>Later: Help visitors at the front desk.</li>'
      '<li>Midday: Help someone print a job application.</li>'
      '<li>Afternoon: Shelve books and process new arrivals.</li>'
      '<li>Before leaving: Tidy the shelves and set up for an evening program.</li></ul>'
      '<p>Some hours are quiet. Others are busy with families and students.</p>'],
     ['How You Learn the Job', '<p><strong>Paths vary.</strong> Some libraries hire people with a high school diploma; others want an associate degree, a certificate, or a bachelor’s degree.</p><ul>'
      '<li><strong>On-the-job training:</strong> Libraries teach their computer system and procedures.</li>'
      '<li><strong>Online programs:</strong> Library technician certificates and associate degrees are offered online by colleges in other states.</li>'
      '<li><strong>Start nearby:</strong> Library page or volunteer roles can open the door.</li></ul>'
      + FUNDING],
     ['Training and Employer Requirements', '<p>We did not find a North Dakota license for library technicians. Requirements depend on the employer. Ask what you need.</p><ul>'
      '<li>Comfort with computers and careful organizing.</li><li>Friendly, patient customer service.</li>'
      '<li>A background check for school libraries.</li><li>Ability to push carts and reach shelves, or ask about the physical demands.</li></ul>'
      '<p><strong>Before you begin:</strong> Ask how new staff are trained.</p>' + SUPPORT],
     ['Pay and Job Outlook', None],
     ['Where This Can Lead', '<ul><li><strong>Senior technician:</strong> Handle cataloging or interlibrary loans.</li>'
      '<li><strong>Branch or department supervisor:</strong> Lead staff.</li>'
      '<li><strong>Librarian:</strong> With a master’s degree in library science.</li>'
      '<li><strong>School library aide:</strong> Work with students.</li></ul>'
      '<p>Ask library staff which paths are open.</p>'],
     ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>A calm, organized place to work.</li><li>Helping people learn.</li>'
      '<li>Being around books and information.</li><li>Steady public jobs.</li></ul>'
      '<p><strong>Things to ask about:</strong></p><ul><li>Modest pay.</li><li>Part-time jobs and evening or weekend hours.</li>'
      '<li>Few openings.</li><li>Visitors who need a lot of patience.</li></ul>'
      '<p>North Dakota projects the number of these jobs to stay about the same from 2024 to 2034, with about 70 openings a year.</p>'
      '<p><strong>A question for yourself:</strong> Do you enjoy organizing things and helping people find what they need?</p>']],
    ('North Dakota library technician pay — May 2025:',
     'Public libraries, school libraries, colleges and universities, and the State Library.',
     'Library front desks, shelves, and workrooms. Some jobs include evenings and Saturdays.',
     'Ask about hourly pay, hours per week, benefits, and training.'),
    'Pay figures are for library technicians. Some libraries use the title library assistant.',
    group='Libraries and Learning Support', hubGroup='Libraries and Learning Support')

C = _ALL[_start:]
