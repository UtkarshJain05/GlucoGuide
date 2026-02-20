from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# PDF path
PDF_PATH = RAW_DATA_DIR / "who_diabetes_guide.pdf"

# Chroma DB path
CHROMA_DIR = PROCESSED_DATA_DIR / "chroma_db"