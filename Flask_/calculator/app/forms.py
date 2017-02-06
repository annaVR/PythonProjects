__author__ = 'anna'

from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import DataRequired, AnyOf, Regexp, Length

class InputForm(FlaskForm):
    first_number = IntegerField('Enter a first number', validators=[DataRequired()])
    second_number = IntegerField('Enter a second number', validators=[DataRequired()])
    operation = SelectField('Choose the operation', choices=[('+', '+'), ('-', '-'), ('*', '*'),    ('/', '/')],
                            validators=[AnyOf(['+', '-', '*', '/'])])



class InputStringForm(FlaskForm):
    string_data = StringField('Enter data', validators=[DataRequired(), Regexp('[\d+\-|\+{1}]+\d{1}', message='The only valid input is: 0-9, +, -.')])