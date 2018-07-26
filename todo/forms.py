from todo import app
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ItemForm(FlaskForm):
    title = StringField('Todo Title', validators=[DataRequired(), Length(min=10, max=120)])
    todoText = TextAreaField('Todo Description')
    submit = SubmitField('Save')
