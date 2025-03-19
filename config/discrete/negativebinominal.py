import streamlit as st
import torch

NEGATIVE_BINOMIAL = {
    "params": lambda: {
        "total_count": st.sidebar.slider("Number of Failures (total_count)", 1, 100, 10, 1),
        "probs": st.sidebar.slider("Success Probability (probs)", 0.01, 0.99, 0.5, 0.01),
    },
    "dist": lambda p: torch.distributions.NegativeBinomial(total_count=p["total_count"], probs=p["probs"]),
    "support": lambda p: (0, None),
}