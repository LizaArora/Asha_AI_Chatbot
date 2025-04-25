
import logging

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def chunk_text(text: str, max_tokens: int = 300) -> list[str]:
    """
    Splits input text into chunks based on a maximum token (word) limit.

    Args:
        text (str): The input text to be chunked.
        max_tokens (int): Maximum number of words per chunk.

    Returns:
        list[str]: A list of text chunks.
    """
    logger.info(f"Starting text chunking with max_tokens={max_tokens}")

    # Split the text into words
    words = text.split()

    # Group words into chunks of max_tokens length
    chunks = [' '.join(words[i:i + max_tokens]) for i in range(0, len(words), max_tokens)]

    logger.info(f"Text chunked into {len(chunks)} chunks.")
    return chunks
