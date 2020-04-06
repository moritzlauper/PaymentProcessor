from src.paymentProcessor.before_payment_system.send_invoice import send_invoice

# in while true awaits await_bill and on returns forms rechnung.csv('s) to invoice.txt & *.xml


async def process_bill(message):
    return await send_invoice(message)
