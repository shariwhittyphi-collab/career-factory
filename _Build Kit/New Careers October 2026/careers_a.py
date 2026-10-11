from content_common import *

C = []

# ---------------------------------------------------------------- Administrative Assistant
c = dict(
    name='Administrative Assistant', slug='administrative-assistant', area='jobs-you-can-start-now',
    areaName='Jobs You Can Start Now', soc='43-6014.00',
    subtitle='Keeping an office organized so everyone else can do their work',
    images=['admin-assistant-1.jpg', 'admin-assistant-2.jpg'],
    alts=['An administrative assistant sorts documents into folders at an office workstation.',
          'An administrative assistant sets out meeting packets around a conference table.'],
    wages=dict(p10=16.79, p25=19.36, p50=22.83, p75=25.91, p90=29.22, p50a=47480),
    proj=dict(y0=2024, y1=2034, **{'from': 6490}, to=6640, pct=2, open=720),
    tags=['office', 'administrative', 'computer', 'scheduling', 'customer service', 'clerical'],
    facets=['20-to-30', 'flat', 'many-openings'],
    motivation=['I like keeping things organized.', 'I like helping people and answering questions.',
                'I want an indoor job that uses a computer.'],
    readiness=['I can keep track of several small tasks at once.',
               'I would learn to use email, a calendar, and word processing programs.',
               'I can answer the phone and take a clear message.',
               'I can check details like names, dates, and spelling.',
               'I can stay calm and polite when someone is upset or in a hurry.',
               'I would keep private information private.',
               'I can sit at a desk and use a computer for much of the day.',
               'I would ask questions when I am not sure how something is done.'],
    future=[['a', 'Talk with an administrative assistant about their day.'],
            ['b', 'Practice the computer skills offices ask for.'],
            ['c', 'Compare office job ads and what they require.']] + FUTURE_TAIL,
    nextSteps=['Ask an office worker what a normal day looks like.',
               'Look at current administrative assistant job ads in your area.',
               'Check which computer programs the ads mention most.',
               'Ask about training, pay, schedule, and support while learning.'],
    futureSteps={'a': ['Ask someone you know who works in an office if you can ask a few questions.',
                       'Ask what they do first thing in the morning and what surprises new people.',
                       'Notice whether the mix of people, phones, and paperwork sounds good to you.'],
                 'b': ['Practice typing, email, a calendar, and a simple spreadsheet.',
                       'Look for free computer classes at a library or job center.',
                       'Save a short list of the programs you can now use for your resume.'],
                 'c': ['Read five job ads and mark the skills that show up again and again.',
                       'Compare full-time, part-time, and temporary office jobs.',
                       'Compare pay, hours, benefits, and how each employer trains new staff.']},
    final=('Almost every business, school, clinic, and government office needs someone who keeps things running. '
           'You can start with skills you build one at a time: phones, email, a calendar, and careful records. '
           'Being organized and kind to the people who walk in matters as much as knowing every program.'),
)
c['recs'] = recs_for('administrative assistant', 'Talking with an administrative assistant is a useful next step.')
c['sources'] = [['O*NET OnLine — occupation information', 'https://www.onetonline.org/link/summary/43-6014.00'],
                ['North Dakota pay — BLS May 2025, via O*NET', 'https://www.onetonline.org/link/localwages/43-6014.00?st=ND'],
                ['North Dakota outlook — Projections Central 2024–2034, via O*NET', 'https://www.onetonline.org/link/localtrends/43-6014.00?st=ND'],
                ['North Dakota schools and programs — via O*NET', 'https://www.onetonline.org/link/localtraining/43-6014.00?st=ND']]
