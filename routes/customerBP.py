from flask import Blueprint
from controllers.customerController import save, find_all, update, delete

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/id/<int:id>', methods=['PUT'])(update)
customer_blueprint.route('/id/<int:id>', methods=['DELETE'])(delete)