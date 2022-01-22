import os
import _thread
from fitvams import create_app,mail,db
from flask_mail import Message




app=create_app()




def create_database():
    with app.app_context() as ctx:
        ctx.push()
        db.create_all()
        
        
        

def send_mail(subject,
       recipients,**kwargs):
    msg=Message(subject,recipients)
    body=kwargs['text']
    html=kwargs['html']
    msg.html=html if html else ''
    msg.body=body if body else ''
    with app.app_context() as ctx:
        ctx.push()
        mail.send(msg)

def send_async_mai(subject,
       recipients,**kwargs):
    _threads.start_new_thread(send_mail,subject,recipients,kwargs)