import asyncio
import threading


async def coro(name, delay):
    print(f"{name} running in: {threading.current_thread().name}")
    await asyncio.sleep(delay)
    print(f"{name} finished")


def thread_worker():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coro("Thread Coroutine", 2))
    loop.close()


async def main():
    thread = threading.Thread(target=thread_worker)
    thread.start()

    # 主线程的事件循环同时运行另一个协程
    await coro("Main Coroutine", 1)
    thread.join()

asyncio.run(main())
