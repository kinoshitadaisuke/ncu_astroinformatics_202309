#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 08:06:35 (CST) daisuke>
#

# importing os module
import os

# getting a list of files and directory
list_files1 = os.scandir ()

# printing list of files and directory
print (f'files and directories:')
for obj in list_files1:
    print (f'  {obj.name}')
    print (f'    is_dir = {obj.is_dir ()}')
    print (f'    mode   = {oct (obj.stat ().st_mode)}')

# directory name
dir_new = 'mynewdir'

# changing file mode
os.chmod (dir_new, 0o750)

# getting a list of files and directory
list_files2 = os.scandir ()

# printing list of files and directory
print (f'files and directories:')
for obj in list_files2:
    print (f'  {obj.name}')
    print (f'    is_dir = {obj.is_dir ()}')
    print (f'    mode   = {oct (obj.stat ().st_mode)}')
