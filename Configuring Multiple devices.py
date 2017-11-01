#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'modi_ios',
    'ip': '192.168.122.71',
    'username': 'badrik',
    'password': 'modi',
}

iosv_l2_s2 = {
    'device_type': 'modi_ios',
    'ip': '192.168.122.72',
    'username': 'badrik',
    'password': 'modi',
}

iosv_l2_s3 = {
    'device_type': 'modi_ios',
    'ip': '192.168.122.73',
    'username': 'badrik',
    'password': 'modi',
}

iosv_l2_s4 = {
    'device_type': 'modi_ios',
    'ip': '192.168.122.74',
    'username': 'badrik',
    'password': 'modi',
}

iosv_l2_s5 = {
    'device_type': 'modi_ios',
    'ip': '192.168.122.75',
    'username': 'badrik',
    'password': 'modi',
}


with open('iosv_l2_modi_design') as f:
    lines = f.read().splitlines()
print lines


all_devices = [iosv_l2_s5, iosv_l2_s4, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 


with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print lines


all_devices = [iosv_l2_s2, iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 