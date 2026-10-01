from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.core.config import settings


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=settings.gemini_api_key
)


client = QdrantClient(
    url=settings.qdrant_url
)


vector_store = QdrantVectorStore(
    client=client,
    collection_name=settings.qdrant_collection,
    embedding=embeddings
)