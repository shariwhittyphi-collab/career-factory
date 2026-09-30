# North Dakota In-Demand Career Assessments

Interactive career assessments for every occupation on the North Dakota
In-Demand Occupations list. **171 careers across 11 areas.**

Built by Shari Whitmire through human-led, AI-assisted design and development
with Claude and ChatGPT. Shari directed requirements, career-assessment subject
matter, accessibility priorities, testing, and quality control.

 Each assessment is a self-contained HTML page: no
server or assessment accounts. Core assessment pages work locally; external
source links require internet, and read-aloud voice availability depends on the browser.
You can email one, put it on a flash drive, or host the whole set as a website.

---

## Who this is for

Someone deciding whether a career is right for them — often a person working
with a career counselor, often someone for whom a wrong training decision is
expensive in money and time they do not have.

The writing aims for roughly a 6th-grade reading level, reads aloud on
demand, resizes its own text, and has a dark mode. It is honest about what is
hard, not just what is good. The goal is a person deciding well, not a person
being sold a career.

---

## What's here

| Area | Careers |
|---|---|
| Skilled Trades | 31 |
| Healthcare | 30 |
| Business and Finance | 23 |
| Tech | 18 |
| Architecture and Engineering | 16 |
| Education | 15 |
| Management | 14 |
| Social Services | 8 |
| Science | 7 |
| Transportation | 5 |
| Arts, Legal and Sales | 4 |
| **Total** | **171** |

### Two formats, same content

**[Career Assessments Web/](Career%20Assessments%20Web/index.html)** — a website. A landing page links 11 area pages,
each listing its careers, one HTML file per career. Open `index.html` to start.
This is the format to host or to browse locally.

**Career Hubs (`*_Career_Assessments.html`)** — one self-contained file per
area, with every assessment for that area embedded inside it. One file to
email or hand over. Larger (2–20 MB each).

Both are generated from the same sources. Never edit one and not the other —
rebuild both. See `_Build Kit`.

---

## What one assessment contains

Eleven sections: what the job is, what a day looks like, how you train for it
in North Dakota, licensing or certification, pay, where the career leads,
the honest downsides, and three sets of questions (motivation, readiness,
future plans). Then a personalised report with scores, an interpretation, and
next steps — which adapt to the answers given, including pointing toward
shorter training routes when someone says a long program is not for them.

Below that sits **Sources & Learn More**: where every number came from, with
links to the actual pages, plus a North Dakota school lookup for that specific
occupation.

---

## Where the data comes from

