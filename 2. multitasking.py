import multitasking
import requests
from time import perf_counter

multitasking.set_max_threads(10)

start = perf_counter()

@multitasking.task
def downloader(id):
    start = perf_counter()
    print(f"Task# {id}")
    requests.get("https://httpbin.org/get").json()
    print(f"Task# {id} ended. Time taken {(perf_counter() - start):.2f}s")

for i in range(0, 50):
    downloader(i)

multitasking.wait_for_tasks()
print(f"Total time taken {(perf_counter() - start):.2f}s")