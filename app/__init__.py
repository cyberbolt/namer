from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)


from .config import Config
app.config.from_object(Config)

def register_blueprints(app):
    # Prevents circular imports
    from app.views import names
    app.register_blueprint(names)


db = MongoEngine(app)
register_blueprints(app)


if __name__ == '__main__':
    app.run()
