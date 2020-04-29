from ftplib import FTP
from zipfile import ZipFile
import os

from src.paymentProcessor.after_payment_system.send_receipt import send_receipt


# in while true awaits await_receipt, collects invoice.txt and calls send_receipt

class ProcessReceipt:

    async def process(self, receipt, model):
        invoice_filename = str(open(receipt).readline()).split(' ')[2].split('.')[0]
        zipObj = ZipFile(invoice_filename + '.zip', 'w')
        zipObj.write(invoice_filename + '.txt')
        zipObj.write(receipt)
        zipObj.close()
        remote_path = '/in/AP17bLauper/'
        with FTP('ftp.haraldmueller.ch', 'schoolerinvoices', 'Berufsschule8005!') as ftp:
            ftp.cwd(remote_path)
            print('Uploading Zip to client ftp server in...')
            print(ftp.storbinary(f'STOR {zipObj.filename}', open(f'{zipObj.filename}', 'rb')))
        await send_receipt(zipObj.filename, model)
        os.remove(invoice_filename + '.txt')
        os.remove(invoice_filename + '.zip')
        os.remove(receipt)
