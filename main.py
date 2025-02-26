import asyncio
import threading


async def my_coroutine():
    print(f"Coroutine running in: {threading.current_thread().name}")
    await asyncio.sleep(1)
    print("Coroutine finished")
    return "Done"


def thread_event_loop():
    # 🏗️ 创建并绑定子线程的事件循环
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(my_coroutine())
    print(f"Result in thread loop: {result}")
    loop.close()  # ✅ 关闭循环以释放资源


thread = threading.Thread(target=thread_event_loop)
thread.start()
thread.join()
