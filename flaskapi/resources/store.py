from pydoc import describe
import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import stores
from schemas import StoreSchema


blp = Blueprint('stores', __name__, description = 'API Operations on stores')

@blp.route('/store')
class StoreList(MethodView):
    def get(self):
        return {
            'stores': list(stores.values())
        }

    @blp.arguments(StoreSchema)
    def post(self, store_data):

        for store in stores:
            if store_data['name'] == store['name']:
                abort(404, {'message': 'This store has been created'})

        new_id = uuid.uuid4().hex
        new_store = {
            'id': new_id,
            **store_data
        }

        stores[new_id] = new_store

        return new_store

@blp.route('/store/<string:store_id>')
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]

        except KeyError:
            abort(404, {'message': 'Store not found'})

    def delete(self, store_id):
        try:
            store = stores[store_id]
            del stores[store_id]
            return {
                'message': f'{store_id} deleted',
                'data': store
            }

        except:
            abort(404, {'message': 'Store not found'})  

