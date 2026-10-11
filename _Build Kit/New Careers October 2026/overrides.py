"""Second-review changes (Chadwick's review, Oct 10 2026): activity-style items and qualified claims."""
# Part 2 items: every item is an activity. The question asks whether it sounds comfortable to try.
READINESS = {
 'administrative-assistant': ['Keeping track of several small tasks at once', 'Using email, a calendar, and word processing programs',
   'Answering the phone and taking a clear message', 'Checking details like names, dates, and spelling',
   'Staying polite when someone is upset or in a hurry', 'Keeping private information private',
   'Working at a desk and computer for much of the day', 'Asking questions when you are not sure how something is done'],
 'office-clerk': ['Following steps in the right order', 'Checking numbers and names carefully', 'Entering information into a computer system',
   'Switching tasks when someone needs help', 'Keeping private records private', 'Answering a question at a front counter or on the phone',
   'Doing the same kind of task for a long stretch', 'Asking questions when you are not sure where something goes'],
 'bank-teller': ['Counting money carefully and checking your work', 'Helping customers face to face all day', 'Learning a new computer system',
   'Following strict rules exactly', 'Keeping customers’ information private', 'Staying calm when a customer is upset',
   'Working at a counter for long stretches', 'Asking questions when you are not sure about a rule'],
 'bookkeeping-clerk': ['Checking numbers carefully and finding small mistakes', 'Learning bookkeeping software', 'Using a spreadsheet',
   'Working on your own for long stretches', 'Keeping financial information private', 'Meeting a deadline at the end of the month',
   'Learning basic accounting words like debit and credit', 'Asking questions when numbers do not match'],
 'payroll-clerk': ['Checking hours and pay carefully and catching mistakes', 'Learning payroll software', 'Using a spreadsheet',
   'Meeting a firm deadline every pay period', 'Keeping everyone’s pay information private', 'Explaining a paycheck to a worker who has questions',
   'Learning the rules for taxes and deductions', 'Asking questions when something does not add up'],
 'medical-secretary': ['Talking with people who are sick or worried', 'Learning medical words and office software', 'Answering the phone and scheduling appointments',
   'Checking names, dates, and insurance details', 'Keeping patient information private', 'Handling several requests at once',
   'Working at a desk and computer for much of the day', 'Asking questions when you are not sure about a rule'],
 'pharmacy-technician': ['Counting and measuring carefully and checking your work', 'Learning the names of many medicines', 'Following strict rules exactly',
   'Keeping patient information private', 'Working on your feet for much of a shift', 'Helping customers who are sick or in a hurry',
   'Studying for a national certification exam', 'Asking a pharmacist when you are not sure'],
 'teacher-assistant': ['Explaining something again when a student needs it', 'Following a teacher’s plan', 'Helping keep a group of students safe and on task',
   'Learning ways to help students with different needs', 'Keeping student information private', 'Staying calm when a student is upset',
   'Moving around the room and staying on your feet', 'Asking the teacher when you are not sure what to do'],
}
# exact text fixes inside section HTML: (slug, old, new)
FIXES = [
 ('administrative-assistant', 'Across the country, the number of these jobs is expected to shrink as offices use more software. In North Dakota, the projection is close to flat',
  'Across the country, the number of these jobs is projected to shrink. In North Dakota, the projection is close to flat'),
 ('office-clerk', 'North Dakota expects the number of office clerk jobs to shrink a little as more records go digital. There are still',
  'North Dakota projects a small drop in office clerk jobs. There are still'),
 ('office-clerk', 'Free classes are often offered at libraries and job centers.', 'Free classes may be available at libraries and job centers.'),
 ('office-clerk', '<p>No state license is needed for this job.', '<p>No state license is needed for general office clerk work. Some specialized clerk jobs have their own rules.'),
 ('administrative-assistant', '<p>No state license is needed for this job.', '<p>No state license is needed for general administrative assistant work. Some specialized roles have their own rules.'),
 ('bank-teller', '<li>Fewer teller jobs as more banking moves online.</li>', '<li>Fewer teller jobs over time.</li>'),
 ('bank-teller', '<li>A background check, which banks usually require.</li>', '<li>A background check; ask each employer what it checks.</li>'),
 ('bookkeeping-clerk', '<li>Software doing more of the routine entry work.</li>', '<li>Changes in software and how the work is done.</li>'),
]
PART2_INTRO = '<p>For each activity, choose whether it sounds comfortable to try. You do not need these skills already, and you can ask for support.</p>'
