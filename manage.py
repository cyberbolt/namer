import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from app import app
from test.autotest import Autotest
from test.integrationtest import Integrationtest
from tools.managers.database_manager import manager as database_manager


manager = Manager(app)

manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
)
manager.add_command("database", database_manager)

# python manage.py autotests
manager.add_command('autotests', Autotest())

# python manage.py integrationtests --url http://test-server.my:5555
manager.add_command('integrationtests', Integrationtest())


if __name__ == '__main__':
    try:
        manager.run()
    except Exception as err:
        sys.exit(1)
