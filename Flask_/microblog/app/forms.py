# from flask.ext.wtf import Form # Form class imported
#
# from wtforms import StringField, BuleanField # 2 field classes imported
#
# from wtforms.validators import DataRequired #import is a validator, a function that can be attached
#                                         # to a field to perform validation on the data submitted by the user.
#                                    # The DataRequired validator simply checks that the field is not submitted empty.
# class LoginForm(Form):
#     openid = StringField('openid', validators=[DataRequired()])
#     remember_me = BooleanField('remember_me', default=False)


from flask_wtf import Form #*
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
