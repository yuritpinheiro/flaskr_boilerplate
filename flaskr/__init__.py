from flask import Flask, jsonify
from flask_restful import Resource, Api

from flaskr.controller.HelloController import HelloController
from flaskr.controller.MLController import MLController

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    
    api.add_resource(HelloController, '/hello')
    api.add_resource(MLController, '/ml')

    return app

app = create_app()