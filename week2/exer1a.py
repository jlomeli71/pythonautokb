#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

NET_PASS = os.getenv("NET_PASS") if os.getenv("NET_PASS") else getpass()

device1 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
}

net_connect = ConnectHandler(**device1)

output = net_connect.send_command_timing("ping", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
net_connect.disconnect()

print()
print(output)
print()

