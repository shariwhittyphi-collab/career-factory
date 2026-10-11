"""Size a picture for Career Factory: crop to 3:2, resize to 1200 x 800, JPEG under 600 KB.
Run: python prepare_images.py <input image> <output.jpg>   (needs Pillow: pip install pillow)"""
import io, sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB')
w, h = im.size
if w / h > 1.5:
    nw = int(h * 1.5); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
elif w / h < 1.5:
    nh = int(w / 1.5); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
im = im.resize((1200, 800), Image.LANCZOS)
for q in (85, 80, 75, 70, 65, 60):
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True, progressive=True)
    if b.tell() < 600_000:
        break
open(out, 'wb').write(b.getvalue())
print(out, '1200x800', b.tell() // 1024, 'KB', 'quality', q)
