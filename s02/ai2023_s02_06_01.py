#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/18 15:24:36 (CST) daisuke>
#

# importing subprocess module
import subprocess

# executing a command "ls -lF /" and capturing output
result = subprocess.run ('ls -lF /', \
                         shell=True, capture_output=True)

# stdout of command execution
output = result.stdout.decode ('utf-8')

# printing result of command execution
print (f'Files and directories at root directory:')
print (f'{output}')
