import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load(df, output_path):

    if df is None or df.rdd.isEmpty():
        logger.error("Input DataFrame is empty")
        raise ValueError("DataFrame cannot be empty")

    if "date" not in df.columns:
        raise ValueError("'date' column not found for partitioning")

    logger.info(f"Starting data load to {output_path}")

    try:
        df = df.repartition("date")
        
        df.write \
          .mode("append") \
          .partitionBy("date") \
          .option("compression", "snappy") \
          .parquet(output_path)

        logger.info("Data successfully written in Parquet format with partitioning")
        
    except Exception as e:
        logger.error(f"Error while writing data: {e}")
        raise

    logger.info("Load process completed successfully")