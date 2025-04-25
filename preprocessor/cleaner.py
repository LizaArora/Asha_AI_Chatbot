
import re
import logging

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """
    Cleans the input text by removing excessive whitespace and trimming.

    Args:
        text (str): Raw input text.

    Returns:
        str: Cleaned text.
    """
    logger.info("Starting text cleaning process.")

    # Replace multiple whitespace characters (spaces, newlines, tabs) with a single space
    cleaned = re.sub(r'\s+', ' ', text).strip()

    logger.info(f"Text cleaned. Original length: {len(text)}, Cleaned length: {len(cleaned)}")
    return cleaned
