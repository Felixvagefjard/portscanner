#Program that scans the top ports (1-1024) for a specific IP-address
import socket #used for network connectivity
import re #regular expressions, here used for validating IP address
from datetime import datetime #used to calculate time that the scan took

#Regex to validate IPv4 addresses
ip_validation = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
open_ports = []

#Asking user for an IP address they wish to scan, continues when a correct address is entered
while True:
    ip_address = input("\nEnter IP you wish to scan: ")
    if ip_validation.search(ip_address):
        print(f"\n{ip_address} is a valid IPv4 address. Port scan is starting...")
        break

#Check time that scan started
t1 = datetime.now()

#Going through ports in range
for port in range(50, 80 + 1):
    try:
        #Create an AF_INET socket object with the name of "s"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5) #Setting a timeout to limit the time it takes to connect.
            s.connect((ip_address, port)) #Try to connect to the given IP address and port
            #If the connection is successfull it will append the open port to the open_ports list
            #If it doesn't manage to connect there will be an exception and it won't be appended to the open_ports list
            open_ports.append(port) 
            
    #Cancel the port scan
    except KeyboardInterrupt:
        print("\n*** Stopping scan ***")
        exit()
    except:
        pass

#For loop that prints every port number in the open_ports list
for port in open_ports:
    print(f"\n*** Port {port} is OPEN on {ip_address} ***")

#Checking time when scan ended and calculates how long the scan took
t2 = datetime.now()
total = t2 - t1
print(f"\nPort scan completed in {total}")
