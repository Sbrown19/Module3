# Program: Function return value Assignment
# Author: Skyler Brown
# Date: 06/17/2020
def get_user_input():
    name = input("Enter your name")
    print(name, " Earned", week_pay_amount,"for the week")

def get_weekly_pay():
     hours_worked = int(input("Please enter your hours for the week"))
    hourly_pay = float(input("What is your hourly wage."))
    week_pay_amount = hourly_pay * hours_worked
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

if __name__== '__main__':
    try:
        get_weekly_pay()
    except ValueError as err:
        print("ValueError encountered! ")
