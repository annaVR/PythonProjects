import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') #This is the path of our database file.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') #the folder where we will store the SQLAlchemy-migrate data files.


WTF_CSRF_ENABLED = True #setting activates the cross-site request forgery prevention
# (note that this setting is enabled by default in current versions of Flask-WTF).
# In most cases you want to have this option enabled as it makes your app more secure.

SECRET_KEY = 'you-will-never-guess' #setting is only needed when CSRF is enabled,
# and is used to create a cryptographic token that is used to validate a form.
# When you write your own apps make sure to set the secret key to something that is difficult to guess.


OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

