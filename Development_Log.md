# 🩺GlucoGuide
## 🛑 CHECKPOINT 0 — PROJECT FOUNDATION

### 🎯 Objective
Establish a clean and reliable development foundation before starting any implementation.

### ✅ What Was Completed
- Created a dedicated project directory
- Initialized a Python virtual environment
- Configured Visual Studio Code for development
- Set up PowerShell as the primary terminal

This checkpoint ensures the project starts with a professional and reproducible setup, aligned with real-world machine learning and AI workflows.

## 🛑 CHECKPOINT 1 — PROJECT FOLDER STRUCTURE

### 🎯 Objective
Design a clean, scalable, and professional folder structure for the project.

### ✅ What Was Completed
- Created a standardized directory layout
- Separated data, source code, notebooks, and tests
- Established a clear location for storing the WHO diabetes PDF
- Ensured the project structure supports future scalability

### 📁 Folder Structure
```text
GlucoGuide/
├── data/
│   └── raw/
├── src/
├── notebooks/
├── tests/
└── README.md
```

## 🛑 CHECKPOINT 2 — DATA INGESTION SETUP (FOUNDATION)

### 🎯 Objective
Prepare the project for reliable document ingestion without implementing processing logic.

### ✅ What Was Completed
- Added the WHO diabetes PDF to the appropriate data directory
- Organized raw documents for future ingestion pipelines
- Configured `.gitignore` to protect unnecessary and sensitive files
- Verified that document images do not affect ingestion workflows

### 📁 Data Layout
```text
data/
└── raw/
    └── who_diabetes_guidelines.pdf
```

## 🛑 CHECKPOINT 3 — PYTHON FOUNDATION (CORE FILES)

### 🎯 Objective
Establish the core Python entry points and configuration files required to start the application.

### ✅ What Was Completed
- Created essential Python source files
- Defined a clear execution entry point
- Added a centralized configuration module
- Ensured the project is ready for controlled expansion

### 📁 Core Source Structure
```text
src/
├── __init__.py
├── config.py
└── main.py
```

## 🛑 CHECKPOINT 4 — DEPENDENCY SETUP

### 🎯 Objective
Configure and install all required project dependencies in a controlled and reproducible environment.

### ✅ What Was Completed
- Created a `requirements.txt` file
- Defined all core Python dependencies explicitly
- Installed libraries inside an isolated virtual environment
- Verified successful installation and compatibility

### 📦 Dependency Management
All dependencies are pinned and managed using `requirements.txt` to ensure consistent behavior across environments.

```text
requirements.txt
```
## 🛑 CHECKPOINT 5 — DOCUMENT LOADING (FIRST RAG STEP)

### 🎯 Objective
Load and validate the WHO diabetes PDF as the first operational step in the RAG pipeline.

### ✅ What Was Completed
- Loaded the WHO diabetes PDF using LangChain document loaders
- Converted the PDF into structured `Document` objects
- Verified successful page extraction
- Printed sample text content to confirm correct parsing
- Confirmed that embedded images do not interfere with text extraction

### 📄 Document Processing
At this stage, the project focuses exclusively on **document ingestion and validation**, ensuring reliable text extraction before downstream processing.

This checkpoint marks the transition from project setup to active RAG pipeline development while maintaining a controlled, incremental approach.

## 🛑 CHECKPOINT 6 — TEXT CHUNKING (CORE RAG CONCEPT)

### 🎯 Objective
Transform raw document text into structured, overlapping chunks suitable for downstream retrieval workflows.

### ✅ What Was Completed
* Implemented recursive text splitting
* Tuned chunk size and overlap for semantic continuity
* Converted extracted PDF text into clean, inspectable chunks
* Validated chunk boundaries and content quality

This checkpoint completes the preprocessing foundation required for embedding and retrieval.

---

## 🛑 CHECKPOINT 7 — LOCAL EMBEDDINGS WITH MINI-LM (WINDOWS-STABLE)

### 🎯 Objective
Enable semantic retrieval using local embeddings in a Windows-compatible environment.

### ✅ What Was Completed
* Implemented MiniLM-based local embeddings (`all-MiniLM-L6-v2`)
* Configured CPU-only inference (no CUDA dependency)
* Stored embeddings in a persistent Chroma vector database
* Enabled semantic similarity search over document chunks

### ⚙️ Platform Stability Measures
To avoid common Windows-related issues:
* CPU-only PyTorch stack was used
* Hugging Face dependencies were carefully pinned
* Known-breaking versions were intentionally avoided

This checkpoint introduced the retrieval backbone of the RAG system.

---

## 🛑 CHECKPOINT 8 — RAG WITH OPENROUTER LLAMA-3.2 (API-BASED LLM)

### 🎯 Objective
Enable end-to-end medical question answering using Retrieval-Augmented Generation with an API-based LLM.

### ✅ What Was Completed
* Implemented a natural language question interface
* Retrieved relevant chunks using MiniLM + Chroma
* Integrated OpenRouter as the LLM gateway
* Generated grounded answers with page-level citations
* Implemented safe refusal when answers are not present in the document
* Added medical safety disclaimers to responses

### 🔁 Critical LLM Integration Fix
During this checkpoint, an important stability issue was identified and resolved:
* Initial use of `meta-llama/llama-3.2-3b-instruct:free` caused non-deterministic provider routing
* The LLM configuration was corrected to:
  * Use the base model identifier (`meta-llama/llama-3.2-3b-instruct`)
  * Explicitly set the OpenRouter `base_url`
  * Pass required OpenRouter headers

This change eliminated intermittent 402 errors and provider instability.

### 🧠 Final RAG Execution Flow
1. User submits a question  
2. Relevant chunks retrieved via Chroma  
3. Context injected into a structured prompt  
4. LLaMA-3.2 Instruct generates a grounded response  
5. Sources and safety disclaimers appended  

This checkpoint completed the fully functional RAG pipeline.

---

## 🛑 CHECKPOINT 9 — DEPENDENCY FREEZE & REPRODUCIBILITY VERIFICATION

### 🎯 Objective
Guarantee that the project can be reliably reproduced on any machine without breaking.

### ✅ What Was Completed
* Inspected the actual working environment using `pip freeze`
* Created a clean, minimal, pinned `requirements.txt`
* Verified installation in a fresh test virtual environment
* Confirmed that:
  * The project runs correctly
  * Existing embeddings are reused
  * No hidden dependencies exist
* Cleaned up the test environment after verification
* Updated `.gitignore` to exclude local editor and environment files

This checkpoint ensures long-term project stability, safe recovery from GitHub, and professional-grade dependency management.

---

## 🧠 Current Project State

At this stage, **GlucoGuide** is:
* Fully functional
* Dependency-stable
* Reproducible
* Safe for medical QA use
* Ready for backend and frontend expansion

---

## 🔜 Next Planned Phase
* FastAPI backend
* Localhost API endpoint
* Frontend integration (Lovable)
* Optional local LLM (Ollama) support

All future changes will build on this stable core.
