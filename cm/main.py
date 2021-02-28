# -*- coding: utf-8 -*-

import os
import yaml
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from flask_jsonpify import jsonify
import random

# app = Flask(__name__, root_path='/api')
# app.config["APPLICATION_ROOT"] = "/api"
app = Flask(__name__)
CORS(app)
api = Api(app)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


@app.route('/')
def index():
	return 'REST SERVER!'

class GetData(Resource):
	
	class Spanish(Resource):
		def get_data(self):
			with open(os.path.join(__location__, "./data.yaml"), 'r', encoding="utf-8") as stream:
				try:
					vocab = yaml.safe_load(stream)
					return random.choice(list(vocab.items()))
				except yaml.YAMLError as exc:
					print(exc)

		#@app.route('api/GetData/Spanish', methods=['GET'])
		def get(self):
			return jsonify( self.get_data() )
			# return self.get_data()

		#@app.route('api/GetData/Spanish', methods=['POST'])
		def post(self):
			return jsonify('Target method not supported!')

api.add_resource(GetData.Spanish, '/api/GetData/Spanish')