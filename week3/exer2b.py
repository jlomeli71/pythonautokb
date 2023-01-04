#!/usr/bin/env python

import yaml
from pprint import pprint
from exer32a import lab_list

# pprint(lab_list)

with open("my_devices.yml", "w") as f:
    yaml.dump(lab_list, f, default_flow_style=False)
