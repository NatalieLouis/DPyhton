import asyncio


async def async_task():
    print("Task started")
    await asyncio.sleep(1)
    print("Task finished")

# 在事件循环未启动时调用 create_task 会抛出错误
task = asyncio.create_task(async_task())  # 会报错

asyncio.run(task)
