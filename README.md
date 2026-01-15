# 🩺 GlucoGuide — Medical Document RAG System

GlucoGuide is a **medical document–based Retrieval-Augmented Generation (RAG) system** built to answer questions **strictly from an official WHO diabetes PDF**.  
The system is designed to be **safe, faithful to source documents, and resistant to hallucinations**, making it suitable for medical and educational use cases.

---

## 🚀 Project Overview

GlucoGuide allows users to ask natural-language questions about a diabetes-related medical document.  
The system retrieves relevant sections from the document and generates answers **only when the information is explicitly present in the source**.

If the answer is **not found in the document**, the system correctly responds:

> *“I don’t know based on the provided document.”*

This strict behavior is intentional and aligns with best practices for **medical RAG systems**.

---

## 🧠 Key Features

- 📄 PDF-based question answering (WHO diabetes document)
- 🔍 Semantic search using vector embeddings
- 🧠 LLM-based answer generation with strict grounding
- 🚫 No hallucinations or unsupported medical claims
- 📚 Source page references for transparency
- 🔐 Secure API key handling using environment variables

---

## 🏗️ Architecture (Current)

```text
User Question
      ↓
MiniLM Embeddings (Local)
      ↓
Chroma Vector Database (Local)
      ↓
Relevant PDF Chunks Retrieved
      ↓
LLaMA-3.2 Instruct (via OpenRouter API)
      ↓
Grounded Answer OR Safe Refusal
```


---

## 🧩 Tech Stack

### Embeddings

* **Model:** `sentence-transformers/all-MiniLM-L6-v2`
* **Execution:** Local (no API cost)

### Vector Store

* **Database:** Chroma (local persistence)
* **Search Type:** Semantic similarity search

### Language Model (LLM)

* **Model:** `meta-llama/llama-3.2-3b-instruct:free`
* **Provider:** OpenRouter
* **Usage:** Answer generation only (no embeddings)

### Frameworks & Tools

* Python
* LangChain
* ChromaDB
* Hugging Face Sentence Transformers
* OpenRouter API
* VS Code (Windows)

---

## 🔐 Security & Safety Design

* API keys are stored securely in a `.env` file (never hardcoded)
* `.env` is excluded via `.gitignore`
* The system does **not** provide:

  * Medical diagnosis
  * Treatment advice
  * Information not present in the document

This ensures **ethical and safe medical AI usage**.

---

## 📁 Project Structure

GlucoGuide/
│
├── src/
│   ├── main.py          # Core RAG pipeline
│   ├── config.py        # Centralized configuration
│
├── data/
│   ├── raw/             # Original PDF document
│   └── processed/       # Chroma vector database
│
├── .env                 # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md

