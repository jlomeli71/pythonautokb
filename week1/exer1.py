#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

NET_PASS = os.getenv("NET_PASS") if os.getenv("NET_PASS") else getpass()

nxos1 = {"host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
    "device_type": "cisco_nxos"}

net_connect = ConnectHandler(**nxos1)
print(net_connect.find_prompt())
