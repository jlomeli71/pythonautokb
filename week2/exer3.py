#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

NET_PASS = os.getenv("NET_PASS") if os.getenv("NET_PASS") else getpass()

device1 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
}
CMD = "show version"
net_connect = ConnectHandler(**device1)

output = net_connect.send_command(CMD, use_textfsm=True)
print()
pprint(output)
print()
print(f"Structure type for {CMD}")
print(type(output))
print()
CMD = ("show lldp neighbors")
output = net_connect.send_command(CMD, use_textfsm=True)
net_connect.disconnect()
print()
pprint(output)
print()
print(f"Neighbor interface: {output[0]['neighbor_interface']}")
print()
print(f"Structure type for {CMD}")
print(type(output))
print()
