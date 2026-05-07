import time
import requests
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract(url):
    logger.info(f"Starting data extraction from {url}")
    token = os.getenv("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "data-engineering-project"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    all_data = []
    

    while url:
        
        logger.info(f"Fetching URL: {url}")

        response = requests.get(url, headers=headers)

        # Handle rate limit
        if response.status_code == 403:
            logger.warning("Rate limit hit. Waiting for 30 seconds...")
            time.sleep(30)
            continue

        if response.status_code != 200:
            raise Exception(f"API failed: {response.status_code}")

        data = response.json()
        all_data.extend(data)

        logger.info(f"Fetched {len(data)} records")

        # Pagination using Link header
        if "next" in response.links:
            url = response.links["next"]["url"]
        else:
            logger.info("No more pages. Ending pagination.")
            break

    return all_data