c['sourceNote'] = 'Pay figures are for secretaries and administrative assistants, not including legal, medical, or executive assistants.'
c['sections'] = [
    ['Welcome', '<p>Someone answers the phone. Someone knows where the file is. Someone set up the meeting and made sure everyone had what they needed. In many offices, that person is the administrative assistant.</p>'
     '<p>This career mixes computer work, people skills, and organization. Explore what it feels like before deciding whether it interests you.</p>'
     '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
    ['What is an Administrative Assistant?', '<p>You help an office run smoothly. You answer phones and greet visitors, keep calendars, prepare documents, and keep files in order. You might work for one boss or for a whole team.</p>{{IMAGE0}}'
     '<ul><li>Answer phones, take messages, and send calls to the right person.</li><li>Greet visitors and help them find what they need.</li>'
     '<li>Schedule and confirm appointments and meetings.</li><li>Type letters, notes, and short reports.</li>'
     '<li>Enter information into computer systems and keep files organized.</li><li>Order supplies and arrange repairs for office equipment.</li></ul>'
     '<p><strong>The real picture:</strong> The job changes a lot from one office to the next. A school office, a clinic, a farm cooperative, and a state agency all need administrative help, but the details and the pace are different.</p>'],
    ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every office runs on its own schedule.</p><ul>'
     '<li>Morning: Check email and voicemail, then look at today\'s calendar.</li>'
     '<li>Later: Greet a visitor, answer several calls, and fix a scheduling mix-up.</li>'
     '<li>Midday: Print and put together packets for an afternoon meeting.</li>'
     '<li>Afternoon: Enter information into a database and file the paperwork.</li>'
     '<li>Before leaving: Write down what is unfinished and set up tomorrow\'s first tasks.</li></ul>'
     '<p>Some days are quiet. Others bring many interruptions at once. Learning to keep a list and come back to a task is part of the job.</p>'],
    ['How You Learn the Job', '<p><strong>A four-year degree is not the usual entry route.</strong> About half of the people in this job say a high school diploma or GED is what the job needs. Many learn the office\'s systems on the job. Some employers ask for an associate degree or office experience, so read the actual job ad.</p><ul>'
     '<li><strong>Build basic skills first:</strong> Typing, email, a calendar, word processing, and a simple spreadsheet. The programs offices list most are Microsoft Outlook, Word, Excel, and PowerPoint.</li>'
     '<li><strong>Start nearby:</strong> A receptionist, front desk, or office clerk job can lead to administrative work.</li>'
     '<li><strong>On-the-job training:</strong> Each office teaches its own phone system, records, and rules.</li>'
     '<li><strong>Optional education:</strong> North Dakota schools offering administrative assistant certificates or associate degrees include Bismarck State College, Cankdeska Cikana Community College in Fort Totten, Dickinson State University, Dakota College at Bottineau, Williston State College, and Rasmussen University in Fargo. Compare cost, length, and whether classes are online.</li></ul>'
     + FUNDING],
    ['Training and Employer Requirements', '<p>No state license is needed for this job. Requirements depend on the employer. Ask what you need to start.</p><ul>'
     '<li>Comfort with a computer, email, and common office programs.</li><li>Clear phone manners and careful spelling.</li>'
     '<li>A background check for jobs in schools, clinics, banks, or government offices.</li>'
     '<li>Training in the office\'s own systems, which the employer usually provides.</li>'
     '<li>Optional office skills certificates; ask whether an employer actually wants one before you pay for it.</li></ul>'
     '<p><strong>Before you begin:</strong> Ask who trains new staff, how long training lasts, and who you can go to with questions.</p>' + SUPPORT],
    ['Pay and Job Outlook', None],
    ['Where This Can Lead', '<ul><li><strong>Experienced assistant:</strong> Handle more complicated scheduling, records, and projects.</li>'
     '<li><strong>Office manager:</strong> Lead the front office and other support staff as experience grows.</li>'
     '<li><strong>Specialized assistant:</strong> Medical, legal, or executive assistant roles may need extra training and often pay more.</li>'
     '<li><strong>A related direction:</strong> Bookkeeping, payroll, human resources, or customer service.</li></ul>'
     '<p>You can enjoy this work for a whole career without becoming a manager. Ask people in the office which paths are actually open.</p>'],
    ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Helping people every day.</li><li>Indoor work with a regular schedule in many offices.</li>'
     '<li>Jobs in almost every town and every kind of business.</li><li>Learning skills you can take to many other jobs.</li></ul>'
     '<p><strong>Things to ask about:</strong></p><ul><li>Interruptions while you are trying to finish something.</li>'
     '<li>Callers or visitors who are upset or in a hurry.</li><li>Long stretches of sitting and computer work.</li>'
     '<li>Busy times with deadlines, such as the end of the month or a big meeting.</li></ul>'
     '<p>Across the country, the number of these jobs is expected to shrink as offices use more software. In North Dakota, the projection is close to flat with about 720 openings a year, mostly from people retiring or changing jobs.</p>'
     '<p><strong>A question for yourself:</strong> Do you like keeping things organized while helping the people around you?</p>'],
]
c['pay'] = pay_section(c, 'North Dakota administrative assistant pay — May 2025:',
    'Schools, clinics, government offices, farm and energy companies, banks, churches, and almost every kind of business.',
    'Usually an office desk with a computer and phone. Many jobs are weekday, daytime hours. Some offices need part-time or early coverage.',
    'Ask about base pay, hours, benefits, paid time off, training, and whether the job is full time, part time, or temporary.')
