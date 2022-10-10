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

@app.get('/store/<string:store_id>')
def get_store(store_id):

    try:
        return stores[store_id], 200

    except KeyError:
        return {'message': 'Store not found'}, 404

@app.delete('/store/<string:store_id>')
def del_store(store_id):
    try:
        store = stores[store_id]
        del stores[store_id]
        return {
            'message': f'{store_id} deleted',
            'data': store
        }

    except:
        return {'message': 'Store not found'}, 404

@app.get('/items')
def get_all_items():

    return {'items': list(items.values())}



@app.get('/items/<string:item_id>')
def get_item_in_store(item_id):
    try:
        return items[item_id], 200
    
    except KeyError:
        return {'message': 'Item not found'}, 404

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

@app.delete('/item/<string:item_id>')
def del_item(item_id):

    try:
        item = items[item_id]
        del items[item_id]
        return {
            'message': f'{item_id} deleted',
            'data': item
        }
    
    except KeyError:
        return {'message': 'Item not found'}, 404

@app.put('/item/<string:item_id>')
def update_item(item_id):

    item_up = request.get_json()

    if 'name' not in item_up or 'price' not in item_up:
        return {'message': "Bad request. Ensure 'price', and 'name' are included in the JSON payload."}, 400
    
    try:
        items[item_id] |= item_up

        return {
            'message': f'{item_id} updated',
            'data': items[item_id]
        }
    
    except:
        return {'message': 'Item not found'}, 404
        
