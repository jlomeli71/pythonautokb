#!/usr/bin/env python
import os
import time
from netmiko import ConnectHandler, file_transfer
from getpass import getpass
from datetime import datetime

# os.environ["PASSWORD"] = "Here is the password"
PASSWORD = os.getenv("PASSWORD") if os.getenv("PASSWORD") else getpass()

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": PASSWORD,
    "secret": PASSWORD,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

# a. Print the current prompt using find_prompt()
net_connect = ConnectHandler(**device1)
print("\nCurrent Prompt: ")
print(net_connect.find_prompt())

# b. Execute the config_mode() method and print the new prompt using find_prompt()
print("\nEnter Config Mode, Current Prompt: ")
net_connect.config_mode()
print(net_connect.find_prompt())

# c. Execute the exit_config_mode() method and print the new prompt using find_prompt()
print("\nExit Config Mode, Current Prompt: ")
net_connect.exit_config_mode()
print(net_connect.find_prompt())

# d. Use the write_channel() method to send the 'disable' command down the SSH channel.
print("\nExit privileged exec (disable), Current Prompt: ")
net_connect.write_channel("disable\n")

# e. time.sleep for two seconds and then use the read_channel() method to read the data cha
time.sleep(2)
output = net_connect.read_channel()
print(output)

# f. Execute the enable() method and print your now current prompt using find_prompt()
print("\nRe-enter enable mode, Current Prompt: ")
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()

print()
print("#"*40)
print("Output file:")
with open(device1["session_log"]) as file:
    log_file = file.read()
print(log_file)

