import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

st.title("📚 ML Assistant (RAG + Ollama)")

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector DB
vectorstore = Chroma(
    persist_directory="embeddings",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever()

# Load LLM
llm = Ollama(model="tinyllama")

# Prompt template
template = """
Answer the question based only on the context below.

Context:
{context}

Question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)

# RAG pipeline (new LangChain style)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

query = st.text_input("Ask a Machine Learning Question:")

if query:
    response = rag_chain.invoke(query)
    st.write(response)


