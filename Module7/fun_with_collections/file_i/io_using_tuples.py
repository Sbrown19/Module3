# Program: file i/0 using tuples assignment
# Author: Skyler Brown
# Date: 06/21/2020

import os as os

file_dir = os.path.dirname(__file__)
file_name = "testscores.txt"
f = open(os.path.join(file_dir, file_name), "r")
line1 = f.read()
print(line1)
f.close()


