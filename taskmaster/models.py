from enum import unique
from taskmaster import db, login_manager
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    tasks = db.relationship('Todo', backref="owner")
    def __repr__(self) -> str:
        return f"<User: ({self.id}, {self.username})>"

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"<Task: ({self.id}, {self.name})>"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))