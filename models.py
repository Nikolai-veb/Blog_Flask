from app import db
from datetime import datetime
import re

def slugfy(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Posts(db.Model):
    """Модель постов"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    slug = db.Column(db.String(150), unique=True)
    text = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Posts, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugfy(self.title.lower())

    def __repr__(self):
        return '<Post_id: {} title: {}'.format(self.id, self.title.lower())

