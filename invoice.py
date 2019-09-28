from datetime import datetime

class Invoice:
    """Class for invoices"""
    def set_date(self):
        self.date = datetime.today().strftime('%Y-%m-%d')  
        self.set_date()
    def process_contact(self):
        self.invoice_billing = self.selected_contact['contact_billing']
        self.invoice_name = self.selected_contact['name']
        self.invoice_ltd = self.selected_contact['contact_LTD']
    def billing_area(self):
        billing_area = "{}{}{}".format(self.invoice_billing, self.invoice_name, self.invoice_ltd)
        return billing_area
    def get_date(self):
        return self.date
    def get_invoice_number(self):   
        pass
    def __init__(self, selected_contact):
        """Constructor"""
        self.selected_contact = selected_contact
        self.process_contact()