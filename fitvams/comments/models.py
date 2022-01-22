from fitvams import db




class Comment(db.Model):
    __tablename__='comment'
    id=db.Column(db.Integer,primary_key=True)
    pass
    
    
from fitvams.posts.models import Post #for circular import 