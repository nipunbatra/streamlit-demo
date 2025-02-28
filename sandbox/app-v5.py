"""
v5: In this version, beyond v4, we will:
- only be using plotly
- add a sidebar for capturing user input and right side for displaying the plot
"""

import streamlit as st
import torch 
import pandas as pd
import plotly.graph_objects as go

st.title('PyTorch Distributions')

# Sidebar for user input
st.sidebar.header("Distribution Parameters")
mu = st.sidebar.slider('Mean (\u03BC)', -10.0, 10.0, 0.0)
sigma = st.sidebar.slider('Standard Deviation (\u03C3)', 0.1, 10.0, 1.0)

normal_dist = torch.distributions.Normal(mu, sigma)

x_range = torch.linspace(-10, 10, 1000)
pdf = normal_dist.log_prob(x_range).exp()

st.sidebar.markdown("### Selected Parameters")
st.sidebar.write(f"**Mean (\u03BC):** {mu:.2f}")
st.sidebar.write(f"**Standard Deviation (\u03C3):** {sigma:.2f}")
st.sidebar.write(f"**Variance:** {sigma**2:.4f}")
st.sidebar.write(f"**Entropy:** {normal_dist.entropy().item():.4f}")

# Main plot area
st.markdown('#### Probability Density Function')
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_range, y=pdf, mode='lines',
                         name='', hovertemplate='x: %{x:.4f}<br>f(x): %{y:.4f}'))
fig.update_layout(xaxis_title='x', yaxis_title='f(x)', showlegend=False)

st.plotly_chart(fig)
