import asyncio
import threading
import time


async def async_task():
    print("Async task started in MainThread")
    await asyncio.sleep(1)
    print("Async task finished in MainThread")
    return "Async Done"


def sync_task_with_async_trigger(loop, event):
    print(f"Sync task running in {threading.current_thread().name}")
    time.sleep(2)
    future = asyncio.run_coroutine_threadsafe(async_task(), loop)
    print(f"Sync task got async result: {future.result()}")
    event.set()  # ✅ 通知主线程


async def main():
    loop = asyncio.get_running_loop()
    event = asyncio.Event()
    thread = threading.Thread(target=sync_task_with_async_trigger, args=(loop, event))
    thread.start()
    await event.wait()  # ✅ 非阻塞等待子线程通知
    thread.join()

asyncio.run(main())
