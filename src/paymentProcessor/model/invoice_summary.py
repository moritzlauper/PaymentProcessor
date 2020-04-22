
class InvoiceSummary:

    def __init__(self, model: dict):
        self.basic_data = {
            'BV.010_Anzahl_der_Rechnungspositionen': model.get('item_count'),
            'BV.020_Gesamtbetrag_der_Rechnung_exkl_MwSt_exkl_Ab_Zuschlag': model.get('total_vat_excluded'),
            'BV.030_Waehrung_Gesamtbetrag_der_Rechnung_exkl_MwSt_exkl_Ab_Zuschlag': 'CHF',
            'BV.040_Gesamtbetrag_der_Rechnung_exkl_MwSt_inkl_Ab_Zuschlag': model.get('total_vat_excluded'),
            'BV.050_Waehrung_Gesamtbetrag_der_Rechnung_exkl_MwSt_inkl_Ab_Zuschlag': 'CHF',
            'BV.060_Steuerbetrag': model.get('total_vat'),
            'BV.070_Waehrung_des_Steuerbetrags': 'CHF',
            'BV.080_Gesamtbetrag_der_Rechnung_inkl_MwSt_inkl_Ab_Zuschlag': model.get('total_vat_included'),
            'BV.090_Waehrung_Gesamtbetrag_der_Rechnung_inkl_MwSt_inkl_Ab_Zuschlag': 'CHF'
        }

        self.taxes = {
            'BV.010_Funktion_der_Steuer': 'Steuer',
            'BV.020_Steuersatz_Kategorie': 'Standard Satz',
            'BV.030_Steuersatz': model.get('percent_vat'),
            'BV.040_Zu_versteuernder_Betrag': model.get('total_vat_excluded'),
            'BV.050_Steuerbetrag': model.get('total_vat'),
            'BV.055_Waehrung_Steuerbetrag': 'CHF'
        }

    def to_dict(self):
        return {
            'I.S.010_Basisdaten' : self.basic_data,
            'I.S.020_Aufschluesselung_der_Steuern': self.taxes
        }
