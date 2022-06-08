from pyspark.sql import SparkSession
from pyspark.sql.functions import *

HOSTNAME = '192.168.233.138'
PORT = 9999

spark = SparkSession.builder \
                    .appName('Streaming Aggregation') \
                    .master('local[2]') \
                    .getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

def socketLines(host, port):

    lines = spark.readStream \
                 .format('socket') \
                 .option('host', host) \
                 .option('port', port) \
                 .load()
    
    return lines

def countStreamLines(lines):

    counts = lines.selectExpr('count(*) as total')

    counts.writeStream \
          .format('console') \
          .outputMode('complete') \
          .start() \
          .awaitTermination()

def sumNums(lines):

    price = lines.select(col('value').cast('double').alias('price'))

    total = price.select(sum(col('price')).alias('Total Price'))

    total.writeStream \
         .format('console') \
         .outputMode('complete') \
         .start() \
         .awaitTermination()

if __name__ == '__main__':

    lines = socketLines(HOSTNAME, PORT)
    # countStreamLines(lines)
    sumNums(lines)