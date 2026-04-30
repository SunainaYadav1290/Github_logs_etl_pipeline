import requests
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def extract(spark, url):
    logger.info(f"Starting data extraction from {url}")
    if not url:
        logger.error("URL is empty")
        raise ValueError("URL cannot be empty")
    try:
       response = requests.get(url,timeout=5)
    except Exception as e:
       logger.error(f"Error during API call: {e}")
       raise 
    if response.status_code != 200:
        logger.error(f"API request failed with status code: {response.status_code}")
        raise Exception(f"API Request failed: {response.status_code}")
    logger.info(f"API request successful: {response.status_code}")
    data = response.json()
    logger.info(f"Extracted {len(data)} records from API")
    cleaned_data = []
    for item in data:
        cleaned_data.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "state": item.get("state"),
            "created_at": item.get("created_at"),
            "number": item.get("number")
        })
    logger.info(f"Created DataFrame with {len(cleaned_data)} records")
    df = spark.createDataFrame(cleaned_data)
   
    return df