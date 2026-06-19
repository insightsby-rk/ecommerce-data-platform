from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EcommercePipeline") \
    .getOrCreate()

df = spark.read.csv(
    "data/raw/customers.csv",
    header=True,
    inferSchema=True
)

print("Schema:")
df.printSchema()

print("Data:")
df.show()

spark.stop()