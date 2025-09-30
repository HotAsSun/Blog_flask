from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired , Length , Email , EqualTo


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

class LoginForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('password',
                             validators=[DataRequired(), Length(min=8,max=63  ) ])
    remember = BooleanField('remember me ')

    submit = SubmitField('log in ')