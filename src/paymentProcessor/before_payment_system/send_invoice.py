import asyncio

# triggered by end of process_bill.py sends to pmt system in via ftp


async def send_invoice(message):
    await asyncio.sleep(1.5)
    return f"{message} was sent to payment system"
