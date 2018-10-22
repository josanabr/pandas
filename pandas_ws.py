import pandas as pd
import time
import pickle
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)
url = "" 
df = ""

# 
# Funciones para manejo de errores
#
@app.errorhandler(400)
def not_defined(error):
	return make_response(jsonify({'ERROR': 'URL no instanciado'}),400)

@app.errorhandler(406)
def not_correct_data(error):
	return make_response(jsonify({'ERROR': 'No se especifico dato en formato JSON'}),406)

#
# Definicion de endpoints
#
@app.route('/pandas/aggr/v1.0', methods=['GET', 'POST'])
def info():
	global url
	global df
	if request.method == 'GET':
		if (url == ""): 
			abort(400)
		else: 
			return make_response(jsonify({'URL': url}), 200)
	elif request.method == 'POST':
		if not request.json or not 'URL' in request.json:
			print("POST")
			abort(406)
		else:
			url = request.json.get('URL',"")
			start = time.time()
			df = pd.read_csv(url)
			end = time.time()
			js = [ {'URL ': url, 'Tiempo descarga (sec)': (end - start) } ]
			return make_response(jsonify(results = js), 200)

#
#
#
@app.route('/pandas/aggr/v1.0/agregado', methods=['POST'])
def agregado():
	global df
	global url
	if (url == ""): 
		abort(400)
	if request.method == 'POST' and request.json:
		agregado = request.json.get('Agregado',"")
		field = request.json.get('Campo',"")
		func = getattr(df,agregado)
		start = time.time()
		result = func() # retorna Series
		end = time.time()
		js = [ {'Result ': result.to_string(), 'Tiempo ejecuion (sec)': (end - start) } ]
		return make_response(jsonify(results = js), 200)
	else:
		abort(406)

#
# Punto de inicio
#
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
