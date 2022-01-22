from datetime import datetime
from flask_login import UserMixin
from fitvams import db,login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model,UserMixin):
    __tablename__='users'
    """Fitvams user models """
    id=db.Column(db.Integer,primary_key=True)
    secondname=db.Column(db.String(50),
    nullable=False)
    firstname=db.Column(db.String(50),
    nullable=False)
    lastname=db.Column(db.String(50),
    nullable=False)
    email=db.Column(db.String(250),
    nullable=False)
    profile_img=db.Column(db.Text,
    default='gender.jpg')
    username=db.Column(db.String(75),
    unique=True,nullable=False)
    pw=db.Column(db.String(1000),nullable=False)
    joined=db.Column(db.DateTime,
    default=datetime.utcnow)
    suspended=db.Column(db.Boolean,
    default=False)
    gender=db.Column(db.String(6))
    last_seen_on=db.Column(db.DateTime,
    default=datetime.utcnow)
    posts=db.relationship('Post',
    backref='author',lazy=True)
    sender=db.relationship('Message',
    backref='sender',
    lazy=True,foreign_keys='Message.from_id')
    receiver=db.relationship('Message',
    backref='receiver',
    lazy=True,foreign_keys='Message.to_id')
    follower=db.relationship('Follow',
    backref='follower_var',
    lazy=True,
    foreign_keys='Follow.follower_id')
    followed=db.relationship('Follow',
    backref='followed_var',
    lazy=True,
    foreign_keys='Follow.followed_id')
    def username(self):
        return self.firstname+self.secondname+self.lastname[0]
    def suspend(self):
        pass
    def issuspended(self):
        pass
    def last_seen(self):
        return self.last_seen_on
    def generate_hash(self):
        pass
    
    
    
    
    
from fitvams.posts.models import Post #import the module after due to circular import
from fitvams.messages.models import Message #import the module after due to circular import
from fitvams.followers.models import Follow