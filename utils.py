import torch
import streamlit as st
import plotly.graph_objects as go

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
