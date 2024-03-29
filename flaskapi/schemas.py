from dataclasses import field
from marshmallow import fields, Schema

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only = True)
    name = fields.Str(required = True)
    created_time = fields.DateTime()

class PlainItemSchema(Schema):
    id = fields.Str(dump_only = True)
    name = fields.Str(required = True)
    price = fields.Float(required = True)
    created_time = fields.DateTime()

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required = True)
    store = fields.Nested(PlainStoreSchema(), dump_only = True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only = True)