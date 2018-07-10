from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.json import jsonify

from os import listdir

app = Flask(__name__)
api = Api(app)

class Services(Resource):
    def get(self):
        return jsonify(listdir('/'))

api.add_resource(Services, '/services')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6880')
