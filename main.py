import asyncio
import threading


async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine finished")
    return "Done"


def run_coroutine_in_thread(loop, event):
    asyncio.set_event_loop(loop)
    loop.run_forever()
    event.set()  # 通知主线程协程已完成


async def main():
    loop = asyncio.new_event_loop()
    event = threading.Event()
    thread = threading.Thread(target=run_coroutine_in_thread, args=(loop, event))
    thread.start()

    # 确保事件循环已经启动
    while not loop.is_running():
        await asyncio.sleep(0.1)

    coroutine = my_coroutine()
    future = asyncio.run_coroutine_threadsafe(coroutine, loop)
    result = future.result()  # 等待协程完成并获取结果
    print(f"Result: {result}")

    loop.call_soon_threadsafe(loop.stop)
    thread.join()
    loop.close()

asyncio.run(main())
