import sys
import argparse
from IPy import IP
import socket

class PortScanner():

    timeout = 0.5
    target = []
    banners = []
    scanned_ports = []

    def __init__(self, ipaddress,port_range):
        self.ipaddress = ipaddress
        self.port_range = port_range

    def check_ip(self):
        try:
            IP(self.ipaddress)
        except ValueError:
            converted_ip = socket.gethostbyname(self.ipaddress)
            return converted_ip
        return self.ipaddress
    
    def ports(self):
        try:
            minMaxPort = self.port_range.split("-")
            minPort = int(minMaxPort[0])
            maxPort = int(minMaxPort[1])
            if minPort < 1 and minPort > 65534 and minPort > maxPort:
                print("[-] Invalid input, try: [minport-maxport]")
            if maxPort > 65535 and maxPort < minPort:
                print("[-] Invalid input, try: [minport-maxport]")
        except IndexError:
            print("[-] Invalid input, try: [minport-maxport]")
            sys.exit(1)
        except ValueError:
            print("[-] Invalid input, try: [minport-maxport]")
            sys.exit(1)
        return minMaxPort


    def scan(self):
        self.ports()
        minPort = int(self.ports()[0])
        maxPort = int(self.ports()[1])
        if ',' in self.ipaddress:
            self.target = self.ipaddress.split(',')
        else:
            self.target.append(self.ipaddress)
        for ips in self.target:
            for port in range(minPort,maxPort + 1):
                self.scanned_ports.append(port)
                try:
                    sock = socket.socket()
                    sock.settimeout(self.timeout)
                    sock.connect((ips,port))
                    try:
                        banner = sock.recv(1024).decode().strip('\n').strip('\r')
                        self.banners.append(banner)
                        print(f"Port {port} is open service {banner}")
                    except:
                        print(f"Port {port} is open")
                except:
                    self.banners.append(" ")

if __name__ == '__main__':
    print("Port scanner by Kajzinger Ákos, happy hacking :)")
    # Arguments
    parser = argparse.ArgumentParser(description='Port scanner')
    parser.add_argument('target', type=str ,action='store', help='specify the target(s) domain name(s) or IP address(es)')
    parser.add_argument('port_range',type=str ,action='store', help = 'specify the port range')
    parser.add_argument('-t', '--timeout', type=float, action='store', help='set the timeout, default: 0.5 (the bigger the timeout the more precise the scan will be)')
    args = parser.parse_args()
    # Timeout
    if args.timeout == True:
        timeout = args.timeout
    else:
        timeout = 0.5
    scan_ports = PortScanner(args.target, args.port_range)
    scan_ports.scan()