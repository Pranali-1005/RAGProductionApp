**README.md Content**

Production RAG PDF Application

This project implements a production-style Retrieval Augmented Generation (RAG) system that allows users to query information from PDF documents using semantic search and a Large Language Model (LLM). The system ingests PDF files, converts their content into embeddings, stores them in a vector database, retrieves the most relevant context, and then generates answers based on that context.

Project Overview

The system demonstrates a full RAG pipeline consisting of several steps. First, PDF documents are ingested and processed. The text from the PDF is split into smaller chunks so that it can be embedded efficiently. These chunks are converted into vector embeddings using a sentence transformer model. The embeddings are stored in a vector database (Qdrant). When a user asks a question, the system generates an embedding of the query and performs a similarity search in the vector database to find the most relevant text chunks. These chunks are then passed to a language model which generates the final answer.

Tech Stack

API Framework: FastAPI
Workflow Orchestration: Inngest
Embeddings Model: SentenceTransformers (all-MiniLM-L6-v2)
Vector Database: Qdrant
LLM: Hugging Face or Ollama
Programming Language: Python
Package Manager: uv

System Architecture

The overall workflow of the system is as follows:

PDF Document → Text Chunking → Embedding Generation → Vector Storage in Qdrant → Semantic Search → Context Retrieval → LLM Answer Generation

Project Structure

RAGProductionApp

* main.py
* data_loader.py
* vector_db.py
* custom_types.py
* README.md
* .gitignore
* .env

Features

The system supports PDF ingestion and automatic chunking of document text. It generates vector embeddings for each chunk and stores them in a Qdrant vector database. When a question is asked, the system performs semantic similarity search to retrieve the most relevant chunks from the database. The retrieved context is then used by a language model to generate a concise and context-aware answer.

Setup Instructions

1. Clone the repository from GitHub.

git clone [https://github.com/Pranali-1005/RAGProductionApp.git](https://github.com/Pranali-1005/RAGProductionApp.git)
cd RAGProductionApp

2. Install dependencies using the uv package manager.

uv pip install -r requirements.txt

3. Start the Qdrant vector database. This can be done using Docker.

docker run -p 6333:6333 qdrant/qdrant

4. Start the FastAPI server.

uv run uvicorn main:app --reload

5. Start the Inngest development server.

npx inngest-cli dev -u [http://127.0.0.1:8000/api/inngest](http://127.0.0.1:8000/api/inngest)

Example Query

A sample query payload for testing the system:

{
"question": "What is Java?",
"top_k": 5
}

This query retrieves the top 5 most relevant document chunks and generates an answer based on those contexts.

Use Cases

This system can be used for document question answering, knowledge base search, research document exploration, and enterprise document retrieval systems.

Author

Pranali Kawade
B.Tech – Artificial Intelligence and Data Science
