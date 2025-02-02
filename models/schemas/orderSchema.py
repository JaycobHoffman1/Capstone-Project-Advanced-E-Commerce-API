from marshmallow import fields
from schema import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=True)
    customer_id = fields.Integer(required=True)
    products = fields.Nested('ProductSchemaId', many=True) # For handling multiple products

# Create an instance of the OrderSchema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True) # For handling multiple orders