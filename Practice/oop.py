# Python Object-Oriented Programming
# Making classes

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)
# Person class ment for python class assignment
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

class Address:
        def __init__(self, st_number, st_name, st_type, city, state, zip, apt_num=''):
            self.street_number = st_number
            self.street_name = st_name
            self.street_type = st_type
            self.apartment_number = apt_num
            self.city = city
            self.state = state
            self.zip_code = zip

        def display(self):
            return(self.street_number + ' ' + self.street_name + ' ' + self.street_type + ' ' + self.apartment_number + '\n' + self.city + ', ' + self.zip_code)

class Customer:
        def __init__(self, fname, lname, phone, verse):
            self.first_name = fname
            self.last_name = lname
            self.phone_number = phone
            self.verse = verse

        def display(self):
            return(self.first_name, ' ' + self.last_name, + self.phone_number + self.verse)



class Invoice:
        def __init__(self, fname, lname, phone, verse):
            self.first_name = fname
            self.last_name = lname
            self.phone_number = phone
            self.verse = verse

        def display(self):
            return(self.first_name, ' ' + self.last_name, + self.phone_number + self.verse)


# Driver
captain_mal = Customer(1, 'Reynolds', 'Mel', 'No Phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
print(invoice())
# emp_1 = Employee('Skyler', 'Brown', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# Driver code
addy1 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111')
person1 = Person('Hammer', 'Martin', addy1)
print(person1.display())
 # Apartment number is at the end. Why?
addy2 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111', '16B')
person2 = Person('Hammer', 'Martin', addy2)
print(person2.display())
del (addy1, addy2)
del (person1, person2)
# p = Person('Hammer', 'M', '123 Main Street, USA')
# print(p.display())

# print(emp_1)
# print(emp_2)
# print(Employee.fullname(emp_1))
# print(emp_1.fullname())
# print(emp_2.fullname())
# print(emp_2.email)

