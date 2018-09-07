#!/usr/bin/python2

import nmap


target_mac = '<Enter MAC Adress>'

nm = nmap.PortScanner()

nm.scan(hosts='192.168.10.0/24', arguments='-sP')

host_list = nm.all_hosts()
for host in host_list:
        if  'mac' in nm[host]['addresses']:
                print(host+' : '+nm[host]['addresses']['mac'])
                if target_mac == nm[host]['addresses']['mac']:
                       print('Target Found')

