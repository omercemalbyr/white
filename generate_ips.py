import random
import socket
import struct

def generate_random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

with open("ipaddress.txt", "w") as file:
    for _ in range(100):  # 100 rastgele IP adresi oluşturabilirsiniz
        ip = generate_random_ip()
        file.write(ip + "\n")
