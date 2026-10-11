from content_common import *

C = []

# ---------------------------------------------------------------- Payroll Clerk
c = dict(
    name='Payroll Clerk', slug='payroll-clerk', area='business-finance', areaName='Business and Finance', soc='43-3051.00',
    subtitle='Making sure every worker is paid the right amount, on time',
    images=['payroll-clerk-1.jpg', 'payroll-clerk-2.jpg'],
    alts=['A payroll clerk checks paper timesheets against a payroll table on her monitor.',
          'A payroll clerk answers a worker\'s question about pay at a company front office.'],
    wages=dict(p10=22.54, p25=25.75, p50=29.13, p75=31.81, p90=37.28, p50a=60600),
    proj=dict(y0=2024, y1=2034, **{'from': 300}, to=280, pct=-9, open=30),
    tags=['payroll', 'timekeeping', 'numbers', 'human resources', 'office', 'spreadsheets'],
    facets=['20-to-30', 'declining', 'few-openings'],
    motivation=['I like working with numbers and rules.', 'I like knowing my work makes a real difference to people.',
                'I am curious about human resources and how businesses run.'],
    readiness=['I can check hours and pay carefully and catch mistakes.', 'I would learn payroll software.',
               'I can use, or would learn, a spreadsheet.', 'I can meet a firm deadline every pay period.',
               'I would keep everyone\'s pay information private.', 'I can explain a paycheck to a worker who has questions.',
               'I would learn the rules for taxes and deductions.', 'I would ask questions when something does not add up.'],
    future=[['a', 'Ask someone who does payroll what the work is like.'],
            ['b', 'Build bookkeeping and spreadsheet skills first.'],
            ['c', 'Look into a beginner payroll certification.']] + FUTURE_TAIL,
    nextSteps=['Ask a payroll, bookkeeping, or human resources worker how payroll is done where they work.',
               'Look at current payroll job ads and what experience they ask for.',
               'Practice spreadsheets and careful number checking.',
               'Ask about training, pay, schedule, and support while learning.'],
    futureSteps={'a': ['Ask what happens on payday and the days before it.', 'Ask what mistakes are most common and how they are fixed.',
                       'Notice whether deadline-driven number work sounds good to you.'],
                 'b': ['Look for a bookkeeping or spreadsheet class.', 'Consider an office or bookkeeping job as a first step.',
                       'Ask whether your employer would let you help with payroll tasks.'],
                 'c': ['Read about the Fundamental Payroll Certification from PayrollOrg.',
                       'Check the current cost and study options before you sign up.',
                       'Ask a local employer whether they value the certification.']},
    final=('Payroll workers make sure people are paid correctly and on time, and workers notice when that goes right. '
           'In North Dakota this is a small field, so many people reach it from bookkeeping, office, or human resources work. '
           'Careful checking and keeping information private are the heart of the job.'),
)
c['recs'] = recs_for('payroll clerk', 'Asking someone who does payroll about their work is a useful next step.')
c['sources'] = [['O*NET OnLine — occupation information', 'https://www.onetonline.org/link/summary/43-3051.00'],
                ['North Dakota pay — BLS May 2025, via O*NET', 'https://www.onetonline.org/link/localwages/43-3051.00?st=ND'],
                ['North Dakota outlook — Projections Central 2024–2034, via O*NET', 'https://www.onetonline.org/link/localtrends/43-3051.00?st=ND'],
                ['PayrollOrg — Fundamental Payroll Certification (FPC)', 'https://www.payroll.org/education-certification/certification/fundamental-payroll-certification-(fpc)']]
c['sourceNote'] = ('Pay figures are for payroll and timekeeping clerks. North Dakota counts only about 300 of these jobs, '
                   'because many businesses give payroll to bookkeepers, office managers, human resources staff, or payroll companies.')