All wage and outlook figures were taken in **September 2026** from
[O*NET OnLine](https://www.onetonline.org/), which reports:

- **Pay** — U.S. Bureau of Labor Statistics, Occupational Employment and Wage
  Statistics survey, **May 2025**, North Dakota figures.
- **Outlook** — Projections Central long-term state projections, **2024–2034**.
- **Schools** — U.S. Department of Labor training finder, built on federal
  college data (IPEDS), filtered to North Dakota.

Every career is keyed to its O*NET-SOC occupation code. Those codes are in
`careers_soc.json` in the Build Kit, and all 171 were checked against O*NET
rather than assumed.

These figures go stale. When BLS publishes a new wage year, the numbers on
every page need refreshing — the Sources block links to the live pages, so a
reader always has a route to current data even if the page itself is behind.

---

## Ground rules

These are not style preferences. Breaking one of them makes a page wrong for
the people it is for.

**Funding.** Financial aid, scholarships, grants and employer help come
**first** — always. Vocational Rehabilitation is not named on any page at all;
the pages say "career counselor". WIOA may be named, but never as the first
place to look. **No page states eligibility rules for any program**, because
eligibility depends on the individual and a page cannot know. Pages tell
people to ask before they enrol, not after.

**Honesty about the gate.** If a career needs four years and calculus, the
page says so plainly, and says what the shorter door is if there is one. No
career is oversold.

**Pictures.** Every career carries at least two embedded images. People shown
are fictional adults doing ordinary work in ordinary work clothes, with a
genuine mix of backgrounds — including Native American, reflecting the
students these are built for. No regalia, no costume, no cultural signalling.
No text, letters, numbers or logos inside any generated image.

**Keep the information.** Content does not get cut to make a page shorter.

**bls.gov is blocked** in the build environment. Do not fetch it and do not
work around the block — use O*NET, which reports the same BLS data.

---

## Decisions worth knowing before you change something

Written down because the reasoning is easy to lose and expensive to rediscover.

**Three different section-navigation schemes exist across the templates.** The
newer pages use `section1`…`section11` with a `show(id)` function; the older
healthcare pages use named section ids; two (Phlebotomy, Radiographic
Technology) use a numeric `showSection(n)` with a `totalSections` counter.
Anything that adds or renumbers a section has to handle all three. This is why
**Sources & Learn More is a standing block at the bottom of the page, not a
twelfth numbered section** — it looks like a section and behaves like one, but
no navigation counter was touched.

**Printing is deliberately two-layered.** Once results are generated, printing
prints the report alone. Before results, printing prints the page being read —
not a blank sheet. Inside a hub the assessment lives in an iframe, so the hub
shell measures the report at printed-page width and expands the frame, or the
report is silently clipped to one page. All of this lives in `printfix2.py`
(pages) and `hubprintfix.py` (hub shells). Both are idempotent.

**Every build pass is idempotent and must stay that way.** Pages get rebuilt
and re-passed constantly; a pass that doubles its own output on a second run
will quietly corrupt 171 files.

**Do not rebuild a page from source data just to shrink its file size.** The
embedded images are not in the source data. Rebuilding destroys them. Shrink
with the image-quality setting in `buildall.py` instead.

---

## Building

The supplied build scripts and data are in `_Build Kit/Career_Assessment_Build_Kit.zip`, with
`START HERE - Directions for New Claude Chat.txt` inside it: the generator, the
per-career data, the post-processing passes in the order they must run, the
occupation-code map, and the test scripts.

Short version:

```
python3 bk/tech/build.py <which>   # generate assessment pages
python3 buildall.py <area>         # build one hub + its web folder
python3 combine.py                 # build the full site
python3 test_all.py                # test all 11 hubs and web folders
```

### Testing means clicking, not reading

Several real bugs in this project were invisible in the HTML and obvious the
moment someone actually completed an assessment and pressed Ctrl+P. Before
shipping a change: finish an assessment, view the results, print them — in
light mode and dark mode, standalone and inside a hub. Test at phone width
(390×844) as well as desktop.

---

## Known gaps

- **Named North Dakota programs** in the Education row of Sources & Learn More.
  Right now that row links a per-occupation lookup of North Dakota schools,
  which works and stays current on its own. Naming specific programs
  ("BSC Civil Engineering Technology AAS") would be more useful and needs
  hand-curation per career.
- **Image review for representation** across the full set — checking that the
  mix of people genuinely reflects the students these are for, with more
  Native American representation.
- **Shorter-route guidance** appears in roughly half the reports. The gaps
  cluster in the teaching licensure tracks and some four-year engineering
  careers, which are exactly where it matters most.

---

## A note on sources

Source links are provided to support verification. The design goal is traceability: a person
deciding whether to spend two years and real money on training deserves to see
where the numbers came from and to check them. If you add a career, add its
sources too.

## Baseline and testing status

The September 29 handoff reports all 171 reports tested in light/dark mode,
standalone and inside hubs. The GitHub baseline adds static integrity and secret
checks; it does not claim a fresh repeat of that full browser/print matrix or
formal accessibility certification. Skip links, text resizing, dark mode,
read-aloud controls, and print support are implemented accessibility features.

The historical `Healthcare Sources` folder is excluded without deleting or moving
its local files. Use the current web healthcare pages or healthcare hub. See
[BASELINE-NOTES.txt](BASELINE-NOTES.txt) for scope, limitations, and exclusions.

Each Sources block contains four occupation-specific O*NET links and one general
RUReady career-planning link. The latter is not an occupation-specific deep link.
The data dates above describe the supplied content, not a fresh data audit.

Build portability: the archived build/test scripts reference Claude's original
Linux scratchpad and input folders. Rebuilding requires remapping those paths
and supplying the referenced inputs; a clean-machine rebuild was not verified.
The shipped HTML works independently of that build environment. The archive is
preserved unchanged for provenance, rather than silently rewritten tonight.
