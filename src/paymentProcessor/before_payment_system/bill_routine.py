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
        try:
            with FTP('ftp.haraldmueller.ch', 'schoolerinvoices', 'Berufsschule8005!') as ftp:
                ftp.cwd(remote_path)
                for file in ftp.nlst('.'):
                    if file.endswith('.data'):
                        try:
                            ftp.retrbinary('RETR ' + file, self.format)
                            await process_bill(self.fileobjects)
                            ftp.delete(file)
                            return False
                        except:
                            print('The file has the wrong format.')
        except:
            print('Could not establish ftp connection')
        return True

    async def bill_routine(self):
        print('---scanning client out---')
        in_progress = True
        while in_progress:
            in_progress = await asyncio.ensure_future(self.await_bill())
            await asyncio.sleep(60)
        model = self.fileobjects
        self.fileobjects = []
        return model
