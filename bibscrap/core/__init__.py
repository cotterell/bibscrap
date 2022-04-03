"""Defines the base APIs for Bibscrap, including its base models, collections, and events."""

import asyncio


class Bibscrap:
    """TODO."""

    def __init__(self) -> None:
        self.queue = asyncio.Queue()
        self.tasks = []

    @classmethod
    async def create(cls):
        self = Bibscrap()
        return self

    async def __worker(self, name):
        while True:
            task = await self.queue.get()
            await self.__worker_done()

    async def __worker_done(self):
        self.queue.task_done()

    async def stop(self):
        for task in self.tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
