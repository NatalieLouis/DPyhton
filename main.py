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
    time.sleep(2)
    future = asyncio.run_coroutine_threadsafe(async_task(), loop)
    try:
        result = future.result()  # ✅ 子线程阻塞等待，但无主线程阻塞
        queue.put(result)         # ✅ 使用线程安全队列返回结果
    except Exception as e:
        print(f"Exception in thread: {e}")


async def main():
    loop = asyncio.get_running_loop()
    from queue import Queue
    result_queue = Queue()
    thread = threading.Thread(target=sync_task_with_async_trigger, args=(loop, result_queue))
    thread.start()

    # ✅ 主线程异步等待子线程完成而非阻塞
    while thread.is_alive():
        await asyncio.sleep(0.1)

    print(f"Sync task got async result: {result_queue.get()}")
    thread.join()

asyncio.run(main())
