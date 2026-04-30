from pyspark.sql import functions as f
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def transform(df):
    if df is None:
        logger.error("Input DataFrame is None")
        raise ValueError("Input DataFrame cannot be empty")
    logger.info("Starting data transformation")
    df = df.withColumn(
    "created_at",
    f.to_timestamp(f.col("created_at"))
)
    
    logger.info("Converted 'created_at' to timestamp format")

    df = df.withColumn("hour", f.hour(f.col("created_at"))) \
       .withColumn("day", f.dayofmonth(f.col("created_at")))
    logger.info("Extracted 'hour' and 'day' from 'created_at'")
    df = df.withColumn(
        "level",
        f.when(f.col("state") == "open", "ERROR").otherwise("INFO")
    )
    logger.info("Assigned 'level' based on 'state'")
    df = df.filter(f.col("level") == "ERROR")
    logger.info("Filtered DataFrame to include only ERROR logs")

    grouped = df.groupBy("day", "hour", "level") \
                .agg(f.count("*").alias("total_logs"))
    
    logger.info("Aggregated logs by day, hour, and level")
    logger.info("Transformation completed successfully")
    
    return grouped