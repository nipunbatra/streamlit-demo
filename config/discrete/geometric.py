import streamlit as st
import torch

GEOMETRIC = {
    "params": lambda: {
        "p": st.sidebar.slider("Success Probability (p)", 0.01, 0.99, 0.5, 0.01),
    },
    "dist": lambda p: torch.distributions.Geometric(p["p"]),
    "support": lambda p: (0, None),
}