#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()

device1 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": PASSWORD,
}

net_connect = ConnectHandler(**device1)

output = net_connect.send_command_timing("ping", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)       # Protocol …
output += net_connect.send_command_timing("8.8.8.8", strip_prompt=False, strip_command=False)  # Target …
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)       # Repeat …
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)       # Datagram …
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)       # Timeout …
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)       # Extended …
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)       # Sweep …
net_connect.disconnect()

print()
print(output)
print()

