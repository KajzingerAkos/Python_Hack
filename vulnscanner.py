from portscanner import PortScanner
import argparse

def vulnscan(vuln_file):
    count = -1
    vulns = 0
    with open(str(vuln_file)) as file:
        lines = file.readlines()
    for vuln_soft in lines:
        for response in scan_ports.banners:
            count += 1
            if vuln_soft == response:
                vulns += 1
                print(f"[+] Port {scan_ports.open_ports[count]} is VULNERABLE!!\nService: {vuln_soft}")
    if vulns == 0:
        print("[-] No vulnerable service found")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Vulnerability scanner")
    parser.add_argument('vuln_file', action='store', help='Specify the vulnerability file')
    parser.add_argument('target', action='store', type=str, help="Specify the target(s) IP address(es) or domain name(s)")
    parser.add_argument('port_range', action='store', type=str, help="Specify the port range [minPort-maxPort]")
    args = parser.parse_args()
    scan_ports = PortScanner(args.target, args.port_range)
    scan_ports.scan()
    vulnscan(args.vuln_file)
