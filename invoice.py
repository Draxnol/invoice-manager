from datetime import datetime


class Invoice:
    """Class for invoices"""

   
    
    def set_date(self):
        self.date = datetime.today().strftime('%Y-%m-%d')

    def get_billing_area(self):
        billing_area = "{}{}{}".format(self.invoice_billing, self.invoice_name, self.invoice_ltd)
        return billing_area
    
    def process_contact(self):
        self.invoice_billing = self.selected_contact['contact_billing']
        self.invoice_name = self.selected_contact['contact_name']
        self.invoice_ltd = self.selected_contact['contact_LTD']
        self.invoice_number = self.selected_contact['invoice_number']
        print(self.get_billing_area())
        print("---------------Contact Processed----------------")
        input()
        
                         
    
    def get_date(self):
        return self.date    
    
    def get_invoice_number(self):
        return self.invoice_number
        
    def __init__(self, selected_contact):
        """Constructor"""
        self.selected_contact = selected_contact
        self.process_contact()
        self.set_date()
        
    