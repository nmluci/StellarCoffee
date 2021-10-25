from flask import Blueprint, request

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/api/auth/signIn", methods=["POST"])
def signIn():
   pass

@auth_bp.route("/api/auth/signup", methods=["POST"])
def signUp():
   pass