#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()

cisco3 = {"host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": PASSWORD,
    "device_type": "cisco_xe",
    "session_log": "cisco3.log"}

net_connect = ConnectHandler(**cisco3)
# print(net_connect.find_prompt())
output = net_connect.send_command("show version")
# print(output)

with open("./cisco3.log") as file:
    content = file.read()
    print(content)

# with open("show_version.txt", "w") as file:
#     file.write(output)

net_connect.disconnect()

