import asyncio
import threading


async def worker(name, delay):
    print(f"{name} running in {threading.current_thread().name}")
    await asyncio.sleep(delay)
    print(f"{name} finished")


def thread_event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # 在子线程事件循环中并发运行多个任务
    loop.run_until_complete(asyncio.gather(
        worker("SubTask-1", 1),
        worker("SubTask-2", 2),
    ))
    loop.close()


thread = threading.Thread(target=thread_event_loop)
thread.start()
thread.join()
