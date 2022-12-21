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

net_connect = ConnectHandler(**nxos1)
print(net_connect.find_prompt())

net_connect.disconnect()

