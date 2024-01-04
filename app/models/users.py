from imports import *
from app.extension import db

# class Users(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     product_key = db.Column(db.String(20), nullable=False)
#     username = db.Column(db.String(20), nullable=False, unique=True)
#     name = db.Column(db.String(40), nullable=False)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)
#     password_hash = db.Column(db.String(128))

#     def __repr__(self):
# 	    return '<Name %r>' % self.name


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
	    return '<Name %r>' % self.name