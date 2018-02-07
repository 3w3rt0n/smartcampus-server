import os
import psycopg2
from flask import Flask, render_template
from flask import request
from flask import json
from string import Template
from flask.ext.socketio import SocketIO

from urllib import parse

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cur = conn.cursor()
cur2 = conn.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html',)

@socketio.on('send_message')
def handle_source(json_data):
    text = json_data['message'].encode('ascii', 'ignore')
    socketio.emit('echo', {'echo': 'Server Says: '+text})
    print("MSG: " + text)

if __name__ == "__main__":
    socketio.run(app)
