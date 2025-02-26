import asyncio


async def async_task(future):
    await asyncio.sleep(1)
    future.set_result("Task Completed!")


async def main():
    future = asyncio.Future()
    asyncio.create_task(async_task(future))
    result = await future  # ✅ 异步等待结果
    print(f"Future result: {result}")

asyncio.run(main())
