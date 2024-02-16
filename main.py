from flask import request
from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route("/get_ip") #, methods=["GET"]
def get_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return "<p> " + request.environ['REMOTE_ADDR'] + " </p>"
    else:
        return "<p> " + request.environ['HTTP_X_FORWARDED_FOR'] + " </p>"

@app.route('/multistep')
def multistep():
    return render_template('multistepform.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
