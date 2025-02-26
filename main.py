import asyncio
import threading
import time


async def notify_async(msg):
    print(f"Notification: {msg} in {threading.current_thread().name}")


def blocking_io_task(loop):
    print("Starting blocking I/O in Thread")
    time.sleep(3)  # 模拟阻塞 I/O
    print("Blocking I/O done")
    # 调用异步通知
    asyncio.run_coroutine_threadsafe(notify_async("I/O Completed"), loop)


async def main():
    loop = asyncio.get_running_loop()
    t = threading.Thread(target=blocking_io_task, args=(loop,))
    t.start()
    t.join()

asyncio.run(main())
