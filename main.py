import asyncio
import threading


async def async_task():
    print(f"Async task executed in {threading.current_thread().name}")
    await asyncio.sleep(1)
    print("Async task finished")


def sync_callback(loop):
    # 通过调用同步函数来启动异步任务
    asyncio.ensure_future(async_task())


def thread_func(loop):
    print(f"Thread running in: {threading.current_thread().name}")
    loop.call_soon_threadsafe(sync_callback, loop)


async def main():
    loop = asyncio.get_running_loop()
    thread = threading.Thread(target=thread_func, args=(loop,))
    thread.start()
    thread.join()

asyncio.run(main())
