from __future__ import print_function, unicode_literals


def show():
    f = open("exercize2/show_version.txt")
    output = f.read()
    print(output)
    print(type(output))
    f.close()

    with open("exercize2/show_version.txt") as f:
        output2 = f.readlines()

    print(output2)
    print(type(output2))
    return 0


def ip():
    # Create a list of five IP addresses.
    ip_list = ['192.168.0.1', '172.16.6.8', '55.4.5.68', '78.66.28.123', '10.3.3.5']
    print(ip_list)

    # Use the .append() method to add an IP address onto the end of the list.
    # Use the .extend() method to add two more IP addresses to the end of the list.
    ip_list.append('10.22.1.3')
    print(ip_list)
    # Use list concatenation to add two more IP addresses to the end of the list.
    ip_list = ip_list + ['1.2.3.3', '34.88.97.26']
    # Print out the entire list of ip addresses. Print out the first IP address in the list.
    # Print out the last IP address in the list.
    print(ip_list)
    print(ip_list[0])
    print(ip_list[len(ip_list)-1])
    # Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
    ip_list.pop(0)
    ip_list.pop()
    ip_list[0] = "2.2.2.2"
    print(ip_list[0])
