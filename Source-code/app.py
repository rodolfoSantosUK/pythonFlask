from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

class Add(Resource):
    def post(self):

        postedData = request.get_json()
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x + y

        retMap = {
            'Sum' : ret,
            'Status code' : 200
        }

    return jsonify(retMap)


    def get(self):
        pass

    def put(self):
        pass

class Substract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass


api.add_resource(Add, "/add")

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__=="__main__":
    app.run(debug=True)
