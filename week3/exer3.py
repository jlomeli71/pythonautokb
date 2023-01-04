#!/usr/bin/env python
import json
from pprint import pprint

with open("my_json.json", "r") as file:
    json_data = json.load(file)

# print(f"Data file is: {type(json_data)}")
# pprint(json_data)

ipv4_list = []
ipv6_list = []

for intf, ipaddr_dict in json_data.items():
    for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
        for ip_addr, prefix_dict in addr_info.items():
            prefix_length = prefix_dict["prefix_length"]
            if ipv4_or_ipv6 == "ipv4":
                ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
            elif ipv4_or_ipv6 == "ipv6":
                ipv6_list.append("{}/{}".format(ip_addr, prefix_length))

print("\nIPv4 Addresses: {}".format(ipv4_list))
print("\nIPv6 Addresses: {}".format(ipv6_list))

