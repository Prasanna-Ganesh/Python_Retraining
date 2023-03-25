from flask import Flask,request
from json_logic import area_perimeter
app = Flask(__name__)


@app.route("/js/",methods = ["POST"])
def js():

    result = area_perimeter(request.json)
    return f"{result}"
    return res


if __name__=="__main__":
    app.run(debug=True)


