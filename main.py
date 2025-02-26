import asyncio
import threading


async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine finished")
    return "Done"


def run_coroutine_in_thread(loop, event):
    try:
        coroutine = my_coroutine()
        future = asyncio.run_coroutine_threadsafe(coroutine, loop)
        result = future.result()  # 等待协程完成并获取结果
        print(f"Result: {result}")
    except Exception as e:
        print(f"Exception in thread: {e}")
    finally:
        event.set()  # 通知主线程协程已完成


async def main():
    loop = asyncio.get_running_loop()
    event = threading.Event()  # ✅ 改为线程安全的 threading.Event
    thread = threading.Thread(target=run_coroutine_in_thread, args=(loop, event))
    thread.start()

    # ✅ 在异步任务中等待线程完成
    await asyncio.to_thread(event.wait)  # 异步等待线程事件
    thread.join()  # ✅ 确保线程正确退出


asyncio.run(main())
