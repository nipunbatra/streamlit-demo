import streamlit as st
import torch

BETA = {
    "params": lambda: {
        "alpha": st.sidebar.slider("Alpha (α)", 0.1, 10.0, 2.0, 0.1, key="beta_alpha"),
        "beta": st.sidebar.slider("Beta (β)", 0.1, 10.0, 2.0, 0.1, key="beta_beta"),
    },
    "dist": lambda p: torch.distributions.Beta(p["alpha"], p["beta"]),
    "support": lambda p: (0, 1),
}