c['sections'] = [
    ['Welcome', '<p>Payday matters to everyone. Behind each paycheck, someone checked the hours, figured the taxes and deductions, and made sure the money went out on time. That is payroll.</p>'
     '<p>This career mixes numbers, rules, and helping workers understand their pay. Explore what it feels like before deciding whether it interests you.</p>'
     '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
    ['What is a Payroll Clerk?', '<p>You make sure employees are paid correctly. You check hours and time sheets, enter pay changes, run payroll in software, and answer workers\' questions about their paychecks.</p>{{IMAGE0}}'
     '<ul><li>Check hours worked, time off, and overtime.</li><li>Enter new workers and pay changes into the payroll system.</li>'
     '<li>Figure pay, taxes, and deductions using payroll software.</li><li>Fix mistakes before paychecks go out.</li>'
     '<li>Prepare reports and match payroll to bank records.</li><li>Answer workers\' questions about their pay.</li></ul>'
     '<p><strong>The real picture:</strong> Payroll runs on firm deadlines. A mistake affects a real person\'s paycheck, so careful checking matters every time.</p>'],
    ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> The week follows the pay schedule.</p><ul>'
     '<li>Morning: Collect time sheets and check for missing hours.</li>'
     '<li>Later: Enter a new hire, a raise, and a change to someone\'s tax form.</li>'
     '<li>Midday: A worker stops by because their overtime looks wrong. Look it up and explain it.</li>'
     '<li>Afternoon: Run a payroll preview and check it line by line.</li>'
     '<li>Before leaving: List anything that must be fixed before payroll is final.</li></ul>'
     '<p>The days before payday are busy. The end of the year brings extra tax forms.</p>'],
    ['How You Learn the Job', '<p><strong>Many people come to payroll from other office work.</strong> Employers often look for bookkeeping, office, or human resources experience. Some ask for a college degree, so read the actual job ad.</p><ul>'
     '<li><strong>Build basic skills first:</strong> Spreadsheets, careful data entry, and basic math with percentages.</li>'
     '<li><strong>Start nearby:</strong> Bookkeeping, office clerk, or human resources assistant jobs can lead to payroll.</li>'
     '<li><strong>Learn the software:</strong> Employers use payroll systems such as ADP, Workday, or Kronos. Each employer trains its own system.</li>'
     '<li><strong>Optional certification:</strong> PayrollOrg offers the Fundamental Payroll Certification for people new to payroll. Its website lists no experience requirement. Check the current cost and requirements on the PayrollOrg website.</li>'
     '<li><strong>Optional education:</strong> Accounting, business, or human resources classes at a North Dakota college can help.</li></ul>'
     + FUNDING],
    ['Training and Employer Requirements', '<p>No state license is needed to do payroll. Requirements depend on the employer. Ask what you need to start.</p><ul>'
     '<li>Comfort with spreadsheets and numbers.</li><li>Experience with payroll or bookkeeping software, or willingness to learn it.</li>'
     '<li>A background check for many jobs.</li><li>Strict care with private pay and tax information.</li>'
     '<li>Willingness to keep learning as tax and wage rules change.</li></ul>'
     '<p><strong>Before you begin:</strong> Ask who checks your work at first and who you go to with a tax or rule question.</p>' + SUPPORT],
    ['Pay and Job Outlook', None],
    ['Where This Can Lead', '<ul><li><strong>Payroll specialist:</strong> Handle more complex payroll, such as several states or many workers.</li>'
     '<li><strong>Payroll manager:</strong> Lead payroll for a larger employer.</li>'
     '<li><strong>Human resources:</strong> Payroll knowledge is useful in benefits and human resources jobs.</li>'
     '<li><strong>Accounting:</strong> More education can lead to accounting work.</li></ul>'
     '<p>Payroll companies also hire people to run payroll for many smaller businesses.</p>'],
    ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Clear rules and a clear right answer.</li><li>Knowing that people count on your work.</li>'
     '<li>Pay that is higher than many entry-level office jobs.</li><li>Skills that connect to human resources and accounting.</li></ul>'
     '<p><strong>Things to ask about:</strong></p><ul><li>Firm deadlines every pay period.</li><li>Workers who are upset when a paycheck looks wrong.</li>'
     '<li>Rules that change and need to be learned.</li><li>Very few jobs with this exact title in North Dakota.</li></ul>'
     '<p>North Dakota has only about 300 payroll clerk jobs and about 30 openings a year. Payroll skills are still useful, because many bookkeepers, office managers, and human resources workers run payroll as part of their job.</p>'
     '<p><strong>A question for yourself:</strong> Do you like careful number work where getting it right helps people directly?</p>'],
]
c['pay'] = pay_section(c, 'North Dakota payroll clerk pay — May 2025:',
    'Hospitals, manufacturers, school districts, government offices, larger businesses, and payroll service companies.',
    'An office desk with a computer. Some jobs can be partly remote once you are trained.',
    'Ask about base pay, hours, benefits, paid time off, training, and help paying for a certification.')
