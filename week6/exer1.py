#!/usr/bin/env python

import os
import pyeapi
from getpass import getpass
from pprint import pprint

# Set up credentials
# $ export PASWORD="Here is the password"
# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()
USERNAME = "pyclass"

arista8 = {
    "transport": "https",
    "host": "arista8.lasthop.io",
    "username": USERNAME,
    "password": PASSWORD,
    "port": 443,
}

connection = pyeapi.client.connect(**arista8)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

print()
pprint(output)
print("-" * 40)
arp_list = output[0]["result"]["ipV4Neighbors"]
for arp_entry in arp_list:
    mac_address = arp_entry["hwAddress"]
    ip_address = arp_entry["address"]
    print("{:^15}{:^5}{:^15}".format(ip_address, "-->", mac_address))

print("-" * 40)
print()

