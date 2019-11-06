from flask_script import Command
import requests

class Integrationtest(Command):
    "Run integration tests on app automatically"

    def __init__(self, url=''):
        self.url = url
        super().__init__()

    def run(self):
        pass
