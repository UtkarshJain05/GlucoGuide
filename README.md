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
- Implemented text chunking using a recursive splitting strategy
- Defined optimal chunk size and overlap for semantic continuity
- Converted extracted PDF text into clean, structured chunks
- Inspected sample chunks to validate content integrity and boundaries

### 🧩 Text Preparation
Chunking ensures that long documents are broken into manageable units while preserving contextual meaning, enabling accurate and efficient retrieval in later stages.

This checkpoint completes the document preprocessing foundation required for embedding and vector storage integration.

## 🛑 CHECKPOINT 7 — LOCAL EMBEDDINGS WITH MINI-LM (WINDOWS-STABLE)

### 🎯 Objective
Enable semantic retrieval by generating document embeddings locally using a Windows-compatible configuration.

### ✅ What Was Completed
- Implemented local embedding generation using the MiniLM model from Hugging Face
- Configured the embedding pipeline to run fully offline and CPU-only
- Applied strict dependency version pinning to ensure Windows compatibility
- Stored vector embeddings in a Chroma vector database
- Enabled semantic similarity search over document chunks

### ⚙️ Platform-Specific Configuration
To ensure stable execution on Windows systems, the embedding stack was configured with carefully selected versions:

- CPU-only PyTorch stack (no CUDA dependency)
- Compatible `sentence-transformers`, `transformers`, and `tokenizers` versions
- Avoided known Windows-breaking updates in newer releases

This configuration prevents common runtime and installation issues observed with MiniLM on Windows environments.

### 🧠 Embedding & Retrieval Layer
This checkpoint introduces the core retrieval mechanism of the RAG pipeline, allowing the system to identify and retrieve contextually relevant document chunks based on user queries.

With embeddings and vector storage in place, the project now supports reliable semantic search over the WHO diabetes documentation.

### 🔒 Dependency Installation Safety
All dependencies were installed using the following command to prevent any automatic or silent dependency upgrades by `pip`:

```bash
pip install -r requirements.txt --no-deps
```

## 🛑 CHECKPOINT 8 — RAG WITH OPENROUTER LLAMA-3.1

### 🎯 Objective
Enable end-to-end medical question answering by integrating Retrieval-Augmented Generation (RAG) with an API-based large language model.

### ✅ What Was Completed
- Implemented a user-facing natural language question interface
- Retrieved the most relevant document chunks using MiniLM embeddings and Chroma DB
- Integrated OpenRouter as the LLM gateway
- Used LLaMA-3.1 via OpenRouter for response generation
- Generated clear, context-grounded medical answers
- Included page-level source citations for transparency
- Appended a medical safety disclaimer to all responses

### 🔁 LLM Architecture Update
This checkpoint replaces the local language model with an API-based LLM accessed through OpenRouter.  
All retrieval, chunking, embedding, and citation logic remains unchanged.

### 🧠 RAG Execution Flow
1. User submits a medical question  
2. Relevant document chunks are retrieved via MiniLM + Chroma DB  
3. Retrieved context is injected into an OpenRouter prompt  
4. LLaMA-3.1 generates a grounded answer  
5. Source citations and medical disclaimer are appended  

This checkpoint completes the full Retrieval-Augmented Generation pipeline, transforming **GlucoGuide** into a functional, scalable, and production-ready medical QA system.
