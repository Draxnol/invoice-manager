#Contact Name, Contact Billing address, Contact ltd, Contact invoice count
import json
class Contact_manager:
    def __init__(self):
        self.contact_book = {}
    def create_contact(self):
        contact_ID = input("Enter contact ID or code or nickname")
        self.contact_book[contact_ID] = {"contact_name":"", "contact_billing":"", "contact_LTD":"", "inovice_count":""} 
        user_input = input("enter contact name\n")
        self.contact_book[contact_ID]["contact_name"] = user_input
        user_input = input("enter contact billing information")
        self.contact_book[contact_ID]["contact_billing"] = user_input
        user_input = input("enter contact ltd number")
        self.contact_book[contact_ID]["contact_LTD"] = user_input
    def modify_contact(self, contact_ID):
        print("Options should be:")
        print("1:\t Change contact name")
        print("2:\t Change contact billing address")
        print("3:\t Change contact ltd number")
        user_input = input("Enter selection:")
        if(int(user_input) == 1):
            print("Current contact name is: {}".format(self.contact_book[contact_ID]["contact_name"]))
            user_input2 = input("Enter new value\n")
            self.contact_book[contact_ID]["contact_name"] = user_input2
        if(int(user_input) == 2):
            print("Current contact billing address is: {}".format(self.contact_book[contact_ID]["contact_billing"]))
            user_input2 = input("Enter new value\n")
            self.contact_book[contact_ID]["contact_name"] = user_input2
        if(int(user_input) == 3):
            print("Current company ltd is: {}".format(self.contact_book[contact_ID]["contact_LTD"]))
            user_input2 = input("Enter new value\n")
            self.contact_book[contact_ID]["contact_name"] = user_input2
    def display_contact(self):
        return self.contact_book
    def save_contacts(self):
        with open("contacts.txt","w") as file:
            file.write(json.dumps(self.contact_book))
    def load_contacts(self):
        with open("contacts.txt", "r+") as file:
            self.contact_book = json.load(file)
