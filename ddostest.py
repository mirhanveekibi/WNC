import threading
import requests

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def stress_test(url, num_requests):
    threads = []
    for i in range(num_requests):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

target_url = "http://javav12.pythonanywhere.com/"
number_of_requests = 10000

stress_test(target_url, number_of_requests)