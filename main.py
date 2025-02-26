import asyncio
import threading


async def async_callback():
    print(f"Async callback executed in {threading.current_thread().name}")


def thread_func(loop):
    print(f"Thread running in: {threading.current_thread().name}")
    loop.call_soon_threadsafe(async_callback)  # 会报错


async def main():
    loop = asyncio.get_running_loop()
    thread = threading.Thread(target=thread_func, args=(loop,))
    thread.start()
    thread.join()

asyncio.run(main())
