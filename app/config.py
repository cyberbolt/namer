import os


class Config(object):
    # If not set fall back to production for safety
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')
    WTF_CSRF_ENABLED = False

    __DB = os.getenv('M_DB', 'DB')
    __HOST = os.getenv('M_HOST', 'localhost')
    __PORT = os.getenv('M_PORT', '27017')
    __USERNAME = os.getenv('M_USERNAME')
    __PASSWORD = os.getenv('M_PASSWORD')

    MONGODB_SETTINGS = {
        'db': __DB,
        'host': __HOST,
        'port': int(__PORT),
        'username': __USERNAME,
        'password': __PASSWORD,
        'alias': 'default'
    }
