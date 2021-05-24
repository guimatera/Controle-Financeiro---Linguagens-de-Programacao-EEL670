from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

class LoginForm (FlaskForm):
    username = StringField('Nome de Usuario', validators = [DataRequired()])
    password = PasswordField('Senha', validators = [DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Acessar')

class RegisterForm(FlaskForm):
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField('Registrar')

