import asyncio
from paymentProcessor.before_payment_system.process_bill import process_bill
from ftplib import FTP


# synchronises client out with local list & can return mutliple 'rechnung.csv'


class BillRoutine:

    def __init__(self, fileobjects=None):
        if fileobjects is None:
            fileobjects = []
        self.fileobjects = fileobjects

    def format(self, file: bytearray):
        for line in list(map(lambda line: line.split(';'), file.decode('utf-8').splitlines())):
            self.fileobjects.append([])
            for element in line:
                self.fileobjects[len(self.fileobjects) - 1]\
                    .append(str(element).split('_', 1)[1] if '_' in element else element)

    async def await_bill(self):
        remote_path = '/out/AP17bLauper/'
        with FTP('ftp.haraldmueller.ch', 'schoolerinvoices', 'Berufsschule8005!') as ftp:
            ftp.cwd(remote_path)
            for file in ftp.nlst('.'):
                if file.endswith('.data'):
                    await asyncio.sleep(1)
                    ftp.retrbinary('RETR ' + file, self.format)
                    await process_bill(file, self.fileobjects)
                    self.fileobjects = []
                    # ftp.delete(file)

    async def bill_routine(self):
        await asyncio.ensure_future(self.await_bill())
