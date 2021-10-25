from flask import Blueprint, request

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/api/user/<username>", methods=["POST"])
def addPoint():
   pass

@user_bp.route("/api/user/<username>", methods=["GET"])
def getUserInfo():
   pass

@user_bp.route("/api/user/leaderboard", methods=["GET"])
def userLeaderboard():
   pass