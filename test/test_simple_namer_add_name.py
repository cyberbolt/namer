from unittest import TestCase, main


class TestNamerNameInput(TestCase):
    def setUp(self): # pragma: no cover
        from app.core.simple_namer import SimpleNamer
        self.namer = SimpleNamer()

    def test_add_name_length_normal(self):
        new_name = 'Peter'
        self.namer.addName(new_name)
        # try:
        #     myFunc()
        # except ExceptionType:
        #     self.fail("myFunc() raised ExceptionType unexpectedly!")

    def test_add_name_empty(self):
        names = self.namer.getNames()
        new_name = ''
        self.namer.addName(new_name)
        new_names = self.namer.getNames()
        self.assertEqual(names, new_names)

    def test_add_name_non_str(self):
        names = self.namer.getNames()
        new_name = 0xDEADBEEF
        self.namer.addName(new_name)
        new_names = self.namer.getNames()
        self.assertEqual(names, new_names)

    def tearDown(self): # pragma: no cover
        pass

    def addCleanup(self): # pragma: no cover
        pass


if __name__ == '__main__':
    main()
