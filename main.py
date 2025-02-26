import asyncio
import threading
from queue import Queue


async def async_task():
    print(f"Async task started in {threading.current_thread().name}")
    await asyncio.sleep(2)
    print(f"Async task finished in {threading.current_thread().name}")
    return "Async Done in SubThread"


def run_async_in_thread(result_queue):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(async_task())
    result_queue.put(result)  # ✅ 使用线程安全的队列
    loop.close()


async def main():
    result_queue = Queue()
    thread = threading.Thread(target=run_async_in_thread, args=(result_queue,))
    thread.start()

    print("Main thread doing other things...")
    while thread.is_alive():
        await asyncio.sleep(0.5)

    thread.join()
    print(f"Got result from sub-thread: {result_queue.get()}")

asyncio.run(main())
