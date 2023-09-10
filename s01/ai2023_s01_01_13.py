#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/10 14:56:28 (CST) daisuke>
#

# importing math module
import math

# (x, y) coordinate
x = +1.0
y = -1.0

# calculation of arctangent
a_rad = math.atan2 (y, x)

# conversion from radian into degree
a_deg = math.degrees (a_rad)

# printing result of calculation
print (f'x            = {x}')
print (f'y            = {y}')
print (f'atan2 (y, x) = {a_rad} rad = {a_deg} deg')
