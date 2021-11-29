from dataclasses import dataclass
from app.baseModel import db

class User(db.Model):
    __tablename__ = 'Userdata'

    uid = db.Column(db.LargeBinary, primary_key=True, unique=True)
    firstname = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    point = db.Column(db.Integer, nullable=False, default=0)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def update(self):
        db.session.commit()

@dataclass
class UserData:
    username: str
    point: str = None
    
