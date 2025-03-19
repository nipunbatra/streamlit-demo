import streamlit as st
import torch

def get_uniform_params():
    b = st.sidebar.slider("Upper Bound (b)", -10.0, 10.0, 5.0)
    a_min = -10.0  
    a = st.sidebar.slider("Lower Bound (a)", a_min, b, max(a_min, b-0.01))
    return {"a": a, "b": b}

UNIFORM = {
    "params": get_uniform_params,
    "dist": lambda p: torch.distributions.Uniform(p["a"], p["b"]),
    "support": lambda p: (p["a"], p["b"]),
}