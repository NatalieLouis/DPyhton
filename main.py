import asyncio
import threading
import time


async def async_task():
    print("Async task started in MainThread")
    await asyncio.sleep(1)
    print("Async task finished in MainThread")
    return "Async Done"


def sync_task_with_async_trigger(loop, queue):
    print(f"Sync task running in {threading.current_thread().name}")
    future = asyncio.run_coroutine_threadsafe(async_task(), loop)
    try:
        result = future.result()  # ✅ 子线程等待异步任务完成
        queue.put(result)
    except Exception as e:
        print(f"Exception in thread: {e}")


async def main():
    loop = asyncio.get_running_loop()
    from queue import Queue
    result_queue = Queue()
    thread = threading.Thread(target=sync_task_with_async_trigger, args=(loop, result_queue))
    thread.start()

    time.sleep(10)

    print(f"Sync task got async result: {result_queue.get()}")
    thread.join()

asyncio.run(main())
