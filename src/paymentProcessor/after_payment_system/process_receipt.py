from src.paymentProcessor.after_payment_system.send_receipt import send_receipt

# in while true awaits await_receipt, collects invoice.txt and calls send_receipt


async def process_receipt(message):
    return await send_receipt(message)