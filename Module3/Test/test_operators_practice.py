# Progream: Basic input and format output Assingment
# Author: Skyler Brown
# Date: 06/06/2020
import unittest
class OperatorsTest(unittest.TestCase):
    def test_equal_operator(self):
        a = 7
        b = 7
        self.assertFalse(a == b)
    def test_notequal_operator(self):
        a = 3
        b = 5
        self.assertTrue(a != b)
    def test_greaterthan_operator(self):
        a = 7
        b = 5
        self.assertTrue(a > b)
    def test_lessthan_operator(self):
        a = 3
        b = 5
        self.assertTrue(a < b)
    def test_greaterthanorequalto_operator(self):
        a = 3
        b = 5
        self.assertTrue(a >= b)
    def test_lessthanorequalto_operator(self):
        a = 3
        b = 5
        self.assertTrue(a <= b)   

unittest.main()
