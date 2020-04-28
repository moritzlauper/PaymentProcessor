import asyncio
from src.paymentProcessor.before_payment_system.bill_routine import BillRoutine
from src.paymentProcessor.after_payment_system.receipt_routine import ReceiptRoutine

bill_routine = BillRoutine()
receipt_routine = ReceiptRoutine()


async def await_bill():
    return await bill_routine.bill_routine()


async def await_receipt(model=''):
    return await receipt_routine.receipt_routine(model)


async def main():
    await asyncio.gather(await_bill(), await_receipt())


#asyncio.run(main())

while True:
    model = asyncio.run(await_bill())
    asyncio.run(await_receipt(model))
