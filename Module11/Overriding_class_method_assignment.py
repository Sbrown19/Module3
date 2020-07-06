# Program: Overriding Class Method 
# Author: Skyler Brown
# Date: 07/02/2020

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





class sallariedEmployee(Employee):
    self.salary = newSalary = '45000'
    return (self.first_name), + (self.last_name), + (self.startdate), + (self.salary )


class HourlyEmployee(Employee):
    self.hourly_pay = '$12.00'
    return (self.first_name), + (self.last_name), + (self.startdate), + (self.salary )


self.update(sallariedEmployee)
print(sallariedEmployee)



