# AI Assistant Demo

This repository contains a simple example of a custom AI assistant built with Python.
The goal is to show how I structure clean, reliable AI tools for real business use cases.

# What this demo does

- Receives a user request (a question or a task description)
- Routes it to a simple "assistant" function
- (Optionally) calls an AI model through an API
- Returns a clear, structured answer

The code is intentionally small and easy to read.  
Real client projects include more complex workflows, integrations and error handling.

# Files

- `main.py` – entry point with a minimal assistant example
- `assistant.py` – core assistant logic
- `config_example.py` – how to store your API keys safely
- `requirements.txt` – Python dependencies

# Quick start

```bash
git clone https://github.com/ludwigkubler/ai-assistant-demo.git
cd ai-assistant-demo
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
