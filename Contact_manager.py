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
    def display_contact(self):
        return self.contact_book
    def save_contacts(self):
        with open("contacts.txt","w") as file:
            file.write(json.dumps(self.contact_book))
    def load_contacts(self):
        with open("contacts.txt", "r+") as file:
            self.contact_book = json.load(file)
