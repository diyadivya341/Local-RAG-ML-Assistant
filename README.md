📚 Project Summary

This project is a fully local Retrieval-Augmented Generation (RAG) system built using LangChain, ChromaDB, Ollama, and Streamlit.

It allows users to ask Machine Learning related questions and receive context-aware answers based on a custom knowledge base.

The system runs completely locally — no API keys required — making it secure, lightweight, and cost-free.

📂 Knowledge Base Details

The system uses:

Machine Learning textbook content

Preprocessed text documents
Vector embeddings for semantic search

The content is stored in a Chroma vector database and retrieved dynamically based on user queries.

🛠️ Technologies Used
🧠 AI & NLP

LangChain (RAG pipeline orchestration)

Ollama (Local LLM execution)

TinyLlama (Lightweight LLM model)

HuggingFace Sentence Transformers

ChromaDB (Vector database)

🖥️ Web Application

Streamlit (Interactive web UI)

📦 Other Tools

Python

Embedding model: all-MiniLM-L6-v2

🛠️ Project Workflow
1️⃣ Document Processing

Text data is loaded and split into chunks.

Each chunk is converted into vector embeddings.

2️⃣ Vector Storage

Embeddings are stored in ChromaDB for fast similarity search.

3️⃣ Retrieval

When a user asks a question, relevant context is retrieved using semantic similarity.

4️⃣ Generation

Retrieved context + question is passed to TinyLlama (via Ollama).

The LLM generates a context-aware answer.

5️⃣ Web Interface

Streamlit provides a simple input box for asking ML questions.

The answer is displayed instantly.

📈 System Features

✔ Fully local execution (No API key required)
✔ Lightweight model (TinyLlama)
✔ Semantic search with embeddings
✔ Interactive Streamlit UI
✔ Modular RAG architecture

🚀 How to Run Locally
pip install -r requirements.txt
ollama pull tinyllama
python -m streamlit run app.py
🧠 Model Used

TinyLlama (via Ollama)

Embedding Model:
sentence-transformers/all-MiniLM-L6-v2

<img width="1721" height="743" alt="Screenshot 2026-02-23 134700" src="https://github.com/user-attachments/assets/b58fbfa3-c3ea-442c-887c-2f512341632a" />

<img width="1433" height="660" alt="Screenshot 2026-02-23 134736" src="https://github.com/user-attachments/assets/fe10a869-086b-43e5-a1e0-60cbcb1f4993" />

<img width="1252" height="612" alt="Screenshot 2026-02-23 134818" src="https://github.com/user-attachments/assets/7a7effb8-3196-41c0-a3df-cf4915beeb24" />
