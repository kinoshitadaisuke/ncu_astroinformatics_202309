#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 18:08:18 (CST) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.Generator (numpy.random.PCG64DXSM ())

# generating 10 random numbers of uniform distribution between 0 and 1
array_x = rng.random (10)

# printing generated random numbers
print (f'{array_x}')
