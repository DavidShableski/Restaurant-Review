Local Pizza Review QA Bot

## YouTube Demo

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red)](https://youtu.be/PTV9xqAAsmI)


A simple local retrieval-augmented generation (RAG) app that answers questions about pizza restaurant reviews.
It reads a CSV file of customer reviews, stores them in a Chroma vector database, retrieves the most relevant reviews based on a user question, and passes them to a local LLM using Ollama to generate an answer. Everything runs fully offline.

How to run it:

Set up Python and install dependencies:
python -m venv venv
source venv/bin/activate (or .\venv\Scripts\activate on Windows)
pip install -r requirements.txt

Install the local models with Ollama:
ollama pull llama3.2
ollama pull mxbai-embed-large

Build the vector database:
python vector.py

Start the question-answering app:
python main.py

What’s in this repo:

main.py — runs the interactive Q&A loop

vector.py — builds the Chroma DB from the CSV

realistic_restaurant_reviews.csv — sample data

requirements.txt — Python packages

.gitignore — skips venv, Chroma DB, and cache files

Why I built this:

I made this as a template project to show how to build a basic local RAG pipeline using Python, LangChain, Ollama, and Chroma. It’s lightweight, uses no external APIs, and is easy to adapt to other datasets.

Notes:

Requires Ollama installed on your machine (https://ollama.com).

You can swap out the CSV or change the prompt template in main.py to customize it.

References: https://www.youtube.com/watch?v=E4l91XKQSgw&ab_channel=TechWithTim