C.append(c)

# ---------------------------------------------------------------- Office Clerk
c = dict(
    name='Office Clerk', slug='office-clerk', area='jobs-you-can-start-now', areaName='Jobs You Can Start Now', soc='43-9061.00',
    subtitle='Records, mail, copies and the many tasks that keep an office moving',
    images=['office-clerk-1.jpg', 'office-clerk-2.jpg'],
    alts=['An office clerk feeds a stack of paper records into a scanner.',
          'An office clerk sorts incoming mail into a wall of mail slots.'],
    wages=dict(p10=16.15, p25=20.52, p50=24.11, p75=29.86, p90=35.93, p50a=50160),
    proj=dict(y0=2024, y1=2034, **{'from': 9960}, to=9760, pct=-2, open=1140),
    tags=['office', 'clerical', 'filing', 'data entry', 'mail', 'computer'],
    facets=['20-to-30', 'declining', 'many-openings'],
    motivation=['I like tasks with clear steps.', 'I like a job where I can see what I finished.',
                'I want an indoor job that uses a computer.'],
    readiness=['I can follow steps in the right order.', 'I can check numbers and names carefully.',
               'I would learn to enter information into a computer system.',
               'I can switch tasks when someone needs help.',
               'I would keep private records private.',
               'I can answer a question at the front counter or on the phone.',
               'I can do some lifting, like boxes of paper or mail bins, or ask about it.',
               'I would ask questions when I am not sure where something goes.'],
    future=[['a', 'Ask an office clerk what the work is really like.'],
            ['b', 'Practice data entry and basic computer skills.'],
            ['c', 'Compare clerk jobs in government, schools, and businesses.']] + FUTURE_TAIL,
    nextSteps=['Ask someone who works in an office what clerks do there.',
               'Look at current office clerk job ads near you.',
               'Practice typing and entering information carefully.',
               'Ask about training, pay, schedule, and support while learning.'],
    futureSteps={'a': ['Ask a clerk what tasks fill most of the day.', 'Ask what new people find hard at first.',
                       'Notice whether the steady, step-by-step work sounds good to you.'],
                 'b': ['Practice typing for speed and accuracy.', 'Practice entering a list of names and numbers into a spreadsheet and checking it.',
                       'Look for free computer classes at a library or job center.'],
                 'c': ['Read job ads from a city or county, a school district, and a private business.',
                       'Compare duties, pay, benefits, and hours.', 'Ask which jobs train beginners.']},
    final=('Office clerks keep records, mail, and paperwork moving so other people can do their jobs. '
           'Many people start here and learn how an organization works from the inside. '
           'Careful, steady work is the main skill, and you can build it one task at a time.'),
)
c['recs'] = recs_for('office clerk', 'Asking an office clerk about their day is a useful next step.')
c['sources'] = [['O*NET OnLine — occupation information', 'https://www.onetonline.org/link/summary/43-9061.00'],
                ['North Dakota pay — BLS May 2025, via O*NET', 'https://www.onetonline.org/link/localwages/43-9061.00?st=ND'],
                ['North Dakota outlook — Projections Central 2024–2034, via O*NET', 'https://www.onetonline.org/link/localtrends/43-9061.00?st=ND']]
