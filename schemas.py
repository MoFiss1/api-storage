from marshmallow import Schema, fields


class PlainProductSchema(Schema):
    id = fields.Int(dump_only=True)
    mark =fields.Str(required=True)
    model = fields.Str(required=True)
    description = fields.Str(required=True)
    upc = fields.Str(required=True)
    condition = fields.Str(required=True)
    weight = fields.Int(required=True)
    count = fields.Int(required=True)


class PlainStorageSchema(Schema):
    id = fields.Int(dump_only=True)
    namestorage = fields.Str()
    adress = fields.Str()


class ProductSchema(PlainProductSchema):
    storage_id = fields.Int(required=True, load_only=True)
    storage = fields.Nested(PlainStorageSchema(), dump_only=True)


class ProductUpdateSchema(Schema):
    mark =fields.Str(required=True)
    model = fields.Str(required=True)
    description = fields.Str(required=True)
    upc = fields.Str(required=True)
    condition = fields.Str(required=True)
    weight = fields.Int(required=True)
    count = fields.Int(required=True)

class StorageSchema(PlainStorageSchema):
    products = fields.List(fields.Nested(PlainProductSchema()), dump_only=True)


class ProductExistence(Schema):
    id = fields.Int(dump_only=True)
    model = fields.Str(required=True)
    count = fields.Int(required=True)
    storage = fields.Nested(PlainStorageSchema(), dump_only=True)

