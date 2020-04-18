

class Invoice:

    def __init__(self, invoice_header: {}, invoice_detail, invoice_summary):
        self.invoice_header = invoice_header
        self.invoice_detail = invoice_detail
        self.invoice_summary = invoice_summary

    def to_dict(self):
        return {
            'Invoice_Header': self.invoice_header,
            'Invoice_Detail': self.invoice_detail,
            'Invoice_Summary': self.invoice_summary
        }