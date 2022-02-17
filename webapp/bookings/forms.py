from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    week = SelectField('Gewenste week', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Boeken')

class UpdateBookingForm(FlaskForm):
    week = SelectField('Gewenste week', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Aanpassen')
