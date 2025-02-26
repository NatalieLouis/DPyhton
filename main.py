import asyncio
import time


def blocking_function(proto):
    print(f"Blocking function started with {proto}")
    time.sleep(2)  # 模拟阻塞操作
    print(f"Blocking function finished with {proto}")


async def main():
    proto = "example_proto"
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, blocking_function, proto)  # 在默认线程池中运行阻塞函数

asyncio.run(main())
