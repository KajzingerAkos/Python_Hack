import sys
import argparse
from IPy import IP
import socket

class PortScanner():

    target = []
    banners = []
    open_ports = []

    def __init__(self, ipaddress,port_range):
        self.ipaddress = ipaddress
        self.port_range = port_range

    def check_ip(self,ipaddress):
        try:
            IP(self.ipaddress)
        except ValueError:
            converted_ip = socket.gethostbyname(self.ipaddress)
            return converted_ip
        return self.ipaddress
    
    def ports(self):
        try:
            minMaxPort = self.portrange.split("-")
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
            self.targtes = self.ipaddress.split(',')
        else:
            self.targtes.append(self.ipaddress)
        for ips in self.targtes:
            for port in range(minPort,maxPort + 1):
                try:
                    sock = socket.socket()
                    sock.settimeout(0.5)
                    sock.connect((ips,port))
                    self.open_ports.append(int(port))
                    try:
                        banner = sock.recv(1024).decode().strip('\n').strip('\r')
                        self.banners.append(banner)
                        print(f"Port {port} is open service {banner}")
                    except:
                        print(f"Port {port} is open")
                except:
                    print(f"[-] Port {port} is closed")
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