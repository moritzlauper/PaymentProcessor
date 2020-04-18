

class InvoiceSummary:

    def __init__(self, model: [[str]]):
        self.basic_data = {
            'BV.010_Anzahl_der_Rechnungspositionen': len(model) - 2,
            'BV.020_Gesamtbetrag_der_Rechnung_exkl_MwSt_exkl_Ab_Zuschlag':
        }

    def to_dict(self):
        return {
            'I.S.010_Basisdaten' : self.basic_data
        }
