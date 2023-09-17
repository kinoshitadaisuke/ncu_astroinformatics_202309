#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 15:53:09 (CST) daisuke>
#

# importing subprocess module
import subprocess

# executing a command "date -u -r 1700000000" and capturing output
result = subprocess.run ('date -u -r 1700000000', \
                         shell=True, capture_output=True)

# stdout of command execution
output = result.stdout.decode ('utf-8')

# printing result of command execution
print (f'1.7 * 10^9 second from 01/Jan/1970 = {output}')
