import threading
import asyncio


async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine finished")
    return "Done"


def thread_event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(my_coroutine())
    print(f"Result in thread loop: {result}")
    loop.close()


thread = threading.Thread(target=thread_event_loop)
thread.start()
thread.join()
