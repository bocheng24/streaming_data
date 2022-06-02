from kafka import KafkaProducer
import json
from data import get_user
import time

TOPIC = 'eshop'

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(
        bootstrap_servers = ['127.0.0.1:9092'],
        value_serializer = json_serializer
    )

if __name__ == '__main__':

    i = 0
    while i < 10:
        user = get_user()
        producer.send(TOPIC, user)
        print(user)
        i += 1
        time.sleep(3)