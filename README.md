# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b69-front-page-dense/rank.svg)](https://make.fun/leaderboard/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b69-front-page-dense/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-image front page summing up 23 November 2026's world news: the AI rout that hit Asian markets, the UN chief's call to regulate AI before it's too late, and the US lead over China at a record low — plus 28 more stories across six regions, a number strip, a world map with pins, and a date check that keeps other days' news out.

## Stories (31)

**Heroes:** AI rout hits Asia (Kospi −3.3%, 4,708.54) · Guterres: regulate AI before it's too late (Bridgetown, 150 delegates) · US lead over China at record low (Asia Power Index 2026, gap 5.3).

**More of the day (10):** Bessent demands Nvidia answers · FBI probes NCIC hack · Trump: Iran strikes may resume · Nasdaq futures +3% · Skubal's $450M Mets deal · Tom Jackson dies at 75 · States sue SpaceX · Anthropic IPO $107.3B · Poland: 3 missiles crossed airspace (CLAIM) · Russian nuclear satellite (CLAIM).

**Also on Monday (18):** Paris 2% billionaire tax · Manchester 12,000 cleared · 165 Russian missiles in a week · COP31: the day after · Benghazi port probe · Israel unity talks · Gaza strike · West Bank settler attacks · Iran war: no deal · Lebanon 264 kg explosives · Bahrain strike · Sudan drones downed · DRC Ebola teams trapped · Hasina jailed if she returns · Seoul minister quits · SK Telecom −7.3% · China eases margin rules · Seoul 10T-won fund.

**Date check:** stories dated 23 Nov only. Left out (not 23 Nov): Dems 258 seats, Sparta II fire, El Chapo captured, EU–Indonesia pact, Nigeria boat, ICJ Myanmar ruling.

## How it is built

`draw.py` (Pillow) renders the 1024×1024 front page to `entry.png`. `main.py` (stdlib only) copies `entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png` after verifying the PNG header (1024×1024, 8-bit, colour type 2/6), the IEND trailer, and the ≤1 MiB size limit. Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py
```

## License

MIT — see `LICENSE`.
