import streamlit as st
import torch

CATEGORICAL = {
    "params": lambda: {
        "probs": st.sidebar.text_input("Probabilities (comma-separated)", "0.1,0.2,0.3,0.4"),
    },
    "dist": lambda p: torch.distributions.Categorical(torch.tensor([float(x) for x in p["probs"].split(',')])),
    "support": lambda p: (0, len(p["probs"].split(',')) - 1),
}