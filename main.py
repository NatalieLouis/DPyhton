import asyncio
async def heartbeat():
    while True:
        print("ping")
        await asyncio.sleep(5)

async def business():
    for i in range(3):
        print("doing business...")
        await asyncio.sleep(2)

async def main():
    asyncio.create_task(heartbeat())
    await business()

asyncio.run(main())
