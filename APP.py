import sys
sys.path.append("src")

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