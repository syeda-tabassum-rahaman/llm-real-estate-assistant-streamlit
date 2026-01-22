# 🏡 LLM-Powered Real Estate Research Assistant (RAG + Streamlit)

## Overview
This project is a **Retrieval-Augmented Generation (RAG)** application that enables users to ask natural language questions about real-estate–related articles (e.g. mortgage rates, housing market news) and receive **accurate, source-backed answers**.

Instead of relying on generic LLM knowledge, the system ingests live URLs, builds a vector database, and generates answers strictly grounded in the provided content.

---

## Problem Statement
Real-estate professionals, analysts, and end users often need to:
- Read multiple long articles from different sources  
- Extract specific facts (rates, dates, trends)  
- Verify answers with reliable references  

Manual reading is time-consuming, error-prone, and does not scale.

---

## Solution
This application addresses the problem by combining:
- Live document ingestion from URLs  
- Semantic search using embeddings  
- LLM-based question answering with cited sources  
- A simple Streamlit interface for non-technical users  

The result is a fast, transparent research assistant that answers **only from ingested content** and always returns **source URLs**.

---

## 🚀 Key Features
- **Automated Document Ingestion**: Scrapes and processes raw HTML from URLs using WebBaseLoader and BeautifulSoup4  
- **Semantic Data Chunking**: Uses RecursiveCharacterTextSplitter to preserve context across long-form articles  
- **High-Performance Vector Search**: Employs the Alibaba-NLP/gte-base-en-v1.5 embedding model with a local ChromaDB vector store  
- **Citations & Transparency**: Leverages RetrievalQAWithSourcesChain to return answers with explicit source URLs, reducing hallucinations  
- **Streamlit Dashboard**: Clean UI for real-time URL indexing and question answering  

---

## Tech Stack
- **Python 3.12**
- **Streamlit** – UI layer  
- **LangChain (modular ecosystem)** – RAG pipeline  
- **ChromaDB** – Vector storage  
- **Groq (LLaMA 3.3)** – LLM inference  
- **HuggingFace Embeddings** – Alibaba-NLP/gte-base-en-v1.5  
- **BeautifulSoup / Web loaders** – Content extraction

## ▶️ How to Run the Application

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/llm-real-estate-assistant-streamlit.git
cd llm-real-estate-assistant-streamlit
