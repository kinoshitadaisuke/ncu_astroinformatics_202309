#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 17:13:45 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.array ([5.0, 3.0, 7.0, 4.0, 9.0, 8.0, 1.0, 6.0, 2.0, 0.0])

# printing "a"
print (f'a:\n{a}')

# sorting by descending order
b = numpy.flip (numpy.sort (a, kind="mergesort"))

# printing "b"
print (f'b = numpy.flip (numpy.sort (a, kind="mergesort")):\n{b}')
