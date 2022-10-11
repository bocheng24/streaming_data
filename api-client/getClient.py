import requests
from faker import Faker
import random

HOST = '127.0.0.1'
PORT = '5000'

BASE_URL = f'http://{HOST}:{PORT}/'

fake = Faker()

def newStore():

    return {
        'name': fake.company()
    }

def newItem(store_id):

    price = round(random.random() * 10, 2)

    return {
        'name': fake.text(),
        'price': price,
        'store_id': store_id
    }

stores = requests.get(f'{BASE_URL}/store').json()
print('---------Initial Store')
print(stores)

for _ in range(5):
    print(newStore())
    store = requests.post(f'{BASE_URL}/store', json = newStore())
    # print(store)

stores = requests.get(f'{BASE_URL}/store').json()
print('---------Stores after post')
print(stores)

for _ in range(5):
    store = random.choice(stores)
    store_id = store['id']

    item = requests.post(f'{BASE_URL}/item', json = newItem(store_id))

items = requests.get(f'{BASE_URL}/item').json()
print(items)





