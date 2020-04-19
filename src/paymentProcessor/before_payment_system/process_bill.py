from paymentProcessor.model import invoice
from xml.dom.minidom import parseString

# from rechnung.data('s) to invoice.txt & *.xml


async def process_bill(filename: str, filecontent: [[str]]):
    xml_string = invoice.to_xml(filecontent)
    print(parseString(xml_string).toprettyxml())


