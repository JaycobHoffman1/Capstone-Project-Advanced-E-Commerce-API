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
