from pyspark.sql import SparkSession
from pyspark.sql.types import *

people = '../Stream_files/people'
peopleSchema = StructType([
    StructField('name', StringType(), True),
    StructField('email', StringType(), True),
    StructField('city', StringType(), True),
    StructField('mac', StringType(), True),
    StructField('timestamp', DateType(), True),
    StructField('creditcard', StringType(), True)
])

spark = SparkSession.builder.appName('file stream').getOrCreate()

def streamFile(srcFile, schema):
    streamDf = spark.readStream \
                    .json(srcFile, schema = schema)
    
    streamDf.writeStream \
            .format('console') \
            .outputMode('append') \
            .start() \
            .awaitTermination()

if __name__ == '__main__':
    streamFile(people, peopleSchema)
