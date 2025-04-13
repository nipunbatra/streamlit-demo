import streamlit as st
import torch
import plotly.graph_objects as go
from config.continuous import CONTINUOUS_DISTRIBUTIONS
from config.discrete import DISCRETE_DISTRIBUTIONS
from utils import compute_pdf, plot_pdf, plot_pmf

st.title("Compare Two Distributions")

dist_type = st.sidebar.radio("Select Distribution Type", ["Continuous", "Discrete"])

if dist_type == "Continuous":
    available_distributions = CONTINUOUS_DISTRIBUTIONS
    plot_title = "Probability Density Function (PDF)"
elif dist_type == "Discrete":
    available_distributions = DISCRETE_DISTRIBUTIONS
    plot_title = "Probability Mass Function (PMF)"

#first distribution
selected_dist_1 = st.sidebar.selectbox("Choose First Distribution", list(available_distributions.keys()))
params_1 = available_distributions[selected_dist_1]["params"]()
dist_1 = available_distributions[selected_dist_1]["dist"](params_1)
support_1 = available_distributions[selected_dist_1].get("support")
support_1 = support_1(params_1) if callable(support_1) else None

#second distribution
available_distributions_2 = [d for d in available_distributions.keys() if d != selected_dist_1]
selected_dist_2 = st.sidebar.selectbox("Choose Second Distribution", available_distributions_2)
params_2 = available_distributions[selected_dist_2]["params"]()
dist_2 = available_distributions[selected_dist_2]["dist"](params_2)
support_2 = available_distributions[selected_dist_2].get("support")
support_2 = support_2(params_2) if callable(support_2) else None

fig = go.Figure()

if dist_type == "Continuous":
    x_range = torch.linspace(-10, 10, 1000)
    pdf_1 = compute_pdf(dist_1, x_range, support_1)
    pdf_2 = compute_pdf(dist_2, x_range, support_2)

    fig.add_trace(go.Scatter(x=x_range.numpy(), y=pdf_1.numpy(), mode="lines", name=selected_dist_1))
    fig.add_trace(go.Scatter(x=x_range.numpy(), y=pdf_2.numpy(), mode="lines", name=selected_dist_2))

else:  
    if support_1:
        min_val_1, max_val_1 = support_1
        x_range_1 = torch.arange(min_val_1, max_val_1 + 1 if max_val_1 is not None else 20)
    else:
        x_range_1 = torch.arange(0, 20)

    if support_2:
        min_val_2, max_val_2 = support_2
        x_range_2 = torch.arange(min_val_2, max_val_2 + 1 if max_val_2 is not None else 20)
    else:
        x_range_2 = torch.arange(0, 20)

    pmf_1 = dist_1.log_prob(x_range_1).exp()
    pmf_2 = dist_2.log_prob(x_range_2).exp()

    fig.add_trace(go.Bar(x=x_range_1.numpy(), y=pmf_1.numpy(), name=selected_dist_1))
    fig.add_trace(go.Bar(x=x_range_2.numpy(), y=pmf_2.numpy(), name=selected_dist_2))

fig.update_layout(title=plot_title, xaxis_title="x", yaxis_title="Probability", legend_title="Distributions")
st.plotly_chart(fig)
