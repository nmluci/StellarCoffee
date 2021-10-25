from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
