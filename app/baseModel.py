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

   def toDict(cls):
      res = {
         "status": "OK",
         "date_created": datetime.utcnow()
      }

      if cls.data:
         res["data"] = cls.data
         res["count"] = len(cls.data)

      if cls.page: 
         res["page"] = cls.page
         res["per_page"] = cls.perPage
         res["total_pages"] = cls.totalPages
      return res

@dataclass
class FailedResponse:
   errorCode: str = None
   errorMessage: str = None

   def toDict(cls):
      res = {
         "status": "ERROR",
         "error_code": cls.errorCode,
         "error_msg": cls.errorMessage,
         "date_created": datetime.utcnow()
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
