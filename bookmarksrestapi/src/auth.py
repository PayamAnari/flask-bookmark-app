from flask import Blueprint, request,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

@auth.post("/register")
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
   
    if len(password) < 6:
        return jsonify({"message": "Password is too short"}), HTTP_400_BAD_REQUEST
   
    if len(username) < 3:
        return jsonify({"message": "Username is too short"}), HTTP_400_BAD_REQUEST
    
    if not username.isalnum() or " " in username:
        return jsonify({"message": "Username should be alphanumeric, also no spaces"}), HTTP_400_BAD_REQUEST

    return "User created"


@auth.get("/me")
def me():
    return {"user": "me"}