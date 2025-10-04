import datetime
from flask import current_app
from itsdangerous import URLSafeSerializer as Serializer
from flaskblog import db , login_manager 
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id ))



class User(db.Model,UserMixin):
    id = db.Column(db.Integer , primary_key=True ,unique = True ,nullable = False)
    username = db.Column(db.String(20) ,unique = True ,nullable = False)
    email = db.Column(db.String(120) ,unique = False ,nullable = False)
    image_url = db.Column(db.String(20) ,nullable = False ,default='default.jpg')
    password = db.Column(db.String(16),nullable = False)
    post = db.relationship('Post' ,backref = 'author' ,lazy=True )


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})   

@staticmethod
def verify_reset_token(token, expires_sec=300):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token, max_age=expires_sec)['user_id']
    except Exception:
        return None
    return User.query.get(user_id)


class Post(db.Model):
    id = db.Column(db.Integer ,primary_key=True ,unique=True ,nullable= False)
    title = db.Column(db.String(100) ,nullable= False)
    date_posted = db.Column(db.DateTime ,nullable= False ,default = datetime.datetime.utcnow)
    content = db.Column(db.Text ,nullable = False)
    user_id = db.Column(db.Integer ,db.ForeignKey('user.id' ),nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

