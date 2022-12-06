#!/usr/bin/env python

import yaml
from pprint import pprint

cisco3 = {"device_name": "cisco3",
"device_type": "cisco_xe",
"host": "cisco3.lasthop.io",
"username": "chonito",
"password": "punito"}
arista1 = {"device_name": "arista1",
"device_type": "arista_eos",
"host": "arista1.lasthop.io",
"username": "chonito",
"password": "punito"}
srx2 = {"device_name": "srx2",
"device_type": "juniper_junos",
"host": "srx2.lasthop.io",
"username": "chonito",
"password": "punito"}
nxos1 = {"device_name": "nxos1",
"device_type": "cisco_nxos",
"host": "nxos1.lasthop.io",
"username": "chonito",
"password": "punito"}

lab_list = [cisco3, arista1, srx2, nxos1]

# pprint(lab_list)

with open("my_devices.yml", "w") as f:
    yaml.dump(lab_list, f, default_flow_style=False)

