import asyncio


async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine finished")
    return "Done"

loop = asyncio.get_event_loop()
result = loop.run_until_complete(my_coroutine())
print(f"Result: {result}")
