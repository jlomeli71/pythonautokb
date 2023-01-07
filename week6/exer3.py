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

if __name__ == "__main__":
    password = PASSWORD

    devices = yaml_load_devices()

    for name, device_dict in devices.items():
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip route")
        pprint(output)      # For verification
        routes = output[0]["result"]["vrfs"]["default"]["routes"]

        print()
        for prefix, route_dict in routes.items():
            route_type = route_dict["routeType"]
            print()
            print(prefix)
            print("-" * 12)
            print(route_type)
            print(">" * 6)
            print(route_dict["vias"][0]["interface"])
            if route_type == "static":
                print(route_dict["vias"][0]["nexthopAddr"])
            print("-" * 12)

        print()
