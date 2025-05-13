import pyfiglet
import sys
import ipaddress
import socket
import termcolor
from datetime import datetime

def scan(target, ports):
    print('\n' + 'Starting scan for: ' + str(target))
    for port in target:
        port_scan(target,port)

def port_scan(ipaddress, port):
    try:
       sock = socket.socket()
       sock.connect((ipaddress,port))
       print('Port opened: ' + str(port))
       socket.close()
    except:
        pass


targets = input("[*] Enter in the IPv4 addresses to scan (split them with a ','): ")
ports = int(input("[*] Enter how many ports you want to scan: "))
if ',' in targets:
    print(termcolor.colored(("[*] Scanning started at: ") + str(datetime.now()), 'green'))
    print(termcolor.colored(("[*] Scanning Targets..."), 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
    else:
        scan(targets,ports)
else:
    print(termcolor.colored(("[*] Scanning started at: ") + str(datetime.now()), 'green'))
    print(termcolor.colored(("[*] Scanning Targets..."), 'green'))
    for ip_addr in targets:
        scan(ip.addr, ports)
    else:
        scan(targets,ports)

#if KeyboardInterrupt:
    #print("\n Exiting Program...")
   #sys.exit()
#if socket.gaierror:
    #print("\n IP could not be resolved, please try again")
    #sys.exit()
#if socket.error:
    #print("\n Host not responding...")
    #sys.exit()