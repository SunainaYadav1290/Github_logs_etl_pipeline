import logging

logger = logging.getLogger(__name__)

def preprocess(data):
    logger.info("Starting preprocessing of raw JSON")

    clean_data = []

    for item in data:
        clean_data.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "state": item.get("state"),
            "created_at": item.get("created_at"),
            "number": item.get("number")
        })

    logger.info("Preprocessing completed")

    return clean_data