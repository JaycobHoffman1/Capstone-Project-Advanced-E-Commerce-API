from flask import Flask
from database import db
from schema import ma
from limiter import limiter
from caching import cache
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
from flask_cors import CORS

from models.customer import Customer
from models.customerAccount import CustomerAccount
from models.order import Order
from models.product import Product
from models.orderProduct import order_product
from models.role import Role
from models.customerManagementRole import CustomerManagementRole

from routes.customerBP import customer_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint
from routes.customerAccountBP import customer_account_blueprint
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Advanced E-commerce API'
    }
)

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)

    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(customer_account_blueprint, url_prefix='/accounts')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

def init_customers_info_data():
    with Session(db.engine) as session:
        with session.begin():
            customers = [
                Customer(name='Customer One', email='customer1@example.com', phone='1234567890'),
                Customer(name='Customer Two', email='customer2@gmail.com', phone='1234567890'),
                Customer(name='Customer Three', email='customer3@hotmail.com', phone='1234567890')
            ]

            customersAccounts = [
                CustomerAccount(username='ctm1', password=generate_password_hash('password1'), customer_id=1),
                CustomerAccount(username='ctm2', password=generate_password_hash('password2'), customer_id=2),
                CustomerAccount(username='ctm3', password=generate_password_hash('password3'), customer_id=3)
            ]

            session.add_all(customers)
            session.add_all(customersAccounts)

def init_roles_data():
    with Session(db.engine) as session:
        with session.begin():
            roles = [
                Role(role_name='admin'),
                Role(role_name='user'),
                Role(role_name='guest')
            ]

            session.add_all(roles)

def init_roles_customers_data():
    with Session(db.engine) as session:
        with session.begin():
            roles_customers = [
                CustomerManagementRole(customer_management_id=1, role_id=1),
                CustomerManagementRole(customer_management_id=2, role_id=2),
                CustomerManagementRole(customer_management_id=2, role_id=3)
            ]

            session.add_all(roles_customers)

def configure_rate_limit():
    limiter.limit('100 per day')(customer_blueprint)
    limiter.limit('100 per day')(product_blueprint)
    limiter.limit('100 per day')(order_blueprint)
    limiter.limit('100 per day')(customer_account_blueprint)

app = create_app('DevelopmentConfig')

blue_print_config(app)
configure_rate_limit()

with app.app_context():
    db.drop_all()
    db.create_all()
    init_customers_info_data()
    init_roles_data()
    init_roles_customers_data()