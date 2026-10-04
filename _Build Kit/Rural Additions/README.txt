RURAL ADDITIONS — October 4, 2026

Run: python "_Build Kit/Rural Additions/build.py"

This folder stores editable career content in careers.json and a shared HTML
assessment template. The template preserves the existing display controls,
Listen/Print tools, report printing, and safe escaping of student notes.
The four JPEGs are embedded into the web and portable hub versions.

The builder refreshes both additions, corresponding hub entries, area-menu
cards, and search-index entries. It does not regenerate the original 193 careers.
Running it again is safe. Original hub assessments remain intact.
If the archived original builder regenerates the index or menus, run this
builder afterward. Homepage copy and student-opportunities.html are static.

Precision Ag Technician: O*NET-SOC 19-4012.01. Wages and projections are for the
broader Agricultural Technicians group (19-4012.00), labelled on page and in
search cards. Parts Counter Salesperson: 41-2022.00. BLS May 2025 wages and
Projections Central 2024–2034 figures were checked through O*NET on October 4.
Sources, named programs, and current employer routes are linked on the pages.

New careers remain unmarked by the July 2026 ND membership file. The precision
specialty is not individually named there; Parts Salespersons is not on it.

Original reflection questions and sample days are illustrations. Reflection
results are not a validated aptitude test, eligibility decision, or prediction.
Next steps adapt to the selected plan, including a short certificate route.

Checks: node "_Build Kit/tests/check-rural-additions.cjs"
        node "_Build Kit/tests/check-area12.cjs"
        node "_Build Kit/tests/check-reading-controls.cjs"
