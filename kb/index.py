import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from docx import Document
from PyPDF2 import PdfReader

DATA_DIR = "data/properties"
INDEX_DIR = "data/vectorstore"
EMBED_MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def read_docx(path):
    doc = Document(path)
    return "\n".join([para.text.strip() for para in doc.paragraphs if para.text.strip()])

def read_pdf(path):
    reader = PdfReader(path)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def chunk_text(text, max_tokens=100):
    sentences = text.split(".")
    chunks = []
    current = ""
    for s in sentences:
        if len((current + s).split()) > max_tokens:
            chunks.append(current.strip())
            current = s
        else:
            current += " " + s
    if current.strip():
        chunks.append(current.strip())
    return chunks

def build_kb():
    documents = []
    for filename in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, filename)
        if filename.endswith(".docx"):
            raw = read_docx(path)
        elif filename.endswith(".pdf"):
            raw = read_pdf(path)
        else:
            continue

        chunks = chunk_text(raw)
        for chunk in chunks:
            documents.append({
                "content": chunk,
                "source": filename
            })

    embeddings = EMBED_MODEL.encode([d["content"] for d in documents], show_progress_bar=True)
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    with open(os.path.join(INDEX_DIR, "documents.json"), "w") as f:
        json.dump(documents, f, indent=2)

    faiss.write_index(index, os.path.join(INDEX_DIR, "faiss_index.bin"))

    print(f"✅ Built KB index with {len(documents)} chunks.")

if __name__ == "__main__":
    build_kb()
 
