import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()

# DATABASE SETUP
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = "my_secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
Migrate(app, db)

from my_blog.error_pages_fold.handlers import error_pages
from my_blog.core_fold.views import core
from my_blog.blog_post_fold.views import blog_posts
from my_blog.users_fold.views import users

# LOGIN CONFIGS

login_manager.init_app(app)
login_manager.login_view = 'users.login'

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(blog_posts)
app.register_blueprint(users)
