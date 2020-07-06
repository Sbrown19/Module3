# Program: Class Composition assignment
# Author: Skyler Brown
# Date: 07/02/2020

class Employee:

        def __init__(self, lname, fname,):
            name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'_")
            if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
                raise ValueError
            self.last_name = lname
            self.first_name = fname


        def display(self):
            return str(self.last_name) + ", " + str(self.first_name) + '\n' + self.address.display()



print(person1.display())




class Student:
        def __init__(self, fname, lname, major, startdate, gpa ):
            self.first_name = fname
            self.last_name = lname
            self.major = major
            self.startdate = startdate
            self.gpa = gpa

        def change_major(self, major):
            self.newmajor = major
            major = 'Being Awesome'
            return newmajor

        def update_gpa(self, gpa):
            self.newgpa = gpa
            gpa = 3.0 +  'Your new gpa is 3.0'
            return newgpa

        def display(self):
            return (self.first_name, self.last_name, self.major, self.startdate, self.gpa)



print(Student)
print(change_major())
print(update_gpa())
print(display())

