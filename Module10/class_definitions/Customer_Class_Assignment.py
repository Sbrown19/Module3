# Program: Invoice Assignment
# Author: Skyler Brown
# Date: 07/01/2020
customer_id = 1234
last_name = "Brown"
first_name = "Skyler"
phone_number = "515-111-1234"
address = "123 Main Road"

class Customer:
 customer_id = 1234
 last_name = "Brown"
 first_name = "Skyler"
 phone_number = "515-111-1234"
 address = "123 Main Road"

    def message(self):
        return 'Hello, Classes!'

# Driver
simpleObj = Customer() # make a class object
print(simpleObj.max)        # access class definition
print(simpleObj.message())  # call class method
del simpleObj               # clean up objects by deletion
