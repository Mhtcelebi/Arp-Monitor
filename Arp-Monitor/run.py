import subprocess
import sys
import time

print("🚀 NETWORK MONITOR BAŞLATILIYOR...")

# main.py (ARP dinleyici)
print("📡 ARP motor başlatılıyor...")
main = subprocess.Popen([sys.executable, "main.py"])

time.sleep(1)

# app.py (dashboard)
print("🌐 Dashboard başlatılıyor...")
web = subprocess.Popen([sys.executable, "app.py"])

print("\n✔ Sistem aktif")
print("👉 http://127.0.0.1:5000")

main.wait()
web.wait()
