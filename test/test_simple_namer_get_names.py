# test_simple_namer_get_names.py
from unittest import TestCase, main


class TestNamerNamesGet(TestCase):
    def setUp(self): # pragma: no cover
        self.names = ['Peter',
                      'John',
                      'Mary',
                      'Paul',
                      'Pauline',
                      'Jane']

    def getNamer(self, data=None):
        from app.core.simple_namer import SimpleNamer
        return SimpleNamer(data)

    def test_get_names_from_empty(self):
        namer = self.getNamer()

    def test_get_names_from_one(self):
        namer = self.getNamer()
        namer.addName(self.names[0])
        names = namer.getNames()
        self.assertEqual(names, [self.names[0]])

    def test_get_names_from_two(self):
        namer = self.getNamer(self.names[:2])
        names = namer.getNames()
        self.assertEqual(names, self.names[:2][::-1])

    def test_get_names_from_three(self):
        namer = self.getNamer(self.names[:3])
        names = namer.getNames()
        self.assertEqual(names, self.names[:3][::-1])

    def test_get_names_from_four(self):
        namer = self.getNamer(self.names[:4])
        names = namer.getNames()
        self.assertEqual(names, self.names[:4][::-1])

    def test_get_names_from_five(self):
        namer = self.getNamer(self.names[:5])
        names = namer.getNames()
        self.assertEqual(names, self.names[:5][::-1])

    def test_get_names_from_more_than_five(self):
        namer = self.getNamer(self.names[:6])
        names = namer.getNames()
        self.assertEqual(names, self.names[1:6][::-1])

    def tearDown(self): # pragma: no cover
        pass

    def addCleanup(self): # pragma: no cover
        pass


if __name__ == '__main__':
    main()
