#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/29 11:05:05 (CST) daisuke>
#

# importing astropy module
import astropy.units

# units
u_sec = astropy.units.s

# t1 = 3600 sec
t1 = 3600.0 * u_sec

# t2 = 900 sec
t2 = 900.0 * u_sec

# calculation of t3 = t1 - t2
t3 = t1 - t2

# printing t1, t2, and t3
print (f't1 = {t1}')
print (f't2 = {t2}')
print (f't3 = t1 - t2 = {t3}')
