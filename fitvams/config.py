
class Config:
    SECRET_KEY='8d8f41a856f22acd4a572fb3710f3daa8164f1ce8a79b5c2b8b60bf4a02176bf'
    secret_key=SECRET_KEY
    SQLALCHEMY_DATABASE_URI="sqlite:///library.sqlite"
    ENV='development'
    MAIL_HOST='smtp.gmail.com'
    MAIL_USERNAME='olatidejoseph17@gmail.com'
    MAIL_USE_TLS=True
    MAIL_PORT=587
    MAIL_PASSWORD='ttnpqxmrxxplofsy'
    TESTING=True
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    