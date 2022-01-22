from werkzeug.security import generate_password_hash as gph
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,RadioField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError,Email,Regexp
from fitvams import db
from fitvams.users.models import User



class LoginForm(FlaskForm):
    email=StringField(None,
    validators=[DataRequired(),Email(),
    Length(min=5,max=150)])
    password=PasswordField(None,
    validators=[DataRequired(),
    Length(min=8,max=8)
    ])
    remember=BooleanField("Remember info")
    submit=SubmitField('Login')
    
class RegisterForm(FlaskForm):
    firstname=StringField(None,
    validators=[DataRequired(),
    Length(min=3,max=16)])
    secondname=StringField(None,
    validators=[DataRequired(),
    Length(min=3,max=16)])
    lastname=StringField(None,
    validators=[DataRequired(),
    Length(min=3,max=16)])
    email=StringField(None,
    validators=[DataRequired(),Email(),
    Length(min=5,max=150)])
    password=PasswordField(None,
    validators=[DataRequired(),
    Length(min=8,max=8)])
    re_pass=PasswordField(None,
    validators=[DataRequired(),
    Length(min=8,max=8),EqualTo('password')])
    gender=RadioField('Gender *',
    validators=[DataRequired()],
    choices=[('Male','Male'),
    ('Female','Female')])
    submit=SubmitField('Submit')
    #functions that saves the field to the database
    def save(self):
        fn=self.firstname.data.title()
        sn=self.secondname.data.title()
        ln=self.lastname.data.title()
        em=self.email.data
        pw=gph(self.password.data)
        gd=self.gender.data
        username=fn+sn+ln[0]
        print(username)
        usre=User(firstname=fn,
                 secondname=sn,
                 email=em,
                 lastname=ln,
                 pw=pw,
                 gender=gd,username=username)
        db.session.add(usre)
        db.session.commit()
        
        
    