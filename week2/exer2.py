#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

NET_PASS = os.getenv("NET_PASS") if os.getenv("NET_PASS") else getpass()

device1 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
    "global_delay_factor": 2,
    "fast_cli": False
}

net_connect = ConnectHandler(**device1)

start_time1 = datetime.now()
output = net_connect.send_command("show lldp neighbors detail")
end_time1 = datetime.now()
# net_connect.disconnect()

print("#"*40)
print("With Global Delay Factor of 2")
print(f"Execution in: {end_time1 - start_time1}")
# print(output)

net_connect = ConnectHandler(**device1)

start_time2 = datetime.now()
output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
end_time2 = datetime.now()
net_connect.disconnect()

print("#"*40)
print("With Delay Factor of 8")
print(f"Execution in: {end_time2 - start_time2}")
# print(output)
print()
