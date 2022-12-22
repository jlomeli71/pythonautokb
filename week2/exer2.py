#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()

device1 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": PASSWORD,
    "global_delay_factor": 2,
    "fast_cli": False
}

net_connect = ConnectHandler(**device1)

start_time1 = datetime.now()
output = net_connect.send_command("show lldp neighbors detail")
end_time1 = datetime.now()

print("Execution of: show lldp neighbors detail:\n")
print(output)
print("#"*40)
print("With Global Delay Factor of 2")
print(f"Execution in: {end_time1 - start_time1}")

start_time2 = datetime.now()
output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
end_time2 = datetime.now()

print("#"*40)
print("With Delay Factor of 8")
print(f"Execution in: {end_time2 - start_time2}")

net_connect.disconnect()
