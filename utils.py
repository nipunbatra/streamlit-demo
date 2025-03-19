import scipy.integrate
import torch
import streamlit as st
import plotly.graph_objects as go
import scipy

def compute_pdf(dist, x_range, support):
    pdf = torch.zeros_like(x_range, dtype=torch.float)

    if support:
        min_val, max_val = support
        mask = (x_range >= min_val) if min_val is not None else torch.ones_like(x_range, dtype=torch.bool)
        if max_val is not None:
            mask &= (x_range <= max_val)
    else:
        mask = torch.ones_like(x_range, dtype=torch.bool)

    pdf[mask] = dist.log_prob(x_range[mask]).exp()
    return pdf

def compute_cdf(dist, x_range, support):
    cdf = torch.zeros_like(x_range, dtype=torch.float)

    if support:
        min_val, max_val = support
        mask = (x_range >= min_val) if min_val is not None else torch.ones_like(x_range, dtype=torch.bool)
        if max_val is not None:
            mask &= (x_range <= max_val)
            cdf[x_range < min_val] = 0.0
            cdf[x_range > max_val] = 1.0
    else:
        mask = torch.ones_like(x_range, dtype=torch.bool)

    try:
        cdf[mask] = dist.cdf(x_range[mask])
    except NotImplementedError:
        cdf[mask] = torch.tensor([scipy.integrate.quad(lambda t: dist.log_prob(torch.tensor(t)).exp().item(), support[0], x)[0] for x in x_range[mask]], dtype=torch.float)

    return cdf

def compute_descrete_cdf(pmf, x_range, support):
    cdf = torch.zeros_like(x_range, dtype=torch.float)
    cdf = pmf.cumsum(dim=0)
    return cdf

def plot_pdf(pdf, x_range, dist_name):
    # Main plot area
    st.markdown(f'#### Probability Density Function for {dist_name} Distribution')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_range, y=pdf, mode='lines',
                            name='', hovertemplate='x: %{x:.2f}<br>f(x): %{y:.2f}'))
    fig.update_layout(xaxis_title='x', yaxis_title='f(x)', showlegend=False)

    st.plotly_chart(fig)
    
def plot_pmf(pmf, x_range, dist_name):
    # Main plot area
    st.markdown(f'#### Probability Mass Function for {dist_name} Distribution')
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x_range.tolist(), y=pmf.tolist(),
                         name='', hovertemplate='x: %{x:.2f}<br>p(x): %{y:.2f}'))
    fig.update_layout(xaxis_title='x', yaxis_title='P(x)', showlegend=False)

    st.plotly_chart(fig)

def plot_cdf(cdf, x_range, dist_name):
    # Main plot area
    st.markdown(f'#### Cumulative Distribution Function for {dist_name} Distribution')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_range, y=cdf, mode='lines',
                            name='', hovertemplate='x: %{x:.2f}<br>F(x): %{y:.2f}'))
    fig.update_layout(xaxis_title='x', yaxis_title='F(x)', showlegend=False)

    st.plotly_chart(fig)

def plot_discrete_cdf(cdf, x_range, dist_name):
    # Main plot area
    st.markdown(f'#### Cumulative Distribution Function for {dist_name} Distribution')
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x_range.tolist(), y=cdf.tolist(),
                         name='', hovertemplate='x: %{x:.2f}<br>F(x): %{y:.2f}'))
    fig.update_layout(xaxis_title='x', yaxis_title='F(x)', showlegend=False)

    st.plotly_chart(fig)
