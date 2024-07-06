from flask import Flask, request
import os
import time

app = Flask(__name__)
request_count = {}
THRESHOLD = 100  # Eşik değer
BLOCK_TIME = 60  # IP'nin bloklandığı süre (saniye)
blocked_ips = {}

def add_blackhole_route(ip):
    command = f"ip route add blackhole {ip}"
    os.system(command)
    print(f"Black hole route added for {ip}")

def remove_blackhole_route(ip):
    command = f"ip route del blackhole {ip}"
    os.system(command)
    print(f"Black hole route removed for {ip}")

@app.route('/')
def home():
    ip = request.remote_addr
    current_time = time.time()

    # Bloklu IP'leri kontrol et
    if ip in blocked_ips:
        if current_time - blocked_ips[ip] < BLOCK_TIME:
            return "Your IP is blocked due to suspected DDoS attack.", 403
        else:
            del blocked_ips[ip]
            remove_blackhole_route(ip)

    # İstek sayısını güncelle
    if ip in request_count:
        request_count[ip]['count'] += 1
        request_count[ip]['last_time'] = current_time

        # Eşik değeri kontrol et
        if request_count[ip]['count'] > THRESHOLD:
            blocked_ips[ip] = current_time
            add_blackhole_route(ip)
            return "Your IP is blocked due to suspected DDoS attack.", 403
    else:
        request_count[ip] = {'count': 1, 'last_time': current_time}

    # Eski kayıtları temizle
    for ip in list(request_count.keys()):
        if current_time - request_count[ip]['last_time'] > BLOCK_TIME:
            del request_count[ip]

    return "Welcome to the Flask web application!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
