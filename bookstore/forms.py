from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddBookForm(FlaskForm):
    isbn = StringField('ISBN', validators=[DataRequired()])
    save = SubmitField('Save')
