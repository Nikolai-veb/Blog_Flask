from app import db

class Posts(db.Model):
    """Модель постов"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    slug = db.Column(db.String(150), unique=True)
