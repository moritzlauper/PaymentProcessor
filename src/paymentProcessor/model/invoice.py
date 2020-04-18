from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

from paymentProcessor.model.invoice_detail import InvoiceDetail
from paymentProcessor.model.invoice_header import InvoiceHeader
from paymentProcessor.model.invoice_summary import InvoiceSummary


def to_dict(filecontent):
    return {
        'Invoice_Header': InvoiceHeader(filecontent).to_dict(),
        'Invoice_Detail': InvoiceDetail(filecontent).to_dict(),
        'Invoice_Summary': InvoiceSummary(filecontent).to_dict()
    }


def to_xml(filecontent):
    xml_string = parseString(dicttoxml(to_dict(filecontent), custom_root='Invoice', attr_type=False)).toxml()
    xml_string = str('<?xml version="1.0" ?><Invoice doctype="ETS Invoice" version="3.1">'
                     + xml_string.split('<?xml version="1.0" ?><Invoice>', 1)[1])
    return xml_string.replace('<item>', '').replace('</item>', '')