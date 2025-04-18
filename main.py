import asyncio

async def slow_func():
    await asyncio.sleep(5)
    return "done"

async def main():
    task = asyncio.create_task(slow_func())  # 创建了 Task 对象

    try:
        result = await asyncio.wait_for(task, timeout=2)  # 等待 Task 的完成
        print("Result:", result)
    except asyncio.TimeoutError:
        print("Task timed out!")
        print("Cancelling task...")
        task.cancel()  # 手动取消任务
        try:
            await task  # 等待取消完成（很重要）
        except asyncio.CancelledError:
            print("Task was cancelled.")

asyncio.run(main())
