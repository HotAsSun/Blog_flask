import secrets
import os
secret_key = secrets.token_hex(16)

class Config():
    SECRET_KEY = secret_key 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
 
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587        
    MAIL_USE_TLS = True   
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'sina.khadem.885@gmail.com'
    MAIL_PASSWORD = 'S!nakhadem885'
    