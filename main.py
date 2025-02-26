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
    time.sleep(2)
    future = asyncio.run_coroutine_threadsafe(async_task(), loop)

    def on_done(fut):
        print(f"Sync task got async result: {fut.result()}")

    future.add_done_callback(on_done)  # ✅ 不阻塞主线程


async def main():
    loop = asyncio.get_running_loop()
    thread = threading.Thread(target=sync_task_with_async_trigger, args=(loop,))
    thread.start()
    await asyncio.sleep(10)  # ✅ 等待 async_task 完成，时间不够长会导致 async_task 未完成报CancelledError
    thread.join()

asyncio.run(main())
