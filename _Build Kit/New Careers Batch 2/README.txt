NEW CAREERS — BATCH 2 — October 11, 2026

Sixteen careers, chosen by Shari: construction & production, and human services & corrections.

  Skilled Trades
    Construction Trades: Construction Laborer, Painter, Roofer, Sheet Metal Worker
    Industrial & Electrical Repair: Maintenance and Repair Worker
  Jobs You Can Start Now
    Warehouse, Factory and Driving: Forklift Operator
    Food and Restaurants: Butcher and Meat Cutter
    Care, Safety and Investigation: Recreation Worker
  Management (Plants, Projects and Science): Production Supervisor
  Social Services and Public Safety
    Public Safety: Correctional Officer, 911 Dispatcher
    Helping People and Families: Substance Abuse Counselor, Social and Human Service
      Assistant, Community Health Worker
  Healthcare (Therapy & Rehabilitation): Psychiatric Technician
  Education (new group "Libraries and Learning Support"): Library Technician

None is marked as on the ND In-Demand list. Skilled Trades, Management, and Social
Services area pages now say "Explore N ... Careers" instead of "Explore N In-Demand
... Careers", because those areas now include careers not on the list.

HOW TO BUILD
  1. Size each image:  python prepare_images.py <Chadwick's file> images/<name>.jpg
  2. Assemble text:    python make_careers.py careers.json   (only after editing careers_c.py / careers_d.py)
  3. Build:            python "_Build Kit/New Careers Batch 2/build.py"
  4. Test:             every file in "_Build Kit/tests", plus
                       "_Build Kit/Soften Reports October 2026/check-no-verdicts.cjs" and api/test.mjs
  Running the build again is safe; it replaces these 16 careers and leaves others alone.
  The tests now read the career count from search-index.json, so adding careers does
  not break them.

WHERE THE WORDS LIVE
  careers_c.py — construction and production; careers_d.py — human services and
  public safety. Each career's activity questions ("readiness") are in its entry.
  content_common.py builds the Pay section from the numbers so each figure is typed once.

WHERE THE FACTS CAME FROM (checked October 11, 2026)
  Pay: BLS May 2025 for North Dakota, via O*NET OnLine localwages.
  Outlook: Projections Central 2024–2034, via O*NET localtrends.
  Schools: O*NET localtraining (IPEDS).
  Notes:
  - Substance Abuse Counselor uses O*NET 21-1011.00. Its ND pay and outlook are for the
    broader group "Substance Abuse, Behavioral Disorder, and Mental Health Counselors".
    License steps: ND Board of Addiction Counseling Examiners (960-hour clinical training,
    board-approved coursework and exam). The board's site does not state a degree level;
    the page tells readers to confirm with the board.
  - Butcher and Meat Cutter uses 51-3021.00 because the meat trimmer code
    (51-3022.00) had incomplete ND data.
  - 911 Dispatcher outlook is for "Police, Fire, and Ambulance Dispatchers"; ND rules
    from NDCC 57-40.6-10.
  - Community Health Worker certification: ND HHS (began October 2025).
  - Roofer contractor rules: NDCC 43-07 and 26.1-39.2. Forklift training: OSHA 1910.178.
  - Correctional Officer: ND DOCR careers page; county jail training NDCC 12-44.1-04.
  - No ND license was found for psychiatric technicians, human service assistants,
    recreation workers, library technicians, or butchers; pages say "we did not find"
    rather than claiming none exists.

IMAGES
  32 photos by Chadwick, prompts in Career-Factory-Batch-2-Image-Prompts.txt.
  Chadwick replaced community-health-worker-2.jpg (plain earrings) and
  production-supervisor-2.jpg (whiteboard shows color blocks) on October 11.
  To swap: size the new file into images/ with the same name and run build.py again.
