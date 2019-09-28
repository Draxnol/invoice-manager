from datetime import datetime

class Invoice:
    """Class for invoices"""

    def set_date(self):
        self.date = datetime.today().strftime('%Y-%m-%d')  
    def __init__(self, invoice_number):
        """Constructor"""
        self.set_date()
        self.invoice_number = invoice_number
    def get_date(self):
        return self.date
    def get_invoice_number(self):   
        return self.invoice_number