from flask import Flask
#flask extensions
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_moment import Moment
from fitvams.config import Config

mail=Mail()
login_manager=LoginManager()
db=SQLAlchemy()
moment=Moment()
csrf=CSRFProtect()

def create_app():
    #App Config
    app=Flask(__name__)
    app.config.from_object(Config)
    #extensions config 
    mail.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view='users.login'
    login_manager.login_message='Please login to view that page!'
    login_manager.login_message_category='warning'
    #Blueprint Requirements func
    from fitvams.home.urls import home
    from fitvams.users.urls import user
    from fitvams.comments.urls import comment
    from fitvams.admin.urls import admin
    from fitvams.posts.urls import post
    from fitvams.followers.urls import follower
    from fitvams.messages.urls import message
    from fitvams.bots import bot
    #Blueprints App
    app.register_blueprint(home)
    app.register_blueprint(comment,
    url_prefix='/comments/')
    app.register_blueprint(user,
    url_prefix='/user/')
    app.register_blueprint(follower,
    url_prefix='/follower/')
    app.register_blueprint(admin,
    url_prefix='/admin/')
    app.register_blueprint(bot,
    url_prefix='/bots_handler')
    app.register_blueprint(message,
    url_prefix='/messages/')
    app.register_blueprint(post,
    url_prefix='/posts/')
    
    
    return app