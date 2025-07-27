# 🤖 AI Virtual Career Counsellor

## Overview
This project is an AI-powered chatbot designed to provide career recommendations based on a user's stated interests. The bot uses Natural Language Processing (NLP) to understand user queries and responds with relevant career information for the **Tech**, **Arts**, and **Commerce** domains.

---

### ## 🚀 Key Features
* **Conversational AI:** Built with the Rasa framework for robust natural language understanding and dialogue management.
* **Dynamic Recommendations:** Utilizes a Python-based custom action to parse user input and provide tailored career advice.
* **Interactive Web UI:** Features a user-friendly chat interface created with Streamlit.
* **Scalable Knowledge:** The bot's career information is stored in a simple JSON file, making it easy to expand its knowledge base.

---

### ## 🛠️ Tech Stack
* **Backend:** Rasa
* **Frontend:** Streamlit
* **Language:** Python
* **Core Libraries:** NLTK

---

### ## ⚙️ Setup and Installation
To run this project locally, you need two separate Conda environments.

**1. Rasa Environment (`career-bot-py38`)**
```bash
# Create and activate the environment
conda create --name career-bot-py38 python=3.8
conda activate career-bot-py38

# Install dependencies
pip install rasa==3.6.0 nltk
```
## 2. Streamlit Environment (streamlit-env)
```
# Create and activate the environment
conda create --name streamlit-env python=3.10
conda activate streamlit-env

# Install dependencies
pip install streamlit requests
```
Of course. We will stop the deployment process and finalize the project by creating a professional README.md file for your GitHub repository.

A good README file is essential as it serves as the front page and instruction manual for your project.

## Professional README Template
Please open the README.md file in your project folder and replace all of its content with the template below.

Markdown

# 🤖 AI Virtual Career Counsellor

## Overview
This project is an AI-powered chatbot designed to provide career recommendations based on a user's stated interests. The bot uses Natural Language Processing (NLP) to understand user queries and responds with relevant career information for the **Tech**, **Arts**, and **Commerce** domains.

---

### ## 🚀 Key Features
* **Conversational AI:** Built with the Rasa framework for robust natural language understanding and dialogue management.
* **Dynamic Recommendations:** Utilizes a Python-based custom action to parse user input and provide tailored career advice.
* **Interactive Web UI:** Features a user-friendly chat interface created with Streamlit.
* **Scalable Knowledge:** The bot's career information is stored in a simple JSON file, making it easy to expand its knowledge base.

---

### ## 🛠️ Tech Stack
* **Backend:** Rasa
* **Frontend:** Streamlit
* **Language:** Python
* **Core Libraries:** NLTK

---

### ## ⚙️ Setup and Installation
To run this project locally, you need two separate Conda environments.

**1. Rasa Environment (`career-bot-py38`)**
```bash
# Create and activate the environment
conda create --name career-bot-py38 python=3.8
conda activate career-bot-py38
# Install dependencies
pip install rasa==3.6.0 nltk
```
2. Streamlit Environment (streamlit-env)
```
# Create and activate the environment
conda create --name streamlit-env python=3.10
conda activate streamlit-env

# Install dependencies
pip install streamlit requests
```
## ▶️ How to Run
You must run three processes in three separate terminals from the project's root directory.

Terminal 1: Start the Rasa Action Server

```
conda activate career-bot-py38
rasa run actions
```
Terminal 2: Start the Rasa Server
```
conda activate career-bot-py38
rasa run --enable-api
```
Terminal 3: Start the Streamlit App
```
conda activate streamlit-env
streamlit run app.py
```
The application will then be available in your web browser at http://localhost:8501.

## 📄 License
This project is licensed under the MIT License.

