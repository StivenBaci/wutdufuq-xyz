from flask import request
from flask import Flask, jsonify, render_template
import os
import dmrv_html_generator as html_generator


app = Flask(__name__,
            static_url_path='', 
            static_folder='templates/assets'
)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gango44')
def gango44():
    return html_generator.getHTMLTable()

@app.route('/luckyluciano')
def luckyluciano():
    return html_generator.getProfileReport()

@app.route("/get_ip", methods=["GET"])
def get_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
