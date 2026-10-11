NEW CAREERS — October 10, 2026

Eight careers your clients ask about that the site did not have yet:
  Jobs You Can Start Now (new "Offices and Banks" group): Administrative Assistant,
      Office Clerk, Bank Teller
  Business and Finance (Accounting and Taxes): Bookkeeping Clerk, Payroll Clerk
  Healthcare (Support Services): Medical Secretary, Pharmacy Technician
  Education (Classroom Teachers): Teacher Assistant

None of them is on the July 2026 ND In-Demand list, so none gets the badge.
The area pages that said "Explore 30 In-Demand Healthcare Careers" now say
"Explore 32 Healthcare Careers" (same for Education and Business and Finance),
because the areas now include careers that are not on the list.

HOW TO BUILD (once all 16 images are approved)
  1. Size each image:   python prepare_images.py <Chadwick's file> images/<name>.jpg
     (1200 x 800, under 600 KB; needs Pillow)
  2. Build:             python "_Build Kit/New Careers October 2026/build.py"
     The build refuses to run while any image is missing. It uses the report
     wording and accessibility fixes in "_Build Kit/Soften Reports October 2026".
  3. Test:              node "_Build Kit/tests/check-new-careers.cjs"
                        node "_Build Kit/tests/check-area12.cjs"
                        node "_Build Kit/tests/check-rural-additions.cjs"
                        node "_Build Kit/tests/check-reading-controls.cjs"
  Running the build again is safe. Existing careers are not changed.

WHERE THE WORDS LIVE
  careers_a.py and careers_b.py hold the page text. overrides.py holds the
  activity questions and the wording fixes from Chadwick's October 10 review. content_common.py holds the
  shared paragraphs and builds the Pay section from the numbers, so each figure is
  typed only once. After editing, run:  python make_careers.py careers.json

WHERE THE FACTS CAME FROM (checked October 10, 2026)
  Pay: BLS OEWS May 2025 for North Dakota, through O*NET OnLine localwages.
  Outlook: Projections Central 2024–2034 through O*NET localtrends.
    Pharmacy Technician: O*NET showed only 2022–2032 for ND; labelled on the page.
  Schools: O*NET localtraining (IPEDS).
  Pharmacy technician rules: ND State Board of Pharmacy.
  Paraprofessional rules: ND Department of Public Instruction.
  Payroll certification: PayrollOrg.
  Teacher Assistant pay is a yearly figure for the broader "teaching assistants,
  except postsecondary" group, which includes special education assistants.

IMAGES — Career Factory image standards
  Two per career, "What Is It?" and "A Day in the Life". Photorealistic, 3:2,
  task-focused, no readable text or logos, a real mix of people across the set.
  The 16 prompts are in the October 10 chat. Approved so far:
  office-clerk-1.jpg, office-clerk-2.jpg

TESTS AFTER BUILD
  The files in "tests after build" go in "_Build Kit/tests" after the build runs.
  check-area12 and check-rural-additions are the same tests with the new counts
  (26 jobs-you-can-start-now careers, 203 total). Copying them earlier would make
  them fail, because the site still has 195 careers until the build runs.
