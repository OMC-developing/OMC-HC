from flask import Flask, request
from flask_restful import Resource, Api
#from json import dumps
from flask.json import jsonify
from docker_api import API
from os import listdir

app = Flask(__name__)
api = Api(app)


class Get_help(Resource):
    def get(self):
        return jsonify(['services'])

class Services(Resource):
    def get(self):
        return jsonify(listdir('/usr/local/OMC/'))

class Docker_help(Resource):
    def get(self):
        return jsonify(['list', 'list/verbose', 'alllist', 'alllist/verbose'])

class Docker_info(Resource):
    def get(self):
        server = API()
        return jsonify(server.info())

class Containers_list(Resource):
    def get(self):
        server = API()                
        return jsonify(server.list())

class Containers_list_verbose(Resource):
    def get(self):
        server = API()                
        return jsonify(server.list(verbose=True))

class Containers_alllist(Resource):
    def get(self):
        server = API()                
        return jsonify(server.list(all=True))

class Containers_alllist_verbose(Resource):
    def get(self):
        server = API()                
        return jsonify(server.list(verbose=True, all=True))

api.add_resource(Get_help, '/get')
api.add_resource(Services, '/get/services')
api.add_resource(Docker_help, '/docker')
api.add_resource(Docker_info, '/docker/info')
api.add_resource(Containers_list, '/docker/list')
api.add_resource(Containers_list_verbose, '/docker/list/verbose')
api.add_resource(Containers_alllist, '/docker/alllist')
api.add_resource(Containers_alllist_verbose, '/docker/alllist/verbose')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6880')
