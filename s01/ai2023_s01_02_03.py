#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/10 15:04:05 (CST) daisuke>
#

# initialisation of a variable "total"
total = 0

# calculating 1 + 2 + 3 + ... + 10 using "for" statement
for i in range (1, 11, 1):
    # adding "i" to "total"
    total += i

# printing result of calculation
print (f'1 + 2 + 3 + ... + 8 + 9 + 10 = {total}')
