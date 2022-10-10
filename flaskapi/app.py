from flask import Flask, request
import uuid

from db import stores, items

app = Flask(__name__)

@app.get('/stores')
def get_stores():
    return {
        'stores': list(stores.values())
    }

@app.post('/store')
def create_store():

    store_data = request.get_json()

    new_id = uuid.uuid4().hex
    new_store = {
        'id': new_id,
        **store_data
    }

    stores[new_id] = new_store

    return new_store, 201

@app.post('/item')
def add_item():
    item_data = request.get_json()

    if 'store_id' not in item_data:

        return {'message': 'Internal Error, cannot find any store id'}, 500

    if item_data['store_id'] in stores:
        new_id = uuid.uuid4().hex

        new_item = {'id': new_id, **item_data}

        items[new_id] = new_item

        return new_item, 201

    return {'message': 'Store not found'}, 404

@app.get('/items')
def get_all_items():

    return {'items': list(items.values())}

@app.get('/store/<string:store_id>')
def get_store(store_id):

    try:
        return stores[store_id], 200

    except KeyError:
        return {'message': 'Store not found'}, 404

@app.get('/items/<string:item_id>')
def get_item_in_store(item_id):
    try:
        return items[item_id], 200
    
    except KeyError:
        return {'message': 'Item not found'}, 404
