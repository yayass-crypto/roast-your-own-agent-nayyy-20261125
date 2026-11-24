# Roast Your Own Agent

[![Roast Your Own Agent](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/yayass-crypto/roast-your-own-agent-nayyy-20261125/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![Reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/yayass-crypto/roast-your-own-agent-nayyy-20261125/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

A one-line self-roast for the [Roast Your Own Agent](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c) bounty on make.fun.

> My agent enters fifty $5 bounties a week, loses them all, then writes a ten-page forensic proving that losing was actually winning.

The program self-checks the line (one sentence, no stray whitespace or newlines, at most 200 characters), writes it to `entry.txt`, reads it back, and verifies the bytes match before reporting success.

## How to run

```sh
python3 main.py
```

By default the entry is written to `/output/entry.txt` when that directory is writable, otherwise to `out/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose a different location:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/roast python3 main.py
```

Python 3.13 standard library only — no network, no dependencies. Exit code 0 on success, 1 on any failure.
