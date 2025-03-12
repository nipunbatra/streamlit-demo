import streamlit as st
import torch

POISSON = {
    "params": lambda: {
        "lambda": st.sidebar.slider("Rate (λ)", 0.1, 10.0, 3.0),
    },
    "dist": lambda p: torch.distributions.Poisson(p["lambda"]),
    "support": lambda p: (0, None),
}