from flask import Blueprint, request
from flask.json import jsonify
import validators
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_201_CREATED
from src.database import Bookmark, db
from flask_jwt_extended import  get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required

bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/v1/bookmarks")

@bookmarks.route("/", methods=["POST", "GET"])
@jwt_required()
def bookmarks():
    current_user = get_jwt_identity()

    if request.method == "POST":
        
        body = request.get_json.get("body", "")
        url = body.get_json.get("url", "")

        if not validators.url(url):
            return jsonify ({
                "error": "Enter a valid url"
                }), HTTP_400_BAD_REQUEST
 
       
        if Bookmark.query.filter_by(url = url).first():
           return jsonify({
               "error": "Url already exists"
               }), HTTP_409_CONFLICT
    


        bookmark = Bookmark(url = url, body = body, user_id = current_user)
        db.session.add(bookmark)
        db.session.commit()


        return jsonify({
            "message": "Bookmark created successfully",
            
            "id": bookmark.id,
            "url": bookmark.url,
            "short_url" : bookmark.short_url,
            "visit": bookmark.visits,
            "body": bookmark.body,
            "created_at": bookmark.created_at,
            "updated_at": bookmark.updated_at
        }), HTTP_201_CREATED
        
    else:

        bookmarks = Bookmark.query.filter_by(user_id = current_user).all()
        return jsonify([{
            "id": bookmark.id,
            "url": bookmark.url,
            "short_url" : bookmark.short_url,
            "visit": bookmark.visits,
            "body": bookmark.body,
            "created_at": bookmark.created_at,
            "updated_at": bookmark.updated_at
        } for bookmark in bookmarks])