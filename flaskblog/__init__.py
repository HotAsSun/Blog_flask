from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flaskblog.config import secret_key
 



app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'



db = SQLAlchemy(app)


from flaskblog import routes