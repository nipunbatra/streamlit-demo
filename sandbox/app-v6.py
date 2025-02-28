"""
v6: In this version, beyond v5, we will:
- use a selectbox to choose the distribution type amongst: Normal and Uniform
- use a slider to set the parameters of the selected distribution
- display the selected parameters in the sidebar
"""

import streamlit as st
import torch 
import pandas as pd
import plotly.graph_objects as go

st.title('PyTorch Distributions')

# Sidebar for user input
st.sidebar.header("Distribution Parameters")

dist_type = st.sidebar.selectbox("Select Distribution", ["Normal", "Uniform"])
x_range = torch.linspace(-10, 10, 1000)

if dist_type == "Normal":
    mu = st.sidebar.slider('Mean (μ)', -10.0, 10.0, 0.0)
    sigma = st.sidebar.slider('Standard Deviation (σ)', 0.1, 10.0, 1.0)
    dist = torch.distributions.Normal(mu, sigma)
    pdf = dist.log_prob(x_range).exp()
    st.sidebar.markdown("### Selected Parameters")
    st.sidebar.write(f"**Mean (μ):** {mu:.2f}")
    st.sidebar.write(f"**Standard Deviation (σ):** {sigma:.2f}")
    st.sidebar.write(f"**Entropy:** {dist.entropy().item():.2f}")

elif dist_type == "Uniform":
    a = st.sidebar.slider('Lower Bound (a)', -10.0, 10.0, -5.0)
    b = st.sidebar.slider('Upper Bound (b)', -10.0, 10.0, 5.0)
    if a >= b:
        st.sidebar.error("Lower bound must be less than upper bound")
    else:
        dist = torch.distributions.Uniform(a, b)
        x_mask = (x_range >= a) & (x_range <= b)
        pdf = torch.zeros_like(x_range)
        pdf[x_mask] = torch.distributions.Uniform(a, b).log_prob(x_range[x_mask]).exp()
        
        st.sidebar.markdown("### Selected Parameters")
        st.sidebar.write(f"**Lower Bound (a):** {a:.2f}")
        st.sidebar.write(f"**Upper Bound (b):** {b:.2f}")
        st.sidebar.write(f"**Entropy:** {dist.entropy().item():.2f}")

# Main plot area
st.markdown(f'#### Probability Density Function for {dist_type} Distribution')
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_range, y=pdf, mode='lines',
                         name='', hovertemplate='x: %{x:.2f}<br>f(x): %{y:.2f}'))
fig.update_layout(xaxis_title='x', yaxis_title='f(x)', showlegend=False)

st.plotly_chart(fig)
