from sqlalchemy.orm import Session
from database import db
from models.customer import Customer
from circuitbreaker import circuit
from sqlalchemy import select

def fallback_function(customer):
    return None

@circuit(failure_threshold=1, recovery_timeout=10, fallback_function=fallback_function)
def save(customer_data):
    try:
        if customer_data['name'] == 'Failure': # 'Failure' implemented for testing purposes
            raise Exception('Failure condition triggered')
        
        with Session(db.engine) as session:
            with session.begin():
                new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
                session.add(new_customer)
                session.commit()

            session.refresh(new_customer)
            return new_customer
        
    except Exception as e:
        raise e
    
def find_all():
    query = select(Customer)
    customers = db.session.execute(query).scalars().all()
    return customers

def find_by_id(id):
    query = select(Customer).where(Customer.id == id).filter_by(id=id)
    customer = db.session.execute(query).scalar_one_or_none()
    return customer

def update(customer_data, id):
    with Session(db.engine) as session:
        with session.begin():
            customer = find_by_id(id)
            customer.name = customer_data['name']
            customer.email = customer_data['email']
            customer.phone = customer_data['phone']
            db.session.commit()
        return customer
    
def delete(id):
    with Session(db.engine) as session:
        with session.begin():
            customer = find_by_id(id)
            if customer is None:
                return None
            db.session.delete(customer)
        db.session.commit()
    return 'Customer deleted'