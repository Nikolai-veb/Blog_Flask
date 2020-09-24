from flask import Blueprint
from flask import render_template

from models import Posts

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
    posts = Posts.query.all()
    return render_template('posts/index.html', posts=posts)


@posts.route('/<slug>')
def post_detail(slug):
    post = Posts.query.filter(Posts.slug==slug).first()
    return render_template('posts/post_detail.html', post=post)
