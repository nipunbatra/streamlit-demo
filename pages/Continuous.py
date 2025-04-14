import streamlit as st
import torch
import plotly.graph_objects as go
from config.continuous import CONTINUOUS_DISTRIBUTIONS
from utils import compute_pdf, plot_pdf, compute_cdf, plot_cdf

st.title("Continuous Distributions")

selected_dist = st.sidebar.selectbox("Choose a Distribution", list(CONTINUOUS_DISTRIBUTIONS.keys()))
params = CONTINUOUS_DISTRIBUTIONS[selected_dist]["params"]()
dist = CONTINUOUS_DISTRIBUTIONS[selected_dist]["dist"](params)
support = CONTINUOUS_DISTRIBUTIONS[selected_dist].get("support")
support = support(params) if callable(support) else None

x_range = torch.linspace(-10, 10, 1000)
pdf = compute_pdf(dist, x_range, support)

plot_pdf(pdf, x_range, selected_dist)
plot_cdf(compute_cdf(dist, x_range, support), x_range, selected_dist)