from flask import Blueprint
from controllers.customerAccountController import find_all, login, update, delete

customer_account_blueprint = Blueprint('customer_account_bp', __name__)
customer_account_blueprint.route('/', methods=['GET'])(find_all)
customer_account_blueprint.route('/login', methods=['POST'])(login)
customer_account_blueprint.route('/id/<int:id>', methods=['PUT'])(update)
customer_account_blueprint.route('/id/<int:id>', methods=['DELETE'])(delete)