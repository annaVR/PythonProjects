__author__ = 'anna'

#!usr/bin/python

from flask import Flask
app = Flask('webwords')

@app.route('/<any:path>')
def webwords():
    return ('<HTML><BODY>This is my first words!</BODY></HTML>');