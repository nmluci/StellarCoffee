from flask import Blueprint, request
from flask.helpers import make_response
from datetime import datetime
from app.baseModel import SuccessResponse, FailedResponse
from app.order.models import EventData, Order, UserOrder
from app.order.services import generateTodaySpecialty, generateTodayEvents, processCheckout, getUserGeneralHistoryCheckout, insertEvents
from app.userdata.models import User, UserData

order_bp = Blueprint("order_bp", __name__)

# {
#     "allItems": [
#         {
#             "menuId": 6,
#             "namaMenu": "Lemon Tea",
#             "hargaMenu": 17000,
#             "totalPrice": 51000,
#             "quantity": 3,
#             "pathGambar": "/assets/img/menu/lemon-tea.jpg"
#         },
#         {
#             "menuId": 7,
#             "namaMenu": "Lychee Tea",
#             "hargaMenu": 20000,
#             "totalPrice": 40000,
#             "quantity": 2,
#             "pathGambar": "/assets/img/menu/lychee-tea.jpg"
#         }
#     ],
#     "quantity": 5,
#     "grandTotal": 91000,
#     "done": False,
#     "created": 1638607395682
# }

@order_bp.route("/api/order/todaySpecials", methods=["GET"])
def todaySpecialty():
   try:
      todaySpecials = generateTodaySpecialty()
      return make_response(SuccessResponse(data=todaySpecials).toDict())
   except Exception as e:
      return make_response(FailedResponse(errorMessage=str(e)).toDict(), 500)

@order_bp.route("/api/order/todayEvents", methods=["GET"])
def todayEvents():
   try:
      todayEvents = generateTodayEvents()

      return make_response(SuccessResponse(data=todayEvents).toDict())
   except Exception as e:
      return make_response(FailedResponse(errorMessage=str(e)).toDict(), 500)

@order_bp.route("/api/order/events", methods=["POST"])
def addEventCoupon():
   try:
      res = request.get_json()
      event = EventData(
         name=res.get("name"),
         coupon=res.get("code"),
         date_start=datetime.strptime(res.get("date_start"), "%Y-%m-%d"),
         date_end=datetime.strptime(res.get("date_end"), "%Y-%m-%d"),
         amount=res.get("amount")
      )
      insertEvents(event)
      return make_response(SuccessResponse(data=[event]).toDict())      
   except Exception as e:
      return make_response(FailedResponse(errorMessage=str(e)).toDict(), 500)

@order_bp.route("/api/order/<uid>/checkout", methods=["POST"])
def checkout(uid):
   try:
      res = request.get_json()
      print(res)
      usr = UserOrder(
         uid=uid,
         done=res["done"],
         total_price=res["grandTotal"],
         total_quantity=res["quantity"],
         date_created=datetime.fromtimestamp(float(res["created"]/1000)),
         orders=list(Order(
            uid=uid,
            itemName=itm["namaMenu"],
            quantity=itm["quantity"],
            price=itm["hargaMenu"],
            total_price=itm["totalPrice"]
         ) for itm in res["allItems"])
      )
      processCheckout(usr)
      return make_response(SuccessResponse(usr.toDict()).toDict())
   except Exception as e:
      import traceback
      traceback.print_exc()
      return make_response(FailedResponse(errorMessage=str(e)).toDict(), 500)

@order_bp.route("/api/order/history/<uid>", methods=["GET"])
def history(uid):
   try:
      return make_response(SuccessResponse(data=getUserGeneralHistoryCheckout(uid)).toDict())
   except Exception as e:
      return make_response(FailedResponse(errorMessage=str(e)).toDict(), 500)