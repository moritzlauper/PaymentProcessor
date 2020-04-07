from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
from bs4 import BeautifulSoup
import xml.etree as etree
from paymentProcessor.model.basic_invoice_data import BasicInvoiceData

# in while true awaits await_bill and on returns forms rechnung.data('s) to invoice.txt & *.xml


'''
def create_xml_tree(filecontent):
    top = Element('Invoice')
    top.set('version', '3.1')
    top.set('doctype', 'ETS Invoice')

    invoice_header = SubElement(top, 'Invoice_Header')
    invoice_header.append(SubElement(invoice_header, 'I.H.010_Basisdaten'))
    invoice_detail = SubElement(top, 'Invoice_Detail')
    invoice_detail.append(SubElement(invoice_detail, 'Invoice_Items'))
    invoice_summary = SubElement(top, 'Invoice_Summary')
    invoice_summary.append(SubElement(invoice_summary, 'I.S.010_Basisdaten'))

    top.append(invoice_header)
    top.append(invoice_detail)
    top.append(invoice_summary)
    #print(BeautifulSoup(etree.ElementTree.tostring(top)).prettify())
'''


async def process_bill(filename: str, filecontent: [[str]]):
    basic_invoice_data = BasicInvoiceData(filecontent[0])
    print(basic_invoice_data.invoice_number)
    print(basic_invoice_data.assignment_number)
    print(basic_invoice_data.location)
    print(basic_invoice_data.date)
    print(basic_invoice_data.time)
    print(basic_invoice_data.paymentduetue)