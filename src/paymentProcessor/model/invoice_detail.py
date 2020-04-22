from paymentProcessor.model.invoice_item import InvoiceItem


class InvoiceDetail:

    def __init__(self, model: [[str]]):
        self.invoice_items = []
        self.total_vat_excluded = 0
        self.total_vat_included = 0
        self.total_vat = 0
        self.percent_vat = 0.00
        for i in range(3, len(model)):
            item = InvoiceItem(model[i], model[0:3])
            self.invoice_items.append({'Invoice_Items': item.to_dict()})
            self.total_vat_excluded += float(item.price_and_quantity.get('BV.070_Bestaetigter_Gesamtpreis_der_Position_netto'))
            self.total_vat_included += float(item.price_and_quantity.get(
                'BV.080_Bestaetigter_Gesamtpreis_der_Position_brutto'))
            self.total_vat += float(item.taxes.get('BV.050_Steuerbetrag'))
            self.percent_vat += float(item.taxes.get('BV.030_Steuersatz'))
        self.percent_vat = float(self.percent_vat / len(self.invoice_items))

    def to_dict(self):
        return self.invoice_items

    def calculate_summary(self):
        return {
            'item_count': len(self.invoice_items),
            'total_vat_excluded': self.total_vat_excluded if str(self.total_vat_excluded).split('.')[1] != '0' else str(self.total_vat_excluded).replace('.0', '.00'),
            'total_vat_included': self.total_vat_included if str(self.total_vat_included).split('.')[1] != '0' else str(self.total_vat_included).replace('.0', '.00'),
            'total_vat': self.total_vat,
            'percent_vat': self.percent_vat
        }
