# Program: Function Parameter Assignment
# Author: Skyler Brown
# Date: 06/17/2020
def multiply_string():
    a = "Hello"
    b = "how"
    c = "are"
    d = "you"
    print(a, (len(a)))
    print(b, (len(b)))
    print(c, (len(c)))
    print(d, (len(d)))
if __name__== '__main__':
    try:
        multiply_string()
    except ValueError as err:
        print("ValueError encountered! ")
