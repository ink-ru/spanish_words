# -*- coding: utf-8 -*-
import os
import yaml
from flask import Flask # send_from_directory
from flask_restful import Resource, Api, reqparse
from flask_jsonpify import jsonify
import random

true = True
false = False
cr_flag = False

try:
	from flask_cors import CORS, cross_origin
except ImportError:
	print('CORS error')
except Exception:
	print('Unknown error')
else:
	cr_flag = True

app = Flask(__name__)

# app = Flask(__name__, root_path='/api')
# app.config["APPLICATION_ROOT"] = "/api"
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'


if cr_flag:
	# https://flask-cors.readthedocs.io/en/latest/
	# CORS(app, support_credentials=True)
	# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
	pass

api = Api(app)

'''
@app.after_request
def add_headers(response):
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
    return response
'''

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


@app.route('/')
# @cross_origin(origin='*',headers=['Content-Type','Authorization'])
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