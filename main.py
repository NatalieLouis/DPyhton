import asyncio
async def slow_op():
    await asyncio.sleep(3)
    return "done"
    
async def do_work(n):
    await asyncio.sleep(n)
    return f"done: {n}"

async def main():
    # 虽然传的是协程对象，但 gather 会帮你转成 Task 并执行
    result = await asyncio.gather(slow_op(), slow_op())
    print(result)

async def do_work(n):
    await asyncio.sleep(n)
    return f"done: {n}"

async def main2():
    tasks = [asyncio.create_task(do_work(i)) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
