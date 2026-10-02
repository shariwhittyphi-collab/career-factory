# -*- coding: utf-8 -*-
"""Adds the site attribution footer to a career page. Idempotent.

WHY THIS EXISTS
  Three separate obligations, one block, because they all belong in the same
  place and nobody reads three footers:

  1. AUTHORSHIP. The homepage credits the author; the 193 career pages did not.
     Career pages are where people actually land — search sends them straight
     there, Google indexes them individually, and a shared link is always a
     specific career. Attribution only on the front door is attribution almost
     nobody sees, and it disappears the next time the front door is redesigned.

  2. O*NET LICENCE. The CC BY 4.0 licence on O*NET content requires crediting
     USDOL/ETA as the original source and linking the licence. The Sources block
     named O*NET but did neither. That was an outstanding compliance gap.

  3. INDEPENDENCE. The site carries ND labour data, state licensing rules and
     training information on a .org domain with "ND" in the name. Saying plainly
     that it is not a state product protects the author and keeps any future
     conversation with an agency clean.
"""
import re, html

MARK = '<!-- Site attribution (attribution.py) -->'
CSS_MARK = '/* ---- Site attribution ---- */'

AUTHOR = 'Sheri Whitmire'
WAGE_VINTAGE = 'U.S. Bureau of Labor Statistics Occupational Employment and Wage Statistics, May 2025'
PROJ_VINTAGE = 'Projections Central, 2024&ndash;2034'

CSS = '''
        ''' + CSS_MARK + '''
        .site-attrib { max-width: 900px; margin: 18px auto 28px; padding: 14px 18px;
            border-top: 1px solid #c7d9ea; font-size: .82rem; line-height: 1.55;
            color: #3a4a57; }
        html[data-theme="dark"] .site-attrib { border-top-color: #2d4a68; color: #9fb3c4; }
        .site-attrib strong { color: #0b4f8a; }
        html[data-theme="dark"] .site-attrib strong { color: #8cc4ff; }
        .site-attrib a { color: #0b4f8a; }
        html[data-theme="dark"] .site-attrib a { color: #8cc4ff; }
        .site-attrib a:focus-visible { outline: 3px solid #0b4f8a; outline-offset: 2px; }
        .site-attrib p { margin: 0 0 6px; }
        .site-attrib p:last-child { margin-bottom: 0; }
        @media print {
            /* Must survive the full-report print, so a printed page carries its
               authorship and its data vintage. Hidden when printing one section. */
            body.print-report:not(.print-one) .site-attrib {
                display: block !important; color: #000 !important;
                border-top: 1px solid #999 !important; page-break-inside: avoid; }
            body.print-report:not(.print-one) .site-attrib a {
                color: #000 !important; text-decoration: none; }
            body.print-one .site-attrib { display: none !important; }
        }
'''

BLOCK = '''    ''' + MARK + '''
    <aside class="site-attrib" aria-label="About this site and where its information comes from">
      <p><strong>Career Factory</strong> &middot; Human-led. AI-assisted. Built with care by ''' + AUTHOR + '''.</p>
      <p>An independent project. Not affiliated with, produced by, or endorsed by any state agency.</p>
      <p>Career information from <a href="https://www.onetonline.org/">O*NET OnLine</a>
         by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA),
         used under the <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0 licence</a>.
         O*NET&reg; is a trademark of USDOL/ETA.
         North Dakota wages: ''' + WAGE_VINTAGE + '''.
         Employment projections: ''' + PROJ_VINTAGE + '''.
         Figures are the vintage shown and are not updated continuously &mdash;
         the source links above always show current data.</p>
    </aside>
'''


def add_attribution(s):
    if MARK in s:
        return s, 'already'
    i = s.rfind('</style>')
    if i == -1:
        return s, 'no </style>'
    s = s[:i].rstrip(' \t') + CSS + '    ' + s[i:]

    # Sit after the Sources block if there is one, otherwise just before </body>.
    anchor = s.rfind('</aside>')
    src = s.rfind('<!-- Sources & Learn More (sources.py) -->')
    if src != -1 and anchor > src:
        return s[:anchor + len('</aside>')] + '\n\n' + BLOCK + s[anchor + len('</aside>'):], 'ok (after sources)'
    m = list(re.finditer(r'</body>', s))
    if not m:
        return s, 'no insertion point'
    j = m[-1].start()
    return s[:j] + BLOCK + '\n' + s[j:], 'ok (before body end)'
