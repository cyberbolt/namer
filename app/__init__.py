import os
from flask import Flask, current_app, send_file

app = Flask(__name__, static_folder='../dist/static')


@app.route('/')
def default_route():
    dist_dir = current.app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')

    return send_file(entry)
