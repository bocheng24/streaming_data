from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("Kafka Stream").getOrCreate()

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "eshop") \
  .load()

df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)", "CAST(topic AS STRING)", "timestamp")

query = df.writeStream \
            .outputMode("append") \
            .format("console") \
            .start() \
            .awaitTermination()