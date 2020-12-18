#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import re

ip_regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

mac_regex = '''^([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})$'''

def show():

    mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
    mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
    mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

    maclist = []
    maclist.append(mac1.split())
    maclist.append(mac2.split())
    maclist.append(mac3.split())

    print(mac1)
    ips = []
    macs = []

    for list in maclist:
        for item in list:
            if re.search(ip_regex, item):
                ips.append(item)
            elif re.search(mac_regex, item):
                macs.append(item)

    # Output
    print("{col1:>20}{col2:>20}".format(col1="IP ADDR",col2="MAC ADDRESS"))
    print("{col1:>20}{col2:>20}".format(col1="-"*20,col2="-"*20))
    index = 0
    for ip in ips:
            print("{col1:>20}{col2:>20}".format(col1=ip, col2=macs[index]))
            index += 1
    return 0