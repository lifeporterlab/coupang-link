"""coupang link PWA 아이콘 생성 — 안드로이드 아이콘과 동일 디자인.

- 흰 배경(라운드 사각) + 빨간 24각 별 + 별 안에 흰 'coupang' / 'link'
- maskable 은 안전영역(80%) 안에 들어가도록 작게 그린다.
"""
from __future__ import annotations

import math
import pathlib

from PIL import Image, ImageDraw, ImageFont

OUT = pathlib.Path(r"C:/Users/lifeporter/projects/coupang-link-pwa")
RED = (200, 45, 45, 255)
WHITE = (255, 255, 255, 255)
FONTS = [r"C:/Windows/Fonts/malgunbd.ttf", r"C:/Windows/Fonts/arialbd.ttf"]


def font(size: int):
    for p in FONTS:
        if pathlib.Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def star(d, cx, cy, r_out, r_in, points, fill):
    verts, step = [], math.pi / points
    for i in range(points * 2):
        ang = i * step - math.pi / 2
        r = r_out if i % 2 == 0 else r_in
        verts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d.polygon(verts, fill=fill)


def draw(size: int, *, rounded: bool, scale: float = 1.0) -> Image.Image:
    ss = 4
    S = size * ss
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    if rounded:
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=WHITE)
    else:
        d.rectangle([0, 0, S - 1, S - 1], fill=WHITE)

    cx = cy = S / 2
    star(d, cx, cy, S * 0.40 * scale, S * 0.315 * scale, 24, RED)

    fw = font(int(S * 0.132 * scale))
    fl = font(int(S * 0.100 * scale))
    for text, f, dy in (("coupang", fw, -S * 0.052 * scale), ("link", fl, S * 0.058 * scale)):
        b = d.textbbox((0, 0), text, font=f)
        d.text((cx - (b[2] - b[0]) / 2 - b[0], cy + dy - (b[3] - b[1]) / 2 - b[1]),
               text, font=f, fill=WHITE)
    return img.resize((size, size), Image.LANCZOS)


def main() -> int:
    jobs = [
        ("icon-192.png", 192, True, 1.0),
        ("icon-512.png", 512, True, 1.0),
        ("icon-180.png", 180, True, 1.0),
        ("icon-maskable-512.png", 512, False, 0.78),
    ]
    for name, size, rounded, scale in jobs:
        draw(size, rounded=rounded, scale=scale).save(OUT / name)
        print(f"  {name} ({size}x{size}, scale={scale})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