C.append(c)

# ---------------------------------------------------------------- Medical Secretary
c = dict(
    name='Medical Secretary', slug='medical-secretary', area='healthcare', areaName='Healthcare', soc='43-6013.00',
    subtitle='Keeping a clinic\'s schedule, records, and front desk running',
    images=['medical-secretary-1.jpg', 'medical-secretary-2.jpg'],
    alts=['A medical secretary wearing a headset schedules appointments at a clinic front desk.',
          'A medical secretary scans insurance cards and paperwork in a clinic back office.'],
    wages=dict(p10=18.00, p25=18.96, p50=21.82, p75=24.14, p90=27.95, p50a=45390),
    proj=dict(y0=2024, y1=2034, **{'from': 970}, to=1030, pct=6, open=100),
    tags=['healthcare', 'clinic', 'front desk', 'scheduling', 'medical office', 'insurance', 'office'],
    facets=['20-to-30', 'steady', 'some-openings'],
    motivation=['I want to work in healthcare without giving hands-on patient care.', 'I like helping people and keeping things organized.',
                'I want an indoor job that uses a computer.'],
    readiness=['I can stay calm and kind with people who are sick or worried.', 'I would learn medical words and office software.',
               'I can answer the phone and schedule appointments carefully.', 'I can check names, dates, and insurance details.',
               'I would keep patient information private.', 'I can handle several requests at once.',
               'I can sit at a desk and use a computer for much of the day.', 'I would ask questions when I am not sure about a rule.'],
    future=[['a', 'Ask someone who works at a clinic front desk about the job.'],
            ['b', 'Look into a medical office certificate program.'],
            ['c', 'Compare medical office jobs at clinics and hospitals.']] + FUTURE_TAIL,
    nextSteps=['Ask a clinic or hospital worker what front office staff do in a day.',
               'Look at current medical secretary and medical receptionist job ads.',
               'Compare short certificate programs and associate degrees.',
               'Ask about training, pay, schedule, and support while learning.'],
    futureSteps={'a': ['Ask what a busy morning at the front desk looks like.', 'Ask how they handle upset or worried patients.',
                       'Notice whether healthcare office work sounds good to you.'],
                 'b': ['Compare medical office programs in North Dakota, including online options.',
                       'Ask about length, cost, and whether the program includes medical words and billing.',
                       'Ask whether graduates find local jobs.'],
                 'c': ['Compare a small clinic, a dental office, and a hospital department.',
                       'Ask which ones train beginners.', 'Compare pay, hours, and benefits.']},
    final=('Medical secretaries are often the first and last person a patient talks to. '
           'You can be part of healthcare without giving hands-on care. '
           'Being organized, kind, and careful with private information are the skills that matter most.'),
)
c['recs'] = recs_for('medical secretary', 'Talking with someone at a clinic front desk is a useful next step.')
c['sources'] = [['O*NET OnLine — occupation information', 'https://www.onetonline.org/link/summary/43-6013.00'],
                ['North Dakota pay — BLS May 2025, via O*NET', 'https://www.onetonline.org/link/localwages/43-6013.00?st=ND'],
                ['North Dakota outlook — Projections Central 2024–2034, via O*NET', 'https://www.onetonline.org/link/localtrends/43-6013.00?st=ND'],
                ['North Dakota schools and programs — via O*NET', 'https://www.onetonline.org/link/localtraining/43-6013.00?st=ND']]
