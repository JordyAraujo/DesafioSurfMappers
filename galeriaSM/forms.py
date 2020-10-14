from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class UploadForm(FlaskForm):
    image = FileField('Escolha seu arquivo', validators=[DataRequired()])
    submit = SubmitField('Upload')
