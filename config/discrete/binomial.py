import streamlit as st
import torch

BINOMIAL = {
    "params": lambda: {
        "n": st.sidebar.slider("Total Count (n)", 1, 20, 10),
        "p": st.sidebar.slider("Success Probability (p)", 0.0, 1.0, 0.5),
    },
    "dist": lambda p: torch.distributions.Binomial(p["n"], p["p"]),
    "support": lambda p: (0, p["n"]),
}