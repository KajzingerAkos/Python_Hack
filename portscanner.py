import sys
import socket
from IPy import IP
import argparse

# Arguments
parser = argparse.ArgumentParser(description='Port scanner')
parser.add_argument('target', type=str ,action='store', help='specify the targets domain name or IP address')
parser.add_argument('port_range',type=str ,action='store', help = 'specify the port range')
parser.add_argument('-t', '--timeout', type=float, action='store', help='set the timeout, default: 0.5 (the bigger the timeout the more precise the scan will be)')
parser.add_argument('-f','--target_file', type=str, action='store', help = 'specify a file to scan multiple targets')
args = parser.parse_args()

isDomainName= 0

# Validate domain names or ips
def check_ip(ip):
    try:
        IP(ip)
    except ValueError:
        converted_ip = socket.gethostbyname(ip)
        return converted_ip
    return ip


# Asks and preforms validity checks on port range
def ports():
    try:
        
        minMaxPort = args.port_range.split("-")
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

# Scan multiple targets
def multiple(targetFile):
    with open(args.target_file, encoding='utf-8') as f:
        lines = f.readlines()
    return lines



# Scanner
def scan():
    minPort = int(ports()[0])
    maxPort = int(ports()[1])
    if args.timeout == True:
        timeout = args.timeout
    else:
        timeout = 0.5
    if args.target_file:
        for ips in multiple(args.target_file):
            print(f"[+] Scanning target {ips}...")
            for port in range(minPort, maxPort + 1):
                try:
                    sock = socket.socket()
                    sock.settimeout(timeout)
                    sock.connect((check_ip(ips),port))
                    print(f"[+] Port {port} is open")
                except:
                    pass
    else:        
        for port in range(minPort, maxPort + 1):
            try:
                sock = socket.socket()
                sock.settimeout(timeout)
                sock.connect((check_ip(args.target),port))
                print(f"[+] Port {port} is open")
            except:
                pass



ports()
scan()