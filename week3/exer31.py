#!/usr/bin/env python

from pprint import pprint

arp_data = """Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""
arp_list = []
# print(arp_data.splitlines()[1:])
for line in arp_data.splitlines()[1:]:
    entry = {}
    line = line.split()
    # print(line)
    entry["mac_addr"] = line[3]
    entry["ip_addr"] = line[1]
    entry["interface"] = line[5]
    arp_list.append(entry)
pprint(arp_list)

