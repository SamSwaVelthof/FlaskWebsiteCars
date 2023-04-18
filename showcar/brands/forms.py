from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField('Naam Merk: ', validators=[DataRequired()])
    submit = SubmitField('Voeg toe')

class EditForm(FlaskForm):
    name = StringField('Naam Merk: ', validators=[DataRequired()])
    submit = SubmitField('Bewerk')