import aiohttp
import asyncio
import pprint
import time

from bs4 import BeautifulSoup


async def worker(name, queue, fetched):
    while True:
        # Get a "work item" out of the queue.
        url = await queue.get()
        #
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print("URL:", url, "Status:", response.status)
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                print(soup.title.string)
                fetched.append(url)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()


"""
fetch("https://dl.acm.org/action/exportCiteProcCitation", {
  "headers": {
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
  },
  "body": "dois=10.1145%2F3372782.3408120&targetFile=custom-acm&format=text",
  "method": "POST",
"""


async def crossref_simple_text_query(text):
    """TODO.

    See Also:
        https://apps.crossref.org/SimpleTextQuery
    """


async def fetch_crossref(doi):
    """ """
    # https://api.crossref.org/works/10.1145/3372782.3408120
    # https://api.crossref.org/works/{doi}
    pass


async def fetch_openlibrary(isbn):
    endpoint = f"https://openlibrary.org/isbn/{isbn}.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(endpoint) as response:
            print("URL:", endpoint, "Status:", response.status)
            print(await response.json())


async def fetch_acm(doi):
    endpoint = "https://dl.acm.org/action/exportCiteProcCitation"
    headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
    data = {
        "dois": doi,
        "targetFile": "custom-acm",
        "format": "text",
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(endpoint, data=data, headers=headers) as response:
            print("URL:", endpoint, "Status:", response.status)
            print(await response.json())


async def main():
    """TODO."""
    queue = asyncio.Queue()
    fetched = []
    tasks = []

    await queue.put("https://dl.acm.org/doi/10.1145/3372782.3408120")
    await fetch_acm("10.1145/3372782.3408120")
    await fetch_openlibrary("9780313379307")

    return

    for i in range(3):
        task = asyncio.create_task(worker(f"worker-{i}", queue, fetched))
        tasks.append(task)

    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)
    print("====")
    print(f"workers time in parallel for {total_slept_for:.2f} seconds")
    print("====")
    print("fetched =")
    for url in fetched:
        print(url)


if __name__ == "__main__":
    asyncio.run(main())
