import requests
import time

start = time.time()

def downloader(id):
    start = time.time()
    print(f"Task# {id}")
    requests.get("https://httpbin.org/get").json()
    print(f"Task# {id} ended. Time taken {time.time() - start}")

for i in range(0, 50):
    downloader(i)

print(f"Total time taken {time.time() - start}")