from paymentProcessor.model.invoice_item import InvoiceItem


class InvoiceDetail:

    def __init__(self, model: [[str]]):
        self.invoice_items = []
        for i in range(3, len(model)):
            self.invoice_items.append({'Invoice_Items': InvoiceItem(model[i], model[0:3]).to_dict()})

    def to_dict(self):
        return self.invoice_items
