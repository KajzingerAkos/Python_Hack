import sys
import socket
from IPy import IP
import argparse

# Arguments
parser = argparse.ArgumentParser(description='Port scanner')
parser.add_argument('target', type=str ,action='store', help='specify the target(s) domain name(s) or IP address(es)')
parser.add_argument('port_range',type=str ,action='store', help = 'specify the port range')
parser.add_argument('-t', '--timeout', type=float, action='store', help='set the timeout, default: 0.5 (the bigger the timeout the more precise the scan will be)')
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

# Scanner
def scan():
    minPort = int(ports()[0])
    maxPort = int(ports()[1])
    if args.timeout == True:
        timeout = args.timeout
    else:
        timeout = 0.5

    # Scan multiple targets
        if ',' in args.target:
            targets = args.target.split(',')
            for ips in targets:
                print(f"[+] Scanning...")
                print(f"[+] Target: {ips}")
                for port in range(minPort, maxPort + 1):
                    try:
                        sock = socket.socket()
                        sock.settimeout(timeout)
                        sock.connect((check_ip(ips),port))
                        print(f"[+] Port {port} is open")
                    except:
                        pass

        else:
            print(f"[+] Scanning...")
            print(f"[+] Target: {args.target}")       
            for port in range(minPort, maxPort + 1):
                try:
                    sock = socket.socket()
                    sock.settimeout(timeout)
                    sock.connect((check_ip(args.target),port))
                    print(f"[+] Port {port} is open")
                except:
                    pass
        
if __name__ == '__main__':
    print("Port scanner by Kajzinger Ákos, happy hacking :)\n")
    ports()
    scan()
