# Program: Basic if elif statement
# Author: Skyler Brown
# Date: 06/10/2020
print("Welcome to the Programmer Toolkit subscription.")
print("Select the level for this months subscription.")
level_selection = input("Select your subscription level:")
level_selection = int(level_selection)
print(f'You entered {level_selection}')
platinum = 60
gold = 50
silver = 40
bronze = 30
free_trial = 0


# If statement
if platinum < 61:
    print(level_selection)
elif level_selection < 51:
    print(gold)
elif level_selection < 41:
    print(silver)
elif level_selection < 31:
    print(bronze)
elif level_selection < 1:
    print(free_trial)
else:
    print("Exit")
