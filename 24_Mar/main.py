from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app)  # we are using restful api

devices_args_parse = reqparse.RequestParser()
devices_args_parse.add_argument("name", type=str, help="employee name has to given", required=True)
devices_args_parse.add_argument("status", type=bool, help="Employee_status")


class Employee(Resource):  # class which can be shared like a restful
    def get(self, emp_id):
        # if emp_id == 23:
        #     abort(404, message="invalid results")
        return {"Employee id" : emp_id}

    def post(self, emp_id):
        # return { "msg":request.form['key']}
        inputs = devices_args_parse.parse_args()
        return {"msg": inputs,"Message":"Employee Added Sucessfully"}, 201

    def delete(self, emp_id):
        return {"Employee id" : emp_id,"msg": "Employee deleted sucessfully"}

    def put(self, emp_id):
        inputs = devices_args_parse.parse_args()
        return {"msg": inputs,"msg": "sucessfully updated employee"}


# register this as a resource.
api.add_resource(Employee, "/emp/<int:emp_id>")

app.run(debug=True)  # dont use in production envrionment
