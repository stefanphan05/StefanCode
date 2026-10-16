#!/usr/bin/env python3
"""Generate a NeetCode progress chart (SVG) and update the README stats.

Counts every problem folder in the repo (anything with a submission-*.* file),
looks up its topic and difficulty in scripts/neetcode_problems.json (the full
NeetCode problem list), and draws assets/progress.svg.

Run from the repo root:  python scripts/update_progress.py
"""
from collections import Counter, OrderedDict
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
DATA = Path(__file__).resolve().parent / "neetcode_problems.json"
SVG_PATH = ROOT / "assets" / "progress.svg"
README = ROOT / "README.md"
SKIP_DIRS = {".git", ".github", "scripts", "assets"}

TOPIC_ORDER = [
    "Arrays & Hashing", "Two Pointers", "Sliding Window", "Stack", "Binary Search",
    "Linked List", "Trees", "Tries", "Heap / Priority Queue", "Backtracking", "Graphs",
    "Advanced Graphs", "1-D Dynamic Programming", "2-D Dynamic Programming", "Greedy",
    "Intervals", "Math & Geometry", "Bit Manipulation", "JavaScript",
]
LISTS = [("neetcode150", "NeetCode 150"), ("blind75", "Blind 75"), ("all", "All NeetCode")]
E, M, H = "Easy", "Medium", "Hard"


def find_solved():
    """Every folder (at any depth) that directly contains a submission file."""
    solved = set()
    for top in ROOT.iterdir():
        if not top.is_dir() or top.name in SKIP_DIRS:
            continue
        for sub in top.rglob("submission-*"):
            if sub.is_file():
                solved.add(sub.parent.name)
    return solved


def compute(problems, solved):
    topic_total = Counter(p["topic"] for p in problems.values())
    topic_done = Counter(problems[s]["topic"] for s in solved if s in problems)
    diff = Counter(problems[s]["difficulty"] for s in solved if s in problems)
    other = sorted(s for s in solved if s not in problems)

    topics = OrderedDict()
    for t in TOPIC_ORDER + sorted(set(topic_total) - set(TOPIC_ORDER)):
        if t not in topic_total:
            continue
        # The JavaScript track is separate from DSA; only show it once started.
        if t == "JavaScript" and not topic_done[t]:
            continue
        topics[t] = (topic_done[t], topic_total[t])

    lists = []
    for key, label in LISTS:
        members = [s for s, p in problems.items() if key == "all" or key in p["lists"]]
        lists.append((label, sum(s in solved for s in members), len(members)))

    return {
        "total": len(solved),
        "topics": topics,
        "diff": diff,
        "other": other,
        "lists": lists,
    }


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


STYLE = """<style>
  .bg{fill:#ffffff;stroke:#d0d7de} .fg{fill:#1f2328} .mu{fill:#656d76} .ln{stroke:#d0d7de}
  .tr{fill:#eaeef2} .fi{fill:#2f81f7} .dn{fill:#1a7f37}
  .e{fill:#1a7f37} .m{fill:#9a6700} .h{fill:#cf222e}
  @media (prefers-color-scheme: dark){
    .bg{fill:#0d1117;stroke:#30363d} .fg{fill:#e6edf3} .mu{fill:#8d96a0} .ln{stroke:#30363d}
    .tr{fill:#21262d} .fi{fill:#4493f8} .dn{fill:#3fb950}
    .e{fill:#3fb950} .m{fill:#d29922} .h{fill:#f85149}}
</style>"""


def bar(out, x, y, w, done, total, h=12):
    out.append(f'<rect class="tr" x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}"/>')
    if done:
        cls = "dn" if done >= total else "fi"
        out.append(f'<rect class="{cls}" x="{x}" y="{y}" '
                   f'width="{max(h, w * min(done, total) / total):.1f}" height="{h}" rx="{h/2}"/>')


