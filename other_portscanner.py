import sys
import argparse
from IPy import IP
import socket

ipaddress = "localhost"
banners = ['hey']
open_ports = []


def scan(ipaddress):
    for port in range(1,100):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((ipaddress,port))
            open_ports.append(int(port))
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                banners.append(banner)
                print("Port {port} is open service {banner}")
            except:
                print(f"Port {port} is open")
        except:
            print(f"[-] Port {port} is closed")
            banners.append(" ")
    print(banners)
    print(open_ports)

scan(ipaddress)