c['sourceNote'] = 'Pay figures are for medical secretaries and administrative assistants in North Dakota.'
c['sections'] = [
    ['Welcome', '<p>A patient calls to make an appointment. Another walks in and needs to check in. A doctor needs a record sent to a specialist. The medical secretary helps keep all of it moving.</p>'
     '<p>This career is a way to work in healthcare from the office side. Explore what it feels like before deciding whether it interests you.</p>'
     '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
    ['What is a Medical Secretary?', '<p>You handle the office work of a clinic, hospital department, or dental office. You schedule appointments, check patients in, handle insurance information, and keep medical records organized and private.</p>{{IMAGE0}}'
     '<ul><li>Answer phones and schedule appointments, tests, and procedures.</li><li>Greet and check in patients.</li>'
     '<li>Collect and enter insurance information.</li><li>Send and receive medical records and test results.</li>'
     '<li>Help patients fill out forms.</li><li>Keep patient information private and secure.</li></ul>'
     '<p><strong>The real picture:</strong> You will see people who are sick, hurting, or worried. A calm, kind voice is part of the job.</p>'],
    ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Clinics are busiest when the doors open.</p><ul>'
     '<li>Morning: Check in a line of patients and scan their insurance cards.</li>'
     '<li>Later: Answer calls and fit a sick patient into a full schedule.</li>'
     '<li>Midday: Send records to a specialist and file test results.</li>'
     '<li>Afternoon: Call patients to confirm tomorrow\'s appointments.</li>'
     '<li>Before leaving: Check that tomorrow\'s schedule and paperwork are ready.</li></ul>'
     '<p>Some clinics have early, evening, or weekend hours.</p>'],
    ['How You Learn the Job', '<p><strong>There is more than one way in.</strong> About half the people in this job say a high school diploma or GED is what new workers need. Others say an associate degree or a college certificate. Read the actual job ad.</p><ul>'
     '<li><strong>Build basic skills first:</strong> Typing, email, scheduling, and clear phone manners.</li>'
     '<li><strong>Learn medical words:</strong> A medical terminology class helps you understand what doctors and nurses write.</li>'
     '<li><strong>Optional education:</strong> North Dakota schools with medical office programs include Turtle Mountain College in Belcourt, Dakota College at Bottineau, Bismarck State College, Williston State College, and Rasmussen University in Fargo.</li>'
     '<li><strong>On-the-job training:</strong> Each clinic trains staff on its own scheduling and records system.</li></ul>'
     + FUNDING],
    ['Training and Employer Requirements', '<p>No state license is needed for this job. Employers set their own requirements. Ask what you need to start.</p><ul>'
     '<li>Comfort with a computer, phone, and scheduling software.</li><li>Training on patient privacy rules, which employers provide.</li>'
     '<li>A background check, which many healthcare employers require.</li><li>Some employers ask for proof of certain vaccinations.</li>'
     '<li>Optional medical office certifications; ask whether an employer wants one before you pay for it.</li></ul>'
     '<p><strong>Before you begin:</strong> Ask how long training lasts and who helps with insurance and billing questions.</p>' + SUPPORT],
    ['Pay and Job Outlook', None],
    ['Where This Can Lead', '<ul><li><strong>Lead front office worker:</strong> Train new staff and handle harder scheduling problems.</li>'
     '<li><strong>Medical records or billing:</strong> More training can lead to medical records specialist or billing jobs.</li>'
     '<li><strong>Office manager:</strong> Run a clinic\'s front office as experience grows.</li>'
     '<li><strong>Patient care:</strong> Some people decide they want hands-on care and train as a medical assistant or nurse.</li></ul>'
     '<p>Ask your employer whether they help pay for healthcare classes.</p>'],
    ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Being part of healthcare without hands-on care.</li><li>Helping people when they need it.</li>'
     '<li>Clinics and hospitals in many North Dakota towns.</li><li>A field that is expected to grow.</li></ul>'
     '<p><strong>Things to ask about:</strong></p><ul><li>Busy phones and several requests at once.</li><li>Patients who are scared, in pain, or frustrated.</li>'
     '<li>Long stretches of sitting and computer work.</li><li>Insurance rules that take time to learn.</li></ul>'
     '<p>North Dakota expects about 6% growth over ten years, with about 100 openings a year.</p>'
     '<p><strong>A question for yourself:</strong> Do you like staying organized and kind when things get busy?</p>'],
]
c['pay'] = pay_section(c, 'North Dakota medical secretary pay — May 2025:',
    'Clinics, hospitals, dental offices, nursing homes, and other healthcare offices.',
    'A front desk or back office with a computer and phone, in a clean indoor setting.',
    'Ask about base pay, hours, weekend or evening shifts, benefits, paid time off, training, and help paying for classes.')
C.append(c)

