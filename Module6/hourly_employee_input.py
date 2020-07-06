# Program: Hourly Employee input
# Author: Skyler Brown
# Date: 06/17/2020
def get_user_input():
    name = input("Enter your name")
    hours_worked = int(input("Please enter your hours for the week"))
    hourly_pay = float(input("What is your hourly wage."))
    print(name, " Worked", hours_worked,"hours this week and make", hourly_pay, "hourly.")


if __name__== '__main__':
    try:
        get_user_input()
    except ValueError as err:
        print("ValueError encountered! ")
# Call function using negative numbers
if __name__== '__main__':
    try:
        get_user_input()
    except ValueError as err:
        print("ValueError encountered! ")
# Call function using bad input
if __name__== '__main__':
    try:
        get_user_input()
    except ValueError as err:
        print("ValueError encountered! ")
