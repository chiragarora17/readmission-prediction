from flask import Flask, jsonify, request, make_response, abort, Response
from flask_restful import Api, Resource
import sys
import FrontDCModel as model

app = Flask(__name__)
api = Api(app)


class PredictAPI(Resource):
	def get(self):
		return make_response(jsonify(message="healthy"), 200)

	def post(self):
		data = request.get_json()
		if (data != None):
			res = model.predict(data)
			strRes = "patient will mostly not admit"
			if (res[0] != 0):
				strRes = "patient may re-admit"
			return make_response(jsonify(message=strRes), 201)
		else:
			return make_response(jsonify(message="invalid input. need json"), 404)

		# if k in data:
		# 	abort(404)
		# else:
		# 	print(request.json)
		# 	# data.append({k:)
		# return make_response(jsonify(message="created"), 201)

api.add_resource(PredictAPI, '/api/v1/predict', endpoint = 'predict')

if __name__ == '__main__':
    app.run(debug=sys.argv[1], host='localhost', port=5005)
