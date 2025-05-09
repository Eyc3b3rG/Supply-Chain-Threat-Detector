# Supply Chain Threat Detector Workflow

# ---------------------------
# STEP 1: Load Required Libraries
# ---------------------------
from dotenv import load_dotenv
load_dotenv()
import os
import zipfile
import json
import faiss
import pickle
import hashlib
import base64
from typing import List
from fastapi import FastAPI, HTTPException, Request
import requests
import PyPDF2 as pdf2
from pydantic import BaseModel
from langchain.embeddings import FakeEmbeddings
from langchain.embeddings.huggingface import HuggingFaceBgeEmbeddings
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from cryptography.fernet import Fernet
from langchain_community.embeddings import FakeEmbeddings, HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.embeddings import FakeEmbeddings
from langchain.embeddings.huggingface import HuggingFaceBgeEmbeddings
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import TextLoader


# ---------------------------
# STEP 2: Initialize Model & Embeddings
# ---------------------------

# ---------------------------
# Model Path Configuration
# ---------------------------
MODEL_NAME = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
MODEL_DIR = os.environ.get("MODEL_DIR", os.path.join(os.path.dirname(__file__), "models"))
base_model_path = os.path.join(MODEL_DIR, MODEL_NAME)

docs_path = os.path.join(os.path.dirname(__file__), "data")
index_file = "vector_index.pkl"
key_file = "secret.key"

# ---------------------------
# STEP 3: Encryption/Decryption Utils
# -------------------------------------
def generate_key():
    """
    Generates a new encryption key using the Fernet symmetric encryption system 
    and saves it to a file.

    The generated key is written to a file specified by the `key_file` variable 
    in binary mode.

    Raises:
        IOError: If there is an issue writing the key to the file.
    """
    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)

def load_key():
    return open(key_file, 'rb').read()

def encrypt_text(text: str, key: bytes) -> str:
    return Fernet(key).encrypt(text.encode()).decode()

# Optional: Simulate Graph RAG-style multi-hop context assembly
# For example, re-chunk or concatenate top N related documents



# Extend chain logic for multiple hops (placeholder simulation)




def decrypt_text(token: str, key: bytes) -> str:
    return Fernet(key).decrypt(token.encode()).decode()

if not os.path.exists(key_file):
    generate_key()
key = load_key()


def validate_data_folder(path):
    if not os.path.exists(path):
        raise RuntimeError(f"Missing folder: {path}")
    txt_files = [f for f in os.listdir(path) if f.endswith(".txt")]
    if not txt_files:
        raise RuntimeError(f"No .txt files found in: {path}")
    print(f"Found {len(txt_files)} .txt files: {txt_files}")

# ----------------------------
# Load Base Model with Adapter (Simulated Fine-Tuning)

from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel, PeftConfig 

base_model_path = base_model_path

# Simulated LoRA adapter load - adjust path to point to your LoRA folder
# Replace with valid adapter if available 

try: 
    model = AutoModelForCausalLM.from_pretrained(base_model_path)
    model = PeftModel.from_pretrained(model, "path_to_your_lora_adapter")  # Replace Path
    tokenizer = AutoTokenizer.from_pretrained(base_model_path)
    llm = model  # Assign to llm
except Exception as e:
    print("Adapter load failed or unavailable; fallback to LlamaCpp.")
    from langchain_community.llms import LlamaCpp
    llm = LlamaCpp(
        model_path=base_model_path,
        n_ctx=2048,
        n_gpu_layers=20,
        n_batch=32,
        f16_kv=True,
        verbose=False
    )

# STEP 4: Build Vector Store
# --------------------------------
def build_vectorstore():
    validate_data_folder(docs_path)
    loader = DirectoryLoader(docs_path, glob="**/*.txt")
    documents = loader.load()

    
    # Initialize the local embedding model (runs offline)
    embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    db = FAISS.from_documents(documents, embedding)
    
    
    with open(index_file, 'wb') as f:
        pickle.dump(db, f)

def load_vectorstore():
    with open(index_file, 'rb') as f:
        return pickle.load(f)

if not os.path.exists(index_file):
    build_vectorstore()
db = load_vectorstore()

# --------------------------------------
# STEP 5: Load LLM

from langchain_community.llms import LlamaCpp

