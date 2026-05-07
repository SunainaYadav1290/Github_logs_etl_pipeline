from pyspark.sql import functions as f

def get_last_loaded_timestamp(spark, output_path):
    try:
        df_existing = spark.read.parquet(output_path)
        last_ts = df_existing.agg(f.max("created_at")).collect()[0][0]
        return last_ts
    except:
        return None