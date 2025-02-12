from models.product import Product
from database import db
from sqlalchemy.orm import Session
from sqlalchemy import select, update

def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit()
        session.refresh(new_product)
        return new_product
    
def find_all():
    query = select(Product)
    products = db.session.execute(query).scalars().all()
    return products

def find_by_id(id):
    query = select(Product).where(Product.id == id).filter_by(id=id)
    product = db.session.execute(query).scalar_one_or_none()
    return product

def update(product_data, id):
    with Session(db.engine) as session:
        with session.begin():
            product = find_by_id(id)
            product.name = product_data['name']
            product.price = product_data['price']
            db.session.commit(product)
        return product
    
def delete(id):
    with Session(db.engine) as session:
        with session.begin():
            product = find_by_id(id)
            if product is None:
                return None
            db.session.delete(product)
        db.session.commit()
    return 'Product deleted'