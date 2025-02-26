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

    def on_done(fut):
        try:
            print(f"Sync task got async result: {fut.result()}")
        except Exception as e:
            print(f"Exception in callback: {e}")
        finally:
            loop.call_soon_threadsafe(event.set)  # ✅ 通知主线程

    future.add_done_callback(on_done)


async def main():
    loop = asyncio.get_running_loop()
    event = asyncio.Event()
    thread = threading.Thread(target=sync_task_with_async_trigger, args=(loop, event))
    thread.start()
    await event.wait()  # ✅ 等待子线程通知协程完成
    thread.join()

asyncio.run(main())
