#!/usr/bin/env python
import os
from netmiko import ConnectHandler, file_transfer
from getpass import getpass

NET_PASS = os.getenv("NET_PASS") if os.getenv("NET_PASS") else getpass()

device1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
}

device2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": NET_PASS,
}

devices = [device1, device2]

for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file("vlans.txt")
    print("#"*40)
    print(f"Output for host: {device['host']}")
    net_connect.save_config()
    net_connect.disconnect()
    print(output)
