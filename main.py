import asyncio
import threading


async def my_coro():
    print(f"Running in thread: {threading.current_thread().name}")
    await asyncio.sleep(1)
    print("Finished coroutine")


def thread_worker(loop):
    asyncio.set_event_loop(loop)  # 在子线程中绑定事件循环
    print(f"Loop set in thread: {threading.current_thread().name}")
    loop.run_until_complete(my_coro())


# 主线程中创建事件循环
loop = asyncio.new_event_loop()
print(f"Loop created in thread: {threading.current_thread().name}")

# 启动子线程并传递事件循环
thread = threading.Thread(target=thread_worker, args=(loop,))
thread.start()
thread.join()

# 检查主线程中的默认事件循环
try:
    asyncio.get_event_loop()
except RuntimeError as e:
    print(f"MainThread get_event_loop error: {e}")