c['sourceNote'] = 'Pay figures are for general office clerks in North Dakota across all kinds of employers, including government.'
c['sections'] = [
    ['Welcome', '<p>Papers need filing. Mail needs sorting. Records need to be entered and found again later. Office clerks handle many of the tasks that keep an office running.</p>'
     '<p>This job can be a first step into office work. Explore what it feels like before deciding whether it interests you.</p>'
     '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
    ['What is an Office Clerk?', '<p>You do a mix of office tasks. You file and scan records, enter information into computers, sort mail, make copies, and answer questions at a counter or on the phone. The exact mix depends on the office.</p>{{IMAGE0}}'
     '<ul><li>File, scan, and find paper and electronic records.</li><li>Enter information into computer systems and check it.</li>'
     '<li>Sort and send mail and packages.</li><li>Make copies and prepare documents.</li>'
     '<li>Answer phones and help people at a front counter.</li><li>Keep track of office supplies.</li></ul>'
     '<p><strong>The real picture:</strong> Many clerk jobs are in government offices, schools, and large companies. Some are mostly computer work; others include more mail, counter work, or lifting boxes of records.</p>'],
    ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> The schedule depends on the office.</p><ul>'
     '<li>Morning: Sort the mail and deliver it to the right desks.</li>'
     '<li>Later: Scan a stack of old paper records and check that each file saved correctly.</li>'
     '<li>Midday: Help a person at the counter who needs a form.</li>'
     '<li>Afternoon: Enter information from forms into a computer system.</li>'
     '<li>Before leaving: Put away files and note what still needs to be done.</li></ul>'
     '<p>Some work is repetitive. Many clerks like knowing exactly what needs to be done and seeing a stack get smaller.</p>'],
    ['How You Learn the Job', '<p><strong>Most office clerks learn on the job.</strong> Many employers ask for a high school diploma or GED. Read the actual job ad for what each employer wants.</p><ul>'
     '<li><strong>Build basic skills first:</strong> Typing, careful data entry, email, and a simple spreadsheet.</li>'
     '<li><strong>Practice accuracy:</strong> Getting names, dates, and numbers exactly right matters more than speed at first.</li>'
     '<li><strong>On-the-job training:</strong> Each office teaches its own filing system, forms, and computer programs.</li>'
     '<li><strong>Optional education:</strong> Short office skills or computer classes can help. Free classes are often offered at libraries and job centers.</li></ul>'
     + FUNDING],
    ['Training and Employer Requirements', '<p>No state license is needed for this job. Ask the employer what you need to start.</p><ul>'
     '<li>Basic computer and typing skills.</li><li>Careful attention to detail.</li>'
     '<li>A background check for some government, school, health, and bank jobs.</li>'
     '<li>Training on privacy rules for the records you handle.</li>'
     '<li>Some jobs include lifting mail bins or boxes; ask how much.</li></ul>'
     '<p><strong>Before you begin:</strong> Ask who trains new staff and how you will know you are doing a task the right way.</p>' + SUPPORT],
    ['Pay and Job Outlook', None],
    ['Where This Can Lead', '<ul><li><strong>Experienced clerk:</strong> Take on more complicated records and special tasks.</li>'
     '<li><strong>Administrative assistant:</strong> Add scheduling, documents, and more contact with people.</li>'
     '<li><strong>Specialized clerk:</strong> Billing, payroll, bookkeeping, or medical records may need extra training.</li>'
     '<li><strong>Office supervisor:</strong> Lead other clerks as experience grows.</li></ul>'
     '<p>Working inside a school, hospital, or government office can also help you learn about other jobs there.</p>'],
    ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Clear tasks you can finish.</li><li>Indoor work with regular hours in many offices.</li>'
     '<li>Jobs in many kinds of workplaces.</li><li>A way to learn how an organization works.</li></ul>'
     '<p><strong>Things to ask about:</strong></p><ul><li>Repetitive tasks for long stretches.</li><li>Sitting and computer work for much of the day.</li>'
     '<li>Lifting boxes or mail bins.</li><li>Busy times when many forms arrive at once.</li></ul>'
     '<p>North Dakota expects the number of office clerk jobs to shrink a little as more records go digital. There are still about 1,140 openings a year, mostly from people retiring or moving to other jobs.</p>'
     '<p><strong>A question for yourself:</strong> Do you like steady, careful work where you can see what you finished?</p>'],
]
c['pay'] = pay_section(c, 'North Dakota office clerk pay — May 2025:',
    'State, city, and county offices; schools and colleges; hospitals and clinics; banks; and large and small businesses.',
    'An office with a desk and computer, plus time at copiers, scanners, mail areas, or a front counter.',
    'Ask about base pay, hours, benefits, paid time off, training, and whether the job is full time, part time, seasonal, or temporary.')
