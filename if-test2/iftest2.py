#!/usr/bin/python3

import ipaddress

#ipchk= '192.168.0.1'
ipchk= input('Apply an IP adress: ')

try:
    ipaddress.ip_address(ipchk)
    if ipchk == '192.168.70.1':
        print ('Looks like the gateway IP address was set: ' + ipchk + 'this is not recommended.')

    else:
        print('Looks like the IP address was set: ' + ipchk)

   # else: 
    #    print('ypu did not provide input, dummy.')

except:
      print('That does not appear to be a Valid IP')
