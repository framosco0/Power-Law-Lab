# Power Law Lab: how many bets does a VC fund need?

A Monte Carlo model that plays the same venture capital fund 10,000 times to answer one question:
**how should a €120M fund build its portfolio to maximise the chance of returning 3x to its investors, net of costs?**

> Work in progress: I'm building it one phase at a time, and each phase lands as its own commit.

## Roadmap

- [ ] Phase 1: outcome of a single startup (power-law distribution from Correlation Ventures data)
- [ ] Phase 2: portfolio size vs risk and return
- [ ] Phase 3: fund economics (management fees, follow-on reserves, dilution, carry) to go from gross to net
- [ ] Phase 4: timing (J-curve, IRR, DPI)
- [ ] Phase 5: strategy comparison and a 2-page memo
- [ ] Phase 6: interactive Streamlit app

## Data and assumptions

Every input of the model is in [`data/outcome_buckets.csv`](data/outcome_buckets.csv), with its source. The model runs under two scenarios.

### Base scenario: Correlation Ventures

Correlation Ventures analysed more than 21,000 venture financings between 2004 and 2013 ([Seth Levine, 2014](https://sethlevine.com/archives/2014/08/venture-outcomes-are-even-more-skewed-than-you-think.html)). It is the most widely cited dataset on venture outcomes, and an update published in 2019 shows almost the same picture: nearly two thirds of financings still lose money and fewer than 4% return more than 10x ([Seth Levine, 2019](https://sethlevine.com/archives/2019/09/the-markets-are-great-but-venture-outcomes-havent-changed-much.html)).

| Outcome | Probability | How it is obtained |
|---|---|---|
| Below 1x | 65% | Stated in the source |
| 1x–5x | 25% | Derived: 35% at or above 1x, minus 10% at 5x or more |
| 5x–10x | 6% | Derived: 10% at 5x or more, minus 4% above 10x |
| Above 10x | 4% | Stated in the source |

### Optimistic scenario: European survey

A 2023 survey of 885 European venture capitalists by Vlerick Business School and seven other business schools found that 9% of investments return more than 10x ([Vlerick, 2023](https://www.vlerick.com/en/insights/45-per-cent-of-european-venture-capital-investments-fail-or-do-not-secure-high-returns/)). The survey does not report the other buckets, so I keep the base scenario and change two numbers:

- **Above 10x:** 9% instead of 4%, from the survey.
- **Below 1x:** 60% instead of 65%. This is my assumption, so that probabilities still add up to 100%.

### Limits

- **Old data.** The base dataset ends in 2013; the 2019 update suggests the shape of the distribution has not changed much.
- **Financings, not companies.** Correlation counts each round separately, so one company can appear more than once.
- **Mostly US data.** It may not describe European funds today.
- **The survey is self-reported.** Investors answering a questionnaire tend to be optimistic, which is why it is the optimistic scenario and not the base case.
- **Ranges inside each bucket are my choice.** In particular, the 100x cap on the top bucket is a placeholder that I revisit in the next step.


## Author

Francesco Moscogiuri, Finance MSc at Nova SBE. [LinkedIn](linkedin.com/in/francesco-moscogiuri) · [Southern Signals](https://francescomoscogiuri.substack.com/?utm_campaign=profile_chips)
