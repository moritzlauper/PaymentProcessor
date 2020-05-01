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

    async def await_bill(self, ftp):
        for file in ftp.nlst('.'):
            if file.endswith('.data'):
                try:
                    ftp.retrbinary('RETR ' + file, self.format)
                    await process_bill(self.fileobjects)
                    return False
                except:
                    self.fileobjects = []
                    print('The file has the wrong format.')
                    return True
                finally:
                    ftp.delete(file)
        return True

    async def bill_routine(self):
        print('---scanning client out---')
        remote_path = '/out/AP17bLauper/'
        try:
            ftp = FTP('ftp.haraldmueller.ch', 'schoolerinvoices', 'Berufsschule8005!')
            ftp.cwd(remote_path)
            in_progress = True
            while in_progress:
                in_progress = await asyncio.ensure_future(self.await_bill(ftp))
                await asyncio.sleep(60)
            model = self.fileobjects
            self.fileobjects = []
            ftp.close()
            return model
        except:
            print('Could not establish ftp connection')
