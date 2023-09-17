#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 13:08:55 (CST) daisuke>
#

# importing pathlib module
import pathlib

# directory name
dir_zone = '/usr/share/zoneinfo'

# making a pathlib object
path_zone = pathlib.Path (dir_zone)

# finding directory contents
list_files = path_zone.iterdir ()

# printing directory contents
print (f'directory contents of "{path_zone}":')
for filename in list_files:
    # printing file name
    print (f'  {filename}')
