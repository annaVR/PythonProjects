#view function

#start from this file: "The login view function" part from Tutorial5

from flask import render_template, flash, redirect, session, url_for, request, g

from flask.ext.login import login_user, logout_user, current_user, login_required

from app import app, db, lm, oid # from 'app' package(folder) import 'app' variable from __init__.py module(which is part of 'app' package)
from .forms import LoginForm #importing LoginForms from our forms.py module
from .models import User

@app.route('/')  #The two route decorators above the function create the mappings from URLs/ and /index to this function
@app.route('/index')
def index():
    user = {'nickname': 'Anna'}  # fake user
    posts = [
        {
            'author': {'nickname': 'Katya'},
            'body': 'I have learned a lot today!'
        },
        {
            'author': {'nickname': 'Mama'},
            'body': 'I feel good today!'
        },
        {
            'author': {'nickname': 'Taruna'},
            'body': 'Vedant was very funny yesterday evening.'
        }
    ]
    return render_template('index.html', user=user, posts=posts) #This function takes a template filename
    #and a variable list of template/
    # arguments and returns the rendered template, with all the arguments replaced

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() #instantiated LoginForm object
    if form.validate_on_submit(): #returns True if all sumbitted date validates successfully.
                                 #returns False if validators fails, and the "/index" page will be rendered again
        flash('Login requested for OpenId="%s", remember_me=%s' % (form.openid.data, str(form.openid.data)))
           #these messages appear in the first page requested by the user after the flash function is called,
           # and then they disappear.
        return redirect('/index') #This function tells the client web browser to navigate to
                         # a different page instead of the one requested. Flashed messages will display even if a view
                         # function ends in a redirect.
    return render_template('login.html',
                           title='Sign In',
                           form=form,               #pass the instance to the template
                           providers=app.config['OPENID_PROVIDERS']) #we grab the configuration by looking it up
                           # in app.config with its key. The array is then added to the render_template call as a template
                           # argument.

@lm.user_loader #load_user function is registered with Flask-Login through the lm.user_loader decorator.
def load_user(id) #a function that loads a user from the database
    return User.query.get(int(id)) #as users id are always unicode we need to convert them to int before we send them to flast_SQLAlchemy

