from flask import Flask,request
from emp_logic_web import empDetails
app = Flask(__name__)


@app.route("/emp/<int:id>",methods = ["GET"])
def emp(id):
    res = empDetails(id)
    return res



if __name__=="__main__":
    app.run(debug=True)