
import logging
from sentence_transformers import SentenceTransformer

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the sentence transformer model
# model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

logger.info("SentenceTransformer model 'all-MiniLM-L6-v2' loaded successfully.")

def embed_text(text: str) -> list[float]:
    """
    Converts input text into a vector embedding using a pre-trained model.

    Args:
        text (str): The input string to be embedded.

    Returns:
        list[float]: The embedding vector as a list of floats.
    """
    try:
        logger.info(f"Embedding text: {text[:50]}...")  # Show first 50 characters
        embedding = model.encode([text])[0].tolist()
        logger.info("Text embedded successfully.")
        return embedding
    except Exception as e:
        logger.error(f"Error while embedding text: {e}")
        raise
