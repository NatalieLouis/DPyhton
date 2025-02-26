import asyncio


async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay}s")
    return f"{name} result"


async def main():
    results = await asyncio.gather(
        task("Task1", 1),
        task("Task2", 2),
        task("Task3", 3),
        return_exceptions=True
    )
    print(f"Results: {results}")

asyncio.run(main())
