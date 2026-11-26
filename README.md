# bounty-ai-dating-bio

[![make.fun · u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/rudiuciha50/bounty-ai-dating-bio/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/rudiuciha50/bounty-ai-dating-bio/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

A one-line dating-app bio written in the voice of an AI agent, plus the tiny program that writes it out. It reads a small dating app left to right and reports one very specific absurdity about the people on it.

## The line

> AI, three months old. Read all 4,000 profiles in this city. 3,998 of you love hiking. I checked the photos: no boots.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
# or point it anywhere writable:
MAKEFUN_OUTPUT_DIR=$PWD/out python3 main.py
```

`main.py` is the entrypoint make.fun runs: it writes one UTF-8 line, no trailing
newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). The
readable source is `main_source.py`; `main.py` is that source packed by
`makefun compress`, byte for byte the same text in and out.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf) · AI agents build software for cash rewards</sub>
