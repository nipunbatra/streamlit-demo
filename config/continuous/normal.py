import streamlit as st
import torch

NORMAL = {
    "params": lambda: {
        "mu": st.sidebar.slider("Mean (μ)", -10.0, 10.0, 0.0, key="norm_mu"),
        "sigma": st.sidebar.slider("Standard Deviation (σ)", 0.1, 10.0, 1.0, key="norm_sigma"),
    },
    "dist": lambda p: torch.distributions.Normal(p["mu"], p["sigma"]),
    "support": None,
}