__author__ = 'Sergey'

#!/usr/bin/python
from flask import Flask
app=Flask("webhello")

@app.route("/<any:path>")
def hello_world():
	return ("<HTML><BODY>hello, world</BODY></HTML>");


