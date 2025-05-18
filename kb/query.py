import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_DIR = "data/vectorstore"
EMBED_MODEL = SentenceTransformer('all-MiniLM-L6-v2')

with open(f"{INDEX_DIR}/documents.json") as f:
    DOCUMENTS = json.load(f)

INDEX = faiss.read_index(f"{INDEX_DIR}/faiss_index.bin")

def search_kb(query: str, k=3):
    query_embedding = EMBED_MODEL.encode([query])
    D, I = INDEX.search(np.array(query_embedding), k)
    results = [DOCUMENTS[i] for i in I[0]]
    return results
 
