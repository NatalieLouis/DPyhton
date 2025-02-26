import asyncio
import threading
import time


async def main_task():
    print("Main task started")
    await asyncio.sleep(5)
    print("Main task finished")


def stop_loop_soon(loop):
    print("SubThread will stop the loop after 2s.")
    time.sleep(2)
    loop.call_soon_threadsafe(loop.stop)  # ⚡ 安全地从子线程停止事件循环


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    t = threading.Thread(target=stop_loop_soon, args=(loop,))
    t.start()
    try:
        loop.run_forever()  # 🏃 子线程2s后会停止该循环
    finally:
        print("Loop stopped by subthread.")
        loop.close()
        t.join()


main()
