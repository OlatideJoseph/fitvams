from fitvams.messages import message
@message.route('/')
def index():
    return 'message home !'
    
    
@message.route('/')
def voiceandmessage():
    pass