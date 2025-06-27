#David Shableski 6/27/2025
#dbshableski@gmail.com
#A local Q&A app for pizza restaurant reviews using LangChain, Chroma, and Ollama. Runs entirely offline with a simple RAG pipeline.

import os
import logging

# Disable known telemetry. This code sets environment variables to disable automatic telemetry so the libraries don’t try to send usage data or trigger errors
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_ENDPOINT"] = ""
os.environ["OLLAMA_DISABLE_TELEMETRY"] = "1"
os.environ["LLAMA_TELEMETRY"] = "off"

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever



# Initialize the LLM
model = OllamaLLM(model="llama3.2")

# Create the prompt template
template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews:
{reviews}

Here is the customer's question:
{question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Compose the chain
chain = prompt | model

# Main loop
try:
    while True:
        print("\n\n--------------------")
        question = input("Ask your question (q to quit): ").strip()
        print("\n\n--------------------")

        if question.lower() == "q":
            print("Goodbye!")
            break

        reviews = retriever.invoke(question)
        result = chain.invoke({"reviews": reviews, "question": question})
        
        print("\nResponse:")
        print(result)

except KeyboardInterrupt:
    print("\nInterrupted by user. Exiting...")
