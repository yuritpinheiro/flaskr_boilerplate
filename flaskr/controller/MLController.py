from flask_restful import Resource
from flask_restful import reqparse


import requests
import json


score_url = "https://us-south.ml.cloud.ibm.com/v3/wml_instances/00a01c40-3bf6-41a4-8cf3-0f1dda0790fc/deployments/83b32e73-851c-4f8f-8264-c2b14ff808cf/online"

parser = reqparse.RequestParser()
parser.add_argument('na_to_k', type=float)
parser.add_argument('age', type=int)

class MLController(Resource):


    def get(self, na_to_k):

        # Paste your Watson Machine Learning service apikey here
        # Use the rest of the code sample as written
        apikey = "IB-zUzADIFWWUmqrkQG9EhUOdZwb0SrokoKpwfZE_7mo"

        # Get an IAM token from IBM Cloud
        url     = "https://iam.bluemix.net/oidc/token"
        headers = { "Content-Type" : "application/x-www-form-urlencoded" }
        data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
        IBM_cloud_IAM_uid = "bx"
        IBM_cloud_IAM_pwd = "bx"
        response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
        iam_token = response.json()["access_token"]

        body = {
            'fields': ["Age", "Sex", "BP", "Cholesterol", "Na_to_K"],
            'values': [[20, 'M', 'HIGH', 'HIGH', na_to_k]]
        }

        headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + iam_token
            }

        response = requests.post(url=score_url, data=json.dumps(body), headers=headers)

        return response.json()

    def post(self):
        args = parser.parse_args()

        print(args['na_to_k'])
        # Paste your Watson Machine Learning service apikey here
        # Use the rest of the code sample as written
        apikey = "IB-zUzADIFWWUmqrkQG9EhUOdZwb0SrokoKpwfZE_7mo"

        # Get an IAM token from IBM Cloud
        url     = "https://iam.bluemix.net/oidc/token"
        headers = { "Content-Type" : "application/x-www-form-urlencoded" }
        data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
        IBM_cloud_IAM_uid = "bx"
        IBM_cloud_IAM_pwd = "bx"
        response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
        iam_token = response.json()["access_token"]

        body = {
            'fields': ["Age", "Sex", "BP", "Cholesterol", "Na_to_K"],
            'values': [[args['age'], 'F', 'HIGH', 'HIGH', float(args['na_to_k'])]]
        }

        headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + iam_token
            }

        response = requests.post(url=score_url, data=json.dumps(body), headers=headers)

        return response.json()
