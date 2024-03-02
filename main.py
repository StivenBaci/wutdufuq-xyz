from flask import request
from flask import Flask, jsonify, render_template
import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='templates/assets'
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get_ip", methods=["GET"])
def get_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return "<p> " + request.environ['REMOTE_ADDR'] + " </p>"
    else:
        return "<p> " + request.environ['HTTP_X_FORWARDED_FOR'] + " </p>"

@app.route('/multistep')
def multistep():
    return render_template('multistepform.html')


@app.route('/hoai')
def multistep():
    return render_template('hoai-newsletter.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