# ---------------------------------------------------------------- Pharmacy Technician
c = dict(
    name='Pharmacy Technician', slug='pharmacy-technician', area='healthcare', areaName='Healthcare', soc='29-2052.00',
    subtitle='Helping pharmacists get the right medicine to the right person',
    images=['pharmacy-technician-1.jpg', 'pharmacy-technician-2.jpg'],
    alts=['A pharmacy technician counts tablets on a counting tray behind a pharmacy counter.',
          'A pharmacy technician stocks medication bins in a hospital pharmacy.'],
    wages=dict(p10=18.45, p25=19.89, p50=22.86, p75=26.08, p90=30.70, p50a=47560),
    proj=dict(y0=2022, y1=2032, **{'from': 920}, to=1030, pct=12, open=100,
              note='These North Dakota projections cover 2022–2032, the newest North Dakota figures shown for this job when checked in October 2026.'),
    tags=['healthcare', 'pharmacy', 'medicine', 'retail', 'hospital', 'certification'],
    facets=['20-to-30', 'growing-fast', 'some-openings'],
    growthLabel='+12% projected ND growth · 2022–2032',
    motivation=['I want to work in healthcare.', 'I like careful, exact work.',
                'I want a career I can train for in a year or two.'],
    readiness=['I can count and measure carefully and check my work.', 'I would learn the names of many medicines.',
               'I can follow strict rules exactly.', 'I would keep patient information private.',
               'I can stand for much of the day, or ask about it.', 'I can stay polite with customers who are sick or in a hurry.',
               'I would study for a national certification exam.', 'I would ask a pharmacist when I am not sure.'],
    future=[['a', 'Ask a pharmacy technician what the work is like.'],
            ['b', 'Look into an accredited pharmacy technician program.'],
            ['c', 'Compare retail and hospital pharmacy jobs.']] + FUTURE_TAIL,
    nextSteps=['Ask a pharmacist or pharmacy technician what a normal day looks like.',
               'Read the North Dakota Board of Pharmacy technician requirements.',
               'Compare accredited school programs and employer training programs.',
               'Ask about training, pay, schedule, and support while learning.'],
    futureSteps={'a': ['Ask at a local pharmacy if a technician can answer a few questions.',
                       'Ask how they learned and how long it took.', 'Notice whether careful, fast-paced work sounds good to you.'],
                 'b': ['Look at the program at North Dakota State College of Science in Wahpeton.',
                       'Ask whether a local pharmacy offers an accredited on-the-job program.',
                       'Ask about cost, length, and help preparing for the certification exam.'],
                 'c': ['Compare a drugstore, a grocery store pharmacy, and a hospital pharmacy.',
                       'Compare hours, weekends, and how much customer contact each has.',
                       'Ask which ones pay for training.']},
    final=('Pharmacy technicians help pharmacists make sure each person gets the right medicine. '
           'North Dakota expects these jobs to grow, and the training is shorter than many healthcare careers. '
           'Care, accuracy, and following the rules every time matter most.'),
)
c['recs'] = recs_for('pharmacy technician', 'Asking a pharmacy technician about their work is a useful next step.')
c['sources'] = [['O*NET OnLine — occupation information', 'https://www.onetonline.org/link/summary/29-2052.00'],
                ['North Dakota pay — BLS May 2025, via O*NET', 'https://www.onetonline.org/link/localwages/29-2052.00?st=ND'],
                ['North Dakota outlook — via O*NET', 'https://www.onetonline.org/link/localtrends/29-2052.00?st=ND'],
                ['North Dakota schools and programs — via O*NET', 'https://www.onetonline.org/link/localtraining/29-2052.00?st=ND'],
                ['North Dakota State Board of Pharmacy', 'https://www.nodakpharmacy.com/']]
