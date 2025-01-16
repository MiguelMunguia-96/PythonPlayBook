import unittest

from easy import *

class TestBaseEasy(unittest.TestCase):
    def test_t01(self):
        self.assertEqual(t01helloWorld("Test"), "Hellow world: Test")
    
    def test_t02(self):
        self.assertEqual(t02ifElse(3), "Weird - it's odd")
        self.assertEqual(t02ifElse(2), "Not weird - in range 2-5")
        self.assertEqual(t02ifElse(6), "Weird in range of 6-20")
        self.assertEqual(t02ifElse(22), "Not weird  n > 20")
    
    def test_t03(self):
        self.assertEqual(t03arithmeticOperators(4, 6), (10, -2 , 24))
        self.assertEqual(t03arithmeticOperators(-1, 6), "out of range")
        self.assertEqual(t03arithmeticOperators(60000, 1), "out of range")
        self.assertEqual(t03arithmeticOperators(1, -1), "out of range")
        self.assertEqual(t03arithmeticOperators(1, 60000), "out of range")

    def test_t04(self):
        self.assertEqual(t04division(4, 3), (1, 1.3333333333333333))
        self.assertEqual(t04division(0, 5), "divied by 0")

    def test_t05(self):
        self.assertEqual(t05loops(5), [0,1,4,9,16])
        self.assertEqual(t05loops(90), "out of range")

    def test_t06(self):
        self.assertTrue(t06function(2024))
        self.assertFalse(t06function(2025))
        self.assertFalse(t06function(1900))

    def test_t07(self):
        self.assertEqual(t07printFunction(5), [1,2,3,4,5])
        self.assertEqual(t07printFunction(155),  "out of range")


if __name__ == '__main__':
    unittest.main()