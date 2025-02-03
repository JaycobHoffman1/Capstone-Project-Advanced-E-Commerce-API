from flask import Flask
from database import db
from schema import ma
from limiter import limiter
from caching import cache
from sqlalchemy.orm import Session

from models.customer import Customer
from models.customerAccount import CustomerAccount
from models.order import Order
from models.product import Product
from models.orderProduct import order_product

from routes.customerBP import customer_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint
from routes.customerAccountBP import customer_account_blueprint

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

def init_customers_info_data():
    with Session(db.engine) as session:
        with session.begin():
            customers = [
                Customer(name='Customer One', email='customer1@example.com', phone='1234567890'),
                Customer(name='Customer Two', email='customer2@gmail.com', phone='1234567890'),
                Customer(name='Customer Three', email='customer3@hotmail.com', phone='1234567890')
            ]

            customersAccounts = [
                CustomerAccount(username='ctm1', password='password1', customer_id=1),
                CustomerAccount(username='ctm2', password='password2', customer_id=2),
                CustomerAccount(username='ctm3', password='password3', customer_id=3)
            ]

            session.add_all(customers)
            session.add_all(customersAccounts)

def configure_rate_limit():
    limiter.limit('100 per day')(customer_blueprint)

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blue_print_config(app)
    configure_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()
        init_customers_info_data()

    app.run(debug=True)