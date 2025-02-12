from sqlalchemy import select
from sqlalchemy.orm import Session
from models.customer import Customer
from models.customerAccount import CustomerAccount
from models.role import Role
from database import db
from utils.util import encode_token
from werkzeug.security import check_password_hash

def find_all():
    query = select(CustomerAccount).join(Customer).where(Customer.id == CustomerAccount.customer_id)
    customer_accounts = db.session.execute(query).scalars().all()
    return customer_accounts

def login_customer(username, password):
    user = (db.session.execute(db.select(CustomerAccount).where(CustomerAccount.username == username)).scalar_one_or_none())
    role_names = [role.role_name for role in user.roles]
    print(user)
    if user:
        if check_password_hash(user.password, password):
            auth_token = encode_token(user.id, role_names)
            resp = {
                'status': 'Success',
                'message': 'Successfully logged in',
                'auth_token': auth_token
            }

            return resp
        else:
            return None
    else:
        return None
    
def find_by_id(id):
    query = select(CustomerAccount).where(CustomerAccount.id == id).filter_by(id=id)
    customer_account = db.session.execute(query).scalar_one_or_none()
    return customer_account

def find_role_by_name(name):
    query = select(Role).where(Role.role_name == name).filter_by(role_name=name)
    role = db.session.execute(query).scalar_one_or_none()
    return role
    
def update(customer_account_data, id):
    with Session(db.engine) as session:
        with session.begin():
            customer_account = find_by_id(id)
            customer_account.username = customer_account_data['username']
            customer_account.password = customer_account_data['password']
            customer_account.roles = [find_role_by_name(role) for role in customer_account_data["role"]]
            db.session.commit()
        return customer_account
    
def delete(id):
    with Session(db.engine) as session:
        with session.begin():
            customer_account = find_by_id(id)
            if customer_account is None:
                return None
            db.session.delete(customer_account)
        db.session.commit()
    return 'Account deleted'