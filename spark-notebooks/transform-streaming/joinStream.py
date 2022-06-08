from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

HOSTNAME = '192.168.233.138'
PORT = 9999

spark = SparkSession.builder \
                    .appName('Join Streaming') \
                    .master('local[2]') \
                    .getOrCreate() 

spark.sparkContext.setLogLevel('ERROR')

usersSchema = StructType([
    StructField('id', LongType(), False),
    StructField('username', StringType(), False),
    StructField('email', StringType(), True),
    StructField('create_time', StringType(), True)
])

shopSchema = StructType([
    StructField('userId', LongType(), False),
    StructField('quantity', IntegerType(), False),
    StructField('price', DoubleType(), True)
])

users = spark.read.json('../Datasets/users.json')

def getUsers(host, port):
    
    users = spark.readStream \
                 .format('socket') \
                 .option('host', host) \
                 .option('port', port) \
                 .load() \
                 .select(from_json(col('value'), usersSchema).alias('users')) \
                 .selectExpr('users.id as id', 'users.username as username', 'users.email as email', 'users.create_time as create_time')

    return users

def getShop(host, port):

    shopStream = spark.readStream \
                      .format('socket') \
                      .option('host', host) \
                      .option('port', port) \
                      .load() \
                      .select(from_json(col('value'), shopSchema).alias('shop')) \
                      .selectExpr('shop.userId as userId', 'shop.quantity as quantity', 'shop.price as price')

    return shopStream


def writeStreamDF(df, format = 'console', mode = 'append'):

    df.writeStream \
      .format(format) \
      .outputMode(mode) \
      .start() \
      .awaitTermination()


def joinShop(shop, joinType = 'inner'):

    condition = users.id == shop.userId

    usersShop = shop.join(users, condition, joinType)
    writeStreamDF(usersShop)

def joinStreaming(leftStm, rightStm, joinType = 'inner'):

    condition = leftStm.id == rightStm.userId

    wholeDf = leftStm.join(rightStm, condition, joinType)
    writeStreamDF(wholeDf)


if __name__ == '__main__':

    usersStm = getUsers(HOSTNAME, 9998)
    shopStm = getShop(HOSTNAME, PORT)
    
    joinShop(shopStm)

