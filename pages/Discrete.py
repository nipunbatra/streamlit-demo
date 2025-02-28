import streamlit as st
import torch
import plotly.graph_objects as go
from config.config_discrete import DISCRETE_DISTRIBUTIONS

st.title("Discrete Distributions")

selected_dist = st.sidebar.selectbox("Choose a Distribution", list(DISCRETE_DISTRIBUTIONS.keys()))
params = DISCRETE_DISTRIBUTIONS[selected_dist]["params"]()
dist = DISCRETE_DISTRIBUTIONS[selected_dist]["dist"](params)
support = DISCRETE_DISTRIBUTIONS[selected_dist].get("support")
support = support(params) if callable(support) else None

if support:
    min_val, max_val = support
    x_range = torch.arange(min_val, max_val + 1 if max_val is not None else 20)
else:
    x_range = torch.arange(0, 20)

pmf = dist.log_prob(x_range).exp()

fig = go.Figure()
fig.add_trace(go.Bar(x=x_range.numpy(), y=pmf.numpy(), name=selected_dist))
st.plotly_chart(fig)