c['sourceNote'] = 'Registration rules can change. Confirm the current requirements with the North Dakota State Board of Pharmacy before you enroll.'
c['sections'] = [
    ['Welcome', '<p>A prescription comes in. Someone has to check it, count or measure the medicine, label it, and have it ready for the pharmacist to check. Pharmacy technicians do much of that work.</p>'
     '<p>This career is a way into healthcare that needs careful, exact work. Explore what it feels like before deciding whether it interests you.</p>'
     '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
    ['What is a Pharmacy Technician?', '<p>You help a pharmacist prepare and hand out medicine. You enter prescriptions into the computer, count or measure medicine, keep the shelves stocked, and help customers. A pharmacist checks the work and answers medicine questions.</p>{{IMAGE0}}'
     '<ul><li>Check prescriptions and enter them into the computer.</li><li>Count, measure, and label medicines.</li>'
     '<li>Keep medicines stored safely and stocked.</li><li>Check deliveries and pull medicine that has expired.</li>'
     '<li>Answer phones and help customers at the counter.</li><li>Send medicine questions to the pharmacist.</li></ul>'
     '<p><strong>The real picture:</strong> The work is exact. A small mistake with medicine matters, so every step is checked.</p>'],
    ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Retail and hospital pharmacies run differently.</p><ul>'
     '<li>Morning: Check in a delivery and put medicine in the right places.</li>'
     '<li>Later: Enter new prescriptions and count tablets for the pharmacist to check.</li>'
     '<li>Midday: Help a line of customers pick up prescriptions.</li>'
     '<li>Afternoon: Call an insurance company about a claim, then restock shelves.</li>'
     '<li>Before leaving: Clean the counting area and finish the day\'s records.</li></ul>'
     '<p>Many pharmacies are open evenings and weekends. Hospital pharmacies may be open around the clock.</p>'],
    ['How You Learn the Job', '<p><strong>North Dakota requires training and registration for pharmacy technicians.</strong> The North Dakota State Board of Pharmacy says technicians must complete a training program accredited by the American Society of Health-System Pharmacists (ASHP), either at a school or through an accredited on-the-job program, and pass a national certification exam. Check the board\'s current rules before you enroll.</p><ul>'
     '<li><strong>School programs:</strong> North Dakota State College of Science in Wahpeton offers pharmacy technician training. Rasmussen University in Fargo offers an associate degree.</li>'
     '<li><strong>Employer programs:</strong> Some pharmacies offer accredited on-the-job training. Ask whether a program is accredited before you start.</li>'
     '<li><strong>Certification:</strong> Plan to study for and pass a national pharmacy technician certification exam.</li>'
     '<li><strong>While you train:</strong> Ask the board whether you can register as a technician in training while you finish your program.</li></ul>'
     + FUNDING],
    ['Training and Employer Requirements', '<p>Pharmacy technicians in North Dakota register with the State Board of Pharmacy. Ask the board and the employer what you need.</p><ul>'
     '<li>An accredited training program, at a school or through an employer.</li><li>National certification.</li>'
     '<li>Registration with the North Dakota State Board of Pharmacy, renewed each year.</li>'
     '<li>Continuing education to keep your registration.</li><li>A background check, which employers usually require.</li></ul>'
     '<p><strong>Before you begin:</strong> Ask whether the employer pays for training and the exam, and how long you have to finish.</p>' + SUPPORT],
    ['Pay and Job Outlook', None],
    ['Where This Can Lead', '<ul><li><strong>Lead technician:</strong> Train new technicians and manage stock.</li>'
     '<li><strong>Hospital pharmacy:</strong> Prepare medicine for hospital patients, sometimes with extra training.</li>'
     '<li><strong>Specialty work:</strong> Some technicians move into insurance billing, inventory, or pharmacy software.</li>'
     '<li><strong>Pharmacist:</strong> Becoming a pharmacist takes a doctor of pharmacy degree, which is many more years of school.</li></ul>'
     '<p>Ask your employer whether they help pay for more training.</p>'],
    ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Being part of healthcare.</li><li>Clear steps and exact work.</li>'
     '<li>Shorter training than many healthcare careers.</li><li>Pharmacies in many North Dakota towns.</li></ul>'
     '<p><strong>Things to ask about:</strong></p><ul><li>Standing for most of the shift.</li><li>Busy rushes and customers who are sick or in a hurry.</li>'
     '<li>Evening, weekend, or holiday hours.</li><li>Training, certification, and yearly registration to keep up.</li></ul>'
     '<p>North Dakota expects about 12% growth, with about 100 openings a year.</p>'
     '<p><strong>A question for yourself:</strong> Do you like exact, careful work that helps people stay healthy?</p>'],
]
c['pay'] = pay_section(c, 'North Dakota pharmacy technician pay — May 2025:',
    'Drugstores, grocery store pharmacies, hospitals, clinics, and long-term care pharmacies.',
    'A pharmacy counter and work area. About 3 in 4 pharmacy technicians say they stand for most of the day.',
    'Ask about base pay, shifts, weekends, benefits, paid time off, and whether the employer pays for training and certification.')
C.append(c)

