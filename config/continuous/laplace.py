import streamlit as st
import torch

LAPLACE = {
    "params": lambda: {
        "mean": st.sidebar.slider("Mean (μ)",  -10.0, 10.0, 0.0),
        "scale": st.sidebar.slider("Scale (λ)", 0.1, 10.0, 1.0),
    },
    "dist": lambda p: torch.distributions.Laplace(p["mean"], p["scale"]),
    "support": None,
}