C.append(c)

# ---------------------------------------------------------------- Bank Teller
c = dict(
    name='Bank Teller', slug='bank-teller', area='jobs-you-can-start-now', areaName='Jobs You Can Start Now', soc='43-3071.00',
    subtitle='Handling money carefully and helping customers at the counter',
    images=['bank-teller-1.jpg', 'bank-teller-2.jpg'],
    alts=['A bank teller counts cash at her drawer behind the teller counter.',
          'A bank teller helps an older customer at a small-town bank counter.'],
    wages=dict(p10=17.84, p25=18.27, p50=18.90, p75=22.04, p90=22.97, p50a=39300),
    proj=dict(y0=2024, y1=2034, **{'from': 1970}, to=1770, pct=-10, open=180),
    tags=['bank', 'money', 'customer service', 'cash handling', 'credit union', 'finance'],
    facets=['under-20', 'declining', 'some-openings'],
    motivation=['I like helping people face to face.', 'I am careful with numbers and money.',
                'I want a job that could lead to more work in banking.'],
    readiness=['I can count money carefully and check my work.', 'I can stay friendly with customers all day.',
               'I would learn to use the bank\'s computer system.', 'I can follow strict rules exactly.',
               'I would keep customers\' information private.', 'I can stay calm if a customer is upset.',
               'I can stand at a counter for much of the day, or ask about other options.',
               'I would ask questions when I am not sure about a rule.'],
    future=[['a', 'Ask a teller or bank staff member about the job.'],
            ['b', 'Practice cash handling and customer service skills.'],
            ['c', 'Compare teller jobs at banks and credit unions.']] + FUTURE_TAIL,
    nextSteps=['Ask a local bank or credit union what a teller does in a day.',
               'Look at current teller job ads in your area.',
               'Practice counting money and making change accurately.',
               'Ask about training, pay, schedule, and support while learning.'],
    futureSteps={'a': ['Ask at a bank or credit union if someone can answer a few questions.',
                       'Ask what a busy day looks like and how tellers balance their drawer.',
                       'Notice whether the mix of money and customers sounds good to you.'],
                 'b': ['Practice counting cash and coins and checking the total twice.',
                       'Practice explaining something simple to a customer clearly.',
                       'Any cashier or customer service job builds these skills.'],
                 'c': ['Compare a large bank, a small-town bank, and a credit union.',
                       'Ask which ones train beginners and what the hours are.',
                       'Ask whether the job can lead to other banking roles.']},
    final=('Tellers are often the first person a customer sees at a bank. '
           'Careful money handling and a friendly manner are the core skills, and both grow with practice. '
           'For some people, the teller window is a first step into a longer banking career.'),
)
c['recs'] = recs_for('bank teller', 'Asking a teller about their day is a useful next step.')
c['sources'] = [['O*NET OnLine — occupation information', 'https://www.onetonline.org/link/summary/43-3071.00'],
                ['North Dakota pay — BLS May 2025, via O*NET', 'https://www.onetonline.org/link/localwages/43-3071.00?st=ND'],
                ['North Dakota outlook — Projections Central 2024–2034, via O*NET', 'https://www.onetonline.org/link/localtrends/43-3071.00?st=ND']]
