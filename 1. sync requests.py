import requests
from time import perf_counter

start = perf_counter()

def downloader(id):
    start = perf_counter()
    print(f"Task# {id}")
    requests.get("https://httpbin.org/get").json()
    print(f"Task# {id} ended. Time taken {(perf_counter() - start):.2f}s")

for i in range(0, 50):
    downloader(i)

print(f"Total time taken {(perf_counter() - start):.2f}s")