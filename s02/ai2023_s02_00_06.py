#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/15 13:34:15 (CST) daisuke>
#

# importing os module
import os

# obtaining the value of environmental variable "SHELL"
env_shell = os.environ['SHELL']

# printing the value of environmental variable "SHELL"
print (f'SHELL = {env_shell}')
