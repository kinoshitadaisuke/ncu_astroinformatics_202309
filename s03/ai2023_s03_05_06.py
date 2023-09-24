#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 15:57:37 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.logspace ()
a = numpy.logspace (-5.0, 5.0, 11)

# printing a
print (f'a = {a}')

# calculation
# no need of using "for"
b = numpy.log10 (a)

# printing b
print (f'b = log10 (a) = {b}')
