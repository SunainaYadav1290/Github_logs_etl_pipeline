from pyspark.sql import SparkSession
from src.extract import extract
from src.preprocess import preprocess
from src.transform import transform
from src.load import load  
from src.utils import get_last_loaded_timestamp
from pyspark.sql.types import StructType, StructField, StringType,LongType
spark = SparkSession.builder.appName("github_logs").getOrCreate()

url = "https://api.github.com/repos/apache/spark/issues?state=all"
output_path = "/mnt/c/Users/HP/Desktop/output"   # choose your path

# Step 1: Extract
data = extract(url)

# Step 2: Preprocess
clean_data = preprocess(data)
schema = StructType([
    StructField("id", LongType(), True),
    StructField("title", StringType(), True),
    StructField("state", StringType(), True),
    StructField("created_at", StringType(), True),
    StructField("number", LongType(), True)
])
# Step 3: Create DataFrame
df = spark.createDataFrame(clean_data,schema=schema)
# Step 4: Transform

df = transform(df)
# Step 5: Incremental logic
last_ts = get_last_loaded_timestamp(spark, output_path)

if last_ts:
    print(f"Last loaded timestamp: {last_ts}")
    df = df.filter(f.col("created_at") > last_ts)


# Step 5: Load 
load(df, output_path)
df = spark.read.parquet("/mnt/c/Users/HP/Desktop/output")
df.show()
spark.stop()