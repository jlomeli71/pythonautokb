#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

NET_PASS = os.getenv("NET_PASS") if os.getenv("NET_PASS") else getpass()

nxos1 = {"host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
    "device_type": "cisco_nxos"}

nxos2 = {"host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
    "device_type": "cisco_nxos"}

devices = [nxos1, nxos2]

print("*"*40)
print("Devices hostnames")
print("")
for host in devices:
    net_connect = ConnectHandler(**host)
    print(net_connect.find_prompt())
    print("-"*40)
