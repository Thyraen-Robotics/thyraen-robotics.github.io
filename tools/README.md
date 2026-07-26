# Tools

Generators for the site's visual assets. Both are deterministic — re-running
them without changing parameters reproduces the committed assets exactly.

## gen_backgrounds.py

Generates the tactical plotting-grid hero backgrounds
(`static/images/backgrounds/bg-{home,operate,connect,build}.svg`):
minor/major grid, crosshair intersections, ruler ticks, and range rings with
bearing ticks, tinted per product group. Requires only Python 3 + numpy.

```bash
python3 tools/gen_backgrounds.py
```

Per-variant seed and hue live in the `VARIANTS` dict at the top.

## og-card.html

Source for the OpenGraph share card (`static/images/og-card.png`). To
regenerate: serve the repo root, open the page at 1200x630, and screenshot it.

```bash
python3 -m http.server 8123   # from the repo root
# then screenshot http://127.0.0.1:8123/tools/og-card.html at 1200x630
```
