from flask import render_template,redirect,url_for,flash,request
from werkzeug.security import check_password_hash as cph
from flask_login import login_required,current_user,login_user,logout_user,current_user
#Apps Needs
from fitvams import csrf
from fitvams.users import user
from fitvams.users.models import User
from fitvams.users.forms import LoginForm,RegisterForm




@user.route('/')
@login_required
def index():
    return 'all user'


    
@user.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.\
        filter_by(email=form.email.data).first()
        fp=form.password.data
        remember=form.remember.data
        if user:
            chk=cph(user.pw,fp)
            if chk:
                login_user(user,remember)
                next=request.args.get('next')
                return redirect(next) if next else redirect('/')
            else:
                print('invalid password')
        else:
            print('invalid user')
    return render_template('user/login.html',form=form)

    
@user.route('/registration',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    form=RegisterForm()
    if form.validate_on_submit():
        form.save()
        return redirect('/')
    return render_template('user/register.html',form=form)


@user.route('/logout')
def logout():
    logout_user()
    return redirect('/')
    
    
@user.route('/<string:username>/profile')
def profile(username):
    pass
