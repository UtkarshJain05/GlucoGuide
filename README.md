# 🩺 GlucoGuide — Medical Document RAG System

GlucoGuide is a Retrieval-Augmented Generation (RAG) system built to answer questions strictly from an official WHO diabetes PDF document.

The system retrieves relevant sections from the document and generates answers only when the information is explicitly present in the source.

If the answer is not found in the document, the system responds:

> "I don't know based on the provided document."

This behavior is intentional to prevent hallucinations and unsupported medical claims.

---

## 🔍 What This Project Demonstrates

- End-to-end RAG pipeline implementation
- Local semantic embeddings using MiniLM
- Persistent vector database using Chroma
- API-based LLM integration (OpenRouter + LLaMA)
- Strict grounding to prevent hallucination
- Clean project structure and reproducibility

---

## 🏗️ Architecture

```
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
- sentence-transformers/all-MiniLM-L6-v2
- CPU-only execution

### Vector Database
- Chroma (local persistent storage)

### LLM
- meta-llama/llama-3.2-3b-instruct
- Accessed via OpenRouter API

### Core Libraries
- LangChain
- ChromaDB
- Hugging Face Transformers
- PyPDF
- Python-dotenv

---

## 📁 Project Structure

```
GlucoGuide/
│
├── core/
│   ├── __init__.py
│   ├── config.py
│   └── main.py
│
├── data/
│   ├── raw/          # Place WHO diabetes PDF here
│   └── processed/    # Chroma DB (auto-generated, ignored by Git)
│
├── .gitignore
├── requirements.txt
├── Journey.md
└── README.md
```

---

## ⚙️ How It Works

1. Load WHO diabetes PDF
2. Split text into overlapping chunks
3. Generate embeddings using MiniLM
4. Store embeddings in Chroma (local persistence)
5. Convert user query into embedding
6. Retrieve top relevant chunks
7. Pass retrieved context to LLaMA (OpenRouter)
8. Generate grounded answer or safe refusal

---

## 🚀 How To Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/UtkarshJain05/GlucoGuide.git
cd GlucoGuide
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Environment Variable

Create a `.env` file in project root:

```
OPENAI_API_KEY=your_openrouter_api_key_here
```

(Used for OpenRouter LLM access)

---

### 5️⃣ Add Your Own PDF Document

This repository does NOT include the WHO PDF.

You must place your own PDF file inside:

```
data/raw/
```

Then update the filename in:

```
core/config.py
```

Example:

```python
PDF_PATH = RAW_DATA_DIR / "your_document.pdf"
```

The system will process whatever PDF is placed in the `data/raw/` directory.

---

### 6️⃣ Run Application

```bash
python core/main.py
```

You can now ask questions about the document.

Type `exit` to quit.

---

## 🧪 Example Behavior

**Question:**
> What is diabetes?

**Answer:**
> Diabetes is a condition in which the level of sugar (glucose) in the blood is higher than normal...

**Sources:**
> PDF pages are displayed.

---

**Question:**
> What is the cure for diabetes?

**Answer:**
> I don't know based on the provided document.

---

## 🔐 Security

- API keys stored in `.env`
- `.env` excluded via `.gitignore`
- Processed vector database is ignored.
- No hardcoded secrets

---

## 📌 Disclaimer

This project is for educational purposes only.

It is not a medical diagnosis or treatment tool.

---

## 🧠 Development Log

See `Development_Log.md` for structured checkpoint-based development progression.