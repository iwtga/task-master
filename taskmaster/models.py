from taskmaster import db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
