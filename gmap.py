"""
The objective for gmap is to run nmap type port scans from code.

 Project Name: gmap
 Developed by grant.stokley
 Creation date 11/30/17

Example usage(s):

nm['127.0.0.1'].hostname()  # get one hostname for host 127.0.0.1, usualy the user record
nm['127.0.0.1'].hostnames()  # get list of hostnames for host 127.0.0.1 as a list of dict [{'name':'hostname1', 'type':'PTR'}, {'name':'hostname2', 'type':'user'}]
nm['127.0.0.1'].hostname()  # get hostname for host 127.0.0.1
nm['127.0.0.1'].state()  # get state of host 127.0.0.1 (up|down|unknown|skipped)
nm['127.0.0.1'].all_protocols()  # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
nm['127.0.0.1']['tcp'].keys()  # get all ports for tcp protocol
nm['127.0.0.1'].all_tcp()  # get all ports for tcp protocol (sorted version)
nm['127.0.0.1'].all_udp()  # get all ports for udp protocol (sorted version)
nm['127.0.0.1'].all_ip()  # get all ports for ip protocol (sorted version)
nm['127.0.0.1'].all_sctp()  # get all ports for sctp protocol (sorted version)
nm['127.0.0.1'].has_tcp(22)  # is there any information for port 22/tcp on host 127.0.0.1
nm['127.0.0.1']['tcp'][22]  # get infos about port 22 in tcp on host 127.0.0.1
nm['127.0.0.1'].tcp(22)  # get infos about port 22 in tcp on host 127.0.0.1
nm['127.0.0.1']['tcp'][22]['state']  # get state of port 22/tcp on host 127.0.0.1 (open

"""
# !/usr/bin/env python
import nmap  # import nmap.py module

nm = nmap.PortScanner()  # instantiate nmap.PortScanner object
# TODO: create a variable to feed into this.
nm.scan('10.224.40.197', '22-443')  # scan host 127.0.0.1, ports from 22 to 443
nm.command_line()  # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
nm.scaninfo()  # get nmap scan information {'tcp': {'services': '22-443', 'method': 'connect'}}
nm.all_hosts()  # get all hosts that were scanned


# a more useful example :
for host in nm.all_hosts():
    print('----------------------LINE 39-------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    print('----------------------LINE 52------------------------------')
    # print result as CSV
    print(nm.csv())

    print('----------------------LINE 56------------------------------')
    # If you want to do a pingsweep on network 192.168.1.0/24:
    # TODO: Advanced, get IP address of the NICs and automatically take a look around.
    # TODO: create variable to pass into this rather than hard coding it.
    nm.scan(hosts='10.224.40.128/25', arguments='-n -sS -PE -PA21,23,80,135,139,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        print('{0}:{1}'.format(host, status))

    print('----------------------LINE 65------------------------------')
    # Asynchronous usage of PortScannerAsync
    nma = nmap.PortScannerAsync()


    def callback_result(host, scan_result):
        print('-------LINE 71--------')
        print(host, scan_result)


    nma.scan(hosts='10.224.40.128/25', arguments='-sP', callback=callback_result)
    while nma.still_scanning():
        print("Waiting ...")
        # Wait until some of the results have come back.
        nma.wait(2)
