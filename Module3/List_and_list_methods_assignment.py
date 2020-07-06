# Progream: List and list Method Assingment
# Author: Skyler Brown
# Date: 06/06/2020
# from typing import List

listOne = ['Hotdogs','Lettuce','Ketchup']
listTwo = ['Soap', 'Toothpaste','Soda']
print(listOne)
# Append
listOne.append("Hamburgers")
print(listOne)
# Clear
listOne.clear()
print(listOne)
# Copy
x = listOne.copy()
print(x)
# Count
y = listOne.count("Ketchup")
print(y)
# Extend
listOne = ['Hotdogs','Lettuce','Ketchup']
m = listOne.extend(listTwo)
print(listOne)
# Index
listOne = ['Hotdogs','Lettuce','Ketchup']
i = listOne.index("Lettuce")
print(i)
# Second run for index
#listOne = ['Hotdogs','Lettuce','Ketchup']
#j = listOne.index('Mayo')
#print(j)
# Insert
listOne = ['Hotdogs','Lettuce','Ketchup']
listOne.insert(1, "Milk")
print(listOne)
# Remove
listOne = ['Hotdogs','Lettuce','Ketchup']
listOne.remove("Hotdogs")
print(listOne)
# Reverse
listOne = ['Hotdogs','Lettuce','Ketchup']
listOne.reverse()
print(listOne)
# Sort
listOne = ['Hotdogs','Lettuce','Ketchup']
listOne.sort()
print(listOne)
