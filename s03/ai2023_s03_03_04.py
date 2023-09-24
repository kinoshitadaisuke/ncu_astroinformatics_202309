#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 13:18:37 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.arange ()
array_o = numpy.arange (0, 30, 2)

# printing Numpy array
print (f'array_o:\n{array_o}')

# printing information
print (f'information:')
print (f'  ndim     = {array_o.ndim}')
print (f'  size     = {array_o.size}')
print (f'  shape    = {array_o.shape}')
print (f'  dtype    = {array_o.dtype}')
print (f'  itemsize = {array_o.itemsize} byte')
