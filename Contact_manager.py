# Contact Name, Contact Billing address, Contact ltd, Contact invoice count
import json



class Contact_manager:

    def __init__(self):
        self.contact_book = {}
        self.file_name = "contacts.txt"

    def create_contact(self):
        contact_ID = input("Enter contact ID or code or nickname\n")
        self.contact_book[contact_ID] = {"contact_ID": contact_ID, "contact_name": "", "contact_billing": "", "contact_LTD": "", "inovice_count": ""}
        
        user_input = input("enter contact name\n")
        self.contact_book[contact_ID]["contact_name"] = user_input
        
        user_input = input("enter contact billing information\n")
        self.contact_book[contact_ID]["contact_billing"] = user_input
        
        user_input = input("enter contact ltd number\n")
        self.contact_book[contact_ID]["contact_LTD"] = user_input

    def modify_contact(self, contact_ID):
        print("Options should be:")
        print("1:\t Change contact name")
        print("2:\t Change contact billing address")
        print("3:\t Change contact ltd number")
        user_input = input("Enter selection:\n")

        if(int(user_input) == 1):
            print("Current contact name is: {}".format(self.contact_book[contact_ID]["contact_name"]))
            user_input2 = input("Enter new value\n")
            self.contact_book[contact_ID]["contact_name"] = user_input2

        if(int(user_input) == 2):
            print("Current contact billing address is: {}".format(self.contact_book[contact_ID]["contact_billing"]))
            user_input2 = input("Enter new value\n")
            self.contact_book[contact_ID]["contact_billing"] = user_input2

        if(int(user_input) == 3):
            print("Current company ltd is: {}".format(self.contact_book[contact_ID]["contact_LTD"]))
            user_input2 = input("Enter new value\n")
            self.contact_book[contact_ID]["contact_LTD"] = user_input2

    def display_contact(self):
       # Here are display options
        print("Display options should be")
        print("1:\tDisplay Contact and contact name")
        print("2:\tDisplay Contact billing addresses")
        print("3:\tDiplay Contacts and contact ltd")
        user_input = input("Enter Selection\n")
        
        if(int(user_input) == 1):
            for k in self.contact_book.values():
                print("_______________")
                print("Contact ID: {}\nContact Name: {}".format(k['contact_ID'], k['contact_name']))
            input("....")
        
        if(int(user_input) == 2):
            for k in self.contact_book.values():
                print("_______________")
                print("Contact ID: {}\nContact Name: {}".format(k['contact_ID'], k['contact_billing']))
            input("....")
        
        if(int(user_input) == 3):
            for k in self.contact_book.values():
                print("_______________")
                print("Contact ID: {}\nContact Name: {}".format(k['contact_ID'], k['contact_LTD']))
            input("....")


    def save_contacts(self):
        with open(self.file_name, "w") as file:
            file.write(json.dumps(self.contact_book))

    def load_contacts(self):
        with open(self.file_name, "r+") as file:
            self.contact_book = json.load(file)
