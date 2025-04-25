
from sentence_transformers import SentenceTransformer
import logging

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")
logger.info("Loaded embedding model: all-MiniLM-L6-v2")

def embed_chunks(chunks: list[str]) -> list[list[float]]:
    """
    Generates embeddings for a list of text chunks.

    Args:
        chunks (list[str]): List of text chunks.

    Returns:
        list[list[float]]: Corresponding list of embedding vectors.
    """
    logger.info(f"Generating embeddings for {len(chunks)} chunks.")
    embeddings = model.encode(chunks).tolist()
    logger.info("Embedding generation completed.")
    return embeddings
