import random
import os

# Dosyadan rastgele bir IP adresi seçin
with open("ipaddress.txt", "r") as file:
    ip_addresses = file.readlines()
    random_ip = random.choice(ip_addresses)

# Seçilen rastgele IP adresini kullanın
new_ip = random_ip.strip()
print(f"Yeni IP Adresi: {new_ip}")

# Programı başlatın
os.system("start RedTeam")
