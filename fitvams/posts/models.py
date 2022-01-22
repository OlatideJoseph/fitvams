from datetime import datetime
from fitvams import db




class Post(db.Model):
     __tablename__='posts'
     """Fitvams posts models """
     id=db.Column(db.Integer,primary_key=True)
     content=db.Column(db.Text,nullable=False)
     img_arr=db.Column(db.PickleType,
     nullable=True)
     last_edit=db.Column(db.DateTime,
     default=datetime.utcnow)
     written_on=db.Column(db.DateTime,
     default=datetime.utcnow)
     viewers=db.Column(db.PickleType,
     nullable=True,index=True)
     author_id=db.Column(db.Integer,
     db.ForeignKey('users.id'))
     
     
     
     
from fitvams.users.models import User #importing the module after due to circular import
from fitvams.comments.models import Comment #For circular import purpose