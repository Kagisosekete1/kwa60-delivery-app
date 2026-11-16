"""Create optional clean product crops from the supplied square promo images.

Requires Pillow (`python -m pip install pillow`). Keeps package/label details
intact and only removes the surrounding headline, price block, and footer.
Originals stay in assets/products; generated crops go to assets/cropped.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "products"
DEST = ROOT / "assets" / "cropped"

# Normalized regions enclosing the product photography in the promo artwork.
# Crop boundaries are conservative to avoid removing product edges/shadows.
REGIONS = {
    "6041629671385928426_121.jpg": (0.17, 0.32, 0.93, 0.72),
    "6041629671385928427_121.jpg": (0.33, 0.24, 0.75, 0.79),
    "6041629671385928428_121.jpg": (0.36, 0.27, 0.66, 0.79),
    "6041629671385928429_121.jpg": (0.18, 0.28, 0.92, 0.75),
    "6041629671385928430_121.jpg": (0.04, 0.28, 0.96, 0.79),
    "6041629671385928431_121.jpg": (0.07, 0.15, 0.90, 0.87),
    "6041629671385928432_121.jpg": (0.06, 0.25, 0.89, 0.84),
    "6041629671385928433_121.jpg": (0.07, 0.16, 0.90, 0.80),
    "6041629671385928434_121.jpg": (0.17, 0.22, 0.83, 0.82),
    "6041629671385928435_121.jpg": (0.22, 0.22, 0.79, 0.82),
    "6041629671385928436_121.jpg": (0.17, 0.23, 0.84, 0.82),
}

DEST.mkdir(parents=True, exist_ok=True)
for filename, (left, top, right, bottom) in REGIONS.items():
    source = SOURCE / filename
    if not source.exists():
        print(f"Missing source: {source}")
        continue
    with Image.open(source) as image:
        width, height = image.size
        box = (round(left * width), round(top * height), round(right * width), round(bottom * height))
        image.crop(box).save(DEST / filename, quality=94)
        print(f"Created {DEST / filename}")
