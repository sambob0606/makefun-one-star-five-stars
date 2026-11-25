# makefun-one-star-five-stars

[![make.fun · u-po-pu-one-star-five-stars-for-the-food-f9166ee7](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/sambob0606/makefun-one-star-five-stars/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/sambob0606/makefun-one-star-five-stars/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

One sentence for make.fun's "One Star, Five Stars for the Food" bounty: an alien tourist gives Earth a one-star review while still complimenting the food. The program writes the sentence to `/output/entry.txt`.

> One star: your gravity bruised all nine of my knees while Earthlings honked in metal boxes for sport, yet your dumplings made my translator render 'home' as a flavor.

Why this line: the grievance is bodily and alien (nine knees bruised by Earth's gravity) and baffled at a human habit (honking in traffic as sport), then the turn lands the food compliment through a translator glitch — "home" rendered as a flavor — so the praise is felt, not merely stated.

## Run it

```sh
python3 main.py
```

It writes the single sentence (166 characters, no trailing newline) to `/output/entry.txt`, reads it back, and verifies the gate (1–200 characters, one sentence) before exiting 0. Standard library only.
