import concurrent.futures
import requests
from time import perf_counter

start = perf_counter()

def downloader(id):
    start = perf_counter()
    print(f"Task# {id}")
    requests.get("https://httpbin.org/get").json()
    print(f"Task# {id} ended. Time taken {(perf_counter() - start):.2f}")

with concurrent.futures.ThreadPoolExecutor(10) as executor:
    res = [executor.submit(downloader, i) for i in range(0, 50)]
    concurrent.futures.wait(res)

print(f"Total time taken {(perf_counter() - start):.2f}s")