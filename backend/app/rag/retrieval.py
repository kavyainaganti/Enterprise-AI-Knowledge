from app.rag.embeddings import embed_texts
from app.rag.vector_store import search_chunks


def retrieve_relevant_chunks(question: str, top_k: int = 5) -> list[dict]:
    """Embed a question and retrieve the closest indexed document chunks."""
    query_vector = embed_texts([question])[0]
    return search_chunks(query_vector, limit=top_k)
