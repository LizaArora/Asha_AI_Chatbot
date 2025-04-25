
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load .env variables
load_dotenv()

# Get Neo4j connection details from .env
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")

# Log connection info (but not password)
logger.info(f"Connecting to Neo4j at {NEO4J_URI} with user {NEO4J_USERNAME}")

# Establish Neo4j driver connection
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

def store_chunks(url: str, title: str, chunks: list[str], embeddings: list[list[float]]):
    """
    Stores text chunks and their embeddings into Neo4j, linking each chunk to a document node by URL.

    Args:
        url (str): The source URL of the document.
        title (str): The title of the document (currently unused but could be stored later).
        chunks (list[str]): List of chunked text strings.
        embeddings (list[list[float]]): Corresponding list of embedding vectors.
    """
    logger.info(f"Storing {len(chunks)} chunks for document: {url}")

    with driver.session(database=NEO4J_DATABASE) as session:
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            try:
                session.run("""
                    MERGE (d:Document {url: $url})
                    CREATE (c:Chunk {
                        id: $id,
                        text: $text,
                        embedding: $embedding
                    })-[:BELONGS_TO]->(d)
                """, {
                    "url": url,
                    "id": f"{url}_chunk_{i}",
                    "text": chunk,
                    "embedding": embedding
                })
                logger.debug(f"Stored chunk {i + 1}/{len(chunks)}")
            except Exception as e:
                logger.error(f"Failed to store chunk {i + 1}: {e}")

    logger.info("All chunks stored successfully.")
