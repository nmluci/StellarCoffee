from flask import Flask, request
from flask.helpers import make_response
from flask_migrate import Migrate
from flask_cors import CORS
import os

from app.baseModel import FailedResponse, db, migrate
from app.auth.controllers import auth_bp
from app.inventory.controllers import inventory_bp
from app.order.controllers import order_bp
from app.userdata.controllers import user_bp

from app.inventory.models import Inventory
from app.order.models import Orders, OrderItems, Events
from app.userdata.models import User

def stellar_app(debug=False):
   app = Flask(__name__)
   app.config["JSON_SORT_KEYS"] = False
   app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
   app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_AUTH") 
   CORS(app)

   @app.before_request
   def headerCheck():
      apiKey = request.headers.get("SC-API-TOKEN", None)
      if (not apiKey) or (apiKey != os.environ.get("API_KEY")):
         print("401 - Key Not Found!")
         return make_response(FailedResponse(
            errorMessage="THOU SHALT NOT PASSED"
         ).toDict(), 401)

   app.register_blueprint(auth_bp)
   app.register_blueprint(inventory_bp)
   app.register_blueprint(order_bp)
   app.register_blueprint(user_bp)
   db.init_app(app)
   
   if debug: 
      migrate.init_app(app,db)
      db.drop_all(app=app)
      db.create_all(app=app)

   @app.route("/")
   @app.route("/api")
   def why():
      return """<!DOCTYPE html>
<html>
<head>
 <title></title>
 <meta name="referrer" content="no-referrer"/>
 <meta charset="utf-8" />
</head>
<body> 
<div class="bd-example" align="middle">
 
<img src="https://i.imgur.com/yHLsngu.jpg" align="middle" />
        
</div>
</body>
</html>"""

   return app