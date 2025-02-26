import asyncio
import threading


async def async_task():
    print("Async task started in MainThread")
    await asyncio.sleep(1)
    print("Async task finished in MainThread")
    return "Async Done"


def sync_task_with_async_trigger(loop, event, result_container):
    print(f"Sync task running in {threading.current_thread().name}")
    future = asyncio.run_coroutine_threadsafe(async_task(), loop)
    try:
        result = future.result()
        result_container.append(result)
    finally:
        loop.call_soon_threadsafe(event.set)  # ✅ 通知主线程事件已完成


async def main():
    loop = asyncio.get_running_loop()
    event = asyncio.Event()
    result_container = []

    thread = threading.Thread(target=sync_task_with_async_trigger, args=(loop, event, result_container))
    thread.start()

    await event.wait()  # ✅ 主线程异步等待子线程通知
    thread.join()
    print(f"Sync task got async result: {result_container[0]}")

asyncio.run(main())
