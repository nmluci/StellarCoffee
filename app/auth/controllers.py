from flask import Blueprint, request, make_response
from app.auth.services import registerUser, verifyUserCredentials
from app.baseModel import SuccessResponse, FailedResponse
from app.auth.models import SignInModel, SignUpModel

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/api/auth/login", methods=["POST"])
def signIn():
   try:
      res = request.get_json()
      usr = SignInModel(
         username=res.get("username"),
         password=res.get("password"))
      print(usr)
      if not verifyUserCredentials(usr):
         raise Exception("Invalid User Credentials")

      return make_response(SuccessResponse().toDict())
   except Exception as e:
      return make_response(FailedResponse(
         errorCode="USR_ERR",
         errorMessage=str(e)
      ).toDict(), 401)

@auth_bp.route("/api/auth/register", methods=["POST"])
def signUp():
   try:
      res = request.get_json()
      usr = SignUpModel(
         username=res.get("username"),
         password=res.get("password"),
         firstName=res.get("first_name"),
         lastName=res.get("last_name")
      )
      registerUser(usr)
      return make_response(SuccessResponse().toDict())
   except Exception as e:
      import traceback
      traceback.print_exc()
      return make_response(FailedResponse(
         errorCode="USR_REG_ERR",
         errorMessage=str(e)
      ).toDict(), 401)