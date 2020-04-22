from paymentProcessor.model import invoice
from xml.dom.minidom import parseString

# from rechnung.data('s) to invoice.txt & *.xml


async def process_bill(filename: str, filecontent: [[str]]):
    with open('K123_21003_invoice.xml', 'w+', encoding='utf-8') as f:
        f.writelines(parseString(invoice.to_xml(filecontent)).toprettyxml())
    with open('K123_21003_invoice.txt', 'w+', encoding='utf-8') as f:
        f.writelines(invoice.to_txt(filecontent))
