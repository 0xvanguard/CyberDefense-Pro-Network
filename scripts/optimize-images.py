#!/usr/bin/env python3
"""Optimize hero-bg image and generate favicon set for CDPN.

Run:  python3 scripts/optimize-images.py
"""
from PIL import Image
import cairosvg
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'docs' / 'assets'
DOCS = ROOT / 'docs'


def svg_to_png(svg_path, size, dark_bg=(10, 14, 26)):
    """Render SVG to PNG via cairosvg, then composite onto dark bg."""
    png_bytes = cairosvg.svg2png(
        url=str(svg_path),
        output_width=size,
        output_height=size
    )
    img = Image.open(io.BytesIO(png_bytes)).convert('RGBA')
    canvas = Image.new('RGB', (size, size), dark_bg)
    canvas.paste(img, (0, 0), img)
    return canvas

# --- 1. Hero background (was misnamed .png; actually JPEG) ---
hero_src = ASSETS / 'hero-bg.png'
hero_jpg = ASSETS / 'hero-bg.jpg'
hero_webp = ASSETS / 'hero-bg.webp'
hero_thumb = ASSETS / 'hero-bg-thumb.webp'

print('Processing hero-bg...')
img = Image.open(hero_src)
print(f'  source: {img.size} {img.mode}')

# Convert to RGB (drop alpha if any) and save as JPG
img_rgb = img.convert('RGB')

# Save optimized JPG (progressive, quality 80)
img_rgb.save(hero_jpg, 'JPEG', quality=80, optimize=True, progressive=True)
print(f'  → {hero_jpg.name} ({hero_jpg.stat().st_size//1024} KB)')

# Save as WebP (much smaller)
img_rgb.save(hero_webp, 'WEBP', quality=82, method=6)
print(f'  → {hero_webp.name} ({hero_webp.stat().st_size//1024} KB)')

# Small thumbnail for mobile / lazy load placeholder
img_thumb = img_rgb.copy()
img_thumb.thumbnail((600, 600))
img_thumb.save(hero_thumb, 'WEBP', quality=70, method=6)
print(f'  → {hero_thumb.name} ({hero_thumb.stat().st_size//1024} KB)')

# --- 2. Favicons from SVG master ---
import shutil, subprocess

favicon_svg = DOCS / 'favicon.svg'
favicons = ASSETS / 'icons'
favicons.mkdir(exist_ok=True)

print('Generating favicon set...')
svg_img_512 = svg_to_png(favicon_svg, 512)

# Standard sizes
for size, name in [
    (16, 'favicon-16x16.png'),
    (32, 'favicon-32x32.png'),
    (180, 'apple-touch-icon.png'),
    (192, 'icon-192.png'),
    (512, 'icon-512.png'),
]:
    out = favicons / name
    resized = svg_img_512.resize((size, size), Image.LANCZOS)
    resized.save(out, 'PNG', optimize=True)
    print(f'  → {name} ({out.stat().st_size//1024} KB)')

# Combined favicon.ico
ico_sizes = [16, 32, 48]
ico_imgs = [svg_img_512.resize((s, s), Image.LANCZOS) for s in ico_sizes]
ico_path = DOCS / 'favicon.ico'
ico_imgs[0].save(
    ico_path,
    format='ICO',
    sizes=[(s, s) for s in ico_sizes],
    append_images=ico_imgs[1:]
)
print(f'  → favicon.ico ({ico_path.stat().st_size//1024} KB)')

# --- 3. OG image (1200x630 — social preview) ---
print('Generating OG image...')
og_dir = ASSETS / 'og'
og_dir.mkdir(exist_ok=True)
og_png = og_dir / 'og-image.png'
og_webp = og_dir / 'og-image.webp'

# Render the SVG large onto a dark canvas
canvas = Image.new('RGB', (1200, 630), (10, 14, 26))
big_shield_png = Image.open(io.BytesIO(cairosvg.svg2png(
    url=str(favicon_svg),
    output_width=420,
    output_height=420
))).convert('RGBA')
canvas.paste(big_shield_png, (80, 105), big_shield_png)
canvas.save(og_png, 'PNG', optimize=True)
canvas.save(og_webp, 'WEBP', quality=85, method=6)
print(f'  → og-image.png ({og_png.stat().st_size//1024} KB)')
print(f'  → og-image.webp ({og_webp.stat().st_size//1024} KB)')

# --- 4. PWA manifest ---
print('Writing manifest.webmanifest...')
manifest = {
    "name": "CyberDefense Pro Network",
    "short_name": "CDPN",
    "description": "Plataforma educativa de ciberseguridad en español",
    "start_url": "/CyberDefense-Pro-Network/",
    "scope": "/CyberDefense-Pro-Network/",
    "display": "standalone",
    "background_color": "#0a0e1a",
    "theme_color": "#0a0e1a",
    "lang": "es",
    "icons": [
        {"src": "assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "favicon.svg", "sizes": "any", "type": "image/svg+xml"}
    ]
}
import json
manifest_path = DOCS / 'manifest.webmanifest'
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'  → manifest.webmanifest')

print('\n✅ All assets generated.')
