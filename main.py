import asyncio
import threading


async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine finished")
    return "Done"


def run_coroutine_in_thread(loop, event):
    asyncio.set_event_loop(loop)
    coroutine = my_coroutine()
    future = asyncio.run_coroutine_threadsafe(coroutine, loop)
    result = future.result()  # 等待协程完成并获取结果
    print(f"Result: {result}")
    event.set()  # 通知主线程协程已完成


async def main():
    loop = asyncio.new_event_loop()
    event = threading.Event()
    thread = threading.Thread(target=run_coroutine_in_thread, args=(loop, event))
    thread.start()
    event.wait()  # 等待子线程完成
    thread.join()
    loop.close()

asyncio.run(main())
