from flask import render_template,url_for,send_file,redirect,current_app
from flask_login import login_required,current_user
from fitvams.home import home

@home.route("/")
@login_required
def index():
    return render_template('home/home.html')

   
@home.route('/robots.txt')
def robots():
    return send_file(current_app.root_path+'/static/robots.txt')