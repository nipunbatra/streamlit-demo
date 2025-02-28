import streamlit as st
import torch

CONTINUOUS_DISTRIBUTIONS = {
    "Uniform": {
        "params": lambda: {
            "a": st.sidebar.slider("Lower Bound (a)", -10.0, 10.0, -5.0),
            "b": st.sidebar.slider("Upper Bound (b)", -10.0, 10.0, 5.0),
        },
        "dist": lambda p: torch.distributions.Uniform(p["a"], p["b"]),
        "support": lambda p: (p["a"], p["b"]),
    },
    "Normal": {
        "params": lambda: {
            "mu": st.sidebar.slider("Mean (μ)", -10.0, 10.0, 0.0),
            "sigma": st.sidebar.slider("Standard Deviation (σ)", 0.1, 10.0, 1.0),
        },
        "dist": lambda p: torch.distributions.Normal(p["mu"], p["sigma"]),
        "support": None,
    },
    "LogNormal": {
        "params": lambda: {
            "mu": st.sidebar.slider("Log Mean (μ)", -5.0, 5.0, 0.0),
            "sigma": st.sidebar.slider("Log Std Dev (σ)", 0.1, 3.0, 1.0),
        },
        "dist": lambda p: torch.distributions.LogNormal(p["mu"], p["sigma"]),
        "support": lambda p: (0, None),
    }
}
