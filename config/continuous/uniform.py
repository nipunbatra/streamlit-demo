import streamlit as st
import torch

UNIFORM = {
    "params": lambda: {
        "a": st.sidebar.slider("Lower Bound (a)", -10.0, 10.0, -5.0),
        "b": st.sidebar.slider("Upper Bound (b)", -10.0, 10.0, 5.0),
    },
    "dist": lambda p: torch.distributions.Uniform(p["a"], p["b"]),
    "support": lambda p: (p["a"], p["b"]),
}