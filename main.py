import asyncio
async def slow_func():
    await asyncio.sleep(5)
    return "done"

async def main():
    try:
        result = await asyncio.wait_for(slow_func(), timeout=2)
    except asyncio.TimeoutError:
        print("Task timed out!")

asyncio.run(main())
