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

## 🛑 CHECKPOINT 7 — LOCAL EMBEDDINGS WITH MINI-LM

### 🎯 Objective
Enable semantic understanding by generating and storing document embeddings locally.

### ✅ What Was Completed
- Implemented local embedding generation using a MiniLM model from Hugging Face
- Generated vector representations fully offline
- Stored embeddings in a Chroma vector database
- Enabled semantic similarity search over document chunks

### 🧠 Embedding & Retrieval Layer
This checkpoint introduces the core retrieval mechanism of the RAG pipeline, allowing the system to identify and retrieve contextually relevant document chunks based on user queries.

With embeddings and vector storage in place, the project now supports true semantic search over the WHO diabetes documentation.
