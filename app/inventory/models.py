from dataclasses import dataclass
from app.baseModel import db

class Inventory(db.Model):
    __tablename__ = "Inventory"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

@dataclass
class Item:
    id: int = None
    name: str = None
    price: int = None

    def toDict(cls):
        res = dict()
        if cls.id: res["id"] = cls.id
        if cls.name: res["item_name"] = cls.name
        if cls.price: res["price"] = cls.price

        return res