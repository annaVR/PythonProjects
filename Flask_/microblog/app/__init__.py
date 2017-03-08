import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy #*
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__) #creates the application object (of class Flask)
app.config.from_object('config') #tell Flask to read it and use it
db = SQLAlchemy(app) #creates db
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))#path to a temp folder where files can be stored
# (OpenID extention required it)

from app import views, models  #from 'app' package(folder) import 'views' module, db 'models'