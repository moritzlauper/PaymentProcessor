import asyncio
from src.paymentProcessor.before_payment_system.bill_routine import bill_routine
from src.paymentProcessor.after_payment_system.receipt_routine import receipt_routine


async def await_bill():
    return await bill_routine()


async def await_receipt():
    return await receipt_routine()


async def main():
    await asyncio.gather(await_bill(), await_receipt())


asyncio.run(main())
