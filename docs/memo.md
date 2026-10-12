# Concentrate or diversify? Portfolio construction for a seed fund

*Investment memo based on the Power Law Lab Monte Carlo simulator. Author: Francesco Moscogiuri.*

## 1. The question

A EUR 120M seed fund must decide how many companies to back. Fewer companies mean higher ownership and more partner time per company. More companies mean a better chance of catching the rare outlier. This memo uses a simulation of 10,000 funds to answer one question:

> How many startups should a seed fund back to give its LPs the best chance of a 3x net return, and does the answer depend on the manager's skill?

## 2. How the model works

- **Startup outcomes.** Each startup falls into one of four outcome bands, based on more than 21,000 financings tracked by Correlation Ventures (2004-2013): 65% return less than 1x, 25% return 1-5x, 6% return 5-10x and 4% return more than 10x. Within each band, multiples are drawn log-uniformly. Half of the losers are written off completely, and home runs are capped at 100x.
- **Fund.** Equal tickets across N startups. The fund multiple (TVPI) is the average of the startup multiples.
- **Fund economics.** 2% annual management fee on committed capital for 10 years, so EUR 96M is invested, and 20% carried interest on profits.
- **Manager skill.** A skilled manager is modelled with 9% home runs and 60% losers, in line with a 2023 survey of 885 European VCs by Vlerick.

## 3. Five findings

**1. A single startup is a bad bet; the average is made by a few outliers.**
The mean multiple of one startup is 2.75x, but the median is only 0.52x and 32% are written off. The top 5% of startups generate about 60% of all value.

**2. Diversification cuts the risk, not the return.**
With an average manager, the gross chance of losing money falls from 38% with 5 startups to about 7% with 30. The expected multiple stays at about 2.75x. The chance of a 3x gross plateaus at about 37% between 30 and 100 startups.

**3. Fees and carry move the bar for LPs.**
A 2.75x gross fund returns 1.96x net to LPs. For a fund of 30 startups, the chance of losing money more than doubles (from 7% to 15%) and the chance of 3x is more than halved (from 36% to 16%). Startups must return 1.25x just for LPs to break even, and about 4.4x for LPs to get 3x.

**4. Timing matters as much as the multiple.**
With capital called in years 1-5 and exits in years 6-12, LPs break even only in year 9. The 1.96x net TVPI translates into a 12.1% IRR, roughly comparable to public equities but locked up for a decade.

**5. The optimal portfolio size depends on skill.**

| Startups | Average manager: P(net ≥ 3x) | Average: P(loss) | Skilled manager: P(net ≥ 3x) | Skilled: P(loss) |
|---|---|---|---|---|
| 15 | 19.9% | 28.2% | 45.5% | 11.5% |
| 30 | 16.1% | 15.6% | 49.1% | 2.8% |
| 100 | 5.2% | 1.9% | 56.6% | 0.0% |

The average manager has the best chance of 3x with about 15 companies, but accepts a 28% chance of losing LP money. The skilled manager's chance of 3x keeps rising with diversification.

## 4. Recommendation

**The rule:** if the expected net multiple is below the target, the fund needs variance, so it concentrates. If the expected multiple is above the target, variance is only risk, so it diversifies.

For a seed fund that can credibly show above-average selection, **a portfolio of 30-50 companies** is the best balance. It captures most of the benefit of diversification (chance of loss below 3%, chance of 3x near 50% in our skilled case) while staying within what a small partnership can realistically source and support.

A manager without an edge should not try to fix it by concentrating. That raises the chance of 3x only from 16% to 20%, and almost doubles the chance of losing money.

## 5. What would change this view

- **Skill does not scale.** The model assumes the same hit rate at any portfolio size. In practice, good deals are scarce and partner time is limited, so the hit rate likely falls as the portfolio grows. This is the main reason not to push beyond about 50 companies.
- **The upside cap.** Raising the home-run cap from 100x to 1000x lifts the mean startup multiple from 2.73x to 9.67x, which is inconsistent with observed fund returns. A power-law (Pareto) tail would be a better model.
- **Data.** Correlation Ventures covers US financings from 2004-2013. The skilled scenario comes from a self-reported survey and is likely optimistic.
- **Simplifications.** No follow-on reserves, no dilution, a flat fee and fixed exit timing. Reserves in particular would let a fund concentrate capital on winners after the first round, which is how many seed funds manage this trade-off in practice.

*Code, data and notebooks: github.com/framosco0/vc-portfolio-simulator*
