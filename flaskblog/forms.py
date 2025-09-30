from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError
from flaskblog.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=4,max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('password',
                             validators=[DataRequired(), Length(min=4,max=16  ) ])
    confirm_password = PasswordField('confirm password',
                             validators=[DataRequired(), Length(min=4,max=16),EqualTo('password')])
    submit = SubmitField('sign up')


    def validate_username(self, username=None):
        
        username = User.query.filter_by(username = username.data).first()

        if username:
            raise ValidationError(f"the username :  {User.username} is already taken  ")
        
    def validate_email(self, email=None):
        
        email = User.query.filter_by(email = email.data).first()

        if email:
            raise ValidationError("the email is already taken please choose and other one  ")



class LoginForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('password',
                             validators=[DataRequired(), Length(min=4,max=63  ) ])
    remember = BooleanField('remember me ')

    submit = SubmitField('log in ')