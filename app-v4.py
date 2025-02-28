"""
v4: In this version, beyond v3, we will make the graph interactive using st.LineChart and plotly.
"""

import streamlit as st
import torch 
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go



st.title('PyTorch Distributions')

mu = st.slider('Mean', -10.0, 10.0, 0.0)
sigma = st.slider('Standard Deviation', 0.1, 10.0, 1.0)

normal_dist = torch.distributions.Normal(mu, sigma)

x_range = torch.linspace(-10, 10, 1000)
pdf = normal_dist.log_prob(x_range).exp()

st.markdown('The **probability density function** of a normal distribution is given by:')
st.latex(r'f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)')


data = {
    'Property': ['Mean', 'Standard Deviation', 'Variance', 'Entropy'],
    'Value': [mu, sigma, sigma**2, normal_dist.entropy().item()]
}

df = pd.DataFrame(data)
st.table(df)

chart_data = pd.DataFrame({"x": x_range, "pdf": pdf})
st.markdown('#### Probability Density Function (made using `st.line_chart`)')
st.line_chart(chart_data, x='x', y='pdf', x_label='x', y_label='f(x)', use_container_width=True)

st.markdown('#### Probability Density Function (made using `plotly`)')
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_range, y=pdf, mode='lines', name='',
                         hovertemplate='x: %{x:.2f}<br>f(x): %{y:.2f}'))
fig.update_layout(xaxis_title='x', yaxis_title='f(x)')

st.plotly_chart(fig)




