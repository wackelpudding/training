#!/usr/bin/env python
from __future__ import print_function, unicode_literals
print("Hello World")
try:
    ip_addr = raw_input("Enter an ip address:  ")  # for python2
except NameError:
    ip_addr = input("Enter an ip address:  ")
print(ip_addr)
