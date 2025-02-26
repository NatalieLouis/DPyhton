import asyncio
import time


def blocking_function(proto):
    print(f"Blocking function started with {proto}")
    time.sleep(2)  # 模拟阻塞操作
    print(f"Blocking function finished with {proto}")


async def main():
    proto = "example_proto"
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking_function, proto)  # 在默认线程池中运行阻塞函数
    await future  # 等待执行器中的任务完成

# 手动创建和关闭事件循环
loop = asyncio.get_running_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
