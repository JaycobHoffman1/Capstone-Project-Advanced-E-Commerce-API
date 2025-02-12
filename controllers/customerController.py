from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required, role_required

@role_required('admin')
@token_required
def save():
    try:
        # Validate and deserialize input
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer_save = customerService.save(customer_data)
    
    if customer_save is not None:
        return customer_schema.jsonify(customer_save), 201
    else:
        return jsonify({ 'message': 'Fallback method error activated', 'body': customer_data }), 400
    
@cache.cached(timeout=1)
@role_required('admin')
@token_required
def find_all():
    customers = customerService.find_all()
    return customers_schema.jsonify(customers), 200

@role_required('admin')
@token_required
def update(id):
    try:
        # Validate and deserialize input
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer = customerService.update(customer_data, id)
    return customer_schema.jsonify(customer), 200

@role_required('admin')
@token_required
def delete(id):
    is_deleted = customerService.delete(id)

    if is_deleted is None:
        return jsonify({ 'message': 'Customer not found' }), 404
    return jsonify({ 'message': is_deleted })