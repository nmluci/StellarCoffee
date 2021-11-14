from enum import unique
from app.baseModel import db

class Orders(db.Model):
    __tablename__ = "Inventory"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text, db.ForeignKey("Inventory.name", ondelete="SET NULL", onupdate="CASCADE"), nullable=False)
    username = db.Column(db.Text, db.ForeignKey("User.name", ondelete="SET NULL", onupdate="CASCADE"), nullable=False)
    sum = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
