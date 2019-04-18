import os
from flask import Flask, current_app, send_file, send_from_directory

from .api import api_bp
from .client import client_bp


app: Flask = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)
# app.register_blueprint(client_bp)

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))


@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)


@app.route('/favicon.ico')
def favicon():
    dist_dir = current_app.config['DIST_DIR']
    return send_from_directory(dist_dir, 'favicon.ico', mimetype='image/vnd.microsoft.icon')