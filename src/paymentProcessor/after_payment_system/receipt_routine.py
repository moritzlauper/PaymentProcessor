import asyncio
from ftplib import FTP
import os

from src.paymentProcessor.after_payment_system.process_receipt import ProcessReceipt

process_receipt = ProcessReceipt()


# awaits out of payment system


class ReceiptRoutine:

    async def await_receipt(self, model, ftp):
        for file in ftp.nlst('.'):
            if file.startswith('quittungsfile'):
                await asyncio.sleep(1)
                with open(file, 'wb') as fp:
                    ftp.retrbinary('RETR ' + file, fp.write)
                await process_receipt.process(file, model)
                ftp.delete(file)
                return False
        return True

    async def receipt_routine(self, model):
        print('---scanning payment service out---')
        remote_path = '/out/AP17bLauper/'
        try:
            ftp = FTP('134.119.225.245', '310721-297-zahlsystem', 'Berufsschule8005!')
            ftp.cwd(remote_path)
            in_progress = True
            while in_progress:
                in_progress = await asyncio.ensure_future(self.await_receipt(model, ftp))
                await asyncio.sleep(60)
            ftp.close()
        except Exception as e:
            print(e)
