__author__ = 'anna'

from wtforms.validators import ValidationError

def my_lenght_check(form, field):
    if len(field.data) > 23:
        raise ValidationError('A field must be less than 24 characters')

