import sys
sys.path.append("src")

import pandas as pd
import numpy as np
import streamlit as st
from outcomes import simulate_fund, net_tvpi

st.title("Power Law Lab")
st.write("How many startups does a VC fund need?")

n = st.slider("Startups per fund", min_value=5, max_value=200, value=30)

scenario = st.radio("Manager", ["base", "skilled"], horizontal=True)

funds = np.array([net_tvpi(simulate_fund(n, scenario)) for _ in range(2000)])

st.metric("Mean net TVPI", f"{funds.mean():.2f}x")
st.metric("P(losing money)", f"{(funds < 1).mean():.0%}")
st.metric("P(net ≥ 3x)", f"{(funds >= 3).mean():.0%}")

@st.cache_data
def p3x_by_size(scenario):
    sizes = [5, 10, 15, 30, 50, 100, 200]
    probs = []
    for s in sizes:
        funds = np.array([net_tvpi(simulate_fund(s, scenario)) for _ in range(1000)])
        probs.append((funds >= 3).mean())
    return pd.DataFrame({"P(net ≥ 3x)": probs}, index=sizes)

st.subheader("Chance of 3x net by portfolio size")
st.line_chart(p3x_by_size(scenario))