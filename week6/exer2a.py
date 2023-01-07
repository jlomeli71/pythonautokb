#!/usr/bin/env python

import os
import pyeapi
import yaml
from getpass import getpass
from pprint import pprint

# Set up credentials
# $ export PASWORD="Here is the password"
# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()

def yaml_load_devices(filename="arista4_device.yml"):
    with open(filename, "r") as f:
        return yaml.safe_load(f)
    raise ValueError("Reading YAML file failed")


def main():

    devices = yaml_load_devices()
    password = PASSWORD

    for name, device_dict in devices.items():
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip arp")
        # For verification next line
        pprint(output)
        print()
        print("-" * 40)
        arp_list = output[0]["result"]["ipV4Neighbors"]
        for arp_entry in arp_list:
            mac_address = arp_entry["hwAddress"]
            ip_address = arp_entry["address"]
            print("{:^15}{:^5}{:^15}".format(ip_address, "-->", mac_address))
        print("-" * 40)
        print()


if __name__ == "__main__":
    main()
