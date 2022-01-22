from fitvams import db




class Follow(db.Model):
    __tablename__='follow'
    id=db.Column(db.Integer,primary_key=True)
    follower_id=db.Column(db.Integer,
    db.ForeignKey('users.id'))
    followed_id=db.Column(db.Integer,
    db.ForeignKey('users.id'))
    
    
    

from fitvams.users.models import User #For circular import!.