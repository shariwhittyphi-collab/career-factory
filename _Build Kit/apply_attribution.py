#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_attribution.py — add the site attribution footer to every career page.

Run it from the repo root. It edits the career pages IN PLACE and does not
touch any index.html, so the homepage and the area pages are left alone.

    python3 apply_attribution.py            # see what it would do
    python3 apply_attribution.py --write    # actually do it

It is idempotent: running it twice changes nothing the second time, so it is
safe to re-run after adding new careers.
"""
import argparse, glob, io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from attribution import add_attribution, MARK

ap = argparse.ArgumentParser()
ap.add_argument('--root', default='.', help='repo root (contains the area folders)')
ap.add_argument('--write', action='store_true', help='apply; otherwise dry run')
a = ap.parse_args()

pages = [f for f in glob.glob(os.path.join(a.root, '*', '*.html'))
         if os.path.basename(f) != 'index.html']
if not pages:
    sys.exit(f'no career pages found under {a.root!r} — run this from the repo root')

counts, changed = {}, []
for f in sorted(pages):
    h = io.open(f, encoding='utf-8').read()
    h2, note = add_attribution(h)
    counts[note] = counts.get(note, 0) + 1
    if note.startswith('ok'):
        changed.append(f)
        if a.write:
            io.open(f, 'w', encoding='utf-8').write(h2)

print(f'career pages found: {len(pages)}   (index.html files skipped)')
for k, v in sorted(counts.items()):
    print(f'   {v:>4}  {k}')
print()
if a.write:
    print(f'WROTE {len(changed)} files.')
else:
    print(f'DRY RUN — {len(changed)} would change. Re-run with --write to apply.')
