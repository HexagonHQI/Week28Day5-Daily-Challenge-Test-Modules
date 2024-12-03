import requests
import time

def get_load_time(url):
    start = time.time()
    try:
        requests.get(url)
        return time.time() - start
    except:
        return "Error"

# Fuction test
for url in ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]:
    print(f"{url}: {get_load_time(url):.4f} seconds")