try:
    
    llm = LlamaCpp(
        model_path=base_model_path,
        n_ctx=2048,
        n_gpu_layers=20,
        n_batch=32,
        f16_kv=True,
        verbose=False
    )


except Exception as e:
    print(f"Failed to load LlamaCpp model: {e}")
    raise
    # Fallback to a different model or handle the error as needed
    # For example, you could use a different model or raise an exception
# --------------------------------
# STEP 6: Build QA Chain
# ---------------------------


from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema import Document

retriever = db.as_retriever(search_kwargs={"k": 5})
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an AI that performs multi-hop threat analysis using supply chain intelligence.

Use the following combined documents to answer the query.

Context:
{context}

Question:
{question}
"""
)

qa_chain = LLMChain(llm=llm, prompt=prompt_template)

def graph_rag_query(query: str):
    docs: list[Document] = retriever.get_relevant_documents(query)
    combined_context = "\n\n".join([doc.page_content for doc in docs])
    result = qa_chain.run({"context": combined_context, "question": query})
    return result, docs

answer, source_docs = graph_rag_query(request.query)
sources = [doc.metadata.get("source", "unknown") for doc in source_docs]


# -------------------------------------
# STEP 7: API Setup
# -----------------------------------------
app = FastAPI()

# Supply Chain Threat Intelligence Sources 

sources = {
     "supply_chain_risks": "./data/supply_chain_risks.txt",
    "nist_guidance": "./data/nist_supply_chain_guidance.txt",
    "mitre_summary": "./data/mitre_system_of_trust.txt",
    "intel_paper": "./data/intel_supply_chain_protections.txt",
    "microsoft_case": "./data/microsoft_silk_typhoon_case.txt"
}

# Function to fetch content from a source URL 


class QueryRequest(BaseModel):
    query: str

@app.post("/detect")
async def detect_threat(request: QueryRequest):
    try:
       answer, source_docs = graph_rag_query(request.query)
       sources = [doc.metadata.get("source", "unknown") for doc in source_docs]
       encrypted_answer = encrypt_text(answer, key)
       return {
            "answer_encrypted": encrypted_answer,
            "sources": sources
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ---------------------------
# STEP 8: Run Locally (if needed)
# ----------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # To run the server, use the command:
    # uvicorn backend_api:app --host ..
# -----------------------------
# STEP 0: Auto-fetch PDFs and Replace .txt Files
# -----------------------------

import fitz  # PyMuPDF
from urllib.parse import urlparse

pdf_sources = {
    "intel_supply_chain_protections.txt": "https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/platform-resilience-supply-chain-paper.pdf",
    "microsoft_silk_typhoon_case.txt": "https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/06/Analyzing-Silk-Typhoon.pdf",
    "mitre_system_of_trust.txt": "https://media.defense.gov/2022/Apr/08/2002969022/-1/-1/0/SYSTEM-OF-TRUST-MITRE-WHITEPAPER.PDF",
    "nist_supply_chain_guidance.txt": "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1.pdf",
    "supply_chain_risks.txt": "https://csrc.nist.gov/csrc/media/Publications/sp/800-161/rev-1/draft/documents/sp800-161r1-draft.pdf"
}

def validate_and_extract_text_from_pdf(url, min_pages=5):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch PDF: {url}")

    with open("temp.pdf", "wb") as f:
        f.write(response.content)

    doc = fitz.open("temp.pdf")
    if doc.is_encrypted:
        raise ValueError("PDF is encrypted or restricted")
    if len(doc) < min_pages:
        raise ValueError(f"PDF has only {len(doc)} pages; minimum required is {min_pages}")

    full_text = ""
    for page in doc:
        full_text += page.get_text()

    doc.close()
    os.remove("temp.pdf")
    return full_text.strip()

def auto_update_txt_from_pdf(data_folder="./data"):
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    for txt_name, url in pdf_sources.items():
        try:
            print(f"Processing: {url}")
            content = validate_and_extract_text_from_pdf(url)
            txt_path = os.path.join(data_folder, txt_name)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated: {txt_name}")
        except Exception as e:
            print(f"Failed to update {txt_name} from {url} — {str(e)}")

# Inject auto-fetch just before vectorstore is built
if not os.path.exists(index_file):
    auto_update_txt_from_pdf()
    build_vectorstore()