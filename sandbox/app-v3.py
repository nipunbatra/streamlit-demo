"""
v3: In this version, beyond v2, we will add a table to mention some properties of the normal distribution. 
We wcan do this via the st.table() function.
"""

import streamlit as st
import torch 
import matplotlib.pyplot as plt
import pandas as pd


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


plt.plot(x_range.numpy(), pdf.numpy())
plt.xlabel('x')
plt.ylabel('Probability Density')
st.pyplot(plt)


