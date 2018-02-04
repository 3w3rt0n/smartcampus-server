import os
from flask import Flask
from flask import request
from flask import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python!"

@app.route("/json", methods=['GET','POST'])
def json():
    if request.json:
        mydata = request.json         
        return "Temperatura: %s *C" % mydata.get("dispositivo")
    else:
        return "Erro: solicitação não é JSON válido."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
