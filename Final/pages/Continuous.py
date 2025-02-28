import streamlit as st
import torch
import plotly.graph_objects as go
from config.config_continuous import CONTINUOUS_DISTRIBUTIONS
from utils import compute_pdf

st.title("Continuous Distributions")

selected_dist = st.sidebar.selectbox("Choose a Distribution", list(CONTINUOUS_DISTRIBUTIONS.keys()))
params = CONTINUOUS_DISTRIBUTIONS[selected_dist]["params"]()
dist = CONTINUOUS_DISTRIBUTIONS[selected_dist]["dist"](params)
support = CONTINUOUS_DISTRIBUTIONS[selected_dist].get("support")
support = support(params) if callable(support) else None

x_range = torch.linspace(-10, 10, 1000)
pdf = compute_pdf(dist, x_range, support)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x_range.numpy(), y=pdf.numpy(), mode="lines", name=selected_dist))
st.plotly_chart(fig)
