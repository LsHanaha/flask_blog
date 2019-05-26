from flask import render_template, Blueprint, request
from my_blog.models import BlogPost

#блюпринт(имя блюпринта и текущий файл, откуда он создается)
core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    print(f"page = {page}")
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)

    return render_template('index.html', blog_posts=blog_posts)


@core.route('/info')
def info():
    return render_template('info.html')

