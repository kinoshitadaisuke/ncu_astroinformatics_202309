#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/10 14:59:50 (CST) daisuke>
#

# reading an integer number from keyboard typing
a_str = input ('Type one integer number: ')

# converting a string into integer
a = int (a_str)

# if and else statements
if (a > 0):
    print ("The number you type is a positive number.")
elif (a < 0):
    print ("The number you type is a negative number.")
else:
    print ("The number you type is zero.")
