from datetime import datetime
from datetime import timedelta


def print_date(date):
    result = ''
    for element in date:
        result += str(element)
    return result


def date_time(date, time):
    return str(print_date(list(reversed(date.split('.')))) + time.replace(':', ''))


def calculate_payment_date(date, time, due_tue_time):
    due_tue_date = datetime.strptime(str(date), '%d.%m.%Y') + timedelta(days=int(due_tue_time))
    return date_time(due_tue_date.strftime('%d.%m.%Y'), time)


class InvoiceHeader:

    def __init__(self, model: [[str]]):
        # I.H.010_Basisdaten
        self.basic_data = {
            'BV.010_Rechnungsnummer': model[0][0],
            'BV.020_Rechnungsdatum': date_time(model[0][3], model[0][4]),
            'BV.030_Funktion_des_Dokuments': 'Original',
            'BV.040_Typ_des_Dokuments': 'Rechnung',
            'BV.050_Rechnungs_Endkennzeichen': 'vollstaendige Rechnung',
            'BV.060_Bestellnummer_des_Kaeufers': model[1][1],  # e.g 1310 - Stefan Holdener or empty
            'BV.080_Waehrung': 'CHF',
            'BV.090_Sprache': 'de'
        }

        # I.H.020_Einkaeufer_Identifikation
        self.client_identification = {
            'BV.010_Nr_Kaeufer_beim_Lieferanten': 'undef',
            'BV.020_Nr_Kaeufer_beim_Kaeufer': '',  # -> ?
            'BV.030_Nr_Kaeufer_bei_ETS': model[2][1],
            'BV.035_Typ_der_Handelsplatz_ID': 'TPID',
            'BV.040_Name1': model[2][2],
            'BV.100_PLZ': str(model[2][4]).split(' ')[0],
            'BV.110_Stadt': str(model[2][4]).split(' ')[1],
            'BV.120_Land': 'CH'
        }

        # I.H.030_Lieferanten_Identifikation
        self.supplier_identification = {
            'BV.010_Nr_Lieferant_beim_Kaeufer': model[1][2],
            'BV.030_Nr_Lieferant_bei_ETS': 'moritz.lauper@edu.tbz.ch', #-> ?
            'BV.040_Name1': model[1][3],
            'BV.070_Strasse': model[1][4],
            'BV.100_PLZ': str(model[1][5]).split(' ')[0],
            'BV.110_Stadt': str(model[1][5]).split(' ')[1],
            'BV.120_Land': 'CH'
        }

        #I.H.040_Rechnungsadresse
        self.bill_address = {
            'BV.040_Name1': model[2][2],
            'BV.100_PLZ': str(model[2][4]).split(' ')[0],
            'BV.110_Stadt': str(model[2][4]).split(' ')[1],
            'BV.120_Land': 'CH'
        }

        #I.H.080_Zahlungsbedingungen
        self.terms_of_payment = {
            'BV.010_Zahlungsbedingungen': 'Faelligkeitsdatum',
            'BV.020_Zahlungsbedingungen_Zusatzwert': calculate_payment_date(model[0][3], model[0][4], model[0][5])
        }

        #I.H.140_MwSt._Informationen
        self.vat_info = {
            'BV.010_Eingetragener_Name_des_Lieferanten': model[1][3],
            'BV.020_MwSt_Nummer_des_Lieferanten': model[1][6]
        }

    def to_dict(self):
        return {
            'I.H.010_Basisdaten': self.basic_data,
            'I.H.020_Einkaeufer_Identifikation': self.client_identification,
            'I.H.030_Lieferanten_Identifikation': self.supplier_identification,
            'I.H.040_Rechnungsadresse': self.bill_address,
            'I.H.080_Zahlungsbedingungen': self.terms_of_payment,
            'I.H.140_MwSt._Informationen': self.vat_info
        }