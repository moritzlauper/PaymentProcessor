from paymentProcessor.model.invoice import Invoice
from xml.dom.minidom import parseString
import ftplib
import asyncio
import os

invoice = Invoice()


# from rechnung.data('s) to invoice.txt & *.xml


async def process_bill(filecontent: [[str]]):
    try:
        session = ftplib.FTP('134.119.225.245', '310721-297-zahlsystem', 'Berufsschule8005!')
        session.cwd('/in/AP17bLauper')
        xml = invoice.to_xml(filecontent)
        txt = invoice.to_txt(filecontent)
        filename = f'{filecontent[1][1]}_{filecontent[0][0]}_invoice'
        with open(f'{filename}.xml', 'w+', encoding='utf-8') as f:
            f.writelines(parseString(xml).toprettyxml())
        with open(f'{filename}.txt', 'w+', encoding='utf-8') as f:
            f.writelines(txt)
        print('Uploading invoice to payment server...')
        print(session.storlines(f'STOR {filename}.txt', open(f'{filename}.txt', 'rb')))
        print(session.storbinary(f'STOR {filename}.xml', open(f'{filename}.xml', 'rb')))
        os.remove(f'{filename}.xml')
        session.quit()
    except Exception:
        raise Exception
    except BaseException:
        raise BaseException
    return
