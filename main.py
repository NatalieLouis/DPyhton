import asyncio
async def work(n):
    await asyncio.sleep(n)
    return f"done {n}"

async def main():
    tasks = [asyncio.create_task(work(i)) for i in [3, 1, 2]]
    done, pending = await asyncio.wait(tasks, timeout=2)

    print("Done:", done)
    print("Pending:", pending)

asyncio.run(main())