c['sourceNote'] = 'Pay figures are for tellers at banks, credit unions, and other financial businesses in North Dakota.'
c['sections'] = [
    ['Welcome', '<p>A customer comes in to deposit a paycheck, take out cash, or ask a question about an account. The bank teller helps them and makes sure every dollar is counted correctly.</p>'
     '<p>This job mixes customer service and careful money handling. Explore what it feels like before deciding whether it interests you.</p>'
     '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
    ['What is a Bank Teller?', '<p>You help customers with everyday banking at a counter or drive-up window. You take deposits, give out cash, cash checks, and answer questions. At the end of the day, your cash drawer has to match the computer exactly.</p>{{IMAGE0}}'
     '<ul><li>Take deposits and payments and give out cash.</li><li>Count money carefully and check it twice.</li>'
     '<li>Use the bank\'s computer system for each transaction.</li><li>Check identification and follow security rules.</li>'
     '<li>Answer questions and send customers to the right person for loans or new accounts.</li><li>Balance your cash drawer at the end of the day.</li></ul>'
     '<p><strong>The real picture:</strong> Banks have strict rules, and tellers must follow them exactly. In small towns, tellers often get to know their customers well.</p>'],
    ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Every branch has its own rhythm.</p><ul>'
     '<li>Morning: Count your cash drawer with a coworker before the doors open.</li>'
     '<li>Later: Help a line of customers with deposits and withdrawals.</li>'
     '<li>Midday: A business brings in a large deposit to count and record.</li>'
     '<li>Afternoon: Answer phone questions and help at the drive-up window.</li>'
     '<li>Before leaving: Balance your drawer so it matches the computer to the penny.</li></ul>'
     '<p>Fridays, paydays, and the first of the month can be busy. Some branches are open Saturday mornings.</p>'],
    ['How You Learn the Job', '<p><strong>Most tellers learn on the job.</strong> About 7 in 10 people in this job say a high school diploma or GED is what new workers need. Many banks also want some cash handling or customer service experience. Read the actual job ad.</p><ul>'
     '<li><strong>Build experience first:</strong> Cashier, retail, or customer service jobs teach counting money and helping customers.</li>'
     '<li><strong>Practice accuracy:</strong> Counting cash and checking your work matters more than speed.</li>'
     '<li><strong>On-the-job training:</strong> The bank teaches its computer system, security rules, and procedures, often for several weeks.</li>'
     '<li><strong>Optional education:</strong> Business or accounting classes can help if you want to move up in banking later.</li></ul>'
     + FUNDING],
    ['Training and Employer Requirements', '<p>No state license is needed to be a teller. Banks have their own requirements. Ask what you need to start.</p><ul>'
     '<li>Comfort counting money and using a computer.</li><li>A background check, which banks usually require.</li>'
     '<li>Training in security, privacy, and fraud rules.</li><li>Clear, friendly communication with customers.</li>'
     '<li>A schedule that may include Saturday mornings; ask.</li></ul>'
     '<p><strong>Before you begin:</strong> Ask how long training lasts and who helps you when your drawer does not balance.</p>' + SUPPORT],
    ['Pay and Job Outlook', None],
    ['Where This Can Lead', '<ul><li><strong>Head teller:</strong> Help other tellers and handle larger transactions.</li>'
     '<li><strong>Personal banker:</strong> Open accounts and help customers choose bank services.</li>'
     '<li><strong>Loan or operations work:</strong> Some tellers move into loan processing or back-office banking jobs.</li>'
     '<li><strong>A related direction:</strong> Bookkeeping, customer service, or office work.</li></ul>'
     '<p>Ask your employer whether they help pay for banking or business classes.</p>'],
    ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Helping people with something important to them.</li><li>Clear rules for how things are done.</li>'
     '<li>Mostly daytime hours at many branches.</li><li>A possible first step into banking.</li></ul>'
     '<p><strong>Things to ask about:</strong></p><ul><li>Standing at a counter for long periods.</li><li>Pressure to get every dollar exactly right.</li>'
     '<li>Customers who are frustrated about their money.</li><li>Fewer teller jobs as more banking moves online.</li></ul>'
     '<p>North Dakota expects about 10% fewer teller jobs over ten years, with about 180 openings a year. Pay is close together from beginner to experienced, so moving up often means moving into another banking role.</p>'
     '<p><strong>A question for yourself:</strong> Do you like helping people while being very careful with details?</p>'],
]
c['pay'] = pay_section(c, 'North Dakota teller pay — May 2025:',
    'Banks, credit unions, and other financial businesses in cities and small towns across the state.',
    'A teller counter or drive-up window with a computer and cash drawer. Many tellers spend about half the day standing. The work is indoors with set opening hours.',
    'Ask about base pay, hours, Saturday shifts, benefits, paid time off, training, and help paying for classes.')
C.append(c)

