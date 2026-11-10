"""Recolor the generated profile-summary cards to the red palette.
Reads profile-summary-card-output/radical/*.svg, writes assets/cards/*.svg."""
import re, pathlib

SRC = pathlib.Path("profile-summary-card-output/radical")
DST = pathlib.Path("assets/cards")
CARDS = {"4-productive-time.svg": "productive-time.svg",
         "2-most-commit-language.svg": "top-languages.svg"}

FIXED = {"#141321": "#0a0507",   # card background
         "#fe428e": "#ff3b3b",   # title
         "#ae81ff": "#cc0000",   # bars
         "#a9fef7": "#ffb3b3"}   # axis / text
RAMP = ["#ff3b3b", "#ff8a5c", "#cc0000", "#ffb3a0", "#8b0000", "#e64a19"]  # language colours

DST.mkdir(parents=True, exist_ok=True)
for src, dst in CARDS.items():
    s = (SRC / src).read_text(encoding="utf-8")
    seen = {}
    def swap(m):
        c = m.group(0).lower()
        if c in FIXED: return FIXED[c]
        if c not in seen: seen[c] = RAMP[len(seen) % len(RAMP)]
        return seen[c]
    out = re.sub(r"#[0-9a-fA-F]{6}\b", swap, s)
    (DST / dst).write_text(out, encoding="utf-8")
    print("wrote", DST / dst)
