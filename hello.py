# -*- coding: utf-8 -*-
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    <h1>Hello heroku</h1>
    """

if __name__ == '__main__':
    app.run()
