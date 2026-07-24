import socket
from concurrent.futures import ThreadPoolExecutor

TARGET = "<TARGET_IP>"

PORTS = [
    21,22,23,25,
    53,80,110,
    135,139,143,
    443,445,
    3306,3389,
    5432,5900,
    8080,8000
]

def scan(port):
    sock = socket.socket()
    sock.settimeout(1)

    try:
        sock.connect((TARGET, port))
        print(f"[+] Porta {port} aberta")
    except:
        pass
    finally:
        sock.close()

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan, PORTS)