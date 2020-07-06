import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

def average(score1, score2, score3):
    NUMBER_TEST = 3
    return float ((score1 + score2 + score3)/NUMBER_TEST)

def test_average_exception(self):
    with self.assertRaises(ValueError):
        average(-90, 89, 78)
raise ValueError

def test_average_exception(self):
    with self.assertRaises(ValueError):
        average(90,-89, 79)

if __name__ == '__main__':
    unittest.main()
