import asyncio
import threading


async def async_task():
    print(f"Async task started in {threading.current_thread().name}")
    await asyncio.sleep(2)
    print(f"Async task finished in {threading.current_thread().name}")
    return "Async Done in SubThread"


def run_async_in_thread(result_holder, lock):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(async_task())
    with lock:  # ✅ 加锁，确保写入是线程安全的
        result_holder.append(result)
    loop.close()


async def main():
    result_holder = []
    lock = threading.Lock()
    thread = threading.Thread(target=run_async_in_thread, args=(result_holder, lock))
    thread.start()

    print("Main thread doing other things...")
    while thread.is_alive():
        await asyncio.sleep(0.5)

    thread.join()
    with lock:
        print(f"Got result from sub-thread: {result_holder[0]}")

asyncio.run(main())
