from models.schemas.customerAccountSchema import customer_accounts_schema, customer_account_schema
from services import customerAccountService
from marshmallow import ValidationError
from flask import jsonify, request
from utils.util import role_required, token_required

@role_required('admin')
@token_required
def find_all():
    customer_accounts = customerAccountService.find_all()
    return customer_accounts_schema.jsonify(customer_accounts), 200

@role_required('admin')
@token_required
def login():
    customer = request.json
    user = customerAccountService.login_customer(customer['username'], customer['password'])
    if user:
        return jsonify(user), 200
    else:
        resp = {
            'status': 'Error',
            'message': 'User does not exist'
        }

        return jsonify(resp), 404

@role_required('admin')
@token_required  
def update(id):
    try:
        # Validate and deserialize input
        customer_account_data = customer_account_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer = customerAccountService.update(customer_account_data, id)
    return customer_account_schema.jsonify(customer), 200

@role_required('admin')
@token_required
def delete(id):
    is_deleted = customerAccountService.delete(id)

    if is_deleted is None:
        return jsonify({ 'message': 'Account not found' }), 404
    return jsonify({ 'message': is_deleted })