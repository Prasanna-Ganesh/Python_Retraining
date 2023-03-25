from flask import Flask,request

app = Flask(__name__)

@app.route("/poc1/<x>",methods=["GET"])
def poc1(x):
    return "poc1 "+x

@app.route("/poc2/",methods=["POST"])
def admin():
    x=request.form["nm"]
    return "poc2 "+x

if __name__ == "__main__":
    app.run(debug=True)