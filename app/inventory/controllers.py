from flask import Blueprint, request
from flask.helpers import make_response

from app.baseModel import FailedResponse, SuccessResponse
from app.inventory.models import Item
from app.inventory.services import registerNewItem

import os

inventory_bp = Blueprint("inventory_bp", __name__)

@inventory_bp.route("/api/inventory", methods=["POST"])
def addItem():
   try:
      hed = request.headers.get("Super-Secret-Key")
      if (not hed) or (hed != os.environ.get("DEV_KEY")):
         raise Exception("WEAKLING!!!")

      res = request.get_json()
      
      newItem = Item(
         id=res.get("id"),
         name=res.get("name"),
         stock=res.get("stock"),
         price=res.get("price")
      )
      registerNewItem(newItem)
      
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)
