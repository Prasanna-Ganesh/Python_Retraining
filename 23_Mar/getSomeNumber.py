from flask import Flask,request

app = Flask(__name__)

@app.route("/getSomeNumber/",methods=["GET"])
def getSomeNumber():
    list1 = [7,8,9]
    a =request.form["nu"]
    print(f"value is {a}")
    return list1


if __name__ == "__main__":
    app.run(debug=True)