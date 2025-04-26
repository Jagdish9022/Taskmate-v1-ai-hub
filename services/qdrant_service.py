from config.config import qdrant_client
from qdrant_client.models import PointStruct
import uuid

def upsert_vector(collection_name: str, vector: list, payload: dict = None):
    """
    Save or update a vector into the Qdrant collection.
    """
    point_id = str(uuid.uuid4())  
    points = [
        PointStruct(
            id=point_id,
            vector=vector,
            payload=payload or {}
        )
    ]
    qdrant_client.upsert(collection_name=collection_name, points=points)
    return point_id

def search_vector(collection_name: str, query_vector: list, top_k: int = 5):
    """
    Search similar vectors from Qdrant.
    """
    hits = qdrant_client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=top_k
    )
    return hits
