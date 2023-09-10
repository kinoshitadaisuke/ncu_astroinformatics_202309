#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/10 14:43:08 (CST) daisuke>
#

# two numbers
a = 23
b = 7

# calculation
quotient  = a // b
remainder = a % b

# printing result of calculation
print (f'a = {a}')
print (f'b = {b}')
print (f'quotient  = {quotient}')
print (f'remainder = {remainder}')
print (f'{b} * {quotient} + {remainder} = {b * quotient + remainder}')
