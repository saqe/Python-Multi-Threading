import multitasking
import requests
import time

multitasking.set_max_threads(10)

start = time.time()

@multitasking.task
def downloader(id):
    start = time.time()
    print(f"Task# {id}")
    requests.get("https://httpbin.org/get").json()
    print(f"Task# {id} ended. Time taken {time.time() - start}")

for i in range(0, 50):
    downloader(i)

multitasking.wait_for_tasks()
print(f"Total time taken: {time.time() - start} seconds")