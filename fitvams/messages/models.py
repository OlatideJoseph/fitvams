from fitvams import db




class Message(db.Model):
    __tablename__='messages'
    id=db.Column(db.Integer,primary_key=True)
    from_id=db.Column(db.Integer,
    db.ForeignKey('users.id'))
    to_id=db.Column(db.Integer,
    db.ForeignKey('users.id'))
    has_seen=db.Column(db.Boolean,default=False)
    message=db.Column(db.Text(),nullable=False)
    
    
    
    
from fitvams.users.models import User