# Contributing to Streamlit Distribution Demo

Thank you for your interest in contributing to this project! This guide will help you understand how to add new probability distributions to the application.

## Adding New Distributions

The application is designed to make adding new distributions as simple as possible. You only need to create a single file for each new distribution you want to add.

### Adding a Continuous Distribution

1. Create a new Python file in the `config/continuous/` directory.
2. Name the file after your distribution (e.g., `exponential.py` for an Exponential distribution).
3. Define a constant with the uppercase name of your distribution (e.g., `EXPONENTIAL`).
4. The constant should be a dictionary with the following keys:
   - `params`: A lambda function that returns a dictionary of parameters using Streamlit widgets.
   - `dist`: A lambda function that takes the parameters and returns a PyTorch distribution.
   - `support`: A lambda function that returns the support of the distribution (optional).

Example:

```python
import streamlit as st
import torch

EXPONENTIAL = {
    "params": lambda: {
        "rate": st.sidebar.slider("Rate (λ)", 0.1, 5.0, 1.0, 0.1),
    },
    "dist": lambda p: torch.distributions.Exponential(p["rate"]),
    "support": lambda p: (0, None),
}
```

### Adding a Discrete Distribution

1. Create a new Python file in the `config/discrete/` directory.
2. Name the file after your distribution (e.g., `geometric.py` for a Geometric distribution).
3. Define a constant with the uppercase name of your distribution (e.g., `GEOMETRIC`).
4. The constant should be a dictionary with the following keys:
   - `params`: A lambda function that returns a dictionary of parameters using Streamlit widgets.
   - `dist`: A lambda function that takes the parameters and returns a PyTorch distribution.
   - `support`: A lambda function that returns the support of the distribution (optional).

Example:

```python
import streamlit as st
import torch

GEOMETRIC = {
    "params": lambda: {
        "p": st.sidebar.slider("Success Probability (p)", 0.01, 0.99, 0.5, 0.01),
    },
    "dist": lambda p: torch.distributions.Geometric(p["p"]),
    "support": lambda p: (0, None),
}
```

## How It Works

The application automatically discovers and loads all distributions in the `config/continuous/` and `config/discrete/` directories. When you add a new file, it will be automatically included in the application without any additional changes needed.

The display name of the distribution in the UI is derived from the filename. For example, a file named `negative_binomial.py` will be displayed as "NegativeBinomial" in the UI.

## Testing Your Changes

After adding a new distribution, run the application to test your changes:

```bash
streamlit run Home.py
```

Navigate to the appropriate page (Continuous or Discrete) and select your new distribution from the dropdown menu to verify it works correctly.