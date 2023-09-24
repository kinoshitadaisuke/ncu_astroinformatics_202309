#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 12:09:41 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) of a specified data type
# int8 : 8-bit integer
array_f = numpy.array ([0, 1, 2, 3, 4, 5, -1, -2, -3, -4], \
                       dtype='int8')

# printing Numpy array
print (f'array_f:\n{array_f}')

# printing information
print (f'information:')
print (f'  ndim     = {array_f.ndim}')
print (f'  size     = {array_f.size}')
print (f'  shape    = {array_f.shape}')
print (f'  dtype    = {array_f.dtype}')
print (f'  itemsize = {array_f.itemsize} byte')
