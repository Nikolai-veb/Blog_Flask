from flask import Blueprint
from flask import render_template
from flask import request
from models import Posts, Tag

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
    q = request.args.get('query')
    if q:
        posts =  Posts.query.filter(Posts.title.contains(q) | Posts.text.contains(q)).all()
    else:
        posts = Posts.query.all()
    return render_template('posts/index.html', posts=posts)


@posts.route('/<slug>')
def post_detail(slug):
    post = Posts.query.filter(Posts.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)



