SOFTEN REPORTS — October 10, 2026

Shari's decision: no career page hands down a verdict ("You are an excellent fit...
Pursue this", "This does not seem like your best fit", "Low Readiness", "The Verdict").
Reports now read like the Rural Additions and the October 2026 careers:
  What interests you  ->  Activities that sound comfortable: X / 8  ->  Something to explore
plus the line "These answers are a conversation starter, not a test of ability or a
prediction. You can learn skills, ask for support, and change your mind."

All career-specific advice was kept. Only judging and scoring wording changed.

Chadwick's review (October 10) added these, now on every career page:
  * No ranking of reasons: which suggestion appears depends only on how many
    activities sounded comfortable. Each reason for exploring gets a neutral note.
  * Manual dark mode: dark text on the light-blue buttons (was 2.2:1, now 7.9:1).
  * Sources print dark on white from either theme.
  * Text size makes headings, buttons and boxes bigger too.
  * Skip link comes first and shows above the career navigation.
  * A missed question moves focus to the first unanswered one.
  * "Review my answers" on the report; Start Over clears the answers.
  * The theme button shows the right starting state when the computer is in dark mode.
  * One-section printing clears itself when the print dialog closes.
  * The 19 original healthcare pages also escape typed comments and no longer
    say "is this right for you" in their introductions.
  * 174 pages share one report template; soften.py rewrites them by pattern.
  * 19 original healthcare pages have their own report code; their reviewed wording
    changes are exact [old, new] pairs in healthcare_pairs.json.
  * The same changes are applied to the copies inside the 12 portable hubs.

Run from the repo root:   python "_Build Kit/Soften Reports October 2026/soften.py"
Check:                    node "_Build Kit/Soften Reports October 2026/check-no-verdicts.cjs"
Running it twice is safe.

Tested October 10, 2026: all existing tests pass; every one of the 195 pages produced
a report with no errors and no verdict wording, with two different sets of answers;
the fixes above were checked in a browser on sample pages from each template.
