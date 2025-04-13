import streamlit as st
import torch

def get_uniform_params():
    a = st.sidebar.slider("Lower Bound (a)", -10.0, 10.0, -5.0, key="uniform_a")
    b_min = a + 0.1
    b_max = 12.0  
    b_default = (b_min + b_max) / 2  
    b = st.sidebar.slider("Upper Bound (b)", b_min, b_max, b_default,  key="uniform_b")
    return {"a": a, "b": b}

UNIFORM = {
    "params": get_uniform_params,
    "dist": lambda p: torch.distributions.Uniform(p["a"], p["b"]),
    "support": lambda p: (p["a"], p["b"]),
}
