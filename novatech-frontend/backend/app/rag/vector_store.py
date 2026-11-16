from functools import lru_cache
from uuid import uuid5, NAMESPACE_URL
from qdrant_client import QdrantClient, models
from app.core.config import settings
from app.rag.embeddings import embedding_dimension

@lru_cache(maxsize=1)
def get_qdrant() -> QdrantClient:
    if settings.qdrant_url:
        return QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key or None)
    path = settings.resolve_path(settings.qdrant_local_path)
    path.mkdir(parents=True, exist_ok=True)
    return QdrantClient(path=str(path))


def ensure_collection() -> None:
    client = get_qdrant()
    name = settings.qdrant_collection
    if not client.collection_exists(name):
        client.create_collection(
            collection_name=name,
            vectors_config=models.VectorParams(size=embedding_dimension(), distance=models.Distance.COSINE),
        )


def upsert_chunks(chunks: list[dict]) -> int:
    if not chunks:
        return 0
    ensure_collection()
    client = get_qdrant()
    points = []
    for chunk in chunks:
        point_id = str(uuid5(NAMESPACE_URL, chunk["chunk_id"]))
        payload = {k: v for k, v in chunk.items() if k != "embedding"}
        points.append(models.PointStruct(id=point_id, vector=chunk["embedding"], payload=payload))
    client.upsert(collection_name=settings.qdrant_collection, points=points, wait=True)
    return len(points)


def search_chunks(vector: list[float], limit: int = 5) -> list[dict]:
    ensure_collection()
    result = get_qdrant().query_points(
        collection_name=settings.qdrant_collection,
        query=vector,
        limit=limit,
        with_payload=True,
    )
    matches = []
    for point in result.points:
        payload = point.payload or {}
        matches.append({**payload, "score": point.score})
    return matches
