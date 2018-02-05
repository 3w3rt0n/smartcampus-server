import os
import urlparse
import psycopg2
from flask import Flask
from flask import request
from flask import json
from string import Template

app = Flask(__name__)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

cur = conn.cursor()
cur2 = conn.cursor()

HTML_TEMPLATE = Template("""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="icon" href="http://imageshack.com/a/img923/6904/Ml2aYx.png" />
    <title>Server IoT</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.bundle.min.js"></script>
  </head>
  <body>
    <div class="jumbotron text-center">
      <h1>Smart Campus - JSON</h1>
      <h4>${dispositivo}</h4>
    </div>

	<div class="container" >		
		<h1>Temperatura: ${temperatura}ºC</h1>
		<h1>Umidade: ${umidade}%</h1>
		<h1>Som: ${som} db</h1>
		<h1>Luminosidade: ${luminosidade} lux</h1>
		
		<div id="canvas-holder" style="width:40%">
			<canvas id="chart-area" />
		</div>
		<script>
		   window.onload = function() {
			var ctx = document.getElementById("chart-area").getContext("2d");
			data = { datasets: [{ data: [10, 20, 30] }], labels: [ 'Red', 'Yellow',  'Blue' ] };
			window.myPieChart = new Chart(ctx, { type: 'pie', data: data, options: {responsive: true} } );
		   }
	    	</script>
	</div>
    
    <div class="panel-footer" style="position: absolute; bottom: 0; width: 100%; text-align: right;">Desenvolvidor por Ewerton Leandro de Sousa - 03/01/2017</div>
  </body>
</html>
""")

@app.route("/")
def hello():
    return "Hello from Python!"

@app.route("/json", methods=['GET','POST'])
def json():
    if request.json:
        mydata = request.json    
        return (HTML_TEMPLATE.substitute(dispositivo=mydata.get("dispositivo"), temperatura=mydata.get("temperatura"), umidade=mydata.get("umidade"), som=mydata.get("som"), luminosidade=mydata.get("luminosidade")))
        #return "Dispositivo: %s\n::Temperatura: %s *C\n::Umidade: %s %%\n::Som: %s db\n::Luminosidade: %s lux\n" % (mydata.get("dispositivo"),mydata.get("temperatura"),mydata.get("umidade"),mydata.get("som"),mydata.get("luminosidade"))
    else:
        return "Erro: solicitação não é JSON válido."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
