import time
import requests
from concurrent import futures

urls = ["https://wpblog.x0y1.com/?p=34"] * 1000
executor = futures.ThreadPoolExecutor(max_workers=5)
session = requests.Session()

start = time.time()
"""用多线程"""
# fs = []
# for url in urls:
#     f = executor.submit(session.get, url)
#     fs.append(f)
# futures.wait(fs)
# result = [f.result().text for f in fs]
"""不用多线程"""
results = []
for url in urls:
    r = session.get(url)
    results.append(r.text)
print("result", results)
end = time.time()

print(f"花费{end-start}秒")