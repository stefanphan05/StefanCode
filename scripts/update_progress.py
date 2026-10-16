#!/usr/bin/env python3
"""Update the progress section of README.md with NeetCode stats.

Counts every problem folder in the repo (anything with a submission-* file),
looks up its topic and difficulty in scripts/neetcode_problems.json (the full
NeetCode problem list), and writes Markdown tables between the
<!-- PROGRESS:START --> and <!-- PROGRESS:END --> markers in README.md.

Run from the repo root:  python scripts/update_progress.py
"""
from collections import Counter, OrderedDict
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
DATA = Path(__file__).resolve().parent / "neetcode_problems.json"
README = ROOT / "README.md"
SKIP_DIRS = {".git", ".github", "scripts", "assets"}

TOPIC_ORDER = [
    "Arrays & Hashing", "Two Pointers", "Sliding Window", "Stack", "Binary Search",
    "Linked List", "Trees", "Tries", "Heap / Priority Queue", "Backtracking", "Graphs",
    "Advanced Graphs", "1-D Dynamic Programming", "2-D Dynamic Programming", "Greedy",
    "Intervals", "Math & Geometry", "Bit Manipulation", "JavaScript",
]
LISTS = [
    ("blind75", "Blind 75"),
    ("neetcode150", "NeetCode 150"),
    ("neetcode250", "NeetCode 250"),
    ("all", "NeetCode All"),
]
E, M, H = "Easy", "Medium", "Hard"
BAR_WIDTH = 20


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
    diff_done = Counter(problems[s]["difficulty"] for s in solved if s in problems)
    diff_total = Counter(p["difficulty"] for p in problems.values())
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
        "diff": [(d, diff_done[d], diff_total[d]) for d in (E, M, H)],
        "other": other,
        "lists": lists,
    }


def bar(done, total):
    filled = round(BAR_WIDTH * done / total) if total else 0
    if done and not filled:
        filled = 1  # show a sliver for any progress
    return "`" + "█" * filled + "░" * (BAR_WIDTH - filled) + "`"


def pct(done, total):
    return f"{done / total:.0%}" if total else "–"


def build_markdown(s):
    icons = {E: "🟢", M: "🟡", H: "🔴"}
    lines = [
        "### 📊 Progress",
        "",
        f"**{s['total']} problems solved** · "
        + " · ".join(f"{icons[d]} {d} {done} / {total}" for d, done, total in s["diff"]),
        "",
        "| List | Progress | Solved | |",
        "| :-- | :-- | --: | --: |",
    ]
    for label, done, total in s["lists"]:
        lines.append(f"| **{label}** | {bar(done, total)} | {done} / {total} | {pct(done, total)} |")

    lines += [
        "",
        "<details open>",
        "<summary><b>By topic</b></summary>",
        "",
        "| Topic | Progress | Solved |",
        "| :-- | :-- | --: |",
    ]
    for name, (done, total) in s["topics"].items():
        mark = " ✅" if done and done >= total else ""
        lines.append(f"| {name}{mark} | {bar(done, total)} | {done} / {total} |")
    lines += ["", "</details>"]

    if s["other"]:
        lines += ["", f"<sub>+ {len(s['other'])} solved problem(s) not in the NeetCode list: "
                      + ", ".join(s["other"]) + "</sub>"]
    lines += ["", "<sub>Auto-updated on every push by `scripts/update_progress.py`.</sub>"]
    return "\n".join(lines)


def update_readme(s):
    start, end = "<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->"
    block = f"{start}\n{build_markdown(s)}\n{end}"
    text = README.read_text(encoding="utf-8")
    if start in text and end in text:
        text = re.sub(re.escape(start) + r".*?" + re.escape(end), lambda _: block, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    README.write_text(text, encoding="utf-8")


def main():
    problems = json.loads(DATA.read_text(encoding="utf-8"))
    s = compute(problems, find_solved())
    update_readme(s)
    print(f"{s['total']} solved | " + ", ".join(f"{l} {d}/{t}" for l, d, t in s["lists"]))
    if s["other"]:
        print("Not in NeetCode list (counted, no topic):", ", ".join(s["other"]))


if __name__ == "__main__":
    main()
