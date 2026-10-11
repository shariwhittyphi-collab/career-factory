"""Soften the reflection report on the original career assessments (October 2026).

Shari's decision (Oct 10 2026): no page should hand down a verdict such as
"You are an excellent fit ... Pursue this" or "This does not seem like your best fit".
The report should read like the Rural Additions and October 2026 careers do:
what interests you, which activities sound comfortable, something to explore.
All career-specific advice is kept; only the judgment wording changes.

Run from the repo root:  python "_Build Kit/Soften Reports October 2026/soften.py"
It changes the web pages and the matching copies inside the portable hubs.
Running it twice is safe.
"""
from pathlib import Path
import base64, json, re, sys

here = Path(__file__).resolve().parent
repo = here.parents[1]
site = repo / 'Career Assessments Web'

INTRO = ('<p>These answers are a conversation starter, not a test of ability or a prediction. '
         'You can learn skills, ask for support, and change your mind.</p>')

# exact swaps inside the shared report function (173 pages + the 9-question variant)
SWAPS = [
    ('<h3>Motivation Score: ${motivationScore} / 10</h3>', '<h3>What interests you</h3>'),
    ("'Strong motivation.'", "'This part of the work interests you.'"),
    ("'Good interest. Get clear on what you want from this job.'", "'There is something here you may want to explore. Think about what you want from this job.'"),
    ("'Not sure yet. Explore more before you spend money on training.'", "'It is fine to be curious without knowing yet. Explore more before you spend money on training.'"),
    ('<h3>${readinessLevel} Readiness: ', '<h3>Activities that sound comfortable: '),
    ("'You look ready.'", "'Many of these activities sound comfortable to you.'"),
    ("'You have most of what it takes.'", "'Some activities sound comfortable; others may need a closer look.'"),
    ("'Some gaps exist. That is OK. Now you know what to work on.'", "'You have things to learn about. That is a normal part of exploring.'"),
    ('Things to work on or look into:', 'Things to ask about or try:'),
    ('<h3>The Verdict</h3>', '<h3>Something to explore</h3>'),
]
MOT_BAR = re.compile(r'\n[ \t]*<div class="score-bar"><div class="score-fill" style="width: \$\{motivationScore \* 10\}%"></div></div>')
LEVEL_LINE = re.compile(r'\n[ \t]*let readinessLevel = [^\n]*;')


def soften_rec(i, r):
    """Rewrite one of the five recommendation lines, keeping any career advice in it."""
    if i == 0:
        m = re.match(r'You are an excellent fit for (.+?)\.(?: You have the [^.]+?\.)?(?: Pursue this\.)?(.*)$', r, re.S)
        if m:
            tail = m[2].strip()
            return ('Many of the activities in ' + m[1] + ' sound comfortable to you. '
                    'Talking with someone who does this work is a good next step.' + (' One possible route: ' + tail if tail else ''))
    if i == 1:
        m = re.match(r'(.+?) is a strong option\. (.*)$', r, re.S)
        if m:
            return 'Most of these activities sound comfortable. ' + m[1] + ' could be worth a closer look. One possible route: ' + m[2]
    if i == 2:
        if r.startswith('You could do well here. '):
            return 'Some activities sound comfortable, and others may need a closer look. ' + r[len('You could do well here. '):]
    if i == 3:
        m = re.match(r'This might work, but (look at|explore) (.+?) too(,| like|\.)(.*)$', r, re.S)
        if m:
            what = m[2].replace('related trades', 'related careers')
            return 'Several activities did not sound comfortable yet, and that is useful to know. You can also ' + m[1] + ' ' + what + m[3] + m[4]
    if i == 4:
        m = re.match(r'This does not seem like your best fit right now\.\s*(?:Explore other [^.]*\.)?\s*(.*)$', r, re.S)
        if m:
            return ('You do not need a clear answer yet. Look back at the parts that interested you, '
                    'and compare a few other careers too.' + (' ' + m[1] if m[1] else ''))
    return r


PAIRS = json.loads((here / 'healthcare_pairs.json').read_text(encoding='utf8'))


