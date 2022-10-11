import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint('items', __name__, description = 'API Operations on Items')

@blp.route('/item')
class ItemList(MethodView):

    def get(self):
        return {'items': list(items.values())}
    
    @blp.arguments(ItemSchema)
    def post(self, item_data):

        # Check if item already exisits
        for item in items.values():
            if item_data['name'] == item['name'] and item_data['store_id'] == item['store_id']:
                abort(404, {'message': {'Item already exists'}})

        new_id = uuid.uuid4().hex
        new_item = {'id': new_id, **item_data}
        items[new_id] = new_item

        return new_item

@blp.route('/item/<string:item_id>')
class Item(MethodView):

    def get(self, item_id):
        try:
            return items[item_id]
        
        except KeyError:
            abort(404, {'message': 'Item not found'})

    @blp.arguments(ItemUpdateSchema)
    def put(self, item_up, item_id):
        
        try:
            items[item_id] |= item_up

            return {
                'message': f'{item_id} updated',
                'data': items[item_id]
            }
        
        except:
            return abort(404, {'message': 'Item not found'})

    def delete(self, item_id):
        try:
            item = items[item_id]
            del items[item_id]
            return {
                'message': f'{item_id} deleted',
                'data': item
            }
        
        except KeyError:
            return abort(404, {'message': 'Item not found'})