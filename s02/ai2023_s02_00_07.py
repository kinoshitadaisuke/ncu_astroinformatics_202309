#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/15 13:46:58 (CST) daisuke>
#

# importing os module
import os

# getting the name of the operating system
os_info = os.uname ()

# printing system information
print (f'about this system:')
print (f'  architecture = {os_info.machine}')
print (f'  OS name      = {os_info.sysname}')
print (f'  version      = {os_info.release}')
