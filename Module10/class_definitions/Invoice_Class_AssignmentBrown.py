# Program: Invoice Assignment
# Author: Skyler Brown
# Date: 07/01/2020

class Invoice:
 invoice_id = 1234
 customer_id = 4321
 last_name = "Brown"
 first_name = "Skyler"
 phone_number = "515-111-1234"
 address = "123 Main Road"


def message(self):
   return 'Hello, Classes!'

# Driver code
invoice = Invoice(1234, 4321, '1011 Main Dr, Anaheim, CA 92802' ,'Rowat', 'Megan', '515-258-3268')
invoice.add_item({'Smart TV': 799.99})
invoice.add_item({'Dirt Bike': 999.99})
invoice.create_invoice()
