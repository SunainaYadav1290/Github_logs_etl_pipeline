
from pyspark.sql import functions as f
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def transform(df):

    if df is None or df.rdd.isEmpty():
        logger.error("Input DataFrame is empty")
        raise ValueError("Input DataFrame cannot be empty")
    
    logger.info("Starting data transformation")

    required_cols = ["id", "title", "state", "created_at", "number"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    df = df.select("id", "title", "state", "created_at", "number")

    df = df.dropDuplicates(["id"])

    df = df.dropna(subset=["id", "created_at", "state"])

    df = df.withColumn(
        "created_at",
        f.to_timestamp("created_at", "yyyy-MM-dd'T'HH:mm:ss'Z'")
    )

    df = df.withColumn("date", f.to_date("created_at"))

    df = df.withColumn("hour", f.hour("created_at")) \
           .withColumn("day", f.dayofmonth("created_at"))

    df = df.withColumn(
        "level",
        f.when(f.col("state") == "open", "ERROR").otherwise("INFO")
    )

    grouped = df.groupBy("date", "day", "hour", "level") \
                .agg(f.count("*").alias("total_logs")) \
                .orderBy("date", "hour")

    logger.info("Transformation completed successfully")

    return grouped