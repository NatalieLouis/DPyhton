import asyncio
import threading


async def task(name):
    print(f"{name} running in thread: {threading.current_thread().name}")
    await asyncio.sleep(1)
    print(f"{name} finished")


async def main():
    await asyncio.gather(task("Task 1"), task("Task 2"))

asyncio.run(main())
