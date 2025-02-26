import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def blocking_function(proto):
    print(f"Blocking function started with {proto}")
    time.sleep(2)  # 模拟阻塞操作
    


async def main():
    proto = "example_proto"
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as executor:
        await loop.run_in_executor(executor, blocking_function, proto)  # 在默认线程池中运行阻塞函数

asyncio.run(main())
