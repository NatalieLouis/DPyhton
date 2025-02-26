import asyncio
import threading


async def my_coroutine():
    print(f"Coroutine running in: {threading.current_thread().name}")
    await asyncio.sleep(1)
    print("Coroutine finished")
    return "Done"


def run_in_thread(loop, event):
    asyncio.set_event_loop(loop)
    loop.run_forever()
    event.set()  # 通知主线程事件循环已停止


async def main():
    loop = asyncio.new_event_loop()
    event = threading.Event()
    thread = threading.Thread(target=run_in_thread, args=(loop, event))
    thread.start()

    # 确保事件循环已经启动
    # while not loop.is_running():
    #     await asyncio.sleep(0.1)

    future = asyncio.run_coroutine_threadsafe(my_coroutine(), loop)  # 跨线程投递协程
    result = future.result()  # 等待协程完成并获取结果
    print(f"Result: {result}")

    loop.call_soon_threadsafe(loop.stop)
    event.wait()  # 等待子线程通知事件循环已停止
    thread.join()  # 确保子线程已经完成
    loop.close()

asyncio.run(main())
