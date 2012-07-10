#!/usr/bin/python

import os

from flask import Flask
app = Flask(__name__)

from scimatch import app
from scimatch.controllers import new_user

@app.route('/')
def home_page():
    return 'Hello World!'



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

