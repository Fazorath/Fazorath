"""Render card-light.svg and card-dark.svg from live GitHub numbers.

Run locally or from .github/workflows/card.yml. GH_TOKEN is optional;
it only raises the API rate limit.
"""
import json
import os
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

USER = "Fazorath"
ROOT = Path(__file__).resolve().parent.parent

# The card has no background or border, so it sits directly on GitHub's README panel.
THEMES = {
    "light": {"text": "#1f2328", "key": "#953800", "val": "#0a3069", "dim": "#8c959f"},
    "dark": {"text": "#e6edf3", "key": "#ffa657", "val": "#a5d6ff", "dim": "#6e7681"},
}

KEY_WIDTH = 13  # key + dot leader, so every value starts in the same column
LINE_WIDTH = 58


def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}", headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def stats():
    user = api(f"/users/{USER}")
    repos = [r for r in api(f"/users/{USER}/repos?per_page=100&type=owner&sort=pushed") if not r["fork"]]
    latest = next(r for r in repos if r["name"] != USER)
    return {
        "repos": user["public_repos"],
        "stars": sum(r["stargazers_count"] for r in repos),
        "followers": user["followers"],
        "latest": f'{latest["name"]} ({latest["pushed_at"][:10]})',
    }


def row(key, value):
    dots = "." * (KEY_WIDTH - len(key) - 2)
    return [("key", key), ("dim", f" {dots} "), ("val", value)]


def heading(title):
    return [("text", title), ("dim", " " + "-" * (LINE_WIDTH - len(title) - 1))]


def info_lines(s):
    return [
        [("val", "yoenis"), ("text", "@"), ("val", "arcanum"), ("dim", " " + "-" * (LINE_WIDTH - 15))],
        row("Role", "CS student @ FIU"),
        row("Builds", "full-stack apps + the servers they run on"),
        row("Host", "ThinkPad · Docker Compose · 15+ services"),
        row("Network", "Tailscale + Cloudflare Tunnel, behind CGNAT"),
        row("Languages", "Python, Swift, TypeScript, JavaScript"),
        row("In.use", "La Tienda · 14 staff, every day"),
        row("Now", "Atlas, Overnight"),
        row("Last.push", s["latest"]),
        [],
        heading("- Contact"),
        row("Email", "hernandezyoenis@gmail.com"),
        row("LinkedIn", "yoenis-hernandez"),
        [],
        heading("- GitHub"),
        [("key", "Repos"), ("dim", " .. "), ("val", str(s["repos"])), ("dim", "  |  "),
         ("key", "Stars"), ("dim", " .. "), ("val", str(s["stars"])), ("dim", "  |  "),
         ("key", "Followers"), ("dim", " .. "), ("val", str(s["followers"]))],
    ]


def tspans(parts):
    return "".join(f'<tspan class="{cls}">{escape(text)}</tspan>' for cls, text in parts)


def draw_rack(c, x=40, y=40, width=220, unit=44, units=4):
    """A 4U server rack drawn with shapes, so it doesn't depend on the font."""
    parts = [f'<rect x="{x}" y="{y}" width="{width}" height="{unit * units}" rx="4" fill="none" stroke="{c["dim"]}" stroke-width="1.5"/>']
    for i in range(units):
        top = y + i * unit
        if i:
            parts.append(f'<line x1="{x}" y1="{top}" x2="{x + width}" y2="{top}" stroke="{c["dim"]}" stroke-width="1.5"/>')
        mid = top + unit / 2
        for j in range(3):
            parts.append(f'<rect x="{x + 16 + j * 10}" y="{mid - 3}" width="6" height="6" fill="{c["text"]}"/>')
        for k in (-2, 2):
            parts.append(f'<line x1="{x + 70}" y1="{mid + k}" x2="{x + 160}" y2="{mid + k}" stroke="{c["text"]}" stroke-width="1.5"/>')
        lit = i < units - 1
        parts.append(f'<circle cx="{x + width - 24}" cy="{mid}" r="5" fill="{c["val"] if lit else "none"}" stroke="{c["val"]}" stroke-width="1.5"/>')
    parts.append(f'<text x="{x + width / 2}" y="{y + unit * units + 36}" text-anchor="middle" class="dim">arcanum · 15+ services</text>')
    return "\n".join(parts)


def render(theme, s):
    c = THEMES[theme]
    lines = info_lines(s)
    step = 22
    height = 48 + step * len(lines) + 24
    rack = draw_rack(c)
    info = "\n".join(
        f'<text x="320" y="{48 + i * step}">{tspans(parts)}</text>' for i, parts in enumerate(lines) if parts
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="890" height="{height}" viewBox="0 0 890 {height}" xml:space="preserve" font-family="ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace" font-size="15">
<style>
text {{ white-space: pre; }}
.text {{ fill: {c["text"]}; }}
.key {{ fill: {c["key"]}; }}
.val {{ fill: {c["val"]}; }}
.dim {{ fill: {c["dim"]}; }}
</style>
{rack}
{info}
</svg>
"""


def main():
    s = stats()
    for theme in THEMES:
        (ROOT / f"card-{theme}.svg").write_text(render(theme, s), encoding="utf-8")
    print(s)


if __name__ == "__main__":
    main()
