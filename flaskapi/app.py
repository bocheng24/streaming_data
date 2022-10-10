from flask import Flask, request

app = Flask(__name__)

stores = [{
    'name': 'elago',
    'items': [
        {
            'name': 'Compatible with iPhone 13 Pro Case, Liquid Silicone Case, Full Body Screen Camera Protective Cover, Shockproof, Slim Phone Case, Anti-Scratch Soft Microfiber Lining, 6.1 inch',
            'price': 12.99,
            'colors': ['Black', 'Brown', 'Burgundy', 'Dark Grey', 'Dark Turquoise']
        },

        {
            'name': 'Hybrid Clear Case Compatible with iPhone 14 Case- 6.1 Inch - US Military Grade Drop Protection, PC + TPU Hybrid Technology, Reduced Yellowing, Crystal Clear, Full Body Protection',
            'price': 11.99,
            'colors': ['Black', 'Clear']
        }
    ]
}]

@app.get('/stores')
def get_stores():
    return {
        'status': 'Success',
        'data': stores
    }

@app.post('/store')
def create_store():

    req_data = request.get_json()

    new_store = {
        'name': req_data['name'],
        'items': []
    }

    stores.append(new_store)

    return new_store, 201

@app.post('/store/<string:name>/item')
def add_item(name):
    req_data = request.get_json()
    for store in stores:
        if name == store['name']:

            new_item = {'name': req_data['name'], 'price': req_data['price']}
            store['items'].append(new_item)
            return new_item
        
        return {'message': 'Store not found'}, 404

@app.get('/store/<string:name>')
def get_store(name):

    for store in stores:
        if name == store['name']:
            return store
    
    return {'message': 'Store not found'}, 404

@app.get('/store/<string:name>/items')
def get_store_items(name):

    for store in stores:
        if name == store['name']:
            return {'items': store['items']}, 200

    return {'message': 'Store not found'}, 404
