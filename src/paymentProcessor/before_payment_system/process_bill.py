from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from paymentProcessor.model.invoice_header import InvoiceHeader
from paymentProcessor.model.invoice_detail import InvoiceDetail
from paymentProcessor.model.invoice_summary import InvoiceSummary
from paymentProcessor.model.invoice import Invoice


# from rechnung.data('s) to invoice.txt & *.xml

async def process_bill(filename: str, filecontent: [[str]]):
    invoice_header = InvoiceHeader(filecontent)
    invoice_detail = InvoiceDetail(filecontent)
    invoice_summary = InvoiceSummary(filecontent)
    invoice = Invoice(invoice_header.to_dict(), invoice_detail.to_dict(), invoice_summary.to_dict())

    xml_string = parseString(dicttoxml(invoice.to_dict(), custom_root='Invoice', attr_type=False)).toxml()
    xml_string = str('<?xml version="1.0" ?><Invoice doctype="ETS Invoice" version="3.1">'
                     + xml_string.split('<?xml version="1.0" ?><Invoice>', 1)[1])
    xml_string = xml_string.replace('<item>', '').replace('</item>', '')

    print(parseString(xml_string).toprettyxml())


