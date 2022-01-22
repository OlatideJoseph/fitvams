from fitvams.followers import follower
@follower.route("/")
def index():
    return 'who followed and following who ?'