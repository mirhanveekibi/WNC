from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import time
from collections import defaultdict, deque

app = Flask(__name__)

# Örnek veri seti
data = {
    'ip': ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5'],
    'request_count': [100, 5000, 120, 150, 3000],
    'time_frame': [60, 60, 60, 60, 60],
    'is_ddos': [0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

# Özellikler ve etiketler
X = df[['request_count', 'time_frame']]
y = df['is_ddos']

# Veri setini bölme ve model eğitimi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
joblib.dump(model, 'ddos_model.pkl')

# Eğitilmiş modeli yükleme
model = joblib.load('ddos_model.pkl')

# IP başına istek sayısını izleme
request_counts = defaultdict(int)
request_times = defaultdict(deque)
blocked_ips = set()
request_logs = []

# İzleme süresi
monitoring_interval = 60  # saniye

def blackhole_ip(ip):
    print(f"IP engellendi: {ip}")
    blocked_ips.add(ip)

def is_ddos(request_count, time_frame):
    # Kullanıcıdan alınan özelliklerle tahmin yapma
    features = pd.DataFrame([[request_count, time_frame]], columns=['request_count', 'time_frame'])
    prediction = model.predict(features)
    return prediction[0]

@app.route('/')
def index():
    ip = request.remote_addr

    # Eğer IP blackhole listesinde ise yanıt verme
    if ip in blocked_ips:
        return "403 Forbidden", 403

    # İstek sayısını ve zamanını güncelle
    request_counts[ip] += 1
    request_times[ip].append(time.time())
    request_logs.append((ip, request_counts[ip], time.time()))

    # Belirli bir zaman diliminde gelen istek sayısını kontrol et
    while request_times[ip] and time.time() - request_times[ip][0] > monitoring_interval:
        request_times[ip].popleft()

    # Makine öğrenimi modeli ile DDoS kontrolü
    request_count = len(request_times[ip])
    if is_ddos(request_count, monitoring_interval) == 1:
        blackhole_ip(ip)

    return "Merhaba, dünya!"

@app.route('/update_model')
def update_model():
    global model

    # Yeni veri seti oluşturma
    df_new = pd.DataFrame(request_logs, columns=['ip', 'request_count', 'timestamp'])
    df_new['time_frame'] = monitoring_interval
    df_new['is_ddos'] = df_new['request_count'].apply(lambda x: 1 if x > 1000 else 0)  # Örnek etiketleme

    X_new = df_new[['request_count', 'time_frame']]
    y_new = df_new['is_ddos']

    # Modeli yeniden eğitme
    X_train_new, X_test_new, y_train_new, y_test_new = train_test_split(X_new, y_new, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train_new, y_train_new)
    joblib.dump(model, 'ddos_model.pkl')

    return jsonify({"message": "Model güncellendi."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
