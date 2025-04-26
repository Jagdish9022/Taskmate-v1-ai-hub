import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")  

qdrant_client = QdrantClient(url=QDRANT_URL)
