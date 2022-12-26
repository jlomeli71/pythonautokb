#!/usr/bin/env python
import yaml
from pprint import pprint
from os import path
from netmiko import ConnectHandler

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

# print(home_dir)
# print(filename)

with open(filename) as file:
    yaml_data = yaml.safe_load(file)
# pprint(yaml_data)

#for each in yaml_data.keys():
#    if "cisco3" in each:
device = yaml_data["cisco3"]
#print(device)

net_connect = ConnectHandler(**device)
print()
print(net_connect.find_prompt())
print()
net_connect.disconnect()
