
import anyio
import logging
from scraper_app.utils import fetch_url_text

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def scrape_url(url: str) -> dict:
    """
    Asynchronously scrapes the given URL by offloading the synchronous
    `fetch_url_text` function to a background thread.

    Args:
        url (str): The URL to scrape.

    Returns:
        dict: A dictionary containing the scraped title and text content.
    """
    logger.info(f"Starting scrape for URL: {url}")
    
    try:
        result = await anyio.to_thread.run_sync(fetch_url_text, url)
        logger.info(f"Successfully scraped URL: {url}")
        return result
    except Exception as e:
        logger.error(f"Error scraping URL {url}: {e}")
        raise
