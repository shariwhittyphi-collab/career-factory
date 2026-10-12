"""Shared helpers for the October 2026 new careers (Career Factory).
Pay and outlook paragraphs are generated from the numbers so figures are typed once."""

def money(x):
    return '${:,.2f}'.format(x)

def dollars(x):
    return '${:,}'.format(int(x))

def pct(x):
    return ('+' if x > 0 else '') + str(x) + '%'

FUNDING = ('<p><strong>Paying for training:</strong></p><ol>'
           '<li>Start with financial aid, scholarships, and grants. The school\'s financial aid office can help.</li>'
           '<li>Ask employers whether they help pay for training.</li>'
           '<li>Ask for the full cost, including books, fees, travel, and a computer.</li>'
           '<li>Ask your career counselor about other help, such as WIOA. WIOA is a federal program that can help some people pay for job training. Ask before you enroll.</li></ol>'
           '<p>Employer help with school may come with a promise to keep working there. Read the terms first.</p>')

SUPPORT = ('<p>Ask about written instructions, an accessible workstation, extra practice time, or other support '
           'that helps you learn and do the work well.</p>')


def pay_section(c, intro, where, setting, compare):
    w = c['wages']
    if c.get('payBasis') == 'annual-contract':
        lines = ('<li>Middle pay: <strong>' + dollars(w['p50a']) + ' a year</strong>. Half of workers earned more and half earned less.</li>'
                 '<li>Half of workers earned between ' + dollars(w['p25a']) + ' and ' + dollars(w['p75a']) + ' a year.</li>'
                 '<li>1 in 10 earned less than ' + dollars(w['p10a']) + ', and 1 in 10 earned more than ' + dollars(w['p90a']) + '.</li>')
    else:
        lines = ('<li>Middle pay: <strong>' + money(w['p50']) + ' an hour (' + dollars(w['p50a']) + ' a year)</strong>. Half of workers earned more and half earned less.</li>'
                 '<li>Half of workers earned between ' + money(w['p25']) + ' and ' + money(w['p75']) + ' an hour.</li>'
                 '<li>1 in 10 earned less than ' + money(w['p10']) + ' an hour, and 1 in 10 earned more than ' + money(w['p90']) + '.</li>')
    lines += '<li>These numbers show what workers earned. They are not a promise of what a new worker will start at.</li>'
    p = c['proj']
    lines += ('<li>North Dakota had about {:,} of these jobs in {}. The state projects about {:,} in {}, a change of {}. '
              'That works out to about {:,} openings a year, mostly from people who retire or change jobs.</li>').format(p['from'], p['y0'], p['to'], p['y1'], pct(p['pct']), p['open'])
    return ('<p><strong>' + intro + '</strong></p><ul>' + lines + '</ul>'
            + ('<p>' + p['note'] + '</p>' if p.get('note') else '')
            + '<p><strong>Where people work:</strong> ' + where + '</p>'
            + '<p><strong>Work setting:</strong> ' + setting + '</p>'
            + '<p><strong>Compare an offer:</strong> ' + compare + '</p>')


def a_an(job):
    return ('an ' if job[0].lower() in 'aeiou' else 'a ') + job


def recs_for(job, step):
    """Five lines picked only by how many activities sound comfortable (7-8, 6, 5, 3-4, 0-2).
    They never say whether someone fits the job."""
    return [
        'Many of these activities sound comfortable to you. ' + step,
        'Most of these activities sound comfortable. Ask how an employer trains someone new as ' + a_an(job) + '.',
        'Some activities sound comfortable, and others may need a closer look. Talking with someone who does the work can help.',
        'Several activities did not sound comfortable yet, and that is useful to know. You can explore this alongside other careers.',
        'You do not need a clear answer yet. Look back at the parts that interested you, and compare a few other careers too.',
    ]


RESEARCH_STEPS = ['Read the O*NET page in the Sources list at the bottom of this page.',
                  'Compare two or three training programs or job ads.',
                  'Write down questions to bring to your career counselor.']
UNDECIDED_STEPS = ['Browse another career that sounds interesting.',
                   'Write down one thing you liked about this job and one thing you did not.',
                   'Talk with your career counselor about what you noticed.']

FUTURE_TAIL = [['research', 'Learn more before applying.'], ['undecided', 'Keep exploring. I do not have a plan yet.']]


def onet_sources(soc, extra=()):
    return ([['O*NET OnLine — occupation information', 'https://www.onetonline.org/link/summary/' + soc],
             ['North Dakota pay — BLS May 2025, via O*NET', 'https://www.onetonline.org/link/localwages/' + soc + '?st=ND'],
             ['North Dakota outlook — Projections Central 2024–2034, via O*NET', 'https://www.onetonline.org/link/localtrends/' + soc + '?st=ND'],
             ['North Dakota schools and programs — via O*NET', 'https://www.onetonline.org/link/localtraining/' + soc + '?st=ND']]
            + [list(x) for x in extra])


def facets_for(w, p):
    pay = 'under-20' if w['p50'] < 20 else '20-to-30' if w['p50'] < 30 else '30-plus'
    g = p['pct']
    growth = 'growing-fast' if g >= 10 else 'steady' if g >= 5 else 'flat' if g >= 0 else 'declining'
    o = p['open']
    opens = 'few-openings' if o < 100 else 'some-openings' if o < 500 else 'many-openings'
    return [pay, growth, opens]


APPRENTICE_PAY = ('<p><strong>Paying for training:</strong> In an apprenticeship you are paid while you learn, and pay usually rises as you complete hours. '
                  'For classes or a certificate, start with financial aid, scholarships, and grants. Ask employers whether they help pay. '
                  'Ask your career counselor about other help, such as WIOA, a federal program that can help some people pay for job training. Ask before you enroll.</p>')