def build_svg(s):
    W, pad = 720, 28
    out = []

    # ---- header -------------------------------------------------------------
    out.append(f'<text class="fg" x="{pad}" y="44" font-size="20" font-weight="600">'
               f'NeetCode progress</text>')
    out.append(f'<text class="mu" x="{W-pad}" y="46" font-size="16" text-anchor="end">'
               f'problems solved</text>')
    out.append(f'<text class="fg" x="{W-pad-140}" y="46" font-size="30" font-weight="700" '
               f'text-anchor="end">{s["total"]}</text>')

    # difficulty chips
    x = pad
    for d, cls in ((E, "e"), (M, "m"), (H, "h")):
        out.append(f'<circle class="{cls}" cx="{x+4.5}" cy="73.5" r="4.5"/>')
        txt = f"{d} {s['diff'][d]}"
        out.append(f'<text class="fg" x="{x+15}" y="78" font-size="13">{txt}</text>')
        x += 15 + len(txt) * 7.4 + 22
    if s["other"]:
        out.append(f'<text class="mu" x="{x}" y="78" font-size="13">'
                   f'+{len(s["other"])} not in NeetCode list</text>')

    # ---- milestone lists (three columns) ------------------------------------
    y = 104
    col_gap = 24
    col_w = (W - 2 * pad - 2 * col_gap) / 3
    for i, (label, done, total) in enumerate(s["lists"]):
        cx = pad + i * (col_w + col_gap)
        out.append(f'<text class="fg" x="{cx}" y="{y+12}" font-size="13" font-weight="600">'
                   f'{esc(label)}</text>')
        out.append(f'<text class="mu" x="{cx+col_w:.1f}" y="{y+12}" font-size="13" '
                   f'text-anchor="end">{done}/{total}</text>')
        bar(out, cx, y + 22, round(col_w, 1), done, total, h=10)

    # ---- topics -------------------------------------------------------------
    y = 160
    out.append(f'<line class="ln" x1="{pad}" x2="{W-pad}" y1="{y}" y2="{y}"/>')
    out.append(f'<text class="mu" x="{pad}" y="{y+24}" font-size="12" font-weight="600" '
               f'letter-spacing="0.5">BY TOPIC</text>')
    out.append(f'<text class="mu" x="{W-pad}" y="{y+24}" font-size="12" text-anchor="end">'
               f'solved / in NeetCode</text>')
    label_w, row_h = 190, 26
    bar_x = pad + label_w
    bar_w = W - bar_x - pad - 72
    y += 36
    for name, (done, total) in s["topics"].items():
        out.append(f'<text class="fg" x="{pad}" y="{y+13}" font-size="13">{esc(name)}</text>')
        bar(out, bar_x, y + 3, bar_w, done, total)
        out.append(f'<text class="mu" x="{W-pad}" y="{y+13}" font-size="13" text-anchor="end">'
                   f'{done}/{total}</text>')
        y += row_h

    Ht = y + 18
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{Ht}" '
            f'viewBox="0 0 {W} {Ht}" font-family="-apple-system,BlinkMacSystemFont,'
            f'Segoe UI,Helvetica,Arial,sans-serif">\n{STYLE}\n'
            f'<rect class="bg" x="0.5" y="0.5" width="{W-1}" height="{Ht-1}" rx="10"/>')
    return head + "\n" + "\n".join(out) + "\n</svg>\n"


def update_readme(s):
    start, end = "<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->"
    lists = " · ".join(f"{label} {done}/{total}" for label, done, total in s["lists"])
    block = (f"{start}\n"
             f"### 📊 Progress\n\n"
             f"**{s['total']} problems solved** "
             f"· 🟢 Easy {s['diff'][E]} · 🟡 Medium {s['diff'][M]} · 🔴 Hard {s['diff'][H]}\n\n"
             f"{lists}\n\n"
             "<img src=\"assets/progress.svg\" alt=\"NeetCode progress by topic\" width=\"720\"/>\n\n"
             "<sub>Auto-updated on every push by `scripts/update_progress.py`.</sub>\n"
             f"{end}")
    text = README.read_text(encoding="utf-8")
    if start in text and end in text:
        text = re.sub(re.escape(start) + r".*?" + re.escape(end), lambda _: block, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    README.write_text(text, encoding="utf-8")


def main():
    problems = json.loads(DATA.read_text(encoding="utf-8"))
    s = compute(problems, find_solved())
    SVG_PATH.parent.mkdir(parents=True, exist_ok=True)
    SVG_PATH.write_text(build_svg(s), encoding="utf-8")
    update_readme(s)
    print(f"{s['total']} solved | " + ", ".join(f"{l} {d}/{t}" for l, d, t in s["lists"]))
    if s["other"]:
        print("Not in NeetCode list (counted, no topic):", ", ".join(s["other"]))


if __name__ == "__main__":
    main()
