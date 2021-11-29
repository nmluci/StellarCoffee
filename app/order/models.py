from dataclasses import dataclass
from enum import unique
from operator import delitem
from re import L
from app.baseModel import db

class Orders(db.Model):
    __tablename__ = "Orders"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    done = db.Column(db.Boolean, nullable=False)
    username = db.Column(db.Text, db.ForeignKey("Userdata.username", ondelete="SET NULL", onupdate="CASCADE"))
    grand_price = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("Events.id", ondelete="SET NULL", onupdate="CASCADE"))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class OrderItems(db.Model):
    __tablename__ = "Orders"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    order_id = db.Column(db.Integer, db.ForeignKey("Orders.id", ondelete="SET NULL", onupdate="CASCADE"))
    username = db.Column(db.Text, db.ForeignKey("Userdata.username", ondelete="SET NULL", onupdate="CASCADE"))
    item_name = db.Column(db.Text, db.ForeignKey("Inventory.name", ondelete="SET NULL", onupdate="CASCADE"))
    sum = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Events(db.Model):
    __tablename__ = "Events"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Text, unique=True)
    item_name = db.Column(db.Text, db.ForeignKey("Inventory.name", ondelete="SET NULL", onupdate="CASCADE"))
    event_date = db.Column(db.Date, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

@dataclass
class Orders: 
    orderId: int
    id: int
    itemName: str = None
    done: bool = False
    username: str = None
    sum: int = 0
    price: int = 0

    def toDict(cls):
        res = dict()
        res["order_id"] = cls.orderId
        res["id"] = cls.id
        
        if cls.itemName:
            res["item_name"] = cls.itemName
            res["done"] = cls.done
            res["sum"] = cls.sum
            res["price"] = cls.price

@dataclass
class UserOrder:
    username: str
    order_id: int = 0
    done: bool = False
    total_price: int = 0
    event_id: int = None
    orders = list[Orders]

    def toDict(cls):
        res = dict()
        res["username"] = cls.username
        if cls.order_id:
            res["order_id"] = cls.order_id
            res["done"] = cls.done
            res["event_id"] = cls.event_id
            res["total_price"] = cls.total_price
        
        if len(cls.orders) >= 1:
            res["orders"] = list(order for order in cls.orders)
        
        return res

@dataclass
class TodaySpecialData:
    item_id: int
    name: str
    price: int

    def toDict(cls):
        return {
            "id": cls.item_id,
            "name": cls.name,
            "price": cls.price,
        }

@dataclass
class TodayEventData:
    event_id: int
    name: str
    disc_amount: int

    def toDict(cls):
        return {
            "event_id": cls.event_ide,
            "title":  cls.name,
            "disc_amount": cls.disc_amount
        }
