from kafka import KafkaConsumer
import json
from database import *

TOPIC = 'eshop'

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers = ['192.168.233.138:9092']
)

for msg in consumer:
    user_dict = json.loads(msg.value)
    print(user_dict)

    user = User(user_dict)
    db.session.add(user)
    db.session.commit()
    
    users = User.query.all()
    print('All users')
    print(users)