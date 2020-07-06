# Program: Unit Test for a Class Assignment
# Author: Skyler Brown
# Date: 07/01/2020
class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)

def message(self):
   return 'Hello, Classes!'

# Driver code
invoice = Student(1234, 4321, '1011 Main Dr, Anaheim, CA 92802' ,'Rowat', 'Megan', '515-258-3268')
invoice.add_item({'Smart TV': 799.99})
invoice.add_item({'Dirt Bike': 999.99})
invoice.create_invoice()
