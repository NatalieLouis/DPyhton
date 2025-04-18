import asyncio

async def bad_task():
    await asyncio.sleep(1)
    raise ValueError("Boom!")

async def main():
    # 创建了一个任务，但没 await 也没 try-except
    asyncio.create_task(bad_task())
    await asyncio.sleep(2)
    print("Main done")

asyncio.run(main())
