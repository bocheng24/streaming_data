import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import StoreModel

from schemas import ItemSchema, ItemUpdateSchema
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel


blp = Blueprint('items', __name__, description = 'API Operations on Items')

@blp.route('/item')
class ItemList(MethodView):

    @blp.response(200, ItemSchema(many = True))
    def get(self):
        return ItemModel.query.all()
    
    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message = str(e))

        return item

@blp.route('/item/<string:item_id>')
class Item(MethodView):

    @blp.response(200, ItemSchema)
    def get(self, item_id):

        item = ItemModel.query.get_or_404(item_id)
        return item

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemUpdateSchema)
    def put(self, item_up, item_id):
        
        item = ItemModel.query.get_or_404(item_id)
        item.price = item_up['price']
        item.name = item_up['name']
        
        try:
            db.session.add(item)
            db.session.commit()
            return item
        except SQLAlchemyError as e:
            abort(404, {'message': str(e)})
    
    def delete(self, item_id):

        item = ItemModel.query.get_or_404(item_id)

        db.session.delete(item)
        db.session.commit()
        return {'message': 'Deleted'}