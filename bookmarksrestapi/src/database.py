from enum import unique
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    id=db.column(db.Integer, primary_key=True)
    username=db.column(db.String(80), unique=True, nullable=False)
    email=db.column(db.String(80), unique=True, nullable=False)
    password=db.column(db.Text(80), unique=True, nullable=False)
    created_at=db.column(db.DateTime, default=datetime.now())
    updated_at=db.column(db.DateTime, onupdate=datetime.now())
    bookmarks=db.relationship("bookmark", backref="user")


    def __repr__(self) -> str:
        return "User>>> {self.username}"


class Bookmark(db.Model):
    id=db.column(db.Integer, primary_key=True)
    body=db.column(db.Text, nullable=False)
    url=db.column(db.Text, nullable=False)
    short_url=db.column(db.String(3), nullable=False)
    visits=db.column(db.Integer, default=0)
    user_id=db.column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at=db.column(db.DateTime, default=datetime.now())
    updated_at=db.column(db.DateTime, onupdate=datetime.now())

    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.short_url=self.generate_short_characters()


    def __repr__(self) -> str:
        return "Bookmark>>> {self.url}"