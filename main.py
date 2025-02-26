import asyncio
import time


def blocking_function(proto):
    print(f"Blocking function started with {proto}")
    time.sleep(2)  # 模拟阻塞操作
    print(f"Blocking function finished with {proto}")
    return "Done"


async def main():
    proto = "example_proto"
    result = await asyncio.to_thread(blocking_function, proto)
    print(f"Result: {result}")

asyncio.run(main())
