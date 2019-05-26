from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user,login_required
from my_blog import db
from my_blog.models import BlogPost
from my_blog.blog_post_fold.forms import BlogPostForm


blog_posts = Blueprint('blog_posts', __name__)


# create post
@blog_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():

        blog = BlogPost(title=form.title.data,
                        text=form.text.data,
                        user_id=current_user.id)
        db.session.add(blog)
        db.session.commit()
        flash('I do not work!')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)


# read post
@blog_posts.route('/<int:blog_post_id>')
def read_post(blog_post_id):

    blog = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html',date=blog.date,post=blog)


# update
@blog_posts.route('/<int:blog_post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(blog_post_id):
    blog = BlogPost.query.get_or_404(blog_post_id)
    print(f"blog = {blog}, current_user = {current_user}")
    if blog.author != current_user:
        abort(403)

    form = BlogPostForm()
    if form.validate_on_submit():

        blog.title = form.title.data
        blog.text = form.text.data
        db.session.commit()

        flash(' i do not work!')
        return redirect(url_for('blog_posts.read_post', blog_post_id=blog.id))

    elif request.method == 'GET':
        form.title.data = blog.title
        form.text.data = blog.text

    return render_template('create_post.html', title="Updating", form=form)


@blog_posts.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(blog_post_id):

    blog = BlogPost.query.get_or_404(blog_post_id)
    if blog.author != current_user:
        abort(403)

    db.session.delete(blog)
    db.session.commit()
    flash('I do not work!')
    return redirect(url_for('core.index'))



