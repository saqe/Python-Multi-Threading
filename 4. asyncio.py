import aiohttp
import asyncio
from time import perf_counter

start = perf_counter()

async def downloader(id):
    start = perf_counter()
    print(f"Task# {id}")
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbin.org/get") as response:
            await response.json()
            print(f"Task# {id} ended. Time taken {(perf_counter() - start):.2f}")

async def main():
    await asyncio.gather(*[downloader(number) for number in range(0,500)])

asyncio.run(main())
print(f"Total time taken {(perf_counter() - start):.2f}s")