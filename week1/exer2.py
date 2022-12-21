#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()

nxos1 = {"host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": PASSWORD,
    "device_type": "cisco_nxos"}
nxos2 = {"host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": PASSWORD,
    "device_type": "cisco_nxos"}

devices = [nxos1, nxos2]

print("*"*40)
print("Devices hostnames")
print("*"*40)
for host in devices:
    net_connect = ConnectHandler(**host)
    print(net_connect.find_prompt())
    print("-"*40)

net_connect.disconnect()

