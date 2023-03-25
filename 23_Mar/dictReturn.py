from model import task
from flask import Flask,request,json,jsonify

app = Flask(__name__)
@app.route('/getdict/', methods=['GET'])
def getdict():
    d1 = {1: 'kishore',2: 'prasanna'}
    data = request.form['number']
    print(f"Value is {data}")
    return d1


if __name__ == "__main__":
    app.run(debug=True)



