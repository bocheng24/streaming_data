import requests

HOST = '127.0.0.1'
PORT = '5000'

BASE_URL = f'http://{HOST}:{PORT}/'

stores = requests.get(f'{BASE_URL}/store').json()
print(stores)

items = requests.get(f'{BASE_URL}/item').json()
print(items)