# ---------------------------------------------------------------- Bookkeeping Clerk
c = dict(
    name='Bookkeeping Clerk', slug='bookkeeping-clerk', area='business-finance', areaName='Business and Finance', soc='43-3031.00',
    subtitle='Recording the money coming in and going out, and making sure it adds up',
    images=['bookkeeping-clerk-1.jpg', 'bookkeeping-clerk-2.jpg'],
    alts=['A bookkeeping clerk matches a stack of receipts to a spreadsheet on his computer.',
          'A bookkeeping clerk files paid invoices in a small business office.'],
    wages=dict(p10=17.95, p25=21.52, p50=23.90, p75=28.36, p90=31.75, p50a=49710),
    proj=dict(y0=2024, y1=2034, **{'from': 4440}, to=4330, pct=-3, open=490),
    tags=['bookkeeping', 'accounting', 'numbers', 'QuickBooks', 'spreadsheets', 'office'],
    facets=['20-to-30', 'declining', 'some-openings'],
    motivation=['I like working with numbers.', 'I like it when things add up and are in order.',
                'I want an office job that could grow into accounting.'],
    readiness=['I can check numbers carefully and find small mistakes.', 'I would learn bookkeeping software.',
               'I can use, or would learn, a spreadsheet.', 'I can work on my own for long stretches.',
               'I would keep financial information private.', 'I can meet a deadline at the end of the month.',
               'I would learn basic accounting words like debit and credit.',
               'I would ask questions when numbers do not match.'],
    future=[['a', 'Ask a bookkeeper what the work is really like.'],
            ['b', 'Try a beginner bookkeeping or spreadsheet class.'],
            ['c', 'Compare bookkeeping jobs and what they require.']] + FUTURE_TAIL,
    nextSteps=['Ask a bookkeeper or small business owner how they keep their books.',
               'Look at current bookkeeping job ads near you.',
               'Check which software the ads mention, such as QuickBooks or Excel.',
               'Ask about training, pay, schedule, and support while learning.'],
    futureSteps={'a': ['Ask a bookkeeper what a normal week looks like.', 'Ask what happens when the numbers do not match.',
                       'Notice whether careful number work sounds good to you.'],
                 'b': ['Look for a short bookkeeping or spreadsheet class online or at a college.',
                       'Practice keeping a simple record of money in and money out.',
                       'Ask whether the class teaches software employers use.'],
                 'c': ['Read job ads from small businesses, farms, clinics, and accounting offices.',
                       'Compare which jobs train beginners and which want experience.',
                       'Compare pay, hours, and busy seasons like tax time.']},
    final=('Every business needs to know where its money goes. Bookkeepers keep that record clear and correct. '
           'If you like numbers and order, this work can grow into accounting, payroll, or office leadership. '
           'Careful checking matters more than being a math whiz.'),
)
c['recs'] = recs_for('bookkeeping clerk', 'Asking a bookkeeper about their work is a useful next step.')
c['sources'] = [['O*NET OnLine — occupation information', 'https://www.onetonline.org/link/summary/43-3031.00'],
                ['North Dakota pay — BLS May 2025, via O*NET', 'https://www.onetonline.org/link/localwages/43-3031.00?st=ND'],
                ['North Dakota outlook — Projections Central 2024–2034, via O*NET', 'https://www.onetonline.org/link/localtrends/43-3031.00?st=ND'],
                ['North Dakota schools and programs — via O*NET', 'https://www.onetonline.org/link/localtraining/43-3031.00?st=ND']]
