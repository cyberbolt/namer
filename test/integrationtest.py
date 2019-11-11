from flask_script import Command, Option
import requests
from time import time


class Integrationtest(Command):
    "Run integration tests on app automatically"

    def __init__(self, url=''):
        self.url = url
        super().__init__()

    def get_options(self):
        return [
            Option('-u', '--url', dest='url', default=self.url),
        ]

    def run(self, url):
        print("Run 1st test..."),
        get_response = requests.get(url)
        if get_response.status_code != 200:
            raise Exception(f"Error getting main page {get_response.status_code}")
        print("OK")

        print("Running 2nd test..."),
        new_name = f'new_name_{time()}'
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "name": new_name
        }
        post_response = requests.post(url,
                                      headers=headers,
                                      data=data)
        if post_response.status_code != 302:
            raise Exception(f"Error posting form data {get_response.status_code}")
        print("OK")

        print("Running 3rd test..."),
        updated_request = requests.get(url)
        if new_name not in updated_request.text:
            raise Exception(f"Cannot find name {new_name} in the names list")
        print("OK")
        print("All integration tests are passed")
