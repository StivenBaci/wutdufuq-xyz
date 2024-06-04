from flask import request, Flask, jsonify, render_template
import os
import dmrv_html_generator as html_generator
from datetime import datetime
import requests


app = Flask(__name__,
            static_url_path='', 
            static_folder='templates/assets'
)


@app.route('/')
def index():
    log_ip()
    return render_template('index.html')

# @app.route('/gango44')
# def gango44():
#     return html_generator.getHTMLTable()

# @app.route('/luckyluciano')
# def luckyluciano():
#     return html_generator.getProfileReport()

@app.route("/get_ip", methods=["GET"])
def get_ip():
    return log_ip()

def log_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = f"IP: {ip}, Timestamp: {timestamp}"
    
    # Generate a unique URL path
    nfty_url = "https://nfty.sh/wutdufuqxyzlog"
    
    # Send the data to the unique nfty.sh URL
    response = requests.post(nfty_url, data=data.encode('utf-8'))
    
    if response.status_code == 200:
        return ip
    else:
        return "Failed to send data", 500

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
