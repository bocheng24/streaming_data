from db import db

class ItemModel(db.Model):

    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    price = db.Column(db.Float(precision = 2), unique = False, nullable = False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), unique = False, nullable = False)
    store = db.relationship('StoreModel', back_populates = 'items')