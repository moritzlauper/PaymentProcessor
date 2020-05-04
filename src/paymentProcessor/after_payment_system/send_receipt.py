from loguru import logger
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# sends input from process_receipt to client via email


async def send_receipt(zip_name, model):
    mail_content = f'''Sehr geehrter {model[1][3]}
    \nAm {model[0][3]} um {model[0][4]} wurde die erfolgreiche Bearbeitung der Rechnung {model[0][0]} vom Zahlungssystem «schweizerische-gewerbekasse/zahlsystem» gemeldet.
    \nMit freundlichen Grüssen
    \nMoritz Lauper
    \n{model[1][2]}
    '''
    # The mail addresses and password
    sender_address = 'lauper.tbz@mail.ch'
    sender_pass = 'TbzTbz123'
    receiver_address = 'harald.mueller@tbz.ch'
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Erfolgte Verarbeitung Rechnung 21003'
    # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    payload = MIMEBase('application', 'octet-stream')
    payload.set_payload(open(zip_name, 'rb').read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment',
                   filename=zip_name)
    message.attach(payload)

    try:
        session = smtplib.SMTP('smtp.mail.ch', 587)
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        logger.info('Mail was sent to client.')
        session.quit()
    except:
        logger.info('Mail could not be sent.')