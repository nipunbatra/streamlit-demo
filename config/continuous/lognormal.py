import streamlit as st
import torch

LOGNORMAL = {
    "params": lambda: {
        "mu": st.sidebar.slider("Log Mean (μ)", -5.0, 5.0, 0.0),
        "sigma": st.sidebar.slider("Log Std Dev (σ)", 0.1, 3.0, 1.0),
    },
    "dist": lambda p: torch.distributions.LogNormal(p["mu"], p["sigma"]),
    "support": lambda p: (0, None),
}