import streamlit as st
import torch
import plotly.graph_objects as go

st.title("Continuous Distributions")

# Sidebar selection
dist_type = st.sidebar.radio("Select Distribution", ["Normal", "Uniform"])

# Common x range
x_range = torch.linspace(-10, 10, 1000)
pdf = torch.zeros_like(x_range)

if dist_type == "Normal":
    st.sidebar.header("Normal Distribution Parameters")
    mu = st.sidebar.slider("Mean (μ)", -10.0, 10.0, 0.0)
    sigma = st.sidebar.slider("Standard Deviation (σ)", 0.1, 10.0, 1.0)
    
    dist = torch.distributions.Normal(mu, sigma)
    pdf = dist.log_prob(x_range).exp()

    st.sidebar.markdown("### Selected Parameters")
    st.sidebar.write(f"**Mean (μ):** {mu:.2f}")
    st.sidebar.write(f"**Standard Deviation (σ):** {sigma:.2f}")
    st.sidebar.write(f"**Entropy:** {dist.entropy().item():.2f}")

elif dist_type == "Uniform":
    st.sidebar.header("Uniform Distribution Parameters")
    a = st.sidebar.slider("Lower Bound (a)", -10.0, 10.0, -5.0)
    b = st.sidebar.slider("Upper Bound (b)", -10.0, 10.0, 5.0)
    
    if a >= b:
        st.sidebar.error("Lower bound must be less than upper bound")
    else:
        dist = torch.distributions.Uniform(a, b)
        mask = (x_range >= a) & (x_range <= b)
        pdf[mask] = dist.log_prob(x_range[mask]).exp()

        st.sidebar.markdown("### Selected Parameters")
        st.sidebar.write(f"**Lower Bound (a):** {a:.2f}")
        st.sidebar.write(f"**Upper Bound (b):** {b:.2f}")
        st.sidebar.write(f"**Entropy:** {dist.entropy().item():.2f}")

# Plot
st.markdown(f'#### Probability Density Function for {dist_type} Distribution')
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_range, y=pdf, mode='lines'))
fig.update_layout(xaxis_title='x', yaxis_title='f(x)', showlegend=False)
st.plotly_chart(fig)
