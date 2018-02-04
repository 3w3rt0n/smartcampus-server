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
        return "Dispositivo: %s\n::Temperatura: %s *C\n::Umidade: %s %%\n::Som: %s db\n::Luminosidade: %s lux\n" % (mydata.get("dispositivo"),mydata.get("temperatura"),mydata.get("umidade"),mydata.get("som"),mydata.get("luminosidade"))
    else:
        return "Erro: solicitação não é JSON válido."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
