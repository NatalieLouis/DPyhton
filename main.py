import asyncio
import threading
import time


async def my_task(loop):
    print("Task started")
    await asyncio.sleep(1)
    print("Task finished")
    loop.stop()  # 🛑 显式停止事件循环


def thread_func():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.ensure_future(my_task(loop))  # ⚡ 提交任务
    loop.run_forever()  # 💡 如果不调用 loop.stop()，线程将一直阻塞在这里
    print("Event loop in thread stopped.")


t = threading.Thread(target=thread_func)
t.start()
t.join()
print("Thread exited.")
