#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

NET_PASS = os.getenv("NET_PASS") if os.getenv("NET_PASS") else getpass()

cisco3 = {"host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
    "device_type": "cisco_xe",
    "session_log": "cisco3.log"}

net_connect = ConnectHandler(**cisco3)
# print(net_connect.find_prompt())
output = net_connect.send_command("show version")
# print(output)

with open("./cisco3.log") as file:
    content = file.read()
    print(content)
