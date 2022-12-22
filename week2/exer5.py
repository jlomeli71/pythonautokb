#!/usr/bin/env python
import os
from netmiko import ConnectHandler, file_transfer
from getpass import getpass
from datetime import datetime

# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()

device1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": PASSWORD,
}

device2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": PASSWORD,
}

devices = [device1, device2]

for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file("vlans.txt")
    print("#"*40)
    net_connect.save_config()
    net_connect.disconnect()
    print(f"Output for device: {device['host']}")
    print(output)


