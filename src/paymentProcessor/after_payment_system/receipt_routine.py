import asyncio
from src.paymentProcessor.after_payment_system.process_receipt import process_receipt

# awaits out of payment system


async def await_receipt():
    while True:
        await asyncio.sleep(1)
        return "receipt"


async def receipt_routine():
    while True:
        await asyncio.ensure_future(process_receipt(await asyncio.ensure_future(await_receipt())))
