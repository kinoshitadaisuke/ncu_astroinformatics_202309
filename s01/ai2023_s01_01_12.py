#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/10 14:55:15 (CST) daisuke>
#

# importing math module
import math

# value of pi
pi = math.pi

# angle in degree
a_deg = 60.0

# angle in radian
a_rad = a_deg / 180.0 * pi

# calculation of sine
tan_a = math.tan (a_rad)

# printing result of calculation
print (f'pi          = {pi}')
print (f'a_deg       = {a_deg} deg')
print (f'a_rad       = {a_rad} rad')
print (f'tan (a_rad) = tan ({a_rad}) = {tan_a}')
