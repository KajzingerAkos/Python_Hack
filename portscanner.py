import sys
import socket
from IPy import IP
import argparse

class PortScanner():

    timeout = 0.5
    open_ports = []
    banners = []

    def __init__(self, ipaddress, portrange):
        self.ipaddress = ipaddress
        self.portrange = portrange

    # Validate domain names or ips
    def check_ip(self):
        try:
            IP(self.ipaddress)
        except ValueError:
            converted_ip = socket.gethostbyname(self.ipaddress)
            return converted_ip
        return self.ipaddress


    # Asks and preforms validity checks on port range
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

    # Scanner
    def scan(self):
        self.ports()
        minPort = int(self.ports()[0])
        maxPort = int(self.ports()[1])
        # Scan multiple targets
        if ',' in self.ipaddress:
            targets = self.ipaddress.split(',')
            for ips in targets:
                print(f"[+] Scanning...")
                print(f"[+] Target: {ips}")
                for port in range(minPort, maxPort + 1):
                    try:
                        sock = socket.socket()
                        sock.settimeout(float(self.timeout))
                        sock.connect((self.check_ip(ips),port))
                        print(f"[+] Port {port} is open")
                        self.ports.append(port)
                        try:
                            banner = sock.recv(1024).decode.strip('\n').strip('\r')
                            self.banners.append(banner)
                        except:
                            self.banners.append(' ')
                    except:
                        pass

        else:
            print(f"[+] Scanning...")
            print(f"[+] Target: {self.ipaddress}")       
            for port in range(minPort, maxPort + 1):
                try:
                    sock = socket.socket()
                    sock.settimeout(float(self.timeout))
                    sock.connect((self.check_ip(),port))
                    print(f"[+] Port {port} is open")
                    self.ports.append(port)
                    try:
                        banner = sock.recv(1024).decode.strip('\n').strip('\n')
                        self.banners.append(banner)
                    except:
                        self.banners.append(' ')
                except:
                    pass
        
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
