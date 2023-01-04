#!/usr/bin/env python
import json
from pprint import pprint

with open("my_arp.json") as file:
    json_data = json.load(file)

# pprint(json_data)

data = json_data["ipV4Neighbors"]
my_dict = {}

for each in data:
    my_dict[each["address"]] = each["hwAddress"]

pprint(my_dict)
