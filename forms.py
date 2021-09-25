from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class AddPetForm(FlaskForm):
    """Form for adding a new pet."""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo")
    age = IntegerField('Age')
    notes = StringField("Notes")