

class InvoiceSummary:

    def __init__(self, model: [[str]]):
        self.basic_data = {
            'BV.010_Anzahl_der_Rechnungspositionen' : '2'
        }

    def to_dict(self):
        return {
            'I.S.010_Basisdaten' : self.basic_data
        }
