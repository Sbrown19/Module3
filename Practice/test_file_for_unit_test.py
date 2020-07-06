import unittest
# import the file you want to test
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        # additional test this will only run it once.
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

      def test_subtract(self):
        # additional test this will only run it once.
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)




if __name__ == '__main__':
    unittest.main()
