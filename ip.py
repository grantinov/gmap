"""
The objective for ip is to ...

 Project Name: gmap
 Developed by grant.stokley
 Date:    12/01/2017
 Time:    09:11


Example usage()s):

"""

import socket

import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("")
print("This IP Address: " + s.getsockname()[0])


def get_ip():
    file = os.popen("ifconfig | grep 'mask:'")
    data = file.read()
    file.close()
    bits = data.strip().split('\n')
    addresses = []
    for bit in bits:
        if bit.strip().startswith("inet "):
            other_bits = bit.replace(':', ' ').strip().split(' ')
            for obit in other_bits:
                if obit.count('.') == 3:
                    if not obit.startswith("127."):
                        addresses.append(obit)
                    break
    return addresses


print("")
print(get_ip())
s.close()
