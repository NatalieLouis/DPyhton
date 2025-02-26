import asyncio
import threading


async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine finished")
    return "Done"


def run_coroutine_in_thread(loop, event):
    coroutine = my_coroutine()
    future = asyncio.run_coroutine_threadsafe(coroutine, loop)
    result = future.result()  # 等待协程完成并获取结果
    print(f"Result: {result}")
    event.set()  # 通知主线程协程已完成


async def main():
    loop = asyncio.get_running_loop()
    event = asyncio.Event()
    thread = threading.Thread(target=run_coroutine_in_thread, args=(loop, event))
    thread.start()
    await event.wait()  # 等待子线程完成
    thread.join()

asyncio.run(main())
