# Program: Input Validation with try Assignment
# Author: Skyler Brown
# Date: 06/10/2020
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
