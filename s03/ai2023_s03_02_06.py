#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 11:28:37 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) of a specified data type
# numpy.dtype ('uint16') : 16-bit unsigned integer
array_g = numpy.array ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], \
                       dtype=numpy.dtype ('uint16') )

# printing Numpy array
print (f'array_g:\n{array_g}')

# printing information
print (f'information:')
print (f'  ndim     = {array_g.ndim}')
print (f'  size     = {array_g.size}')
print (f'  shape    = {array_g.shape}')
print (f'  dtype    = {array_g.dtype}')
print (f'  itemsize = {array_g.itemsize} byte')
