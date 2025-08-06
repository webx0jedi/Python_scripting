import socket
import re


# checks if IP is valid with while loop
while True:
    target = input("Please enter in an IP address: \n")
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    if(re.search(regex, target)):
        print("Correct IP. Continuing program...\n")
        break
    else:
        print("Inavalid IP, please try again")

# checks valid port with while loop
while True:
    try:
        port = int(input("Please enter a port: \n"))
        if 1 <= port <= 65535:
            break
        else:
            raise ValueError
    except ValueError:
        print("This is not a valid port number, try again.")


# main banner grabbing function
def banner_grab(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        banner = s.recv(1024)
        print("[+] Banner: " + banner.decode().strip())
        s.close()
    except Exception as e:
        print("[-] Error: " + str(e))

banner_grab(target, port)
