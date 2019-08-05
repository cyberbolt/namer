import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server, Command
from app import app

manager = Manager(app)

manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
)

from tools.managers.database_manager import manager as database_manager
manager.add_command("database", database_manager)

class Autotest(Command):
    "Run unittests on app automatically"
    def run(self):
        import unittest
        test_directory = 'test'

        suite = unittest.defaultTestLoader.discover(test_directory)
        tests_result = unittest.TextTestRunner(verbosity=2).run(suite)
        
        if len(tests_result.failures) > 0 or len(tests_result.errors) > 0:
            raise Exception


manager.add_command('autotests', Autotest())


if __name__ == '__main__':
    try:
        manager.run()
    except Exception as err:
        sys.exit(1)
