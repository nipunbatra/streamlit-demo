---
title: probability-distributions
emoji: 🚀
colorFrom: pink
colorTo: pink
sdk: streamlit
sdk_version: 1.42.2
app_file: app.py
pinned: false
---

# Visualising Distributions in PyTorch

This repository contains a Streamlit app that visualises the distributions in PyTorch. The app allows you to select a distribution and visualise the probability density function (PDF) and Probability Mass Function (PMF) of the selected distribution.

You can either run the app locally or use the [Hugging Face](https://huggingface.co/spaces/Nipun/probability-distributions)

# Steps to run this app locally
```
python
pip install -r requirements.txt
streamlit run Home.py
```

# Steps I took to deploy this app on Hugging Face and manage via Github

1. Create a new Hugging Face Space. Mine is called `probability-distributions`
2. Added Hugging Face as a remote to my local git repository using `git remote set-url space git@hf.co:spaces/Nipun/probability-distributions`
3. Pushed the code to the Hugging Face Space using `git push --force space main`
4. Now, whenever I make changes to the code, I can push the changes to the Hugging Face Space using `git push space main` in addition to pushing the changes to Github.
5. To avoid multiple pushes, I created a githook that pushes the changes to the Hugging Face Space whenever I push the changes to Github. The githook is located at `.git/hooks/post-push` and contains the following code:
```bash
#!/bin/bash
git push space main
```
6. Make the githook executable using `chmod +x .git/hooks/post-push`

