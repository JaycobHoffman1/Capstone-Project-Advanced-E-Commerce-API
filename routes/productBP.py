from flask import Blueprint
from controllers.productController import save, find_all, find_by_id, update, delete

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/id/<int:id>', methods=['GET'])(find_by_id)
product_blueprint.route('/id/<int:id>', methods=['DELETE'])(delete)
product_blueprint.route('/id/<int:id>', methods=['PUT'])(update)