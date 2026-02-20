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
- 🧩 Stable OpenRouter integration with explicit configuration

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
* **Execution:** API-based (answer generation only)

### ⚠️ Important Implementation Note
* The LLM is configured using an explicit OpenRouter-compatible setup (custom base URL and headers).
* This avoids provider routing instability and ensures reliable inference across sessions.

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
```text
GlucoGuide/
│
├── core/
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
├── Journey.md
└── README.md
```


---

## ⚙️ How It Works (Step-by-Step)

1. Load the WHO diabetes PDF
2. Split the document into overlapping text chunks
3. Convert chunks into embeddings using MiniLM
4. Store embeddings in a local Chroma vector database
5. Convert user query into an embedding
6. Retrieve top relevant chunks
7. Pass retrieved context to LLaMA (OpenRouter)
8. Generate a grounded answer or safely refuse

---

## 🧪 Example Behavior

**Question:**

> What is diabetes?

**Answer:**

> Diabetes is a condition in which the level of sugar (glucose) in the blood is higher than normal…

**Sources:**

> PDF pages: [0, 2, 3]

---

**Question:**

> What is the cure for diabetes?

**Answer:**

> I don’t know based on the provided document.

**Sources:**

> PDF pages searched are shown for transparency.

---

## ⚠️ Important Design Choices

### Strict RAG Enforcement
* The system **does not answer from general knowledge**
* Answers are generated **only if supported by the document**
* This prevents hallucinations and misinformation

### LangChain Warning Note
* A known LangChain deprecation warning may appear related to embeddings
* This warning does not affect functionality or correctness
* Dependency versions are intentionally pinned for stability
* Warning suppression is deferred to a future controlled upgrade

---

## 🛠️ Current Status

✅ Core RAG pipeline completed  
✅ Local embeddings and vector database working  
✅ Stable OpenRouter LLaMA integration (fixed configuration)  
✅ Safe refusal behavior implemented  
✅ Source citation enabled  

---

## 🔜 Upcoming Enhancements (Planned)

* Backend API (FastAPI)
* Localhost endpoint for interaction
* Frontend UI (Lovable)
* Improved UX for unanswered queries
* Deployment-ready architecture
* Optional local LLM execution mode (Ollama)

*(Enhancements will be added incrementally and documented here.)*

---

## 📌 Disclaimer

This project is for **educational and informational purposes only**.
It is **not a medical diagnosis or treatment tool**.

---

## 🙌 Acknowledgements

* World Health Organization (WHO)
* Hugging Face
* LangChain
* OpenRouter
* Meta (LLaMA models)
