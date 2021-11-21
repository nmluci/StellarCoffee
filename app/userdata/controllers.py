from flask import Blueprint, request
from flask.helpers import make_response

from app.baseModel import FailedResponse, SuccessResponse

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/api/user/<username>", methods=["POST"])
def addPoint():
   try:
      res = request.get_json()
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)

@user_bp.route("/api/user/<username>", methods=["GET"])
def getUserInfo():
   try:
      res = request.get_json()
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)

@user_bp.route("/api/user/leaderboard", methods=["GET"])
def userLeaderboard():
   try:
      res = request.get_json()
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse().toDict(), 500)
