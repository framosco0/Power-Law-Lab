import numpy as np

# Cumulative thresholds: loss, small, good (home_run is the rest)
SCENARIOS = {
    "base":    (0.65, 0.90, 0.96),   # average manager (Correlation Ventures)
    "skilled": (0.60, 0.85, 0.91),   # skilled manager (9% home runs, Vlerick)
}

rng = np.random.default_rng(42)
WRITE_OFF_SHARE = 0.5
HOME_RUN_CAP = 100


FUND_SIZE = 120      # committed capital, EUR M
FEE_RATE = 0.02      # annual management fee
FEE_YEARS = 10       # fee period
CARRY = 0.20         # share of profits to the GP


def pick_bucket(u, scenario = "base"):
    t1, t2, t3 = SCENARIOS[scenario]
    
    if u<t1:
        return "loss"
    elif u<t2:
        return "small"
    elif u<t3:
        return "good"
    else:
        return "home_run"

def draw_multiple(bucket):

    v = rng.random()                      # second random number between 0 and 1
    if bucket == "loss":
        if rng.random() < WRITE_OFF_SHARE:
            return 0.0                    # total failure
        return v                          # recover a portion between 0 and 1x
    if bucket == "small":
        lo, hi = 1, 5
    elif bucket == "good":
        lo, hi = 5, 10
    else:
        lo, hi = 10, HOME_RUN_CAP
    return lo * (hi / lo) ** v 

def draw_outcome(scenario = "base"):
# NEW
    bucket = pick_bucket(rng.random(), scenario)    # 1. Range
#NEW    
    return draw_multiple(bucket)          # 2. Return


def net_tvpi(gross_multiple):
    fees = FEE_RATE * FUND_SIZE * FEE_YEARS                                   # total fees, EUR M
    invested = FUND_SIZE - fees                  # capital actually invested
    returned = gross_multiple * invested                               # cash returned by startups
    profit = max(returned - FUND_SIZE, 0)        # no carry if the fund loses money
    to_lps = returned - CARRY * profit                      # subtract carry
    return to_lps / FUND_SIZE


def simulate_fund(n_startups, scenario = "base"):
    multiples = []

    for i in range(n_startups):
        multiples.append(draw_outcome(scenario))

    return np.mean(multiples)