c['sourceNote'] = 'Pay figures are for bookkeeping, accounting, and auditing clerks together.'
c['sections'] = [
    ['Welcome', '<p>A business sells something, pays a bill, and buys supplies. Someone has to record each of those and make sure it all adds up. That is the bookkeeper\'s job.</p>'
     '<p>This career is about numbers, order, and careful checking. Explore what it feels like before deciding whether it interests you.</p>'
     '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
    ['What is a Bookkeeping Clerk?', '<p>You keep a business\'s money records. You enter sales and bills into software, match receipts and bank statements, and find mistakes. Your records help owners and accountants make good decisions.</p>{{IMAGE0}}'
     '<ul><li>Record money coming in and going out.</li><li>Enter bills and invoices and track which are paid.</li>'
     '<li>Match bank statements to the business\'s records.</li><li>Find and fix mistakes when numbers do not match.</li>'
     '<li>Prepare simple reports for owners or accountants.</li><li>Keep financial files organized.</li></ul>'
     '<p><strong>The real picture:</strong> In a small business, one bookkeeper may do everything. In a larger company, you might handle just one part, like bills or customer payments.</p>'],
    ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> The work follows the calendar.</p><ul>'
     '<li>Morning: Enter yesterday\'s sales and receipts into the bookkeeping software.</li>'
     '<li>Later: Pay bills that are due this week and file the invoices.</li>'
     '<li>Midday: Answer a question from a vendor about a payment.</li>'
     '<li>Afternoon: Match the bank statement to the records and track down a small difference.</li>'
     '<li>Before leaving: Note what is left before the end-of-month report.</li></ul>'
     '<p>The end of the month and tax time are often the busiest. Many bookkeepers like the quiet focus of the rest of the month.</p>'],
    ['How You Learn the Job', '<p><strong>There is more than one way in.</strong> About 4 in 10 people in this job say a high school diploma or GED is what new workers need. About 1 in 5 say a short college certificate. Small businesses often train on the job. Read the actual job ad.</p><ul>'
     '<li><strong>Build basic skills first:</strong> Spreadsheets, careful data entry, and basic math with percentages.</li>'
     '<li><strong>Learn the software:</strong> Many employers use QuickBooks or similar programs.</li>'
     '<li><strong>Optional education:</strong> North Dakota schools offering accounting technology or bookkeeping certificates and associate degrees include Williston State College, Dickinson State University, Bismarck State College, Turtle Mountain College in Belcourt, Dakota College at Bottineau, Minot State University, and Rasmussen University in Fargo.</li>'
     '<li><strong>On-the-job training:</strong> Each business has its own way of organizing its books.</li></ul>'
     + FUNDING],
    ['Training and Employer Requirements', '<p>No state license is needed to be a bookkeeper. Requirements depend on the employer. Ask what you need to start.</p><ul>'
     '<li>Comfort with spreadsheets and numbers.</li><li>Experience with bookkeeping software, or willingness to learn it.</li>'
     '<li>A background check for some jobs.</li><li>Care with private financial information.</li>'
     '<li>Optional bookkeeping certifications; ask whether an employer values one before you pay for it.</li></ul>'
     '<p><strong>Before you begin:</strong> Ask who reviews your work at first and who you go to when numbers do not match.</p>' + SUPPORT],
    ['Pay and Job Outlook', None],
    ['Where This Can Lead', '<ul><li><strong>Full-charge bookkeeper:</strong> Handle all of a small business\'s books.</li>'
     '<li><strong>Payroll:</strong> Specialize in paying employees correctly.</li>'
     '<li><strong>Accountant:</strong> A bachelor\'s degree in accounting can lead to accountant jobs.</li>'
     '<li><strong>Office manager:</strong> Combine bookkeeping with running the office.</li></ul>'
     '<p>Some bookkeepers work for themselves and keep books for several small businesses.</p>'],
    ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Work where things add up and you can check them.</li><li>Quiet, focused tasks.</li>'
     '<li>Jobs in many kinds of businesses, including farms and ranches.</li><li>A path toward accounting.</li></ul>'
     '<p><strong>Things to ask about:</strong></p><ul><li>Long stretches at a computer.</li><li>Busy deadlines at month end and tax time.</li>'
     '<li>Hunting for a small mistake that throws everything off.</li><li>Software doing more of the routine entry work.</li></ul>'
     '<p>North Dakota expects a small drop in these jobs over ten years, with about 490 openings a year, mostly from retirements and job changes.</p>'
     '<p><strong>A question for yourself:</strong> Do you enjoy making things add up and finding what is wrong when they do not?</p>'],
]
c['pay'] = pay_section(c, 'North Dakota bookkeeping clerk pay — May 2025:',
    'Small businesses, farms and ranches, accounting offices, clinics, schools, nonprofits, and government offices.',
    'An office desk with a computer. Some jobs are part time or can be partly remote once you are trained.',
    'Ask about base pay, hours, busy seasons, benefits, paid time off, training, and help paying for classes.')
C.append(c)
