import asyncio
from concurrent.futures import ThreadPoolExecutor
import threading


async def async_task(name, delay):
    print(f"[{threading.current_thread().name}] {name} started")
    await asyncio.sleep(delay)
    print(f"[{threading.current_thread().name}] {name} finished after {delay}s")
    return f"{name} result"


def sync_task(loop, future):
    print(f"[{threading.current_thread().name}] Running sync_task")
    asyncio.run_coroutine_threadsafe(async_task("Thread-Task", 2), loop)\
        .add_done_callback(lambda f: future.set_result(f.result()))


async def main():
    loop = asyncio.get_running_loop()
    future = asyncio.Future()

    # 子线程触发异步任务
    threading.Thread(target=sync_task, args=(loop, future)).start()

    # 同时运行其他任务
    task1 = asyncio.create_task(async_task("Task1", 1))
    task2 = asyncio.ensure_future(async_task("Task2", 3))

    # 等待所有任务完成
    results = await asyncio.gather(task1, task2, future)
    print(f"[{threading.current_thread().name}] All results: {results}")

asyncio.run(main())
