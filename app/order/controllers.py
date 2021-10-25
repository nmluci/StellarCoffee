from flask import Blueprint, request

order_bp = Blueprint("order_bp", __name__)

@order_bp.route("/api/order/todaySpecials", methods=["GET"])
def todaySpecialty():
   pass

@order_bp.route("/api/order/todayEvents", methods=["GET"])
def todayEvents():
   pass

@order_bp.route("/api/order/addItem", methods=["POST"])
def addItemToCart():
   pass

@order_bp.route("/api/order/returnItem", methods=["POST"])
def returnItemFromCart():
   pass

@order_bp.route("/api/order/checkout", methods=["GET"])
def checkout():
   pass

@order_bp.route("/api/order/queue", methods=["GET"])
def getQueueStats():
   pass

@order_bp.route("/api/order/queue", methods=["POST"])
def addQueue():
   pass