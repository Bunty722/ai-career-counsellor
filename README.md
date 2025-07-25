# 🤖 AI Virtual Career Counsellor

## Objective
This project is an AI-powered chatbot designed to provide career recommendations based on a user's stated interests. The bot can currently advise on career paths in **Tech**, **Arts**, and **Commerce**.

---

## 🚀 Features
- **Conversational AI:** Uses Rasa for natural language understanding and dialogue management.
- **Keyword-Based Recommendations:** Employs a Python-based custom action to parse user input and provide relevant career advice.
- **Web-Based UI:** A user-friendly chat interface built with Streamlit.

---

## 🛠️ Tech Stack
- **Backend:** Rasa
- **Frontend:** Streamlit
- **Language:** Python
- **Core Libraries:** NLTK

---

## ⚙️ Setup and Installation

To run this project locally, you will need two separate Conda environments.

**1. Rasa Environment Setup:**
```bash
# Create and activate the environment
conda create --name career-bot-py38 python=3.8
conda activate career-bot-py38

# Install dependencies
pip install rasa==3.6.0 nltk

# Create and activate the environment
conda create --name streamlit-env python=3.10
conda activate streamlit-env
```
## 2. Streamlit Environment Setup:
```
# Install dependencies
pip install streamlit requests
```
## ▶️ Usage
You need to run three processes in three separate terminals from the project's root directory.

Terminal 1 (Rasa Actions):
```
conda activate career-bot-py38
rasa run actions
```
## Terminal 2 (Rasa Server):
```
conda activate career-bot-py38
rasa run --enable-api
```
## Terminal 3 (Streamlit Frontend):
```
conda activate streamlit-env
streamlit run app.py
```
The application will then be available in your web browser, typically at http://localhost:8501.
