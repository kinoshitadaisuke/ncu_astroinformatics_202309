#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 17:49:43 (CST) daisuke>
#

# importing uncertainties module
import uncertainties

# quantity "a": 8.0 +/- 0.8
a = uncertainties.ufloat (8.0, 0.8)

# quantity "b": 4.0 +/- 0.6
b = uncertainties.ufloat (4.0, 0.6)

# calculation of a / b
c = a / b

# printing value of "c"
print (f'c = a / b = {a} / {b} = {c}')
