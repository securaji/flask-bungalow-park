from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webapp.models import User

class RegisterForm(FlaskForm):
    first_name = StringField('Voornaam', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Achternaam', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    confirm_password = PasswordField('Bevestig wachtwoord', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registreer')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('De gekozen emailadres bestaat al.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    remember = BooleanField('Onthoud mij')
    submit = SubmitField('Inloggen')