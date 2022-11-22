#!/usr/bin/env python

import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

NET_PASS = os.getenv("NET_PASS") if os.getenv("NET_PASS") else getpass()

device1 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
    "fast_cli": False
}
CMD = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]
net_connect = ConnectHandler(**device1)
start_false = datetime.now()
output = net_connect.send_config_set(CMD)
end_false = datetime.now()
net_connect.disconnect()

device2 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
    "fast_cli": True
}
net_connect = ConnectHandler(**device2)
# output = net_connect.send_config_from_file(config_file="config.txt")
start_true = datetime.now()
output = net_connect.send_config_set(CMD)
end_true = datetime.now()

ping_output = net_connect.send_command("ping google.com")
if "!!" in ping_output:
    print("Ping Successful:")
    print("\nPing Output: {}\n".format(ping_output))
else:
    raise ValueError("\nPing Failed: {}\n".format(ping_output))
net_connect.disconnect()
print()
print(output)
print()
print(f"With fast cli as False: {end_false - start_false}")
print(f"With fast cli as True: {end_true - start_true}")
