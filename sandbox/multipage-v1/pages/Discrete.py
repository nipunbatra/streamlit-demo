import streamlit as st
import torch
import plotly.graph_objects as go

st.title("Discrete Distributions")

# Sidebar selection
dist_type = st.sidebar.radio("Select Distribution", ["Poisson", "Binomial"])

# Common x range for discrete distributions
x_range = torch.arange(0, 20, 1)
pmf = torch.zeros_like(x_range, dtype=torch.float)

if dist_type == "Poisson":
    st.sidebar.header("Poisson Distribution Parameters")
    lambda_ = st.sidebar.slider("Rate (λ)", 0.1, 10.0, 3.0)
    
    dist = torch.distributions.Poisson(lambda_)
    pmf = torch.exp(dist.log_prob(x_range))

    st.sidebar.markdown("### Selected Parameters")
    st.sidebar.write(f"**Rate (λ):** {lambda_:.2f}")
    st.sidebar.write(f"**Mean:** {dist.mean.item():.2f}")
    st.sidebar.write(f"**Variance:** {dist.variance.item():.2f}")

elif dist_type == "Binomial":
    st.sidebar.header("Binomial Distribution Parameters")
    n = st.sidebar.slider("Number of Trials (n)", 1, 20, 10)
    p = st.sidebar.slider("Success Probability (p)", 0.01, 1.0, 0.5)
    
    dist = torch.distributions.Binomial(n, torch.tensor(p))
    
    # Adjust x_range to be within [0, n]
    x_range = torch.arange(0, n + 1)  
    pmf = torch.exp(dist.log_prob(x_range))

    st.sidebar.markdown("### Selected Parameters")
    st.sidebar.write(f"**Trials (n):** {n}")
    st.sidebar.write(f"**Probability (p):** {p:.2f}")
    st.sidebar.write(f"**Mean:** {dist.mean.item():.2f}")
    st.sidebar.write(f"**Variance:** {dist.variance.item():.2f}")

# Plot
st.markdown(f'#### Probability Mass Function for {dist_type} Distribution')
fig = go.Figure()
fig.add_trace(go.Bar(x=x_range.tolist(), y=pmf.tolist()))
fig.update_layout(xaxis_title='x', yaxis_title='P(x)', showlegend=False)
st.plotly_chart(fig)
