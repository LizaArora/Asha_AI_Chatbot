
import os
import numpy as np
from neo4j import GraphDatabase
from dotenv import load_dotenv
import logging

# Load .env variables
load_dotenv()

# Set up logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Connection details from .env
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")

# Check if environment variables are loaded successfully
if not NEO4J_URI or not NEO4J_USERNAME or not NEO4J_PASSWORD or not NEO4J_DATABASE:
    logger.error("One or more Neo4j environment variables are missing in .env file.")
else:
    logger.info("Neo4j configuration loaded successfully from .env")

# Connect to Neo4j
try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    logger.info(f"Connected to Neo4j database: {NEO4J_DATABASE}")
except Exception as e:
    logger.error(f"Error connecting to Neo4j: {e}")

# Cosine similarity function
def cosine_similarity(a, b):
    """
    Calculate the cosine similarity between two vectors.

    Args:
        a (list): First vector.
        b (list): Second vector.

    Returns:
        float: Cosine similarity score between the two vectors.
    """
    try:
        a, b = np.array(a), np.array(b)
        similarity = float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
        return similarity
    except Exception as e:
        logger.error(f"Error calculating cosine similarity: {e}")
        return 0.0  # Return 0.0 in case of error

# Function to find top-k relevant text chunks
def find_relevant_chunks(query_vector: list[float], top_k: int = 5) -> list[str]:
    """
    Find the top-k relevant chunks from the Neo4j database based on cosine similarity.

    Args:
        query_vector (list): Embedding of the user's question.
        top_k (int): The number of top chunks to return.

    Returns:
        list: A list of the top-k relevant chunk texts.
    """
    try:
        with driver.session(database=NEO4J_DATABASE) as session:
            result = session.run("""
                MATCH (c:Chunk)
                WHERE c.embedding IS NOT NULL
                RETURN c.text AS text, c.embedding AS embedding
            """)

            scored = []
            for record in result:
                embedding = record["embedding"]
                if embedding is None:
                    logger.warning(f"⚠️ Skipping chunk with missing embedding: {record['text'][:50]}")
                    continue

                try:
                    score = cosine_similarity(query_vector, embedding)
                    scored.append((score, record["text"]))
                except Exception as e:
                    logger.error(f"⚠️ Error comparing vectors: {e}")
                    continue

            # Sort the chunks by descending similarity score
            scored.sort(reverse=True, key=lambda x: x[0])

            # Log the top-k results
            logger.info(f"Top-{top_k} relevant chunks found.")
            return [text for _, text in scored[:top_k]]

    except Exception as e:
        logger.error(f"Error finding relevant chunks: {e}")
        return []

