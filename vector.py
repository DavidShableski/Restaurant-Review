from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

#Configuration
DATA_FILE = "realistic_restaurant_reviews.csv"
DB_PATH = "./chrome_langchain_db"
COLLECTION_NAME = "restaurant_reviews"
EMBEDDING_MODEL = "mxbai-embed-large"

#Load Data
df = pd.read_csv(DATA_FILE)

#Set up Embeddings
embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

#Determine if we need to add documents ---
needs_initialization = not os.path.exists(DB_PATH)

#Prepare documents if first run
documents_to_add = []
if needs_initialization:
    for idx, row in df.iterrows():
        content = f"{row['Title']} {row['Review']}"
        doc = Document(
            page_content=content,
            metadata={
                "rating": row["Rating"],
                "date": row["Date"]
            },
            id=str(idx)
        )
        documents_to_add.append(doc)

#Create / Load Vector Store
vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

#Populate vector DB if needed
if needs_initialization:
    vector_store.add_documents(documents=documents_to_add)

#Create Retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
