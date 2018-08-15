from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from todo import db

class Items(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    todo_title = db.Column(db.String(140), nullable=False)
    todo_text = db.Column(db.String(1255))
    todo_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    todo_close = db.Column(db.Integer(), default=1)


    def __repr__(self):
        return f"Items('{self.todo_title}')"
