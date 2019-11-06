from flask_script import Command


class Autotest(Command):
    "Run unittests on app automatically"

    def run(self):
        import unittest
        test_directory = '.'

        suite = unittest.defaultTestLoader.discover(test_directory)
        tests_result = unittest.TextTestRunner(verbosity=2).run(suite)

        if len(tests_result.failures) > 0 or len(tests_result.errors) > 0:
            raise Exception