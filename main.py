import asyncio
import threading


def sync_task(msg):
    print(f"[{threading.current_thread().name}] {msg}")


def run_in_thread(loop):
    print(f"[{threading.current_thread().name}] Thread started")
    loop.call_soon_threadsafe(sync_task, "Hello from thread!")


async def main():
    loop = asyncio.get_running_loop()
    thread = threading.Thread(target=run_in_thread, args=(loop,))
    thread.start()
    thread.join()

asyncio.run(main())
