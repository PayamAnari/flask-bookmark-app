from flask import Blueprint, request
import validators


bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/v1/bookmarks")

@bookmarks.route("/", methods=["POST", "GET"])
def bookmarks():

    if request.method == "POST":
        
        body = request.get_json.get("body", "")
        url = body.get_json.get("url", "")
    elif request.method == "GET":
        # Get all bookmarks
        pass