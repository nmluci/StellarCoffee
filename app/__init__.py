from flask import Flask
from flask.scaffold import F
from flask_migrate import Migrate, migrate
from flask_cors import CORS
from app.models import setup_db

from app.auth.controllers import auth_bp
from app.inventory.controllers import inventory_bp
from app.order.controllers import order_bp
from app.userdata.controllers import user_bp

migrate = Migrate()

def create_app():
   app = Flask(__name__)
   app.config["JSON_SORT_KEYS"] = False
   app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
   setup_db(app)
   
   app.register_blueprint(auth_bp)
   app.register_blueprint(inventory_bp)
   app.register_blueprint(order_bp)
   app.register_blueprint(user_bp)

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