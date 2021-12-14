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
         id=res.get("menuId"),
         name=res.get("namaMenu"),
         price=res.get("hargaMenu"),
         path_picture=res.get("pathGambar")
      )
      registerNewItem(newItem)
      
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      import traceback
      traceback.print_exc()
      return make_response(FailedResponse(str(e)).toDict(), 500)