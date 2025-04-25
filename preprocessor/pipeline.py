
import logging
from preprocessor.cleaner import clean_text
from preprocessor.chunker import chunk_text
from preprocessor.embedder import embed_chunks
from preprocessor.neo4j_store import store_chunks

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_and_store(url: str, title: str, raw_text: str):
    """
    Complete preprocessing pipeline:
    Cleans raw text, chunks it, embeds the chunks, and stores them in Neo4j.

    Args:
        url (str): Source URL of the content.
        title (str): Title of the web page.
        raw_text (str): Raw text scraped from the web page.
    """
    try:
        logger.info(f"Starting preprocessing for URL: {url}")

        # Step 1: Clean the raw text
        cleaned = clean_text(raw_text)
        logger.info("Text cleaned successfully.")

        # Step 2: Split the cleaned text into chunks
        chunks = chunk_text(cleaned)
        logger.info(f"Text chunked into {len(chunks)} pieces.")

        # Step 3: Generate embeddings for each chunk
        embeddings = embed_chunks(chunks)
        logger.info("Embeddings generated successfully.")

        # Step 4: Store the chunks and embeddings in Neo4j
        store_chunks(url, title, chunks, embeddings)
        logger.info("Chunks and embeddings stored in Neo4j successfully.")

    except Exception as e:
        logger.error(f"Error during preprocessing and storing: {e}")
        raise
