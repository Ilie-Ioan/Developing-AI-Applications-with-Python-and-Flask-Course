import unittest

from mymodule import square,double,add

class TestSquare(unittest.TestCase):

    def test1(self):

        self.assertEqual(square(2), 4)
        self.assertEqual(square(3.0), 9)

class TestDouble(unittest.TestCase):
    def test2(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(-3.1), -6.2)
        self.assertEqual(double(0), 0)

class TestAdd(unittest.TestCase):
    def test3(self):
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(3.0, 2.0), 5.0)
        self.assertEqual(add('Hello', 'World'), 'HelloWorld')
        self.assertNotEqual(add(-2, -2),0)

unittest.main()

