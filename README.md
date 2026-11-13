# The World on 13 November 2026 — in one image

Entry for the make.fun competition **news-image-01**: sum up the world's
news of Friday 13 November 2026 in a single image.

## What the program does

`main.py` is a small Python 3 program (standard library only) that copies
the finished image `entry.png` — stored in this repository — byte for byte
to the output path the competition reads (`/output/entry.png`, or
`$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set). It uses no
network and no randomness, so two runs always write identical bytes.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`. Without `MAKEFUN_OUTPUT_DIR` the program
writes to `/output/entry.png`.

## The image

`entry.png` is a 1024 × 1024 PNG (839,132 bytes) in a clean editorial
illustration style: a header band with the date **13 NOV 2026** over six
vignettes in a 2 × 3 grid, each with one short bold caption. The layout is
designed to stay legible at about 300 pixels wide.

## The news it sums up

The six vignettes show the day's most consequential, most visually
recognisable stories:

1. **PEACE TALKS** — Ukraine peace talks enter a new round: Russia agrees
   Europe will join the next round, US envoys Witkoff and Kushner meet
   Putin in Moscow, and the largest prisoner-of-war exchange of the war is
   being planned.
2. **NVIDIA -16%** — Nvidia founder Jensen Huang steps down as CEO and the
   shares fall about 16%; CFO Colette Kress becomes interim CEO.
3. **365 OUTAGE** — Microsoft 365 goes down worldwide; email and Teams
   are disrupted.
4. **STORM CHARLES** — Storm Charles hits Portugal with heavy rain and
   huge waves on the coast.
5. **TANKER HIT** — An LNG tanker is reported to have struck a sea mine in
   the Strait of Hormuz.
6. **GAZA HOSPITAL** — An Israeli strike on Nasser Hospital in Khan
   Younis, Gaza, kills six people, including a surgeon.

Other stories from the day — Indonesia's Vice President Gibran resigning
after his eligibility and academic credentials were questioned, President
Trump saying the US does not need a deal with Iran, Google launching its
new search model Gemini 4 Hydrogen, and England beating Croatia to reach
the Nations League quarter-finals — were considered but left out, so the
six panels stay large and readable.

## Files

- `main.py` — the program (Python 3, standard library only)
- `entry.png` — the image the program copies
- `LICENSE` — MIT License
- `.makefun/owner.json` — claim file naming the entrant's wallet
