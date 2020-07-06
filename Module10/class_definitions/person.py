class definitions:

    height = 6.2

    def message(self):
        return 'The height is'


# Driver
simpleObj = definitions() # make a class object
print(simpleObj.height)        # access class definition
print(simpleObj.message())  # call class method
del simpleObj

class Person:
    """Person class"""
    def __init__(self, lname, fname, ssn=''):         # Constructor
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def __str__(self):
        return 'Person with last name ' + str(self.last_name) + ', first name ' + str(self.first_name)
# Driver
# Valid person
person1 = Person('Duck', 'Donald') # ssn not required
print(str(person1))
