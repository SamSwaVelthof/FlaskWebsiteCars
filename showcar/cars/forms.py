from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField('Naam Auto: ', validators=[DataRequired()])
    description = StringField('Beschrijving: ', widget=TextArea(), validators=[DataRequired()])
    brand = SelectField('Merk', choices=[])
    submit = SubmitField('Voeg toe')

class EditForm(FlaskForm):
    name = StringField('Naam Auto: ', validators=[DataRequired()])
    description = StringField('Beschrijving: ', widget=TextArea(), validators=[DataRequired()])
    brand = SelectField('Merk', choices=[])
    submit = SubmitField('Bewerk')