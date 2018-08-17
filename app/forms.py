from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    inputURL = StringField('inputURL', validators=[DataRequired()])
    shortener = StringField('shortener', validators=[DataRequired()])

