from flask import Flask
from flask import request





app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"



@app.route("/loadModel", methods=['POST'])
def loadModel():
	#TODO Write model code here




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=3007)
