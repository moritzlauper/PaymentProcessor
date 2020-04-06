import asyncio
from src.paymentProcessor.after_payment_system.process_bill import process_bill

# synchronises client out with local list & can return mutliple "rechnung.csv"


async def await_bill():
    while True:
        await asyncio.sleep(1)
        return "bill"


async def bill_routine():
    while True:
        print(await asyncio.ensure_future(process_bill(await asyncio.ensure_future(await_bill()))))