def soften_handwritten(h):
    """The 19 original healthcare pages each have their own report code. Their reviewed
    wording changes live in healthcare_pairs.json as exact [old, new] pairs."""
    for name, pairs in PAIRS.items():
        if all(h.count(old) == 1 for old, new in pairs):
            for old, new in pairs:
                h = h.replace(old, new)
            return h
    return h


# Which suggestion someone sees depends only on how many activities sounded comfortable.
# Their reason for exploring is acknowledged, never ranked (Chadwick's review, Oct 10 2026).
MOT_TERNARY = re.compile(r"\$\{motivationScore >= 8 \? '[^']*' : motivationScore >= 6 \? '[^']*' : '[^']*'\}")
MOT_NOTE = ("${({salary: 'Pay and stability matter. Look at the whole job too, including the hard parts.', "
            "recommend: 'Someone thought of you for this work. It is worth finding out what you think.', "
            "explore: 'It is fine to be curious without knowing yet. Explore more before you spend money on training.'})[motivation] "
            "|| 'This part of the work interests you.'}")


def fix_selection(h):
    h = re.sub(r'motivationScore >= \d+ && ', '', h)
    h = h.replace('else if (motivationScore >= 5) recommendation', 'else if (readinessScore >= 3) recommendation')
    return MOT_TERNARY.sub(lambda m: MOT_NOTE, h)


