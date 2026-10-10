import numpy as np

rng = np.random.default_rng(42)
WRITE_OFF_SHARE = 0.5

def pick_bucket(u):

    if u<0.65:
        return "loss"
    elif 0.65<=u<0.90:
        return "small"
    elif 0.90<=u<0.96:
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
        lo, hi = 10, 100
    return lo * (hi / lo) ** v 

def draw_outcome():

    bucket = pick_bucket(rng.random())    # 1. Range
    return draw_multiple(bucket)          # 2. Return