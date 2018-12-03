from flask import Flask,abort,jsonify,Response,json
from flask import request
from flask import request,render_template,send_file,send_from_directory

import datetime
import requests


app = Flask(__name__)
# Create a new user, if user already exists then return the response to select another user name else, return user id


@app.route("/")
def index():
   return send_file("index.html")

@app.route("/ui/<path:path>")
def file(path):
   return send_from_directory("ui",path)

@app.route('/getPredication')
def getPredication(path):
	#TODO : on submit this method will be called.

	return send_from_directory("server",path)


def preprocessData(data):
	# TODO : process the data to map to model
	
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=3005)
