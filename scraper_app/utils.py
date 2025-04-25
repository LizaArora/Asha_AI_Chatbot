
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def fetch_url_text(url: str) -> dict:
    """
    Uses Selenium to open the given URL in a headless browser,
    scrolls the page to trigger lazy loading, and extracts visible text content.

    Args:
        url (str): The URL to scrape.

    Returns:
        dict: A dictionary with the page title, visible text, and original URL.
    """
    logger.info(f"Initializing headless browser for URL: {url}")

    # Set up headless Chrome browser options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Launch browser
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    logger.info("Browser launched and navigated to URL")

    # Wait for body to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        logger.info("Page body loaded successfully")
    except Exception as e:
        logger.warning(f"Timeout waiting for body tag: {e}")

    # Scroll down to trigger lazy-loaded content
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(3):  # Scroll multiple times to ensure full content loads
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)  # Wait for dynamic content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            logger.info("Reached end of page during scroll")
            break
        last_height = new_height
        logger.debug(f"Scrolled page iteration {i+1}")

    # Extract title and raw text
    title = driver.title
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Remove scripts, styles, and noscript tags
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)
    driver.quit()
    logger.info(f"Successfully extracted content from URL: {url}")

    return {
        "title": title,
        "text": text,
        "url": url
    }
