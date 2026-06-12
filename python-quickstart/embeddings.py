"""
DEVUP AI — Embeddings & Semantic Search
=========================================
Generate text embeddings for semantic search, clustering, and RAG pipelines.

Install:
    pip install openai numpy
    
Usage:
    export DEVUPAI_API_KEY="dvup_your_key_here"
    python embeddings.py
"""

import os
import numpy as np
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEVUPAI_API_KEY"),
    base_url="https://api.devupai.com/v1",
)

EMBEDDING_MODEL = "BAAI/bge-m3"  # Best multilingual model — supports Arabic, French, English


def get_embedding(text: str, model: str = EMBEDDING_MODEL) -> list[float]:
    """Generate an embedding vector for a single text."""
    text = text.replace("\n", " ")
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding


def get_embeddings(texts: list[str], model: str = EMBEDDING_MODEL) -> list[list[float]]:
    """Generate embedding vectors for multiple texts in one API call."""
    texts = [t.replace("\n", " ") for t in texts]
    response = client.embeddings.create(input=texts, model=model)
    return [item.embedding for item in response.data]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two embedding vectors."""
    a_np = np.array(a)
    b_np = np.array(b)
    return float(np.dot(a_np, b_np) / (np.linalg.norm(a_np) * np.linalg.norm(b_np)))


def semantic_search(
    query: str,
    documents: list[str],
    top_k: int = 3,
) -> list[tuple[float, str]]:
    """
    Find the most semantically similar documents to a query.
    Returns list of (score, document) tuples sorted by relevance.
    """
    print(f"🔍 Searching for: '{query}'")

    # Get embeddings for query and all documents in parallel
    all_texts = [query] + documents
    all_embeddings = get_embeddings(all_texts)

    query_embedding = all_embeddings[0]
    doc_embeddings = all_embeddings[1:]

    # Compute similarities
    scores = [
        (cosine_similarity(query_embedding, doc_emb), doc)
        for doc_emb, doc in zip(doc_embeddings, documents)
    ]

    # Sort by similarity descending
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:top_k]


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Example knowledge base (mix of Arabic, French, English — BGE-M3 handles all)
    knowledge_base = [
        "DEVUP AI is Algeria's first AI inference gateway with DZD billing.",
        "You can pay for AI API access using Edahabia or CIB cards.",
        "The platform supports 170+ open-source models including Llama, Qwen, and Mistral.",
        "DEVUP AI offers zero cold starts and sub-second time-to-first-token.",
        "مرحبا بك في ديفاب أي، منصة الذكاء الاصطناعي الجزائرية",
        "Vous pouvez accéder à plus de 170 modèles IA via une API compatible OpenAI.",
        "API keys can be scoped with model whitelists and per-key spending budgets.",
        "The platform enforces strict zero-retention policies — your data is never stored.",
    ]

    # Test 1: English query
    print("\n=== Semantic Search Demo ===\n")
    results = semantic_search(
        query="How do I pay for the API?",
        documents=knowledge_base,
        top_k=3,
    )
    print("\nTop results:")
    for score, doc in results:
        print(f"  [{score:.3f}] {doc}")

    # Test 2: French query — BGE-M3 handles cross-lingual search
    print()
    results = semantic_search(
        query="Quels modèles sont disponibles?",
        documents=knowledge_base,
        top_k=3,
    )
    print("\nTop results:")
    for score, doc in results:
        print(f"  [{score:.3f}] {doc}")

    # Test 3: Similarity between two texts
    print("\n=== Similarity Check ===")
    text_a = "Pay AI with Algerian Dinar"
    text_b = "Use DZD to access AI models"
    emb_a = get_embedding(text_a)
    emb_b = get_embedding(text_b)
    sim = cosine_similarity(emb_a, emb_b)
    print(f"Similarity between:\n  '{text_a}'\n  '{text_b}'\n  → {sim:.4f} ({sim*100:.1f}% similar)")
