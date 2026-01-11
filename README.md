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