# ---------------------------------------------------------------- Teacher Assistant
c = dict(
    name='Teacher Assistant', slug='teacher-assistant', area='education', areaName='Education', soc='25-9042.00',
    subtitle='Helping students learn, one small group or one child at a time',
    images=['teacher-assistant-1.jpg', 'teacher-assistant-2.jpg'],
    alts=['A teacher assistant kneels beside a student\'s desk to help with a worksheet.',
          'A teacher assistant leads a small reading group at a round table.'],
    wages=dict(p10a=29130, p25a=35990, p50a=38240, p75a=44570, p90a=46260),
    payBasis='annual-contract',
    proj=dict(y0=2024, y1=2034, **{'from': 5260}, to=5600, pct=7, open=700),
    tags=['education', 'school', 'paraprofessional', 'para', 'children', 'special education', 'classroom'],
    facets=['under-20', 'steady', 'many-openings'],
    motivation=['I like helping children or teens learn.', 'I want to work in a school.',
                'I want to see whether teaching might be right for me.'],
    readiness=['I can be patient when a student needs to hear something again.', 'I can follow a teacher\'s plan.',
               'I can help keep a group of students safe and on task.', 'I would learn ways to help students with different needs.',
               'I would keep student information private.', 'I can stay calm when a student is upset.',
               'I can be on my feet and move around the room, or ask about it.', 'I would ask the teacher when I am not sure what to do.'],
    future=[['a', 'Ask a teacher assistant what the job is really like.'],
            ['b', 'Find out what my school district requires.'],
            ['c', 'Compare general classroom and special education assistant jobs.']] + FUTURE_TAIL,
    nextSteps=['Ask a teacher or teacher assistant what a normal school day looks like.',
               'Look at current paraprofessional job ads from nearby school districts.',
               'Read the North Dakota Department of Public Instruction paraprofessional page.',
               'Ask about training, pay, schedule, and support while learning.'],
    futureSteps={'a': ['Ask what a teacher assistant does from the first bell to the last.', 'Ask what is hardest and what is best about the job.',
                       'Notice whether working with students all day sounds good to you.'],
                 'b': ['Ask the district which paraprofessional certificate the job needs.',
                       'Find out whether you meet the Title I requirements or need a skills test or college credits.',
                       'Ask whether the district provides required training.'],
                 'c': ['Ask how special education assistant jobs differ from general classroom jobs.',
                       'Ask about the training required for special education assistants.',
                       'Compare hours, pay, and age groups.']},
    final=('Teacher assistants give students the extra help that lets them learn. '
           'Many people start here, and some go on to become teachers. '
           'Patience, kindness, and following the teacher\'s lead matter more than knowing every subject.'),
)
c['recs'] = recs_for('teacher assistant', 'Asking a teacher assistant about their day is a useful next step.')
c['sources'] = [['O*NET OnLine — occupation information', 'https://www.onetonline.org/link/summary/25-9042.00'],
                ['North Dakota pay — BLS May 2025, via O*NET', 'https://www.onetonline.org/link/localwages/25-9042.00?st=ND'],
                ['North Dakota outlook — Projections Central 2024–2034, via O*NET', 'https://www.onetonline.org/link/localtrends/25-9042.00?st=ND'],
                ['North Dakota schools and programs — via O*NET', 'https://www.onetonline.org/link/localtraining/25-9042.00?st=ND'],
                ['ND Department of Public Instruction — paraprofessional certificates', 'https://www.nd.gov/dpi/educators/credentials-and-certificates/paraprofessional-certificates']]
c['sourceNote'] = ('Pay figures are yearly totals for teaching assistants, except college, and include special education assistants. '
                   'Many of these jobs follow the school year, so yearly pay reflects fewer working months than a full-year job.')
