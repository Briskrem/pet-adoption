from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange


class AddPet(FlaskForm):

    name =  StringField('Pet Name', validators=[InputRequired()])
    species =  StringField('Species')
    photo_url =  StringField('image url')
    age = IntegerField('age', validators=[InputRequired(), NumberRange(min=0, max=15)])
    notes =  StringField('enter notes', validators=[InputRequired(), Length(min=5, max=100)])
    available = BooleanField('is pet available') 