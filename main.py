import asyncio
from concurrent.futures import ThreadPoolExecutor


def blocking_io():
    import time
    time.sleep(2)
    return "Blocking IO result"


async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(blocking_io)
        wrapped_future = asyncio.wrap_future(future)
        result = await wrapped_future
        print(f"Got result: {result}")

asyncio.run(main())