FIX_MARK = '<!-- Career Factory fixes (October 2026) -->'
FIX_END = '<!-- /Career Factory fixes -->'
FIX_BLOCK = FIX_MARK + '''
<style>
/* Selected text-size button: always a solid fill with white text in the light theme
   (two healthcare pages showed white text on a white background). */
html:not([data-theme="dark"]) .a11y-bar button[aria-pressed="true"] {
  background-color: #0b4f8a !important; border-color: #0b4f8a !important; color: #fff !important; }
/* Light-blue controls get dark text in every dark path (manual or the computer's setting).
   Background and text are set together so the pair is always readable (7.9:1). */
html[data-theme="dark"] :is(.btn-primary, .section-number, .a11y-bar button[aria-pressed="true"], .tool-btn.speaking) {
  background-color: #6cb4ff !important; border-color: #6cb4ff !important; color: #0b1b2e !important; }
html[data-theme="dark"] .btn-primary:hover { background-color: #8cc4ff !important; }
@media (prefers-color-scheme: dark) {
  html:not([data-theme="light"]) :is(.btn-primary, .section-number, .a11y-bar button[aria-pressed="true"], .tool-btn.speaking) {
    background-color: #6cb4ff !important; border-color: #6cb4ff !important; color: #0b1b2e !important; }
  html:not([data-theme="light"]) .btn-primary:hover { background-color: #8cc4ff !important; }
}
/* Skip link: same readable colors in every theme, above the sticky career navigation. */
.skip-link:focus { background: #0b4f8a !important; color: #fff !important; z-index: 10001 !important; }
/* Text size grows headings, buttons and boxes too, not only body text. */
html:has(body.text-large) { font-size: 115%; }
html:has(body.text-xl) { font-size: 135%; }
body.text-large, body.text-xl { font-size: 1rem; }
/* Sources print dark on white from either theme. */
@media print { .srcsec, .srcsec * { color: #000 !important; background: #fff !important; } .srcsec a { color: #0b4f8a !important; } }
</style>
<script>
(function () {
    var de = document.documentElement;
    var mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
    var tb = document.getElementById('themeBtn');
    // The theme button shows the real starting theme when the computer is in dark mode.
    if (tb && !de.getAttribute('data-theme') && mq && mq.matches) { tb.innerHTML = '\\u2600 Light mode'; tb.setAttribute('aria-pressed', 'true'); }
    if (typeof window.toggleTheme === 'function') {
        var tt = window.toggleTheme;
        window.toggleTheme = function () { if (!de.getAttribute('data-theme')) de.setAttribute('data-theme', mq && mq.matches ? 'dark' : 'light'); tt(); };
    }
    // The skip link is the first thing a keyboard user reaches.
    var sl = document.querySelector('.skip-link');
    if (sl && document.body.firstElementChild !== sl) document.body.insertBefore(sl, document.body.firstChild);
    // Printing one part clears itself when the print dialog closes.
    window.addEventListener('afterprint', function () {
        document.body.classList.remove('print-one');
        var o = document.querySelectorAll('.print-me');
        for (var i = 0; i < o.length; i++) o[i].classList.remove('print-me');
    });

    // ---- Missed questions: move to the first unanswered one. Works with every page style:
    // the shared alert box, the healthcare pages' inline alert, and plain pop-up alerts.
    function focusMissing(alertEl) {
        var scope = document.querySelector('.section.active') || document;
        var radios = scope.querySelectorAll('input[type=radio]');
        var seen = {};
        for (var i = 0; i < radios.length; i++) {
            var n = radios[i].name;
            if (seen[n]) continue;
            seen[n] = 1;
            if (!document.querySelector('input[name="' + n + '"]:checked')) {
                var group = radios[i].closest('fieldset') || radios[i].closest('.question, .assessment-question') || radios[i].parentNode;
                if (alertEl) {
                    if (!alertEl.id) alertEl.id = 'cfAlert';
                    group.setAttribute('aria-describedby', alertEl.id);
                }
                radios[i].focus();
                if (document.activeElement !== radios[i]) { group.setAttribute('tabindex', '-1'); group.focus(); }
                return true;
            }
        }
        return false;
    }
    if (typeof window.alertMsg === 'function') {
        var am = window.alertMsg;
        window.alertMsg = function (msg) { am(msg); focusMissing(document.getElementById('alertBox')); };
    }
    if (window.MutationObserver) {
        new MutationObserver(function (list) {
            for (var i = 0; i < list.length; i++) for (var j = 0; j < list[i].addedNodes.length; j++) {
                var nd = list[i].addedNodes[j];
                if (nd.nodeType === 1 && nd.getAttribute('role') === 'alert' && nd.id !== 'alertBox') { focusMissing(nd); return; }
            }
        }).observe(document.body, { childList: true, subtree: true });
    }
    var nativeAlert = window.alert;
    window.alert = function (msg) { nativeAlert.call(window, msg); focusMissing(null); };

    // ---- Report: "Review my answers" goes back to the first question; Start Over clears answers.
    function goToSectionEl(el) {
        if (!el) return;
        var num = el.id && /^section(\\d+)$/.test(el.id) ? +el.id.replace('section', '') : (el.getAttribute('data-section') ? +el.getAttribute('data-section') : null);
        if (typeof window.show === 'function' && el.id) {
            try { if (num) currentSection = num; } catch (e) {}
            window.show(el.id);
        } else if (typeof window.goToSection === 'function' && el.id) {
            window.goToSection(el.id);
        } else if (typeof window.showSection === 'function' && num) {
            window.showSection(num);
        } else {
            var all = document.querySelectorAll('.section');
            for (var i = 0; i < all.length; i++) all[i].classList.remove('active');
            el.classList.add('active');
            try { if (num) currentSection = num; } catch (e) {}
            window.scrollTo(0, 0);
        }
        if (typeof window.updateProgress === 'function') { try { window.updateProgress(); } catch (e) {} }
        var h = el.querySelector('h2');
        if (h) { if (!h.hasAttribute('tabindex')) h.setAttribute('tabindex', '-1'); h.focus(); }
    }
    function firstQuestionSection() {
        var q = document.querySelector('input[type=radio]');
        return q && q.closest('.section, [data-section]');
    }
    function setupReview() {
        var report = document.getElementById('report') || document.getElementById('reportSection');
        if (!report || document.getElementById('reviewBtn')) return;
        var first = report.querySelector('.button-group') || (report.querySelector('button') && report.querySelector('button').parentNode);
        if (!first || !firstQuestionSection()) return;
        var rb = document.createElement('button');
        rb.type = 'button'; rb.id = 'reviewBtn'; rb.className = 'btn-secondary'; rb.textContent = 'Review my answers';
        rb.onclick = function () { goToSectionEl(firstQuestionSection()); };
        first.insertBefore(rb, first.firstChild);
        var btns = report.querySelectorAll('button');
        for (var k = 0; k < btns.length; k++) {
            if ((btns[k].getAttribute('onclick') || '').indexOf('location.reload') > -1) {
                btns[k].onclick = function () {
                    var f = document.querySelectorAll('input[type=radio], input[type=checkbox]');
                    for (var a = 0; a < f.length; a++) f[a].checked = false;
                    var t = document.querySelectorAll('textarea, input[type=text]');
                    for (var b = 0; b < t.length; b++) t[b].value = '';
                    location.reload();
                };
            }
        }
    }
    // Some pages draw their questions after loading, so try again once everything is ready.
    setupReview();
    document.addEventListener('DOMContentLoaded', setupReview);
    window.addEventListener('load', setupReview);
})();
</script>
''' + FIX_END


