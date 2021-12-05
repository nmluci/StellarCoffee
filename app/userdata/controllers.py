from operator import add
from os import add_dll_directory, remove
from flask import Blueprint, request
from flask.helpers import make_response

from app.baseModel import FailedResponse, SuccessResponse
from app.userdata.models import UserData
from app.userdata.services import getUserData, usePoint

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/api/user/<username>", methods=["POST"])
def addPoint(username):
   try:
      addedPoint = request.args.get("add_point", default=0, type=int)
      if addedPoint: addPoint(username, addedPoint)

      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse(errorMessage=str(e)), 500)

@user_bp.route("/api/user/<username>", methods=["GET"])
def getUserInfo(username):
   try:
      usr = UserData(username=username)

      getUserData(usr)
      return make_response(SuccessResponse(data=[usr]).toDict())
   except Exception as e:
      import traceback
      traceback.print_exc()
      return make_response(FailedResponse(errorMessage=str(e)).toDict(), 500)

@user_bp.route("/api/user/leaderboard", methods=["GET"])
def userLeaderboard():
   try:
      res = request.get_json()
      return make_response(SuccessResponse(data=["Fufufu NOT NOW"]).toDict())
   except Exception as e:
      return make_response(FailedResponse(errorMessage=str(e)).toDict(), 500)
