from flask import Blueprint, request
from flask.helpers import make_response

from app.baseModel import SuccessResponse, FailedResponse
from app.order.services import generateTodaySpecialty, generateTodayEvents, generateCheckout
from app.userdata.models import User, UserData

order_bp = Blueprint("order_bp", __name__)

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

@order_bp.route("/api/order/checkout", methods=["POST"])
def checkout():
   try:
      res = request.get_json()
      usr = UserData(
         #TODO : Need change to uid, because frontend pass uid and better to user uid
         username=res.get("username")
      )
      generateCheckout(usr)
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse(errorMessage=str(e)).toDict(), 500)
