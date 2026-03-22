# CLI Chatbot with Memory (LLM-Powered)

An intelligent command-line chatbot built using OpenAI’s LLM API, designed to simulate natural conversations with contextual memory and structured responses.

---

## Overview

This project demonstrates how to build a production-style conversational AI system in Python.
The chatbot maintains conversation history, generates context-aware responses, and provides a clean CLI interface for interaction.

---

## Key Features

* **Conversational Memory**
  Maintains chat history to generate context-aware responses

* **LLM Integration**
  Uses OpenAI API for intelligent and human-like responses

* **Structured Messaging System**
  Implements role-based messaging (`user`, `assistant`, `system`)

* **CLI Interface**
  Lightweight and interactive terminal-based chatbot

* **Secure API Handling**
  Environment variables used to protect API keys

---

## 🛠️ Tech Stack

* **Python**
* **OpenAI API**
* **python-dotenv**
* **CLI (Terminal-based interface)**

---

## Project Structure

```bash
CliChatbot/
│── main.py          # Entry point (CLI interaction loop)
│── llm.py           # Handles API calls to OpenAI
│── config.py        # Configuration (API key, model)
│── .env             # Environment variables (not committed)
│── requirements.txt
│── README.md
```

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/cli-chatbot.git
cd cli-chatbot
```

2. Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your API key in `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Run the Chatbot

```bash
python main.py
```

---

## Example Interaction

```bash
You: Hello
Bot: Hi! How can I help you today?

You: Explain Python loops
Bot: Python loops allow you to iterate over sequences...
```

---

## Future Improvements

* Add persistent memory (database / vector store)
* Upgrade to FastAPI backend
* Implement streaming responses
* Add multi-agent capabilities
* Integrate embeddings for semantic search

---

## What I Learned

* Working with LLM APIs in real applications
* Managing conversational state and memory
* Structuring scalable Python projects
* Handling API security using environment variables

---

## Why This Project Matters

This project showcases practical skills in:

* Building LLM-powered applications
* Designing conversational systems
* Backend-ready Python development

---

## Author

Built with ❤️ as part of an Agentic AI journey.
