from pyspark.sql import SparkSession
from pyspark.sql.functions import *

HOSTNAME = '192.168.2.35'
PORT = 9999

spark = SparkSession.builder.appName('socket streaming').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

def socketLines(HOSTNAME, PORT):
    lines = spark.readStream \
                    .format('socket') \
                    .option('host', HOSTNAME) \
                    .option('port', PORT) \
                    .load()
    
    return lines

def printLines(lines):
    query = lines.writeStream \
                    .outputMode("append") \
                    .format("console") \
                    .start()

    query.awaitTermination()
        
if __name__ == '__main__':

    lines = socketLines(HOSTNAME, PORT)
    printLines(lines)

