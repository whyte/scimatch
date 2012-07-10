#!/usr/bin/python

from flask import Flask, Markup, request, g
#from database import connection
#import config

app = Flask(__name__)
#app.config.from_object(config)
#db = connection.Connection(app.config['DATABASE'])

#@app.before_request
#def start_session():
#    pass
#    g.session = db.get_session()
#
#@app.after_request
#def shutdown_session(response):
#    g.session.close()
#    return response
