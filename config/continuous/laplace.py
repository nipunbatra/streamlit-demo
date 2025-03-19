import streamlit as st
import torch

LAPLACE = {
    "params": lambda: {
        "loc": st.sidebar.slider("Location (μ)", -10.0, 10.0, 0.0, 0.1),
        "scale": st.sidebar.slider("Scale (b)", 0.1, 5.0, 1.0, 0.1),
    },
    "dist": lambda p: torch.distributions.Laplace(p["loc"], p["scale"]),
    "support": lambda p: (None, None),
}