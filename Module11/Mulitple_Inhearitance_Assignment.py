# Program: Multiple Inheritance Assignment
# Author: Skyler Brown
# Date: 07/03/2020
# This is my message.

class Employee:

        def __init__(self, lname, fname, date, salary, hourlyPay):
            name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'_")
            if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
                raise ValueError
            self.last_name = lname
            self.first_name = fname
            self.date = date
            self.salary = salary
            self.hourly_pay = hourlyPay

        def display(self):
            return str(self.last_name) + ", " + str(self.first_name) + '\n' + self.address.display()

class Person:

        def __init__(self, lname, fname, addy=''):
            name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'_")
            if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
                raise ValueError
            self.last_name = lname
            self.first_name = fname
            self.address = addy

        def display(self):
            return str(self.last_name) + ", " + str(self.first_name) + '\n' + self.address.display()

class Manager(Person, Employee):
        def __init__(self, department, mangerID, salary, directReports):
            self.department = department
            self.mangerID = mangerID
            self.direct_reports = directReports
            self.salary = salary


        def display(self):
            return str(self.department) + ", " + str(self.mangerID) + '\n' + self.salary.display() + self.direct_reports




manager1 = Manager('Manager', '356', '42000', 'Report 1')
print(manager1.display())
