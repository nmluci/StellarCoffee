from flask import Blueprint, request

inventory_bp = Blueprint("inventory_bp", __name__)

@inventory_bp.route("/api/inventory/addItem", methods=["POST"])
def addItemToCart():
   pass

@inventory_bp.route("/api/inventory/checkout", methods=["GET"])
def checkout():
   pass