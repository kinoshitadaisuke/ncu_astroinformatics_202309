#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 16:47:30 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.linspace (0.0, 10.0, 11)

# printing A
print (f'a:\n{a}')

# accessing to an element by indexing
print (f'a[2:5] = {a[2:5]}')
print (f'a[6:] = {a[6:]}')
print (f'a[:3] = {a[:3]}')
print (f'a[:] = {a[:]}')
print (f'a[-3:] = {a[-3:]}')
