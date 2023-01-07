#!/usr/bin/env python
import os
import pyeapi
from my_funcs import yaml_load_devices, output_printer
from getpass import getpass
from pprint import pprint

# Set up credentials
# $ export PASWORD="Here is the password"
# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()

def main():

    devices = yaml_load_devices()
    password = PASSWORD

    for name, device_dict in devices.items():
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip arp")
        # pprint(output)	# For verification
        arp_list = output[0]["result"]["ipV4Neighbors"]
        output_printer(arp_list)


if __name__ == "__main__":
    main()
