from flask import send_from_directory
from flask_restful import Resource
from flask_restful import reqparse
import werkzeug

import requests
import json

import os

score_url = "https://us-south.ml.cloud.ibm.com/v3/wml_instances/00a01c40-3bf6-41a4-8cf3-0f1dda0790fc/deployments/83b32e73-851c-4f8f-8264-c2b14ff808cf/online"

parser = reqparse.RequestParser()
parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

class ImageController(Resource):

    def get(self, file_name):
        # parse = reqparse.RequestParser()
        # parse.add_argument('file', type=str)
        # args = parse.parse_args()
        return send_from_directory("/home/ryuga/Documentos/Dev Projetos/flask_boilerplate/", file_name+ ".jpg", as_attachment=True)
        # return { "message": "aafasdf" }, 200

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        audioFile = args['file']
        audioFile.save("your_file_name.jpg")
        return { "message": "OK"}, 200