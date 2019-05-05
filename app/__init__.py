import os
import json
import datetime
from bson.objectid import ObjectId
from flask import Flask, current_app, send_file, send_from_directory
from flask_pymongo import PyMongo

from .api import api_bp
from .client import client_bp


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


app: Flask = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))


app.config['MONGO_URI'] = Config.DB
# app.register_blueprint(client_bp)
mongo = PyMongo(app)

# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
app.json_encoder = JSONEncoder




@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)


@app.route('/favicon.ico')
def favicon():
    dist_dir = current_app.config['DIST_DIR']
    return send_from_directory(dist_dir, 'favicon.ico', mimetype='image/vnd.microsoft.icon')