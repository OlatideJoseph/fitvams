from flask_login import login_required
from fitvams.posts import post



@post.route("/discover")
@login_required
def discover():
    return ''
    
    
@post.route('/')
@login_required
def index():
    pass