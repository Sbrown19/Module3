# Program: Customer invoice assignment
# Author: Skyler Brown
# Date: 07/02/2020
class Customer:
        def __init__(self, fname, lname, phone, verse, tax, total):
            self.first_name = fname
            self.last_name = lname
            self.phone_number = phone
            self.verse = verse
            self.tax = tax
            self.total = total

        def display(self):
            return(self.first_name, ' ' + self.last_name, + self.phone_number + self.verse, + self.tax, + self.total)



class Invoice:
        def __init__(self, fname, lname, phone, verse, tax, total):
            self.first_name = fname
            self.last_name = lname
            self.phone_number = phone
            self.verse = verse
            self.tax = tax
            self.total = total


        def display(self):
            return(self.first_name, ' ' + self.last_name, + self.phone_number + self.verse)


# Driver
captain_mal = Customer('Reynolds', 'Mel', 'No Phones', 'Firefly, somewhere in the', '$108.00', '$1907.98')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
print(invoice())
