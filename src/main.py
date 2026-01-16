# import warnings
# from langchain_core._warnings import LangChainDeprecationWarning

# warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

from config import PDF_PATH

load_dotenv()

SYSTEM_PROMPT = """x
You are GlucoGuide, a medical document assistant.

You MUST follow these rules:
1. Answer ONLY using the provided context.
2. If the answer is not present in the context, say:
   "I don't know based on the provided document."
3. Do NOT use outside medical knowledge.
4. Do NOT give diagnosis or treatment advice.
5. Be clear, concise, and factual.
"""


def answer_question(query, vectorstore, llm):
    results = vectorstore.similarity_search_with_score(query, k=3)

    context = ""
    sources = set()

    for doc, score in results:
        context += doc.page_content + "\n\n"
        sources.add(doc.metadata.get("page"))

    final_prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(final_prompt)

    return response.content, sorted(sources)


def main():
    print("🚀 GlucoGuide starting (RAG + OpenRouter LLaMA)...")

    # 1. Load PDF
    loader = PyPDFLoader(str(PDF_PATH))
    documents = loader.load()

    # 2. Split text  ✅ REQUIRED
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)  # ← THIS WAS MISSING / MISPLACED

    # 3. Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 4. Vector store
    CHROMA_DIR = "data/processed/chroma_db"

    if Path(CHROMA_DIR).exists():
        vectorstore = Chroma(
            persist_directory=CHROMA_DIR,
            embedding_function=embeddings
        )
    else:
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=CHROMA_DIR
        )

    # 5. LLM
    llm = ChatOpenAI(
        model="meta-llama/llama-3.2-3b-instruct:free",
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0.2
    )


    # 6. Chat loop

    print("\n💬 Ask questions about the WHO diabetes document.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("🧑‍⚕️ Question: ")

        if query.lower() in ["exit", "quit"]:
            print("👋 Exiting GlucoGuide.")
            break

        answer, sources = answer_question(query, vectorstore, llm)

        print("\n🩺 Answer:\n")
        print(answer)
        print("\n📚 Sources (PDF pages):", sources)
        print("\n⚠️ Disclaimer: Educational use only. Not medical advice.\n")


if __name__ == "__main__":
    main()
