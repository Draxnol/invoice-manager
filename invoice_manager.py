from invoice import Invoice
#Going to need date, invoice number from contact
#Then update invoice count for object

class Invoice_manager:
    def __init__(self, contact_manager):
        self.con_mgr = contact_manager
    def print(self):
        self.con_mgr.display_contact()
    def create_invoice(self):
        self.current_invoice = Invoice()
    def get_invoice_date(self):
        print(self.current_invoice.get_date())