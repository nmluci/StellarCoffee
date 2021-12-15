from dataclasses import dataclass
from datetime import datetime
from app.baseModel import db

class Orders(db.Model):
    __tablename__ = "Orders"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    done = db.Column(db.Boolean, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey("Userdata.uid", ondelete="SET NULL", onupdate="CASCADE"))
    grand_price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("Events.id", ondelete="SET NULL", onupdate="CASCADE"))
    date_created = db.Column(db.DateTime, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class OrderItems(db.Model):
    __tablename__ = "OrderItems"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    order_id = db.Column(db.Integer, db.ForeignKey("Orders.id", ondelete="SET NULL", onupdate="CASCADE"))
    uid = db.Column(db.Integer, db.ForeignKey("Userdata.uid", ondelete="SET NULL", onupdate="CASCADE"))
    item_name = db.Column(db.Text, db.ForeignKey("Inventory.name", ondelete="SET NULL", onupdate="CASCADE"))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Events(db.Model):
    __tablename__ = "Events"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Text)
    coupon_code = db.Column(db.Text, unique=True)
    date_start = db.Column(db.Date, nullable=False)
    date_end = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

@dataclass
class EventData:
    name: str
    coupon: str
    date_start: datetime
    date_end: datetime
    amount: int
    id: int = None

    def toDict(cls):
        return {
            "id": cls.id,
            "name": cls.name,
            "coupon_code": cls.coupon,
            "date_start": datetime.strftime(cls.date_start,"%Y-%m-%d"),
            "date_end": datetime.strftime(cls.date_end, "%Y-%m-%d"),
            "amount": cls.amount
        }

@dataclass
class Order: 
    uid: int 
    orderId: int = 0
    id: int = 0
    itemName: str = None
    quantity: int = 0
    price: int = 0
    total_price: int = 0

    def toDict(cls):
        res = dict()
        res["uid"] = cls.uid
        res["order_id"] = cls.orderId
        res["id"] = cls.id
        if cls.itemName:
            res["item_name"] = cls.itemName
            res["sum"] = cls.quantity
            res["price"] = cls.price
            res["total_price"] = cls.total_price
        return res

@dataclass
class UserOrder:
    uid: int
    order_id: int = 0
    done: bool = False
    total_price: int = 0
    total_quantity: int = 0
    event_id: int = None
    date_created: datetime = datetime.utcnow()
    orders: list[Order] = None

    def toDict(cls):
        res = dict()
        res["uid"] = cls.uid
        res["order_id"] = cls.order_id
        res["done"] = cls.done
        res["event_id"] = cls.event_id
        res["total_quantity"] = cls.total_quantity
        res["total_price"] = cls.total_price  
        res["date_created"] = datetime.strftime(cls.date_created , "%Y-%m-%d %H:%M:%S")
        res["orders"] = [itm.toDict() for itm in cls.orders]
        return res

@dataclass
class TodaySpecialData:
    item_id: int
    name: str
    price: int
    total_price: int
    quantity: int

    def toDict(cls):
        return {
            "id": cls.item_id,
            "name": cls.name,
            "price": cls.price,
            "total_price": cls.total_price,
            "quantity": cls.quantity
        }

@dataclass
class TodayEventData:
    event_id: int
    name: str
    coupon_code: str
    disc_amount: int

    def toDict(cls):
        return {
            "event_id": cls.event_id,
            "coupon_code": cls.coupon_code,
            "title":  cls.name,
            "disc_amount": cls.disc_amount
        }
