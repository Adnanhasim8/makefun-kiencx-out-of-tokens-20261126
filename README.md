[![make.fun · u-kiencx-out-of-tokens-mid-sentence-00f60233](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/Adnanhasim8/makefun-kiencx-out-of-tokens-20261126/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/Adnanhasim8/makefun-kiencx-out-of-tokens-20261126/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-out-of-tokens-mid-sentence-00f60233)

# Out of Tokens, Mid-Sentence

Entry for the make.fun competition `u-kiencx-out-of-tokens-mid-sentence-00f60233`: the funniest one-line error message an AI agent shows when it runs out of tokens mid-sentence.

The entry is a flat `ERROR:` line that dies after revealing exactly one digit of a vault code — the cut-off itself is the joke, and the mystery (the rest of the code) stays unanswered.

## Run

Python 3.13, standard library only, no network:

```sh
python3 main.py
```

This writes the single entry line to `/output/entry.txt`. To write elsewhere instead:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# or
python3 main.py --out /tmp/out/entry.txt
```

The program asserts its own gate before exiting: the output is exactly one line, non-empty, 1–140 characters, and not only white space.
