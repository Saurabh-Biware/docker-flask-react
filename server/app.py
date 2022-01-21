from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=["GET"])
def index():
    return{
        "channel": "My Show",
        "Saurabh": "Saurabh"
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')