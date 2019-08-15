from flask import Flask, jsonify
from flask_restful import Resource, Api

from flaskr.controller.HelloController import HelloController

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    
    api.add_resource(HelloController, '/hello')

    # a simple page that says hello
    # @app.route('/hello2', methods=['GET'])
    # def hello2():
    #     return 'Hello, World!'

    return app
