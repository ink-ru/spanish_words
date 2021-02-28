# -*- coding: utf-8 -*-

import os
import yaml
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jsonpify import jsonify
import random

true = True
false = False
cr_flag = False

'''
try:
	from flask_cors import CORS
except ImportError:
	print('CORS error')
except Exception:
	print('Unknown error')
else:
	cr_flag = True
'''

# app = Flask(__name__, root_path='/api')
# app.config["APPLICATION_ROOT"] = "/api"
app = Flask(__name__)

if cr_flag:
	# https://flask-cors.readthedocs.io/en/latest/
	cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

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