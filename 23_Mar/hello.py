from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/admin",methods=["POST"])
def admin():
    scrap=request.form["nm"]
    print("Welcome Admin")
    return "Hiiii "+scrap

if __name__ == "__main__":
    app.run(debug=True)