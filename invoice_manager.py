from invoice import Invoice
#Going to need date, invoice number from contact
#Then update invoice count for object

class Invoice_manager:
    def __init__(self):
        self.con_mgr = None
    def print(self):
        self.con_mgr.display_contact()
    def create_invoice(self):
        self.current_invoice = Invoice(self.selected_contact)
    def get_invoice_date(self):
        print(self.current_invoice.get_date())
    def select_contact(self, contact):
        self.selected_contact = contact
    def get_selected_contact(self):
        return self.selected_contact
    def get_current_invoice(self):
        return self.current_invoice
        