def add_fixes(h):
    """Add the shared fixes, replacing an earlier copy of them if the page already has one."""
    if FIX_MARK in h:
        a = h.index(FIX_MARK)
        e = h.find(FIX_END, a)
        b = e + len(FIX_END) if e != -1 else h.index('</script>', a) + len('</script>')
        h = h[:a] + h[b:].lstrip('\n')
    if '</body>' not in h:
        return h
    i = h.rindex('</body>')
    return h[:i] + FIX_BLOCK + '\n' + h[i:]


def soften(h):
    """Return the page with verdicts removed and the shared fixes added."""
    crlf = '\r\n' in h
    t = h.replace('\r\n', '\n')
    t2 = soften_handwritten(t)
    if t2 == t and 'function generateReport()' in t and 'const DATA = ' in t:
        for a, b in SWAPS:
            t2 = t2.replace(a, b)
        t2 = MOT_BAR.sub('', t2)
        t2 = LEVEL_LINE.sub('', t2)
        m = re.search(r'(const DATA = )(\{.*\})(;\n)', t2)
        data = json.loads(m[2])
        if 'recs' in data:
            data['recs'] = [soften_rec(i, r) for i, r in enumerate(data['recs'])]
            t2 = t2[:m.start(2)] + json.dumps(data, ensure_ascii=False) + t2[m.end(2):]
        t2 = re.sub(r'(Assessment Results</h2>)(\n)(?!\s*<p>These answers)', lambda x: x[1] + x[2] + '            ' + INTRO + x[2], t2, count=1)
        t2 = fix_selection(t2)
    t2 = t2.replace('Part 2: Are You Ready?', 'Part 2: Things You Could Try')
    t2 = add_fixes(t2)
    return t2.replace('\n', '\r\n') if crlf else t2


def rd(p):
    with open(p, encoding='utf8', newline='') as f:
        return f.read()


def wr(p, t):
    with open(p, 'w', encoding='utf8', newline='') as f:
        f.write(t)


if __name__ == '__main__':
    changed = 0
    for p in sorted(site.glob('*/*.html')):
        if p.name == 'index.html':
            continue
        s = rd(p)
        t = soften(s)
        if t != s:
            wr(p, t); changed += 1
    hubs = 0
    for hub in sorted(repo.glob('*_Career_Assessments.html')):
        s = rd(hub)
        m = re.search(r'var ASSESSMENTS_DATA = (\{.*?\});', s, re.S)
        blob = m[1]
        def fix(x):
            raw = base64.b64decode(x[2]).decode('utf8')
            new = soften(raw)
            return x[1] + base64.b64encode(new.encode('utf8')).decode()
        nb = re.sub(r'("[^"]+ Career Assessment"\s*:\s*")([A-Za-z0-9+/=]+)', lambda x: fix(x), blob)
        if nb != blob:
            wr(hub, s[:m.start(1)] + nb + s[m.end(1):]); hubs += 1
    print(f'Softened {changed} web pages and updated {hubs} hubs.')
