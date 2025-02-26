import asyncio
import threading
import time


async def async_task():
    print("Async task started in MainThread")
    await asyncio.sleep(1)
    print("Async task finished in MainThread")
    return "Async Done"


def sync_task_with_async_trigger(loop):
    print(f"Sync task running in {threading.current_thread().name}")
    time.sleep(2)  # 模拟耗时任务
    future = asyncio.run_coroutine_threadsafe(async_task(), loop)
    print(f"Sync task got async result: {future.result()}")


async def main():
    loop = asyncio.get_running_loop()
    thread = threading.Thread(target=sync_task_with_async_trigger, args=(loop,))
    thread.start()
    thread.join()

asyncio.run(main())
