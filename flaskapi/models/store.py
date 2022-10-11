from enum import unique
from db import db

class StoreModel(db.Model):

    __tablename__ = 'store'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)

    db.relationship('ItemModel', back_populates = 'store', lazy = 'dynamic')