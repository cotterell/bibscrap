import asyncio


async def foreach(func, iterable):
    for item in iterable:
        func(item)


async def fetcher(name, queue):
    while True:
        url = await queue.get()
        # stuff here
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    tasks = []

    await queue.join()
    await foreach(asyncio.Task.cancel, tasks)
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
