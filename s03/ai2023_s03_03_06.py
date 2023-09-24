#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 13:29:10 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.logspace ()
array_q = numpy.logspace (0, 5, 11)

# printing Numpy array
print (f'array_q:\n{array_q}')

# printing information
print (f'information:')
print (f'  ndim     = {array_q.ndim}')
print (f'  size     = {array_q.size}')
print (f'  shape    = {array_q.shape}')
print (f'  dtype    = {array_q.dtype}')
print (f'  itemsize = {array_q.itemsize} byte')
