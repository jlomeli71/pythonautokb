#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()
# in .bashrc
# export NET_TEXTFSM=/path/to/ntc-templates/templates/

device1 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": PASSWORD,
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

