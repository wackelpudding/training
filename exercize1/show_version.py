#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# 1. Remove all leading and trailing whitespace from the string.
# 2. Split the string and extract the model and serial_number from it.
# 3. Check if 'Cisco' is contained in the model string (ignore capitalization).
# 4. Check if '881' is in the model string.
# 5. Print out both the serial number and the model.
show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

# 1. Remove all leading and trailing whitespace from the string.

show_version = show_version.strip()
print("-" * 50)
print("# 1. Remove all leading and trailing whitespace from the string.")
print("{stripped:^50}\n".format(stripped=show_version))

# 2. Split the string and extract the model and serial_number from it.
splitted_version = show_version.split()

model = splitted_version[1]
serial_number = splitted_version[2]


# 3. Check if 'Cisco' is contained in the model string (ignore capitalization).
# 4. Check if '881' is in the model string.

print('Is "Cisco" in model?:  ', 'Cisco'.upper() in model.upper())
print('Is "881" in model?:  ', '881' in model)

print("#" * 63, "\n", "|{model:^30}|{serial:^30}|".format(model=model, serial=serial_number), "\n", "#" * 63, sep='')
