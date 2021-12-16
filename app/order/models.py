from typing import Dict, List, Mapping

from dataclasses import dataclass
from datetime import datetime

from sqlalchemy.util.langhelpers import monkeypatch_proxied_specials
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
        
class Graph:
	def __init__(self, vertices: List[List[int]], alias: List):
		self.alias = alias
		self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		self.V = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

	def isSafe(self, v, colour, c):
		for i in range(self.V):
			if self.graph[v][i] == 1 and colour[i] == c:
				return False
		return True
	
	def graphColourUtil(self, m, colour, v):
		if v == self.V:
			return True

		for c in range(1, m + 1):
			if self.isSafe(v, colour, c) == True:
				colour[v] = c
				if self.graphColourUtil(m, colour, v + 1) == True:
					return True
				colour[v] = 0

	def graphColouring(self, m: int) -> Dict:
		mappedColour = dict(list())
		colour = [0] * self.V
		if self.graphColourUtil(m, colour, 0) == None:
			return False
		
		for idx, c in enumerate(colour):
			if not mappedColour.get(c):
				mappedColour[c] = [self.alias[idx]]
			else:
				mappedColour[c].append(self.alias[idx])

		return mappedColour

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
    path: str

    def toDict(cls):
        return {
            "id": cls.item_id,
            "name": cls.name,
            "price": cls.price,
            "pics": cls.path
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

@dataclass
class generalHistory:
    order_id: int = 0
    date_created: datetime = 0
    grand_total: int = 0
    total_item: int = 0
    status: bool = False

    def toDict(cls):
        return {
            "order_id": cls.order_id,
            "date_created": cls.date_created,
            "grand_total": cls.grand_total,
            "total_item": cls.total_item,
            "status": cls.status
        }