---
title: probability-distributions
emoji: 🚀
colorFrom: pink
colorTo: pink
sdk: streamlit
sdk_version: 1.42.2
app_file: Home.py
pinned: false
---

# Visualizing Probability Distributions in PyTorch

This repository contains a Streamlit app that visualizes various probability distributions in PyTorch. The app allows you to select a distribution and visualize its Probability Density Function (PDF) or Probability Mass Function (PMF).

## Running the App Locally

### Prerequisites
Make sure you have Python installed. Then, install the required dependencies:
```sh
pip install -r requirements.txt
```

### Running the Streamlit App
```sh
streamlit run Home.py
```

---

## Deploying on Hugging Face and Managing with GitHub

### Step 1: Create a Hugging Face Space
Create a new Hugging Face Space for your Streamlit app. In this example, we assume the space is named `probability-distributions`.

### Step 2: Add Hugging Face as a Remote

Check your existing remotes:
```sh
git remote -v
```
You should see something like this:
```
origin  https://github.com/nipunbatra/streamlit-demo.git (fetch)
origin  https://github.com/nipunbatra/streamlit-demo.git (push)
```

Now, add Hugging Face as a remote:
```sh
git remote add space git@hf.co:spaces/Nipun/probability-distributions
```
Verify that both remotes exist:
```sh
git remote -v
```
Output:
```
origin  https://github.com/nipunbatra/streamlit-demo.git (fetch)
origin  https://github.com/nipunbatra/streamlit-demo.git (push)
space   git@hf.co:spaces/Nipun/probability-distributions (fetch)
space   git@hf.co:spaces/Nipun/probability-distributions (push)
```

### Step 3: Push Code to Both GitHub and Hugging Face

Instead of using hooks, we define a Git alias to push to both remotes:

```sh
git config --global alias.pushall '!git push origin main && git push space main'
```

Now, whenever you make changes, commit them and use:
```sh
git add .
git commit -m "Your commit message"
git pushall
```
This ensures that your changes are pushed to both GitHub and Hugging Face.

---

### Explanation of Key Concepts

- **Remote**: A remote is a version of your repository stored on another server. Here, `origin` refers to GitHub, and `space` refers to Hugging Face.
- **Branch**: A branch represents a line of development in Git. Here, we are using the `main` branch.
- **`git remote -v`**: Lists all remote repositories associated with the project.
- **`git push`**: Sends committed changes from your local branch to a remote repository.
- **Git Alias (`pushall`)**: A custom shortcut to push changes to multiple remotes in one command.

With this setup, you can easily develop your app locally, push updates to GitHub for version control, and deploy to Hugging Face seamlessly.


