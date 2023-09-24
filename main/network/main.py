import ipaddress
import socket
import scapy.all as scapy
import re

class Network:
    # Regular Expression Pattern to recognise IPv4 addresses.
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    ip = socket.gethostbyname(socket.gethostname())


    def myHostname():
         # Getting a name from out device.
         name = socket.gethostname()
         return name

    def pattern():
        ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
        return ip_add_range_pattern

    def myadress():
        # Getting a ip adress from out device.
        ip = socket.gethostbyname(socket.gethostname())
        return ip

    def subnet():
       # Getting a subnet from out device.
       return socket.gethostbyname(socket.gethostname())


    def arp():
#TODO: make it working properly that function shuold return a list of all the devices on the network.
        ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
        ip = socket.gethostbyname(socket.gethostname())
        ip_address = ipaddress.ip_address(ip)
        network = ipaddress.ip_network(ip_address)
        subnet = str(network.network_address) + "/" + str(network.subnets())

        # Get the address range to ARP
        while True:
            ip_add_range_entered = subnet
            if ip_add_range_pattern.search(ip_add_range_entered):
                print(f"{ip_add_range_entered} is a valid ip address range")
                break

            # Try ARPing the ip address range supplied by the user.
            # The arping() method in scapy creates a pakcet with an ARP message
            # and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff.
            # If a valid ip address range was supplied the program will return
            # the list of all results.
        return scapy.arping(ip_add_range_entered)
