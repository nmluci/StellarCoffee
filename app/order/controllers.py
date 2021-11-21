from flask import Blueprint, request
from flask.helpers import make_response

from app.baseModel import SuccessResponse, FailedResponse

order_bp = Blueprint("order_bp", __name__)

@order_bp.route("/api/order/todaySpecials", methods=["GET"])
def todaySpecialty():
   try:
      res = request.get_json()
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)

@order_bp.route("/api/order/todayEvents", methods=["GET"])
def todayEvents():
   try:
      res = request.get_json()
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)

@order_bp.route("/api/order/addItem", methods=["POST"])
def addItemToCart():
   try:
      res = request.get_json()
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)

@order_bp.route("/api/order/returnItem", methods=["POST"])
def returnItemFromCart():
   try:
      res = request.get_json()
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)

@order_bp.route("/api/order/checkout", methods=["GET"])
def checkout():
   try:
      res = request.get_json()
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)

@order_bp.route("/api/order/queue", methods=["GET"])
def getQueueStats():
   try:
      res = request.get_json()
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)

@order_bp.route("/api/order/queue", methods=["POST"])
def addQueue():
   try:
      res = request.get_json()
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)
