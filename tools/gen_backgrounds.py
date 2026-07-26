"""Generate tactical plotting-grid SVG backgrounds: grid, ticks, range rings."""
import math
import numpy as np
from pathlib import Path

W, H = 1600, 900
OUT = Path(__file__).resolve().parents[1] / "static" / "images" / "backgrounds"
OUT.mkdir(parents=True, exist_ok=True)

VARIANTS = {
    "home":    {"seed": 7,  "hue": "#8ab4d8"},
    "operate": {"seed": 21, "hue": "#8ab4d8"},
    "connect": {"seed": 42, "hue": "#7fc9c4"},
    "build":   {"seed": 63, "hue": "#c4b48a"},
}

for name, cfg in VARIANTS.items():
    rng = np.random.default_rng(cfg["seed"])
    hue = cfg["hue"]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'preserveAspectRatio="xMidYMid slice">',
        f'<rect width="{W}" height="{H}" fill="#0a0d11"/>',
    ]

    # minor grid (50 px)
    g = ['<g stroke="#dce6f0" stroke-opacity="0.025" stroke-width="1">']
    for gx in range(0, W + 1, 50):
        g.append(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}"/>')
    for gy in range(0, H + 1, 50):
        g.append(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}"/>')
    g.append("</g>")
    parts.extend(g)

    # major grid (200 px)
    g = ['<g stroke="#dce6f0" stroke-opacity="0.06" stroke-width="1">']
    for gx in range(0, W + 1, 200):
        g.append(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}"/>')
    for gy in range(0, H + 1, 200):
        g.append(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}"/>')
    g.append("</g>")
    parts.extend(g)

    # crosses at major intersections
    g = ['<g stroke="#dce6f0" stroke-opacity="0.13" stroke-width="1">']
    for gx in range(200, W, 200):
        for gy in range(200, H, 200):
            g.append(f'<line x1="{gx - 6}" y1="{gy}" x2="{gx + 6}" y2="{gy}"/>')
            g.append(f'<line x1="{gx}" y1="{gy - 6}" x2="{gx}" y2="{gy + 6}"/>')
    g.append("</g>")
    parts.extend(g)

    # ruler ticks along major gridlines (every 25 px, short)
    g = ['<g stroke="#dce6f0" stroke-opacity="0.05" stroke-width="1">']
    ruler_y = 200 * int(rng.integers(1, H // 200))
    for gx in range(0, W + 1, 25):
        tick = 6 if gx % 100 == 0 else 3
        g.append(f'<line x1="{gx}" y1="{ruler_y - tick}" x2="{gx}" y2="{ruler_y + tick}"/>')
    ruler_x = 200 * int(rng.integers(1, W // 200))
    for gy in range(0, H + 1, 25):
        tick = 6 if gy % 100 == 0 else 3
        g.append(f'<line x1="{ruler_x - tick}" y1="{gy}" x2="{ruler_x + tick}" y2="{gy}"/>')
    g.append("</g>")
    parts.extend(g)

    # range rings with bearing ticks, centered off-axis
    cx = float(rng.uniform(0.6, 0.85)) * W
    cy = float(rng.uniform(0.2, 0.5)) * H
    g = [f'<g fill="none" stroke="{hue}" stroke-width="1">']
    for i, r in enumerate(range(140, 1000, 140)):
        op = 0.10 if i % 2 == 0 else 0.055
        g.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r}" stroke-opacity="{op}"/>')
    # bearing ticks every 15 degrees between outer two rings
    r0, r1 = 840, 870
    for deg in range(0, 360, 15):
        a = math.radians(deg)
        x0, y0 = cx + r0 * math.sin(a), cy - r0 * math.cos(a)
        x1, y1 = cx + r1 * math.sin(a), cy - r1 * math.cos(a)
        g.append(f'<line x1="{x0:.0f}" y1="{y0:.0f}" x2="{x1:.0f}" y2="{y1:.0f}" stroke-opacity="0.14"/>')
    # two faint radial bearing lines
    for deg in (float(rng.uniform(190, 250)), float(rng.uniform(100, 160))):
        a = math.radians(deg)
        x1, y1 = cx + 980 * math.sin(a), cy - 980 * math.cos(a)
        g.append(f'<line x1="{cx:.0f}" y1="{cy:.0f}" x2="{x1:.0f}" y2="{y1:.0f}" stroke-opacity="0.06"/>')
    # center mark
    g.append(f'<line x1="{cx - 10:.0f}" y1="{cy:.0f}" x2="{cx + 10:.0f}" y2="{cy:.0f}" stroke-opacity="0.18"/>')
    g.append(f'<line x1="{cx:.0f}" y1="{cy - 10:.0f}" x2="{cx:.0f}" y2="{cy + 10:.0f}" stroke-opacity="0.18"/>')
    g.append("</g>")
    parts.extend(g)

    parts.append("</svg>")
    svg = "\n".join(parts)
    out = OUT / f"bg-{name}.svg"
    out.write_text(svg)
    print(f"{out.name}: {len(svg) // 1024} KB")
