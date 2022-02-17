from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.widgets.html5 import NumberInput
from wtforms.validators import DataRequired, ValidationError
from webapp.models import Bungalow

class AddBungalowForm(FlaskForm):
    name = StringField('Naam', validators=[DataRequired()])
    content = TextAreaField('Beschrijving', validators=[DataRequired()])
    bungalow_type = SelectField('Aantal personen', choices=[('4', '4 Personen'), ('6', '6 Personen'), ('8', '8 Personen')], validators=[DataRequired()])
    weekprice = IntegerField('Weekprijs', widget=NumberInput(), validators=[DataRequired()])
    submit = SubmitField('Voeg bungalow toe')

    def validate_name(self, name):
        name = Bungalow.query.filter_by(name=name.data).first()
        if name:
            raise ValidationError('De gekozen bungalownaam bestaat al.')