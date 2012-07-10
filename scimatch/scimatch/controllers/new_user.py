from flask import g, render_template, Module
from scimatch import app

#@app.route("/")
#def index():
#    return "Index Page"

@app.route("/new_user")
def new_user():

	returnDict = dict()
	returnDict["test"] = "test"
	
	return render_template('new_user.html', **returnDict)

