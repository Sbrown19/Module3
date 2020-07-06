# Program: Function keyword and arbitrary arguments assignment
# Author: Skyler Brown
# Date: 06/21/2020

def average_scores(*args):
    pass

if __name__ == '__main__':
    print(average_scores(40, 30, 20, 40))
    print(average_scores(41, 13, 25, 4, 5, 91))
    print(average_scores(4.5, 7.4))

    def average_scores(*args, **kwargs):
    # Use *args for average calculation
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    # return


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))

