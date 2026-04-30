from pyspark.sql import SparkSession
from src.extract import extract
from src.transform import transform
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def main():
    spark = SparkSession.builder.appName("github_logs_aggregator").getOrCreate()
    logger.info("SparkSession created successfully")
    url = "https://api.github.com/repos/apache/spark/issues?state=all"

    df = extract(spark, url)
    logger.info("Extracted DataFrame successfully")
    result = transform(df)
    logger.info("Transformed DataFrame successfully")
    result.write.mode("overwrite").parquet("output/my_log1.parquet")
    logger.info("Saved transformed DataFrame to output/my_log1.parquet")
if __name__ == "__main__":
    main()