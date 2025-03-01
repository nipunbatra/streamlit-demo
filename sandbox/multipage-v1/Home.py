import streamlit as st
import torch 
import plotly.graph_objects as go

st.set_page_config(page_title="PyTorch Distributions")
st.title('PyTorch Distributions')

st.markdown("This is a Streamlit app that demonstrates the probability density functions of various PyTorch distributions. "
            "Use the sidebar to select between continuous and discrete distributions, and set the parameters of the selected distribution.")

st.markdown("---")
st.mardown("Made on 1st March 2025")