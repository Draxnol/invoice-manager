from datetime import datetime

class Invoice:
    """Class for invoices"""

    def set_date(self):
        self.date = datetime.today().strftime('%Y-%m-%d')  
    def __init__(self,):
        """Constructor"""
        self.set_date()
    def get_date(self):
        return self.date
   