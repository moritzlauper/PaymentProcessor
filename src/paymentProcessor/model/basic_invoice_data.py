

class BasicInvoiceData:

    def __init__(self, model: [str]):
        self.invoice_number = model[0]
        self.assignment_number = model[1]
        self.location = model[2]
        self.date = model[3]
        self.time = model[4]
        self.paymentduetue = model[5]