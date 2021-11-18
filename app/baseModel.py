from __future__ import annotations

from typing import Any, List
from dataclasses import dataclass
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import dotenv

db = SQLAlchemy()
migrate = Migrate()
dotenv.load_dotenv()

@dataclass
class SuccessResponse:
   data: List[Any] = None
   count: int = None
   perPage: int = None
   page: int = None
   totalPages: int = None
   created: datetime = None

   def toDict(cls):
      res = {
         "status": "OK",
         "date_created": datetime.utcnow()
      }

      if cls.data:
         res["data"] = cls.data
         res["data"] = len(cls.data)

      if cls.page: 
         res["page"] = cls.page
         res["per_page"] = cls.perPage
         res["total_pages"] = cls.totalPages
      return res

@dataclass
class FailedResponse:
   errorCode: str = None
   errorMessage: str = None
   created: datetime = None

   def toDict(cls):
      res = {
         "status": "ERROR",
         "error_code": cls.errorCode,
         "error_msg": cls.errorMessage
      }
      return res

def setup_db(app):
   db_path = "mysql+pymysql://root:kopikopikopi@3.145.27.206:8080/stellarCoffee"
   app.config["SQLALCHEMY_DATABASE_URI"] = db_path
   db.app = app
   db.init_app(app)

def db_drop_and_create_all():
   db.drop_all()
   db.create_all()
   
class User(db.Model):
   __tablename__ = 'Userdata'

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(120), nullable=False)
   username = db.Column(db.String(30), nullable=False, unique=True)
   # Just for the purpose of the project
   # NOT ADVISABLE FOR REAL PROJECT (security_concern)
   password = db.Column(db.String(30), nullable=False) 
   user_point = db.Column(db.Integer, default=0, nullable=False)

class Inventory(db.Model):
   __tablename__ = 'Inventory'

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   stock = db.Column(db.Integer, nullable=False)
   price = db.Column(db.Integer, nullable=False)

class UserCart(db.Model):
   __tablename__ = 'UserCart'

   id = db.Column(db.Integer, primary_key=True)
   user = db.Column(db.String(100), db.ForeignKey("UserData.username"))
   item_name = db.Column(db.String(100), db.ForeignKey("Inventory.name"))
   sum = db.Column(db.Integer, nullable=False)
   price = db.Column(db.Integer, nullable=False)
