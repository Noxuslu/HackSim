import time
import random

def loading_bar(task_name, length=20):
    print(f"[+] {task_name} başlatılıyor...")
    for i in range(length + 1):
        percent = int((i / length) * 100)
        bar = "#" * i + "-" * (length - i)
        print(f"\r[{bar}] {percent}%", end="")
        time.sleep(random.uniform(0.05, 0.2))
    print(" ✓")

def start_hack(ip):
    print(f"[!] {ip} adresine bağlantı sağlanıyor...")
    loading_bar("Port taraması")
    loading_bar("Güvenlik duvarı atlatma")
    loading_bar("Parola brute force denemesi")
    time.sleep(1)
    print("\n[+] Sistem raporu oluşturuluyor...")
    time.sleep(1)
    report = generate_report(ip)
    print(report)
    return report

def generate_report(ip):
    vulns = ["Açık port bulundu", "Zayıf parola tespit edildi", "SQL Injection açığı", "XSS açığı"]
    found = random.sample(vulns, random.randint(1, len(vulns)))
    return f"""
==== HackSim Penetrasyon Raporu ====
Hedef: {ip}
Bulunan açıklar:
- {'\n- '.join(found)}
====================================
"""
