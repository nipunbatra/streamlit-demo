import streamlit as st
import torch

EXPONENTIAL = {
    "params": lambda: {
        "rate": st.sidebar.slider("Rate (λ)", 0.1, 5.0, 1.0, 0.1, key="exp_rate"),
    },
    "dist": lambda p: torch.distributions.Exponential(p["rate"]),
    "support": lambda p: (0, None),
}