from email.policy import default
from db import db
from datetime import datetime

class StoreModel(db.Model):

    __tablename__ = 'store'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    created_time = db.Column(db.Date, nullable = False, default = datetime.now)
    items = db.relationship('ItemModel', back_populates = 'store', lazy = 'dynamic')