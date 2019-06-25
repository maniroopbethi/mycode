#!/usr/bin/python3
import os
import pyexcel

from netmiko import ConnectHandler

def retv_excel(par):
    d = {}
    records = pyexcel.iget_records(file_name=par)
    for record in records:
        d.update({record['IP']:record['driver']})
    return d

def ping_router(hostname):
    response = os.system('ping -c 1 ' + hostname)
    if response == 0:
        return True
    else:
        return False

def interface_check(dev_type,dev_ip,dev_un,dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        my_command = open_connection.send_command('show ip int brief')
    except:
        my_command = '** Command Failed **'
    finally:
        return my_command

def login_router(dev_type,dev_ip,dev_un,dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        return True
    except:
        return False

def main():
    file_location = str(input('\nWhere is the file? '))
    entry = retv_excel(file_location)

    print('\n Begin SSH')
    for x in entry.keys():
        if login_router(str(entry[x]),x,'admin','alta3'):
            print('\n\tIP: - ' + x + ' - SSH UP\n')
        else:
            print('\n\tIP: - ' + x + ' - SSH DOWN\n')

    print('\n BEGIN ICMP')
    for x in entry.keys():
        if ping_router(x):
            print('\n\tIP: - ' + x + ' - ICMP UP\n')
        else:
            print('\n\tIP: - ' + x + ' - ICMP DOWN\n')
    
    print('\n\tIP INT BRIEF')
    for x in entry.keys():
        print('\n' + interface_check(str(entry[x]),x,'admin','alta3'))


main()
