#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 12:33:25 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with a specified data type
# complex64 : 64-bit complex number
array_i = numpy.array ([1.0 + 2.0j, 3.0j, 4.0, 5.0 - 6.0j, -7.0 + 8.0j, \
                        -9.0 - 10.0j, -11.0j, -12.0, 13.0 + 14.0j, 15.0j], \
                       dtype='complex64')

# printing Numpy array
print (f'array_i:\n{array_i}')

# printing information
print (f'information:')
print (f'  ndim     = {array_i.ndim}')
print (f'  size     = {array_i.size}')
print (f'  shape    = {array_i.shape}')
print (f'  dtype    = {array_i.dtype}')
print (f'  itemsize = {array_i.itemsize} byte')
