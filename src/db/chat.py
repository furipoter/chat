from src.db import db


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_name = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
