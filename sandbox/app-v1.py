import streamlit as st
import torch 
import matplotlib.pyplot as plt

st.title('PyTorch Distributions')

mu = st.slider('Mean', -10.0, 10.0, 0.0)
sigma = st.slider('Standard Deviation', 0.1, 10.0, 1.0)

normal_dist = torch.distributions.Normal(mu, sigma)

x_range = torch.linspace(-10, 10, 1000)
pdf = normal_dist.log_prob(x_range).exp()

plt.plot(x_range.numpy(), pdf.numpy())
plt.xlabel('x')
plt.ylabel('Probability Density')
st.pyplot(plt)


