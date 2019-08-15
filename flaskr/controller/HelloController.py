from flask_restful import Resource


class HelloController(Resource):
    def get(self):
        return {'message': 'Hello, World! From restful'}
