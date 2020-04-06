import asyncio

# sends input from process_receipt to client via email in rechnung.csv and via ftp to client in


async def send_receipt(message):
    await asyncio.sleep(1.5)
    return f"{message} was sent to client"