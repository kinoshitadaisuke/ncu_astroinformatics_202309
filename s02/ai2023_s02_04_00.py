#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 12:42:49 (CST) daisuke>
#

# importing pathlib module
import pathlib

# file name
file_hosts = '/etc/hosts'

# making a pathlib object
path_hosts = pathlib.Path (file_hosts)

# existence check
if (path_hosts.exists ()):
    print (f'The file "{path_hosts}" exists!')
else:
    print (f'The file "{path_hosts}" DOES NOT exist!')
