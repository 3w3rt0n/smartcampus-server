# -*- coding: utf-8 -*-
import os
import sys
import datetime
import time
import Flask


app = Flask("Hello World")


@app.route("/")
def indexHTML():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
