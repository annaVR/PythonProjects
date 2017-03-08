#!flask/bin/python
# a script that starts up the development web server with our application
#The script simply imports the app variable from our app package and invokes its run method to start the server

from app import app  #from 'app' package(folder) import 'app' variable from __init__.py module(which is part of 'app' package)
app.run(debug=True)
