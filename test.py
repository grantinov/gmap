"""
The objective for test is to...

 Project Name: grantNmap
 Developed by root
 Creation date 11/30/17

Example usage(s):

"""
import nmap
nm = nmap.PortScanner()
nm.scan('localhost', arguments='-S 127.0.0.1')
for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))