c['sections'] = [
    ['Welcome', '<p>A student is stuck on a math problem. A small group needs someone to read with them. A child needs a calm adult nearby. Teacher assistants, often called paraprofessionals or paras, help teachers give students that extra attention.</p>'
     '<p>This career means working closely with students all day. Explore what it feels like before deciding whether it interests you.</p>'
     '<p><strong>Go at your pace.</strong> The short questions at the end are for reflection. There are no right or wrong answers.</p>'],
    ['What is a Teacher Assistant?', '<p>You help a teacher in the classroom. You work with students one at a time or in small groups, help keep students safe and on task, and support the teacher\'s plan. Some assistants work with students who have disabilities.</p>{{IMAGE0}}'
     '<ul><li>Help students with lessons one at a time or in small groups.</li><li>Read aloud and practice skills the teacher has taught.</li>'
     '<li>Watch students in classrooms, hallways, lunchrooms, and playgrounds.</li><li>Help students follow school rules and get along.</li>'
     '<li>Get materials ready and help clean up.</li><li>Talk with the teacher about how students are doing.</li></ul>'
     '<p><strong>The real picture:</strong> You are with students almost all day. The teacher plans the lessons, and you help carry them out.</p>'],
    ['A Day in the Life', '{{IMAGE1}}<p><strong>One possible day:</strong> Your day follows the school schedule.</p><ul>'
     '<li>Morning: Greet students and help them get settled.</li>'
     '<li>Later: Lead a small reading group while the teacher works with others.</li>'
     '<li>Midday: Watch students at lunch and recess.</li>'
     '<li>Afternoon: Sit beside a student who needs extra help with math.</li>'
     '<li>Before leaving: Tell the teacher what went well and what a student found hard.</li></ul>'
     '<p>Some days are calm. Others bring upset students or sudden changes. Staying patient is part of the job.</p>'],
    ['How You Learn the Job', '<p><strong>There is more than one way in.</strong> School districts set their own hiring rules, and some jobs have state requirements. Read the actual job ad.</p><ul>'
     '<li><strong>Title I paraprofessionals:</strong> For jobs paid with Title I funds, North Dakota requires a high school diploma or equivalent plus one of these: two years of college (48 semester hours), an associate degree or higher, or passing a North Dakota-approved test of reading, math, and writing skills.</li>'
     '<li><strong>Special education paraprofessionals:</strong> North Dakota requires 20 hours of training within the first year on the job. Valley City State, Minot State, and Mayville State universities offer courses that meet this certificate.</li>'
     '<li><strong>Optional education:</strong> Dakota College at Bottineau and Sitting Bull College in Fort Yates offer teacher assistant associate degrees.</li>'
     '<li><strong>On-the-job training:</strong> Districts train assistants on school rules, safety, and how to help students.</li></ul>'
     + FUNDING],
    ['Training and Employer Requirements', '<p>Paraprofessional certificates are handled by the North Dakota Department of Public Instruction through NDTeach. Ask the school district which one the job needs.</p><ul>'
     '<li>A Title I or special education paraprofessional certificate, depending on the job.</li><li>A background check, which schools require.</li>'
     '<li>Training on student privacy and safety.</li><li>Some districts ask for first aid or CPR.</li>'
     '<li>A teaching license counts in place of the Title I paraprofessional certificate.</li></ul>'
     '<p><strong>Before you begin:</strong> Ask what training the district provides and who you go to with questions about a student.</p>' + SUPPORT],
    ['Pay and Job Outlook', None],
    ['Where This Can Lead', '<ul><li><strong>Special education assistant:</strong> Work closely with students who have disabilities.</li>'
     '<li><strong>Special education technician:</strong> North Dakota has a technician credential for experienced special education paraprofessionals.</li>'
     '<li><strong>Teacher:</strong> Some assistants earn a bachelor\'s degree and a teaching license. Ask about programs for working paraprofessionals.</li>'
     '<li><strong>A related direction:</strong> Childcare, after-school programs, or youth work.</li></ul>'
     '<p>Working in a school is a good way to find out whether teaching is right for you.</p>'],
    ['The Real Talk', '<p><strong>Things you might like:</strong></p><ul><li>Helping students learn and grow.</li><li>A schedule that follows the school year in many jobs.</li>'
     '<li>Schools in almost every North Dakota town.</li><li>A way to try out working in education.</li></ul>'
     '<p><strong>Things to ask about:</strong></p><ul><li>Pay that is lower than many full-year jobs.</li><li>Summers that may be unpaid.</li>'
     '<li>Students who are upset or have big needs.</li><li>Being on your feet and moving around all day.</li></ul>'
     '<p>North Dakota expects about 7% growth over ten years, with about 700 openings a year.</p>'
     '<p><strong>A question for yourself:</strong> Do you have the patience to help a student keep trying until they get it?</p>'],
]
c['pay'] = pay_section(c, 'North Dakota teacher assistant pay — May 2025 (yearly):',
    'Public and private schools, preschools, and special education programs across the state.',
    'Classrooms, hallways, lunchrooms, and playgrounds. You work close to students and move around much of the day.',
    'Ask about hourly or yearly pay, hours per day, whether summers are paid, benefits, and paid training.')
C.append(c)
