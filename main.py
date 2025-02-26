import asyncio
import threading


async def async_task():
    await asyncio.sleep(1)
    return "Result from async_task"


def thread_func(loop, future):
    print(f"Thread running in: {threading.current_thread().name}")
    asyncio.run_coroutine_threadsafe(async_task(), loop).add_done_callback(
        lambda f: future.set_result(f.result())
    )


async def main():
    loop = asyncio.get_running_loop()
    future = asyncio.Future()
    thread = threading.Thread(target=thread_func, args=(loop, future))
    thread.start()
    result = await future  # ✅ 异步等待线程中任务结果
    print(f"Got result: {result}")
    thread.join()

asyncio.run(main())
