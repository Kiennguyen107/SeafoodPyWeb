from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=True)
    created_date = db.Column(db.DateTime, nullable=False)


class Order(db.Model):
    id_cus = db.Column(db.Integer, db.ForeignKey(Customer.id))
    id = db.Column(db.Integer, primary_key=True)
    name_PD = db.Column(db.String(40), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now)
    edited = db.Column(db.DateTime, onupdate=datetime.now)


class Bill(db.Model):
    id = db.Column(db.String, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_money = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now)
