#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 12:51:04 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with a specified data type
# numpy.dtype ( ('unicode', 10) ) : 10-character Unicode string
array_j = numpy.array (['Ceres', 'Pallas', 'Juno', 'Vesta', 'Astraea', \
                        'Hebe', 'Iris', 'Flora', 'Metis', 'Hygiea'], \
                       dtype=numpy.dtype ( ('unicode', 10) ) )

# printing Numpy array
print (f'array_j:\n{array_j}')

# printing information
print (f'information:')
print (f'  ndim     = {array_j.ndim}')
print (f'  size     = {array_j.size}')
print (f'  shape    = {array_j.shape}')
print (f'  dtype    = {array_j.dtype}')
print (f'  itemsize = {array_j.itemsize} byte')
