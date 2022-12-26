#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
from getpass import getpass

# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()

device4 = {
    "device_type": "cisco_ios",
    "host": " cisco4.lasthop.io",
    "username": "pyclass",
    "password": PASSWORD,
}

net_connect = ConnectHandler(**device4)
output = net_connect.send_command("show run")
net_connect.disconnect()

# print(output)

# When feeding config directly - CiscoConfParse requires a list
cisco_config = CiscoConfParse(output.splitlines())
interfaces = cisco_config.find_objects_w_child(
    parentspec=r"^interface", childspec=r"^\s+ip address"
    )

for interface in interfaces:
    print()
    print("Interface Line: {}".format(interface.text))
    ip_address = interface.re_search_children(r"ip address")[0].text
    print("IP Address Line: {}".format(ip_address))
    print()
