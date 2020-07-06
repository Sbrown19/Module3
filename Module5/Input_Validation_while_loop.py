# Program: Input Validation while loop
# Author: Skyler Brown
# 06/13/2020
# First input validation
random_var = int(input("Enter a number between 1 and 100"))
while random_var < 100:
    print("Your number is not in range")
    break
# Second input validation
number_guessed = int(input("Enter a number between 1 and 100"))
while number_guessed < 1:
    print("Enter another number")
    break
while number_guessed > 100:
    print("Enter another number")
    break
while number_guessed <= 1 >= 100:
    print("True")
    break
list_start = number_guessed
number_guessed2 = list_start
number_guessed = number_guessed2
print(list_start)

