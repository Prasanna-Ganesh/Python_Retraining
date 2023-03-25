from model import task
from flask import Flask,request,json,jsonify

app = Flask(__name__)
@app.route("/object/",methods=["GET"])
def object():
    b=[]
    a = task(1,"First","Best",5)
    b.append(a)
    # print(f"value is {a}")
    return json.dumps(a)


if __name__ == "__main__":
    app.run(debug=True)