from flask import Blueprint
from flask import render_template
from flask import request

from flask import url_for
from flask import redirect

from models import Posts, Tag
from .forms import PostForm
from app import db

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_posts():
    if  request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        try:
            post = Posts(title=title, text=text)
            db.session.add(post)
            db.session.commit()
        except:
            print('SOME MISTAKE')
        else:
            return redirect(url_for('posts.index'))
    form = PostForm()
    return render_template('posts/create_posts.html', form=form)


@posts.route('/')
def index():
    q = request.args.get('query')
    if q:
        posts =  Posts.query.filter(Posts.title.contains(q) | Posts.text.contains(q)).all()
    else:
        posts = Posts.query.order_by(Posts.created.desc())
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



