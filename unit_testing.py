import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.lower(), 'foo')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestCustom(unittest.TestCase):

    def test_equation(self):
        self.assertEqual(5 + 2, 7)

    def test_variables(self):
        a = 5
        b = 7
        self.assertEqual(a + b, 12)

if __name__ == '__main__':
    unittest.main()