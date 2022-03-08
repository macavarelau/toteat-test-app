from flask import Flask, jsonify
from flask_cors import CORS
import requests


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/', methods=['GET'])
def index():
    r = requests.get('https://storage.googleapis.com/backupdatadev/ejercicio/ventas.json')
    return jsonify(r.json())


if __name__ == '__main__':
    app.run()