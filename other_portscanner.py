import sys
import argparse
from IPy import IP
import socket

banners = []
open_ports = []

class PortScanner():

    def __init__(self, ipaddress,):
        self.ipaddress = ipaddress
        #self.port_range = port_range

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

if __name__ == '__main__':
    print("Port scanner by Kajzinger Ákos, happy hacking :)")
    # Arguments
    parser = argparse.ArgumentParser(description='Port scanner')
    parser.add_argument('target', type=str ,action='store', help='specify the target(s) domain name(s) or IP address(es)')
    #parser.add_argument('port_range',type=str ,action='store', help = 'specify the port range')
    parser.add_argument('-t', '--timeout', type=float, action='store', help='set the timeout, default: 0.5 (the bigger the timeout the more precise the scan will be)')
    args = parser.parse_args()
    # Timeout
    if args.timeout == True:
        timeout = args.timeout
    else:
        timeout = 0.5
    
    scan_ports = PortScanner(args.target, args.port_range)
    scan_ports.scan()