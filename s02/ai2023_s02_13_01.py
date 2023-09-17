#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 17:38:39 (CST) daisuke>
#

# importing decimal module
import decimal

# two numbers "a" and "b" using decimal module
a = decimal.Decimal ('1.2')
b = decimal.Decimal ('2.4')

# calculation of c = a + b
c = a + b

# printing result of calculation
print (f'{a} + {b}             = {c}')

# the other calculations
d = decimal.Decimal ('1.1')
e = decimal.Decimal ('1.1')
f = decimal.Decimal ('1.1')
g = d + e
h = d + e + f
i = d + e + f - decimal.Decimal ('3.3')
print (f'{d} + {e}             = {g}')
print (f'{d} + {e} + {f}       = {h}')
print (f'{d} + {e} + {f} - 3.3 = {i}')
