from paymentProcessor.model.invoice_header import date_time


class InvoiceItem:

    def __init__(self, model_of_current: [str], model: [[str]]):
        self.basic_data = {
            'BV.010_Positions_Nr_in_der_Rechnung': model_of_current[1],
            'BV.020_Artikel_Nr_des_Lieferanten': '',    # -> ? e.g 569503/0589
            'BV.030_Artikel_Nr_des_Lieferanten_Erweiterung': model_of_current[1],
            #'BV.040_Referenz_zur_Bestellung_Bestell_Nr_des_Kaeufers': '', braucht es die?
            'BV.070_Artikel_Beschreibung': 'Beschreibung...',    # -> ?
            'BV.140_Abschlussdatum_der_Lieferung_Ausfuehrung': date_time(model[0][3], model[0][4])
        }

        self.price_and_quantity = {
            'BV.010_Verrechnete_Menge': model_of_current[3],
            'BV.020_Mengeneinheit_der_verrechneten_Menge': 'BLL',
            'BV.030_Verrechneter_Einzelpreis_des_Artikels': model_of_current[4],
            'BV.040_Waehrung_des_Einzelpreises': 'CHF',
            'BV.070_Bestaetigter_Gesamtpreis_der_Position_netto': model_of_current[5],
            'BV.080_Bestaetigter_Gesamtpreis_der_Position_brutto': float(model_of_current[5]) + (float(model_of_current[5]) * float(str(model_of_current[6]).split('%')[0]) / 100),
            'BV.090_Waehrung_des_Gesamtpreises': 'CHF'
        }

        self.taxes = {
            'BV.010_Funktion_der_Steuer': 'Steuer',
            'BV.020_Steuersatz_Kategorie': 'Standard Satz',
            'BV.030_Steuersatz': str(model_of_current[6]).split('%')[0],
            'BV.040_Zu_versteuernder_Betrag': model_of_current[5],
            'BV.050_Steuerbetrag': (float(model_of_current[5]) * float(str(model_of_current[6]).split('%')[0]) / 100)
        }

    def to_dict(self):
        return {
            'I.D.010_Basisdaten': self.basic_data,
            'I.D.020_Preise_und_Mengen': self.price_and_quantity,
            'I.D.030_Steuern': self.taxes
        }